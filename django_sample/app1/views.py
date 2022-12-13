from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TestDataModelForm


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
            return redirect("app1:index")
