from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ("body_text",)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
