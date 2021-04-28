from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Barber, Time, Order
import json


class MainPage(ListView):
    template_name = 'main.html'
    model = Barber
    context_object_name = 'barbers'


class BarberTimeList(ListView):
    template_name = 'booking.html'
    queryset = Time.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b = get_object_or_404(Barber, name=self.kwargs['name_barber'])
        context['barber'] = b
        context['times_barber'] = b.time.all()
        context['barber_name'] = b.name
        return context

    context_object_name = 'times'


def process_booking(request):
    form = json.loads(request.body)['form']
    barber_ = Barber.objects.get(name=form['barber'])
    tm_ = Time.objects.get(tm=form['time'])
    Order.objects.create(
        barber=barber_,
        tm=tm_,
        client_tel=form['phone'],
        client_name=form['name'],
        client_email=form['email']
    )
    barber_.time.add(tm_)
    return JsonResponse('Complete', safe=False)
