# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import EbookModel
from .forms import EbookModelForm, SignupForm, LoginForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def base(request):
    return render(request, 'base.html')

# signup


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, "accounts created sucessfully")
            form.save()
            form = SignupForm()  # to show emptyform

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {"form": form})


# login
# login url came with usename and password on post request
# login () if you have an athenticated user and you want to attach a current session i.e done by login() function
# login() takes user obj and request then saves the userid in session framework
# function name should be not equal with login()
def user_login(request):
    # verify if a user is logged in
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = request.POST['username']
                upass = request.POST['password']
                # username = formfield of Loginform
                user = authenticate(request, username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully ")
                    form = LoginForm()
        else:
            form = LoginForm()
        return render(request, 'registration/login.html', {"form": form})
    else:
        return redirect('user_login')


# profile
def profile(request):
    if request.user.is_authenticated:
        form = UserProfileForm(instance=request.user)
        return render(request, 'registration/profile.html', {'name': request.user.username, "form": form})

    return render(request, 'registration/profile.html')




# logout
# when logout all session data are cleaned out from the session
def user_logout(request):
    logout(request)
    return redirect("user_login")


# upload
# request.POST is a dict and request.POST[key] and key is modelfield_name and we used here model Form not form API

def upload(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # request.FILES a Querydict where datas are saved
            form = EbookModelForm(request.POST, request.FILES)
            # print("THIS IS :-", request.FILES)
            if form.is_valid():
                cov = request.FILES["cover"]
                books = request.FILES["books_pdf"]
                tit = request.POST['title']
                pub = request.POST['publisher']
                year = request.POST['year']
                auth = request.POST['author']

                # every instance of model collects the variables which store these data means model_instance(cover) = cover(variable)
                form = EbookModel(cover=cov, books_pdf=books,
                                  title=tit, publisher=pub, year=year, author=auth)
                form.save()
                # showing direct book_list after upload
                return redirect("book_list")
        else:
            form = EbookModelForm()  # empty Form
        return render(request, 'Ebook/upload.html', {"form": form})
    else:
        return redirect('user_login')


# booklist so through get method we can get the Queryset
# @login_required
def book_list(request):
    # if request.user.is_authenticated:
    books = EbookModel.objects.all()

    # print(books) == <QuerySet [<EbookModel: Tittle > Django>]>
    return render(request, 'Ebook/book_list.html', {"books": books})


# delete
# primary_key=True already done by django during migrate so you can use it here
# delete is a  raw SQL queries(CRUD) written in django by devlopers
# i just give permisson from adminpanel if request.user is superuser then he cant delete
def delete(request, id):
    if request.method == "POST":
        # every table pk = id we took and # get the primary key from model
        delete = EbookModel.objects.get(pk=id)
        if request.user.is_superuser:
            delete.delete()
        else:
            pass
    return redirect("book_list")
