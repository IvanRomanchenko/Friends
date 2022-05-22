from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.conf import settings

from loguru import logger

from .forms import LoginForm, SignUpForm, UpdateForm


def get_client_ip(request):
    """ Returns user ip from request """
    if x_forwarded_for := request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def terms(request):
    return render(request, 'terms.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/my_profile/")

            else:
                msg = 'Invalid credentials'

        else:
            msg = 'Error validating the form'

    return render(request, "auth/login.html",
                  {"form": form, "msg": msg})


def logout_view(request):
    logout(request)
    return redirect("/login/")


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                login(request, user)
                return redirect("/my_profile/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "auth/register.html",
                  {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
def my_profile(request):
    user = get_user(request)
    alert = None

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            if 'update' in request.POST.keys():
                user = form.save(commit=False)
                user.ip = get_client_ip(request)
                user.save()

                alert = {'msg': 'Profile has been updated', 'status': 'success'}

            elif 'delete' in request.POST.keys():
                user.delete()

                return logout_view(request)

        else:
            logger.error(form.errors.as_json())

            alert = {'msg': 'Form is invalid', 'status': 'danger'}

    else:
        form = UpdateForm(instance=user)

    return render(request, "profile/my_profile.html",
                  {"form": form, "username": user.username, "alert": alert})


@login_required(login_url="/login/")
def other(request):
    return redirect("/my_profile/")


def favicon(request):
    return FileResponse(
        open(settings.STATICFILES_DIRS[0] / 'assets/img/favicon.png', 'rb')
    )
