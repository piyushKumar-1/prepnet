from django.shortcuts import render
from .forms import TryingForm


def test(request):
    return render(request, 'codetest/question.html')

def mytest(request):



    return render(request, 'codetest/mytest.html')