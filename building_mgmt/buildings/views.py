from django.views import generic

from .models import Building, Unit

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'buildings/index.html'
    context_object_name = 'building_list'

    def get_queryset(self):
        return Building.objects.all()


class DetailView(generic.DetailView):
    model = Building
    template_name = 'buildings/detail.html'


class UnitView(generic.DetailView):
    model = Building
    template_name = 'buildings/units.html'


class UnitList(generic.ListView):
    template_name = 'units/index.html'
    context_object_name = 'unit_list'

    def get_queryset(self):
        return Unit.objects.all()


class UnitDetail(generic.DetailView):
    model = Unit
    template_name = 'units/detail.html'
