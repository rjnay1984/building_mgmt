from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('buildings/', views.BuildingList.as_view(), name='buildingindex'),
    path('buildings/<int:pk>', views.BuildingDetail.as_view(), name='buildingdetail'),
    path('buildings/<int:pk>/units',
         views.UnitView.as_view(), name='buildingunits'),
    path('units', views.UnitList.as_view(), name='unitindex'),
    path('buildings/units/<int:pk>', views.UnitDetail.as_view(), name='unitdetail')
]
