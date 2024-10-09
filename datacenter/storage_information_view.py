from datacenter.models import format_duration, get_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    all_visits = Visit.objects.all()

    for visit in all_visits:
        if not visit.leaved_at:
            non_closed_visits = [
                {
                    'who_entered': visit.passcard,
                    'entered_at': visit.entered_at,
                    'duration': format_duration(get_duration(visit)),
                }
            ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
