import django_tables2 as tables
from .models import Elev

class ElevTable(tables.Table):
    fornavn = tables.Column()
    efternavn = tables.Column()
    
    class Meta:
        model = Elev
        template_name = 'django_tables2/bootstrap.html'
        fields = ['fornavn', 'efternavn', 'sfo_gruppe__gruppe_nummer']
        order_by = 'sfo_gruppe__id'
