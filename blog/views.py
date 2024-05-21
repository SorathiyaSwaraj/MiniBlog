from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
	home = Home.objects.all()
	cate = Category.objects.all()

	allPost = Post.objects.all()
	RecentPost = Post.objects.all()[::-1]

	data = request.GET.get('category')
	if data is not None:
		cate_data = Post.objects.filter(category=data)
		context = {'home':home,'cate_filter':cate_data,'cate':cate}
		return render(request,'blog/category.html',context)


	context = {'home':home,'cate':cate,'posts':allPost,'recentpost':RecentPost}
	return render(request,'blog/index.html',context)


def blog(request):
	home = Home.objects.all()
	cate = Category.objects.all()
	allPost = Post.objects.all()[::-1]



	context = {'home':home,'cate':cate,'posts':allPost}
	return render(request,'blog/blog.html',context)

def contact(request):


	return render(request,'blog/contact.html',)


def category(request):
	home = Home.objects.all()
	cate = Category.objects.all()

	context = {'home':home,'cate':cate}
	return render(request,'blog/category.html',context)





def single(request,slug):
	home = Home.objects.all()
	cate = Category.objects.all()
	post = Post.objects.filter(slug=slug).first()

	# comment = Comment.objects.filter(post=post)
	

	# if request.method == "POST":
	# 	name = request.POST['name']
	# 	email = request.POST['email']
	# 	postsno = request.POST.get('postsno')
	# 	website = request.POST['website']
	# 	message = request.POST['message']

	# 	post_data = Post.objects.get(sno=postsno)
		
	# 	comment = Comment(name=name,email=email,post=post_data,website=website,message=message)
	# 	comment.save()
	# 	messages.success(request,"Comment Successfully Submit")

	# 	return redirect('/')


	context = {'home':home,'cate':cate,'post':post}
	return render(request,'blog/single.html',context)

	



def my_single(request,sno):
	home = Home.objects.all()
	cate = Category.objects.all()
	post = Post.objects.filter(sno=sno).first()

	# comment = Comment.objects.filter(post=post)
	

	# if request.method == "POST":
	# 	name = request.POST['name']
	# 	email = request.POST['email']
	# 	postsno = request.POST.get('postsno')
	# 	website = request.POST['website']
	# 	message = request.POST['message']

	# 	post_data = Post.objects.get(sno=postsno)
		
	# 	comment = Comment(name=name,email=email,post=post_data,website=website,message=message)
	# 	comment.save()
	# 	messages.success(request,"Comment Successfully Submit")

	# 	return redirect('/')


	context = {'home':home,'cate':cate,'post':post}
	return render(request,'blog/single.html',context)



def signupForm_view(request):
    
    if request.method == "POST":
        
        print("Welcomm to sign up page")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        
        # Check if the user already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'User already exists. Please log in.')
            # return redirect("/login_view")      
        
        else:
            user = CustomUser.objects.create_user(username, email, password, phone_no = phone_no)
            
            print(user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/home")
            else:
                # No backend authenticated the credentials
                return redirect("/signupForm_view")

    return render(request, "signup.html")



def login_view(request):

    if request.method == "POST":
       
        print("Welcomm to login page is valid")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'User not exists. Please Sign up.')

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/home")

def page_count(request, sno):

	try:
		post = Post.objects.all()
		total_post = post.count() + 1

		next = (sno+1)%total_post
		if(next == 0):
			next = next + 1

		user = request.user
		user.pageviews = user.pageviews + 1
		user.total_pages = user.total_pages + 1

		user.save()

		return redirect('/' + str(next))
	except Exception as e:
		return redirect("/login_view")



def gifts_view(request):

    user = CustomUser.objects.get(username = request.user)
    pageviews = user.pageviews
    total_pages = user.total_pages
    rewards = "{:.2f}".format(pageviews*0.10)
    upi = user.upi

    return render(request, 'gifts.html', {'pageviews' : pageviews, 'total_pages' : total_pages, 'rewards' : rewards, 'upi' : upi})

def save_upi(request):

    upi = request.POST.get("upi_id")
    user = CustomUser.objects.get(username = request.user)
    user.upi = upi

    user.save()

    return redirect('gifts_view')
