import random

from django.http import HttpResponseNotFound, HttpResponseServerError

from django.shortcuts import render

from .data import departures, description, tours, title, subtitle


def main_view(request):
    rand_tours = {}
    rand_list = random.sample(range(1, len(tours) + 1), 6)
    for num in rand_list:
        rand_tours[num] = tours[num]
    context = {'rand_tours': rand_tours, 'title': title, 'subtitle': subtitle, 'description': description}
    return render(request, 'tours/index.html', context)


def departure_view(request, departure):
    departure_dict = {}
    nights_list = []
    price_list = []
    for key, value in tours.items():
        if value['departure'] == departure:
            departure_dict[key] = value
            nights_list.append(value['nights'])
            price_list.append(value['price'])
    return render(request, 'tours/departure.html', {'departure_dict': departure_dict, 'sum': len(departure_dict),
                                                    'dep_in_rus': departures[departure], 'min_night': min(nights_list),
                                                    'max_night': max(nights_list), 'min_price': min(price_list),
                                                    'max_price': max(price_list)})


def tour_view(request, id):
    star_str = ''
    context = tours[id]
    context['dep_in_rus'] = departures[context['departure']]
    for i in range(0, int(context['stars'])):
        star_str += '★'
    context['star_str'] = star_str
    return render(request, 'tours/tour.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound("Упс, ошибка 404")


def custom_handler500(request):
    return HttpResponseServerError("Упс, ошибка 500")
