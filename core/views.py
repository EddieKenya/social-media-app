from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth
from.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST ['email']
        firstname = request.POST ['firstname']
        lastname = request.POST ['lastname']
        passwword = request.POST ['password']
        password2 = request.POST ['password2']

        if passwword == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already taken!')
                return redirect('signup')
            else:
                new_user = User.objects.create_user(username=username, email=email,  password=passwword)
                # new_user.is_active = False
                # new_user.first_name = firstname
                # new_user.last_name = lastname
                new_user.save()

                user_model = User.objects.get(username=username)
                user_profile = Profile.objects.create(user=user_model, id_user = user_model.id) 
                return redirect('login')
        
        else:
            messages.info(request, 'Password Not Matching')
            return redirect ('signup')
            
    else:
        return render(request, 'signup.html')


@csrf_exempt
@login_required(login_url='login')
def home (request):
    user_profile = Profile.objects.get(user = request.user)
    user_posts = Post.objects.all
    

   
   
    
    context={
        'user_profile': user_profile,
        'userpost':user_posts,

    }
    

    return render (request, 'home.html', context)

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST ['password']

        

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login( request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials Invalid')
            return redirect ('login')
     


    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request) 
    return redirect('login')

@login_required(login_url='login')
def settings(request):

    user_profile = Profile.objects.get (user= request.user)

    if request.method == 'POST':
        if request.FILES.get ('image') == None:
            img = user_profile.profileimg
            firstname = request.POST['firstname']
            secondname = request.POST['lastname']
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = img
            user_profile.first_name = firstname
            user_profile.second_name = secondname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') !=None:
            img = request.FILES.get('image')
            firstname = request.POST['firstname']
            secondname = request.POST['lastname']
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = img
            user_profile.first_name = firstname
            user_profile.second_name = secondname
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
    return render( request, 'settings.html', {'user_profile':user_profile})  

def post (request):

    if request.method == 'POST':
    
        if request.FILES.get('image') != None:
            user = request.user.username
            post_image = request.FILES.get('image')
            caption = request.POST['caption']

            new_post = Post.objects.create(user=user, posts_image=post_image, caption=caption)
            new_post.save()
            return redirect('home')
       
    return render ( request , 'post.html')

def like(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post= Post.objects.get(id=post_id)

    user_filter= likes.objects.filter(username=username, post_liked=post_id).first()

    if user_filter == None:
        new_like = likes.objects.create(username=username, post_liked=post_id)
        new_like.save()
        post.no_of_likes += 1
        post.save()
        return redirect('home')
    else:
        user_filter.delete()
        post.no_of_likes -=1
        post.save()
        return redirect('home')


def comments(request):
    post_commented = request.GET.get('post_id')

    post= Post.objects.get(id=post_commented)
    comments= Comments.objects.filter(post_commented=post.id)

    if request.method == 'POST':
        username = request.user.username
        comment_post = post_commented
        new_comments = request.POST['comments']

        comments_section = Comments.objects.create(username=username, post_commented=comment_post, comments=new_comments)
        comments_section.save()
        
        
    comments_length = len (comments)
    post.post_no_comments = comments_length 

    

    context={
        'post': post,
        'comments': comments,
        'commentcount': comments_length

    }

    return render(request, 'comments.html',context)
                                                    

