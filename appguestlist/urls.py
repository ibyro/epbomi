from django.urls import path
from .views import ListInvites
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listInvites, name='home'),
    path('ajouter/', views.AjouterInvite , name="AjouterInvite" ),
    path('invite/add/', views.addInvite, name='invite-add'),
    path('invite/<int:id>/edit/', views.editInvite, name='invite-edit'),
    path('invite/<int:id>/delete/', views.deleteInvite, name='invite-delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)