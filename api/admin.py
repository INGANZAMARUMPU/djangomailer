from django.contrib import admin
from .models import *

@admin.register(Email)
class ProduitAdmin(admin.ModelAdmin):
	list_display = "title", "subject", "to", "body"
	list_filter = "title", "subject", "to", "body"
	search_fields = "title", "subject", "to", "body"
