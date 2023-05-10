from django.contrib import admin
from .models import Publication, PostImage, TypePost

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

admin.site.register(Publication, PublicationAdmin)

class TypePostAdmin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(TypePost, TypePostAdmin)