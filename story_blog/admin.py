from django.contrib import admin
from .models import Story, Category, StoryPart, Slide
from .models import Comic, ComicPart, ShortStory, MovieIdea

class StoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Category)
admin.site.register(StoryPart)
admin.site.register(Story, StoryAdmin)
admin.site.register(Slide)


class ComicPartInline(admin.TabularInline):
    model = ComicPart
    extra = 1

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ComicPartInline]

@admin.register(ShortStory)
class ShortStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

# admin.py

@admin.register(MovieIdea)
class MovieIdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories']  # ✅ nice UI for multiple select