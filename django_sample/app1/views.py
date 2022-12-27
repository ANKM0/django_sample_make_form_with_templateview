from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TestDataModelForm
from .models import TestData


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    form_class = TestDataModelForm

    def get(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class()
        context = {
            "form": form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app1:index")
        else:
            context = {"form": form}
            return render(request, self.template_name, context)


class DataListView(ListView):
    template_name: str = "app1/data_list.html"
    model = TestData
