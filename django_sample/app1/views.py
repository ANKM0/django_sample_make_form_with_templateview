from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render

from .models import TestData
from .forms import TestDataForm


class IndexView(TemplateView):
    template_name: str = "app1/index.html"
    form_class = TestDataForm

    def post(self, request, *args, **kwargs) -> HttpResponse:

        print(request.POST.get("number"))
        print(type(request.POST.get("number")))

        number = request.POST.get("number")
        name = request.POST.get("name")
        price = request.POST.get("price")

        default_data = {
            "number": number,
            "name": name,
            "price": price,
        }
        form = self.form_class(default_data)

        if form.is_valid():
            print("ax")
            TestData.objects.create(number=number, name=name, price=price)
        else:
            print("aa")
            print(f"error:{form.errors}")

        context = {
            "error_list": form.errors,
        }

        return render(request, self.template_name, context)


class DataListView(ListView):
    template_name: str = "app1/data_list.html"
    model = TestData
