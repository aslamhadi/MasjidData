from django.views import generic

from masjid_data.models import Masjid


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'masjid_list'

    def get_queryset(self):
        return Masjid.objects.all()
