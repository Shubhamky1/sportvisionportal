from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Player
from .forms import PlayerForm

@login_required
def player_list(request):
    # Admin/coach see all players; players see only themselves
    if request.user.role in ['admin', 'coach']:
        players = Player.objects.select_related('user').all()
    else:
        players = Player.objects.filter(user=request.user)

    return render(request, 'players/player_list.html', {'players': players})


@login_required
def player_create(request):
    # Only admin or coach can create players manually
    if request.user.role not in ['admin', 'coach']:
        messages.error(request, "You are not authorized to add players.")
        return redirect('player_list')

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)

            # Automatically assign user role = "player"
            if player.user.role != 'player':
                player.user.role = 'player'
                player.user.save()

            player.save()
            messages.success(request, f"Player '{player.user.username}' added successfully!")
            return redirect('player_list')
    else:
        form = PlayerForm()

    return render(request, 'players/player_form.html', {'form': form})


@login_required
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)

    # PLAYER role → can edit only their own skills
    if request.user.role == 'player':
        if player.user != request.user:
            messages.error(request, "Players can only edit their own profile.")
            return redirect('player_list')

        if request.method == 'POST':
            player.skills = request.POST.get('skills')
            player.save()
            messages.success(request, "Your skills were updated successfully!")
            return redirect('player_list')

        return render(request, 'players/player_skill_update.html', {'player': player})

    # ADMIN or COACH → full edit access for any player
    if request.user.role in ['admin', 'coach']:
        form = PlayerForm(request.POST or None, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, f"Player '{player.user.username}' updated successfully!")
            return redirect('player_list')

        return render(request, 'players/player_form.html', {'form': form})

    # Fallback
    messages.error(request, "You are not authorized to edit players.")
    return redirect('player_list')


@login_required
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)

    # Admin + Coach can delete
    if request.user.role not in ['admin', 'coach']:
        messages.error(request, "Only admin or coach can delete players.")
        return redirect('player_list')

    if request.method == 'POST':
        username = player.user.username
        player.delete()
        messages.success(request, f"Player '{username}' deleted successfully!")
        return redirect('player_list')

    return redirect('player_list')


