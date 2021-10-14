from django.test import TestCase
from django.urls import reverse

from .models import Building, Unit

# Create your tests here.


class BuildingViewTests(TestCase):
    fixtures = ['data.json']

    def test_building_index(self):
        response = self.client.get(reverse('buildingindex'))
        self.assertIs(response.status_code, 200)
        self.assertIs(len(response.context['building_list']), 4)

    def test_building_detail(self):
        building = Building.objects.filter(pk=1).first()
        url = reverse('buildingdetail', args=(building.id,))
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)
        self.assertEquals(response.context['building'], building)

    def test_building_units(self):
        building = Building.objects.filter(pk=1).first()
        unit = Unit.objects.filter(building=building).first()
        url = reverse('buildingunits', args=(building.id,))
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)
        self.assertContains(response, unit.number)


class UnitViewTests(TestCase):
    fixtures = ['data.json']

    def test_unit_index(self):
        response = self.client.get(reverse('unitindex'))
        self.assertIs(response.status_code, 200)
        self.assertIs(len(response.context['unit_list']), 6)

    def test_unit_detail(self):
        unit = Unit.objects.filter(pk=1).first()
        url = reverse('unitdetail', args=(unit.id,))
        response = self.client.get(url)
        self.assertIs(response.status_code, 200)
        self.assertContains(response, unit.description)
