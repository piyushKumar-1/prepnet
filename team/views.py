from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.urls import reverse
from .forms import Team_ticket, Member_skills
from .models import Team_req, Team_skill


def team(request):
    i=0
    form = Team_ticket()
    if request.method == 'POST':
        form = Team_ticket(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            user_pr = form.save(commit=False)
            user_pr.save()
            print(form.instance.id)
            return redirect('team:skill', size=form.instance.team_size, i=i, id=form.instance.id)
    return render(request, 'team/maketeam.html', {'form':form, 'url':'/timeline/team/'})

def skills(request, size,i, id):
    print(size)
    if request.method == 'POST':
        form = Member_skills(request.POST)
        if form.is_valid():
            k = get_object_or_404(Team_req, id=id)
            size = k.team_size
            form.instance.team = k
            user_pr = form.save(commit=False)
            user_pr.save()
            i += 1
            if i<size:
                return render(request, 'team/maketeam.html', {'form': Member_skills(), 'url':f'/timeline/team/member_skill/{size}/{i}/{id}'})
            else:
                return redirect('timeline:homepage')
    return render(request, 'team/maketeam.html', {'form': Member_skills(), 'url': f'/timeline/team/member_skill/{size}/{i}/{id}'})


def myteam(request):
    return render(request, 'team/myteam.html')


def show_all(request):
    teams = []
    try:
        teams = Team_req.objects.all()
    except:
        pass

    return render(request, 'team/allteams.html', {'teams':teams,'size':len(teams)})


def team_details(request,id):
    team = []
    try:
        team = Team_skill.objects.all().filter(team_id=id)
    except:
        pass

    return render(request, 'team/team_details.html', {'team':team})

