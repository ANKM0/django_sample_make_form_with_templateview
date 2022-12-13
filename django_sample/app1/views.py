from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import TestDataModelForm


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    form_class = TestDataModelForm

    def get(self, request, *args, **kwargs):
        context = {
            "form": self.form_class
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            "form": self.form_class
        }

        return render(request, self.template_name, context)
