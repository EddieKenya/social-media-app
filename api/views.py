from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import PostSerializer
from rest_framework.response  import Response
from rest_framework import status
from core.models import Post,likes,Comments


class PostAPI(APIView):
    def post(self, request,*args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data})
        else:
            return Response({'errors':serializer.errors}, status= status.HTPP_400_BAD_REQUEST)

    def get(self,request,*args, **kwargs):
        query = Post.objects.all()
        serializer = PostSerializer(query, many=True)
        return Response({'data':serializer.data})


# Create your views here.
