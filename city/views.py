from django.shortcuts import render, redirect, get_object_or_404
from .models import City, Comment, Like_comment
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Comment_form, Like_comment_form, City_form

# Create your views here.


def index(request):
    cities = City.objects.all()

    return render(
        request,
        "cities.html",
        {
            "cities": cities,
        },
    )


@login_required
def get_city(request, id):
    if request.method == "GET":
        city = City.objects.get(id=id)

        comments = Comment.objects.filter(city=id)

        like_user = Like_comment.objects.filter(user=request.user)

        list_ = []

        for i in like_user:
            list_.append(i.comment.id)

        user = request.user

        likes = {}

        for comment in comments:
            likes[comment.id] = Like_comment.objects.filter(comment=comment.id).count()

        return render(
            request,
            "city.html",
            {
                "city": city,
                "form": Comment_form,
                "comments": comments,
                "likes": likes,
                "like_user": like_user,
                "list": list_,
            },
        )


@login_required
def create_new_city(request):
    if request.method == "GET":
        return render(request, "create_city.html", {"form": City_form})

    else:
        form = City_form(request.POST, request.FILES)
        if form.is_valid():
            new_city = form.save(commit=False)

            new_city.user = request.user

            new_city = form.save()

            return redirect("home")

        else:
            return redirect("create_new_city")


@login_required
def create_new_comment(request, id):
    if request.method == "POST":
        form = Comment_form(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.city = City.objects.get(id=id)

            new_comment.save()

            return redirect("city", id=id)

        else:
            return redirect("city", id=id)


@login_required
def like_comment(request, id_city, id_comment):
    if Like_comment.objects.filter(comment=id_comment):
        if Like_comment.objects.get(comment=id_comment).user.id == request.user.id:
            like = Like_comment.objects.get(comment=id_comment)

            like.delete()

            return redirect("city", id=id_city)

        else:
            form = Like_comment_form()

            like = form.save(commit=False)
            like.user = request.user
            like.comment = Comment.objects.get(id=id_comment)

            like.save()

            return redirect("city", id=id_city)
    else:
        form = Like_comment_form()

        like = form.save(commit=False)
        like.user = request.user
        like.comment = Comment.objects.get(id=id_comment)

        like.save()

        return redirect("city", id=id_city)


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)

                return redirect("home")

            except:
                return render(request, "signup.html", {"error": "User already exists"})

        else:
            return render(
                request, "signup.html", {"error": "Passwords do not concidence"}
            )


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")

    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user:
            login(request, user)
            return redirect("home")

        else:
            return render(
                request, "signin.html", {"error": "Username or password incorrect"}
            )


def signout(request):
    logout(request)
    return redirect("home")
