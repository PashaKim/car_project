from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import get_language
from django.views import View
from django.views.generic import TemplateView

from car_project.settings import TELEGRAM_VALUE, VIBER_VALUE, PHONE_VALUE, LANGUAGES
from car_project.utils import get_client_ip
from main.forms import CustomerRequestForm


# Create your views here.


class LandingView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram_value'] = TELEGRAM_VALUE
        context['viber_value'] = VIBER_VALUE
        context['phone_value'] = PHONE_VALUE
        context['languages'] = list(dict(LANGUAGES).keys())
        context['language_code'] = get_language()

        return context


class CustomerRequestFormView(View):

    def post(self, request):
        form = CustomerRequestForm(get_client_ip(request), request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"})

        return JsonResponse({"status": "error", "detail": form.errors})


def redirect_main(request):
    return redirect('/')


def customhandler404(request, exception=None, template_name='404.html'):
    return render(request, template_name, status=404)


def customhandler500(request, exception=None,  template_name='500.html'):
    return render(request, template_name, status=500)
