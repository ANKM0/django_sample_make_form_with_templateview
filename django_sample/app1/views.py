from django.views.generic.edit import ModelFormMixin
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy

from .forms import TestDataModelForm
from .models import TestData


class IndexView(TemplateView, ModelFormMixin):
    # https://docs.djangoproject.com/en/4.1/ref/class-based-views/mixins-single-object/
    template_name: str = "app1/index.html"
    form_class = TestDataModelForm
    success_url = reverse_lazy('app1:list')
    model = TestData

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DataListView(ListView):
    template_name: str = "app1/data_list.html"
    model = TestData
