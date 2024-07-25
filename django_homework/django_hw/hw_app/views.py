from django.shortcuts import render


def home(request):
    return render(request, "hw_app/home.html")

