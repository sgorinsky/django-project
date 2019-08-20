from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # creating an instance of a form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,
                  'users/register.html', 
                  {'form': form} )

# if someone tries to access the '/profile' url, then they will be redirected to the login page thanks to LOGIN_URL in settings, then they will be redirected to the profile view
@login_required # decorator that adds restrictions to our profile requests
def profile(request):
     
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Updated profile!')
        return redirect('profile')
            
    else:           
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }      
    return render(request,
                  'users/profile.html',
                  context)


