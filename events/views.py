from django.shortcuts import render

from events.models import Event


def index(request, arg2):
    event_list = Event.objects.order_by('date')[:5]
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)
