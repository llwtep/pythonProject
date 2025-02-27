from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registeration_new_user(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for{username}!')
            form.save()
            return redirect('login')
        else:
            messages.error(request,'No correct data')

    form=UserRegisterForm()


    return render(request, 'users/registration_form.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    context={
        'u_form': u_form,
        'p_form': p_form
    }



    return render(request, 'users/profile.html',context)