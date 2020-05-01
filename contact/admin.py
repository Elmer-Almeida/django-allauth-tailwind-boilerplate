from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

    fields = ['__str__', 'email', 'timestamp', ]
    search_fields = ['email', 'first_name', 'last_name', 'message', ]


admin.site.register(Contact, ContactAdmin)
