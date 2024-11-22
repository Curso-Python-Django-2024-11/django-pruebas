from django.contrib import admin

from blog.models import Post

admin.site.site_header = "Administración del blog"


@admin.action(description="Publicar posts seleccionados")
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'published')
    list_filter = ('published',)
    fields = ('title', 'body', 'featured_image', 'slug', 'published')
    prepopulated_fields = {'slug': ['title']}
    actions = [make_published]

    def save_model(self, request, obj, form, change):
        # Forzamos que el autor del post sea el usuario autenticado
        obj.author = request.user
        super().save_model(request, obj, form, change)






# Register your models here.
admin.site.register(Post, PostAdmin)