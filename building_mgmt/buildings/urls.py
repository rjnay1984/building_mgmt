from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='buildingindex'),
    path('<int:pk>', views.DetailView.as_view(), name='buildingdetail'),
    path('<int:pk>/units', views.UnitView.as_view(), name='buildingunits'),
    path('units', views.UnitList.as_view(), name='unitindex'),
    path('units/<int:pk>', views.UnitDetail.as_view(), name='unitdetail')
]
