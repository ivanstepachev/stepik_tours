from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html', {'departure': departure})


def tour_view(request, id):
    return render(request, 'tours/tour.html', {'id': id})


def custom_handler404(request, exception):
    return HttpResponseNotFound("Упс, ошибка 404")


def custom_handler500(request):
    return HttpResponseServerError("Упс, ошибка 500")
