from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .form import Invites


def AjouterInvite(request):
    form = AjouterInvite(request.POST or None)
    if form.is_valide():
        form.save()
        return redirect('invite-add')
    return render(request, 'formulaire.html', {'form': form})

# class pour afficher mes invités
class ListInvites(ListView):
    model = Invites
    template_name = 'index.html'
    context_object_name = 'invites'

from django.shortcuts import render, redirect, get_object_or_404
from .models import Invites

def listInvites(request):
    invites = Invites.objects.all()
    return render(request, 'index.html', {'invites': invites})


def addInvite(request):
    if request.method == "POST":
        Invites.objects.create(
            nom=request.POST['nom'],
            prenom=request.POST['prenom'],
            telephone=request.POST['telephone'],
            dateinvitation=request.POST['dateinvitation'],
            commune=request.POST['commune'],
            quartier=request.POST['quartier'],
            invitepar=request.POST['invitepar'],
            motifdepresence=request.POST['motifdepresence'],
            communauteorigine=request.POST['communauteorigine'],
        )
        return redirect('home')


def editInvite(request, id):
    invite = get_object_or_404(Invites, id=id)

    if request.method == "POST":
        invite.nom = request.POST['nom']
        invite.prenom = request.POST['prenom']
        invite.telephone = request.POST['telephone']
        invite.dateinvitation = request.POST['dateinvitation']
        invite.commune = request.POST['commune']
        invite.quartier = request.POST['quartier']
        invite.invitepar = request.POST['invitepar']
        invite.motifdepresence = request.POST['motifdepresence']
        invite.communauteorigine = request.POST['communauteorigine']
        invite.save()

        return redirect('home')


def deleteInvite(request, id):
    invite = get_object_or_404(Invites, id=id)

    if request.method == "POST":
        invite.delete()
        return redirect('home')

