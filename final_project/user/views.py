from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm

User = get_user_model()


def index(request):
    return render(request, "index.html")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
    else:
        logout(request)
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    # TODO: 1. /login로 접근하면 로그인 페이지를 통해 로그인이 되게 해주세요
    # TODO: 2. login 할 때 form을 활용해주세요
    msg = None
    is_ok = False
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                is_ok = True
                return HttpResponseRedirect("/")
        else:
            msg = "올바른 유저ID와 패스워드를 입력하세요."
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})


def logout_view(request):
    # TODO: 3. /logout url을 입력하면 로그아웃 후 / 경로로 이동시켜주세요						
    logout(request)
    return redirect("/")



def user_list_view(request):
    # TODO: 7. /users 에 user 목록을 출력해주세요
    # TODO: 8. user 목록은 로그인 유저만 접근 가능하게 해주세요
    # TODO: 9. user 목록은 pagination이 되게 해주세요
    if request.user.is_authenticated:
        page = int(request.GET.get("p", 1))
        users = User.objects.all().order_by("-id")
        paginator = Paginator(users, 10)
        users = paginator.get_page(page)
        return render(request, "users.html", {"users": users})
    else:
        return redirect("/")
