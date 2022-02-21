from django.shortcuts import render,redirect
from .models import Profile
from .forms import SignupForm,ProfileForm,UserForm
from django.contrib.auth import authenticate,login



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile')
        
    else:
        form = SignupForm()
        return render(request,'registration/signup.html',{"form":form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userForm = UserForm(request.POST,instance=request.user)
        profileForm = ProfileForm(request.POST,instance=profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myForm = profileForm.save(commit=False)
            myForm.user = request.user
            myForm.save()
            return redirect("/accounts/profile")

    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(request.POST,instance=profile)
    return render(request,'profile/profile_edit.html',{"userForm":userForm,"profileForm":profileForm})