from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404


from profiles.models import Profile
from .forms import Entry_form, Comment_form
from .models import New_Project, Comment


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']




def get_object(obj, p_id):
    return get_object_or_404(obj, id=p_id)



def home_page(request):
    dp = None
    profiles = []
    images =[]
    try:
        profiles = Profile.objects.all()
    except:
        pass
    try:
        dp = get_object_or_404(Profile, user_id=request.user)
    except:
        pass
    comments = []
    try:
        images = New_Project.objects.all()
        str = 'Innovations people are doing:'
    except:
        pass
    try:
        cmnts = Comment.objects.all()
        for image in images:
            for i in range(len(cmnts)):
                cmnt = cmnts[len(cmnts)-1-i]
                print(cmnts)
                if cmnt.project_id == image.id:
                    by = get_object_or_404(Profile, user_id=cmnt.user_id)
                    print(by.name)
                    comments.append({'comment': cmnt, 'id': image.id, 'by':by.name})
                    break
        print(comments)
    except:
        pass
    if len(images)==0:
        str = 'No posts as of now be the first to add project by clicking the gear on the left.......'
    context = {'posts': reversed(images) ,'dp': dp, 'cmnts': comments, 'profiles':profiles, 'str':str}

    return render(request, 'timeline/homepage.html', context)




def add_Project(request):
    form = Entry_form()
    if request.method == 'POST':
        form = Entry_form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse("wrong file")
            user_pr.save()
            return render(request, 'upload/uploaded.html', {'user_pr': user_pr})
    context = {"form": form, }
    return render(request, 'upload/create.html', context)


def project_details(request, p_id):
    project = get_object(New_Project, p_id)
    comment = Comment.objects.all().filter(project_id=project.id)
    profile = get_object_or_404(Profile, id=comment[0].user_id)
    tech = list(project.technologies.split(','))
    print(tech)
    if len(comment) == 1:
        comment = [comment]
    context = {'post': project, 'tech': tech, 'cmnts':comment, 'prof':profile}
    return render(request, 'timeline/project_details.html', context)



def my_projects(request):
    try:
        dp = get_object_or_404(Profile, user_id=request.user)
        images = New_Project.objects.all()
        return render(request, 'timeline/myprojects.html', {'posts': images, 'dp':dp})
    except:
        return redirect('profiles:myprofile')





def read_comments(request, id):
    try:
        profiles = Profile.objects.all()
    except:
        pass
    try:
        dp = get_object_or_404(Profile, user_id=request.user)
    except:
        pass
    comments = []
    try:
        images = New_Project.objects.all()
    except:
        pass
    try:
        cmnts = Comment.objects.all()
        print(cmnts)
        for image in images:
            if image.id == id:
                img = image
                for i in range(len(cmnts)):

                    cmnt = cmnts[len(cmnts)-1-i]
                    print(cmnt.project_id, image.id, cmnt.user_id)
                    if cmnt.project_id == image.id:
                        by = get_object_or_404(Profile, user_id=cmnt.user_id)
                        print(by.name)
                        comments.append({'comment': cmnt, 'id': image.id, 'by':by.name, 'at':cmnt.created_at})
        print(comments)
    except:
        pass
    return render(request, 'timeline/read_comment.html', {'posts': [img], 'dp': dp, 'cmnts': comments, 'profiles':profiles})






def add_comment(request, p_id):
    cmt = request.GET['cmnt']
    form = Comment_form(request.POST, request.FILES)
    if form.is_valid():
        form.instance.user = request.user
        form.instance.comment = cmt
        form.instance.project = get_object(New_Project, p_id=p_id)
        user_pr = form.save(commit=False)
        user_pr.save()
        return redirect('timeline:homepage')
    else:
        return redirect('timeline:homepage')

