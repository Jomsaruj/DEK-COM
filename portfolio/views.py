from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from blog.models.post import Post
from django.db.models import Q

from users.form import FormUpdate, DateForm, AddressForm, ZipCodeForm, PhoneForm, GitForm, ProfileImageForm, \
    ProfessionForm


def profile(request, username):
    """Gennerate the profile for the user."""
    user_profile = User.objects.filter(username=username).first()
    return render(request, 'portfolio/profile.html', {'user': user_profile})


@login_required
def profile_update(request, username):
    """Update profile of each user."""
    user_profile = User.objects.filter(username=username).first()
    if request.method == 'POST':
        form = FormUpdate(request.POST, instance=request.user)
        date_form = DateForm(request.POST, instance=request.user.date)
        address_form = AddressForm(request.POST, instance=request.user.address)
        zip_form = ZipCodeForm(request.POST, instance=request.user.zipcode)
        phone_form = PhoneForm(request.POST, instance=request.user.phone)
        git_form = GitForm(request.POST, instance=request.user.git)
        profile_image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        c_form = ProfessionForm(request.POST, instance=request.user.profession)

        if form.is_valid() and phone_form.is_valid():
            form.save()
            date_form.save()
            address_form.save()
            zip_form.save()
            phone_form.save()
            git_form.save()
            profile_image_form.save()
            c_form.save()
            return redirect('/blog')

    else:
        form = FormUpdate(instance=request.user)
        date_form = DateForm(instance=request.user.date)
        address_form = AddressForm(request.POST, instance=request.user.address)
        zip_form = ZipCodeForm(request.POST, instance=request.user.zipcode)
        phone_form = PhoneForm(request.POST, instance=request.user.phone)
        git_form = GitForm(request.POST, instance=request.user.git)
        profile_image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        c_form = ProfessionForm(request.POST, instance=request.user.profession)

    return render(request, 'portfolio/profile_update.html', {
        'form': form,
        'date_form': date_form,
        'address_form': address_form,
        'zip_form': zip_form,
        'phone_form': phone_form,
        'git_form': git_form,
        'user': user_profile,
        'profile_image_form': profile_image_form,
        'c_form': c_form
    })






