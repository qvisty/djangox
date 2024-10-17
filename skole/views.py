from django.shortcuts import render
from .models import Elev
from itertools import groupby
from .tables import ElevTable


def sfo_elever(request):
    elevs = Elev.objects.filter(sfo_gruppe__isnull=False).order_by(
        "sfo_gruppe__gruppe_nummer", "fornavn"
    )
    elevs_grouped = [
        (sfo_gruppe, list(elev_list))
        for sfo_gruppe, elev_list in groupby(elevs, key=lambda x: x.sfo_gruppe)
    ]
    return render(request, "skole/sfo_elever.html", {"elevs_grouped": elevs_grouped})


def sfo_grupper(request):
    elevs = Elev.objects.filter(sfo_gruppe__isnull=False).order_by(
        "sfo_gruppe__gruppe_nummer", "fornavn", "efternavn"
    )
    table = ElevTable(elevs)
    groups = [
        (key, list(group))
        for key, group in groupby(
            elevs,
            lambda elev: elev.sfo_gruppe.gruppe_nummer
            if elev.sfo_gruppe
            else "Not Assigned",
        )
    ]
    return render(request, "skole/sfo_grupper.html", {"groups": groups,'table': table})


