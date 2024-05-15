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
	# home = Home.objects.all()
	# cate = Category.objects.all()

	# context = {'home':home,'cate':cate}

	# if request.method == "POST":
	# 	firstname = request.POST['fname']
	# 	lastname = request.POST['lname']
	# 	email  = request.POST['email']
	# 	subject = request.POST['subject']
	# 	message = request.POST['message']

	# 	if len(firstname) > 4:
	# 		contact = Contact(first_name=firstname,last_name=lastname,email=email,subject=subject,message=message)
	# 		contact.save()
	# 		messages.success(request,'Successfully Form Submit')
	# 		return redirect('/contact')
	# 	else:
	# 		messages.error(request,'First Name Should Be more then 4 chars')
	# 		return redirect('/contact')


	return render(request,'blog/contact.html',)


def category(request):
	home = Home.objects.all()
	cate = Category.objects.all()

	context = {'home':home,'cate':cate}
	return render(request,'blog/category.html',context)

# def single(request,slug):
# 	home = Home.objects.all()
# 	cate = Category.objects.all()
# 	post = Post.objects.filter(slug=slug).first()

# 	comment = Comment.objects.filter(post=post)
	

# 	if request.method == "POST":
# 		name = request.POST['name']
# 		email = request.POST['email']
# 		postsno = request.POST.get('postsno')
# 		website = request.POST['website']
# 		message = request.POST['message']

# 		post_data = Post.objects.get(sno=postsno)
		
# 		comment = Comment(name=name,email=email,post=post_data,website=website,message=message)
# 		comment.save()
# 		messages.success(request,"Comment Successfully Submit")

# 		return redirect('/')


# 	context = {'home':home,'cate':cate,'post':post,'comment':comment}
# 	return render(request,'blog/single.html',context)



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