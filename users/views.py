from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm,UserProfileForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile= profile_form.save(commit=False)

            profile.user =user
            profile.email = user.email

            profile.save()

            username = form.cleaned_data.get('username')

            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()


    return render(request,'users/register.html',{'form': form,'profile_form': profile_form})


def dashboard(request):
    return render(request,'users/dashboard.html')


