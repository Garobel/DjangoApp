from django.shortcuts import render


def home(request):

    return render(request,"etsy/index2.html")