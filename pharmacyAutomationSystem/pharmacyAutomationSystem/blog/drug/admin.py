from django.contrib import admin

from .models import Drug
# Register your models here.
@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    
    list_display = ["title","created_date"]
    search_fields = ["title"]
    class Meta:
        model = Drug