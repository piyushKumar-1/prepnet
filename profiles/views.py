from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm
from prep.models import User

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


'''

def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            def form_valid(self, form):
                obj = form.save(commit=False)
                obj.user = self.request.user
                obj.save()
                return HttpResponseRedirect(self.get_success_url())
            user_pr = form.save(commit=False)
            user_pr.save()
            return render(request, 'profiles/my_profile.html')
    context = {"form": form, }
    return render(request, 'profiles/add_profile.html', context)

'''

def my_profile(request):
    profiles = Profile.objects.filter(user_id=request.user.id)
    if profiles:
        return render(request, 'profiles/my_profile.html', {'profiles':profiles})

    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user)
            form.instance.user = request.user
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse("wrong file")
            user_pr.save()
            return redirect('profiles:myprofile')
    context = {"form": form, }
    return render(request, 'profiles/add_profile.html', context)


def search_profile(request):
    st = request.GET['search']
    profiles = Profile.objects.all()
    result = []
    for profile in profiles:
        if st.lower() in profile.name.lower():
            result.append(profile)
    for profile in profiles:
        if st.lower() in profile.user.email.lower():
            if profile not in result:
                result.append(profile)

    print(profiles)
    print(result)
    return render(request, 'profiles/result.html', {'profiles':result})
