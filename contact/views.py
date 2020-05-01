from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm


class Contact(View):
    template_name = 'contact/view.html'

    def get(self, request):
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form,
        }
        return render(request, self.template_name, context)
