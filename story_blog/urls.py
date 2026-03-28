from django.urls import path
from .views import home, story_detail,part_detail, stories_list, about, contact, comics_list, comic_detail, short_stories_list, short_story_detail
from . views import movie_ideas_list, movie_idea_detail
urlpatterns = [
    path('', home, name='home'),
    path('story/<slug:slug>/', story_detail, name='story_detail'),
    path('story/<slug:slug>/part/<int:part_number>/', part_detail, name='part_detail'),
    path('stories/', stories_list, name='stories_list'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('comics/', comics_list, name='comics_list'),
    path('comics/<slug:slug>/', comic_detail, name='comic_detail'),
    path('comics/<slug:slug>/part/<int:part_number>/', comic_detail, name='comic_part_detail'),
    path('short-stories/', short_stories_list, name='short_stories_list'),
    path('short-stories/<slug:slug>/', short_story_detail, name='short_story_detail'),
    path('movie-ideas/', movie_ideas_list, name='movie_ideas_list'),
    path('movie-ideas/<slug:slug>/', movie_idea_detail, name='movie_idea_detail'),
]
