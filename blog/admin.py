from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'published')
    list_filter = ('published',)
    fields = ('title', 'body', 'slug', 'published')
    prepopulated_fields = {'slug': ['title']}

    def save_model(self, request, obj, form, change):
        # Forzamos que el autor del post sea el usuario autenticado
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)