from django.shortcuts import render, redirect
from django.contrib import messages
from users.form import CustomRegistrationForm


def register(request):
    if request.method == 'POST':  # user click SignUp button
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():  # all information is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to DEK-COM {username} !!')
            return redirect('index')  # redirect to portfolio index (home.html)
    else:
        form = CustomRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

