from django.shortcuts import render, redirect
from django.contrib import messages
from users.form import CustomRegistrationForm


def register(request):
    if request.method == 'POST':  # user click SignUp button
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():  # all information is valid
            user = form.save()
            user.refresh_from_db()
            user.profession.is_java = form.cleaned_data.get('is_java')
            user.profession.is_python = form.cleaned_data.get('is_python')
            user.profession.is_JavaScript = form.cleaned_data.get('is_JavaScript')
            user.profession.is_Csharp = form.cleaned_data.get('is_Csharp')
            user.profession.is_C = form.cleaned_data.get('is_C')
            user.profession.is_Cpp = form.cleaned_data.get('is_Cpp')
            user.profession.is_Go = form.cleaned_data.get('is_Go')
            user.profession.is_R = form.cleaned_data.get('is_R')
            user.profession.is_Swift = form.cleaned_data.get('is_Swift')
            user.profession.is_PHP = form.cleaned_data.get('is_PHP')
            user.profession.is_Kotlin = form.cleaned_data.get('is_Kotlin')
            user.profession.is_Ruby = form.cleaned_data.get('is_Ruby')
            user.profession.is_Dart = form.cleaned_data.get('is_Dart')
            username = form.cleaned_data.get('username')
            user.save()
            messages.success(request, f'Welcome to DEK-COM {username}!!')
            return redirect('login')  # redirect to portfolio index (home.html)
    else:
        form = CustomRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
