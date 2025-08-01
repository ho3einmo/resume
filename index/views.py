from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import About
# Create your views here.


class index(TemplateView):
    template_name = "index\index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.prefetch_related('social_set','experience_set','education_set','skill_set','workflow_set','interests_set','awards_set').get(is_active=True)
        return context