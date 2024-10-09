from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get_object_or_404(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': is_visit_long(visit),
                'is_strange': False
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
