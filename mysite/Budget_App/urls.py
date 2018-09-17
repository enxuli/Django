from django.contrib import admin
from django.urls import path

from . import views


app_name = 'Budget_App'

urlpatterns = [
    path('', views.plan_list, name='list'),
    path('add-plan', views.PlanCreateView.as_view(),name = 'add'),
    path('<slug:plan_slug>', views.plan_detail, name='detail'),
]
