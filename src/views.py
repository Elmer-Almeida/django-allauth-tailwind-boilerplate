from django.shortcuts import render
from django.views.generic import View


class Landing(View):
    template_name = 'pages/landing.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


class About(View):
    template_name = 'pages/about.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)
