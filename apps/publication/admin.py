from django.contrib import admin
from .models import Publication, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Publication, PublicationAdmin)
