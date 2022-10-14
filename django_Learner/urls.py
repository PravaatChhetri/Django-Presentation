from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('addS/', views.addS),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]