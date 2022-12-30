from django.contrib import admin
from .models import Contact,BookTable

# Register your models here.
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'email', 'subject', 'message']

@admin.register(BookTable)
class ContactModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'email', 'date', 'time','person']