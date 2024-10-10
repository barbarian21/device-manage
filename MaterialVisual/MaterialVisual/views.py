from django.http import HttpResponse
from django.views.generic.base import View

class HealthzView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("up")