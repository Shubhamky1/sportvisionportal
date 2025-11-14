from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from players.models import Player
from .forms import UserRegisterForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")

            if user.role == 'player':
                Player.objects.create(user=user, age=0, contact='', skills='')

            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home')


@login_required
def profile_view(request):
    user = request.user
    player = None

    # Get player details for player role users
    if user.role == "player":
        player, created = Player.objects.get_or_create(user=user)

        if request.method == "POST":
            player.age = request.POST.get("age", player.age)
            player.contact = request.POST.get("contact", player.contact)
            player.skills = request.POST.get("skills", player.skills)
            player.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")

    return render(request, "user/profile.html", {"user": user, "player": player})