from django.contrib import admin
from .models import Invites

@admin.register(Invites)
class InvitesAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/phone_mask.js',)

    list_display = (
        "nom",
        "prenom",
        "telephone",
        "dateinvitation",
        "commune",
        "quartier",
        "invitepar",
        "motifdepresence",
        "communauteorigine",
        "ministere",
        "Activitepro",
        "sitmatrimoniale",
        "groupesanguin"
    )

    list_display_links = ("nom", "prenom")

    search_fields = (
        "nom",
        "prenom",
        "telephone",
        "commune",
        "quartier",
        "invitepar",
        "communauteorigine",
    )

    list_filter = (
        "commune",
        "quartier",
        "invitepar",
        "dateinvitation",
        "communauteorigine",
    )

    ordering = ("-dateinvitation",)

    list_per_page = 35

# Personnalisation interface Admin
admin.site.site_header = "Gestion des invités EPBOMI"
admin.site.site_title = "Gestion des invités EPBOMI"
admin.site.index_title = "Gestion des invités EPBOMI"
