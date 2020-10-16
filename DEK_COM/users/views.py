from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':  # user click SignUp button
        print("submit")
        form = UserCreationForm(request.POST)
        if form.is_valid():  # all information is valid
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to DEK-COM {username}!!')
            return redirect('/home')  # redirect to portfolio index (home.html)
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
