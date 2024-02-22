from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from events.models import Category


class HomePageView(TemplateView):
    """View für das Anzeigen einer Homepage / Dashboards."""

    template_name = "index.html"

    def get_context_data(self, **kwargs: Any):
        """Hier eigenen Context für das Template-Rendern
        einfügen."""
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.all()

        return ctx
