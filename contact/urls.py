from django.urls import path

from . import views

urlpatterns = [
    path('/', views.ContactView.as_view({'post':'create'}), name='contact-create')
]
