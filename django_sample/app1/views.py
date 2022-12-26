from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TestDataModelForm
from .models import TestData


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    form_class = TestDataModelForm

    def get_context_data(self, **kwargs):
        # get処理だけ書く
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = self.form_class()
        return ctx

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app1:data_list")
        else:
            context = {
                "error_list": form.errors,
            }
            return render(request, self.template_name, context)


class DataListView(ListView):
    template_name: str = "app1/data_list.html"
    model = TestData
