from django.contrib import admin
from blog.models import contactFormModel

class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'message')

admin.site.register(contactFormModel, ContactFormModelAdmin)
