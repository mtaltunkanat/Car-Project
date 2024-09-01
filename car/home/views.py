from django.shortcuts import render


def index(request):
    return render(request, "sevenge.html")


def about(request):
    return render(request, "about.html")


def car(request):
    return render(request, "cars.html")


def contact(request):
    return render(request, "contact.html")