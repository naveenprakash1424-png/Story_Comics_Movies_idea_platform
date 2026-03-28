from django.shortcuts import render,get_object_or_404
from .models import Story, StoryPart, Category, Comic, ShortStory, MovieIdea
from django.db.models import Q
from .models import Slide
def get_story_slides(stories):
    slides = []
    for story in stories:
        if story.image:
            slides.append({
                'title': story.title,
                'image': story.image
            })
    return slides
def home(request):
    stories = Story.objects.all().order_by('-created_at')[:5]
    slides = get_story_slides(stories)
    return render(request, 'home.html', {'stories': stories, 'slides': slides})


def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    parts = story.parts.all()
    slides = get_story_slides(parts)

    return render(request, 'story_detail.html', {
        'story': story,
        'parts': parts,
        'slides':slides
    })

def part_detail(request, slug, part_number):
    story = get_object_or_404(Story, slug=slug)
    part = get_object_or_404(StoryPart, story=story, part_number=part_number)

    next_part = StoryPart.objects.filter(
        story=story,
        part_number__gt=part.part_number
    ).order_by('part_number').first()

    prev_part = StoryPart.objects.filter(
        story=story,
        part_number__lt=part.part_number
    ).order_by('-part_number').first()

    return render(request, 'part_detail.html', {
        'story': story,
        'part': part,
        'next_part': next_part,
        'prev_part': prev_part
    })
def stories_list(request):
    stories = Story.objects.all().order_by('-created_at')
    slides = get_story_slides(stories)
    
    return render(request, 'stories_list.html', {
        'stories': stories,
        'slides': slides
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        # later: save or email
        success = True

    return render(request, 'contact.html', {'success': success})


def story_list(request):
    stories = Story.objects.all()
    categories = Category.objects.all()

    print("GET DATA:", request.GET)   # 👈 DEBUG

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    if query:
        print("SEARCH:", query)
        stories = stories.filter(title__icontains=query)

    if category_id:
        print("FILTER:", category_id)
        stories = stories.filter(categories__id=category_id)

    print("RESULT COUNT:", stories.count())  # 👈 DEBUG

    return render(request, 'stories_list.html', {
        'stories': stories,
        'categories': categories
    })

from .models import Comic

def comics_list(request):
    comics = Comic.objects.all().order_by('-created_at')
    slides = get_story_slides(comics)

    return render(request, 'comics_list.html', {'comics': comics, 'slides': slides})
def comic_detail(request, slug, part_number=1):
    comic = get_object_or_404(Comic, slug=slug)
    parts = comic.parts.all().order_by('part_number')

    # Get the current part
    current_part = parts.filter(part_number=part_number).first()
    if not current_part:  # fallback to first part
        current_part = parts.first()
        part_number = current_part.part_number if current_part else 1

    # Determine next / previous
    next_part = parts.filter(part_number__gt=part_number).first()
    prev_part = parts.filter(part_number__lt=part_number).last()

    return render(request, 'comic_detail.html', {
        'comic': comic,
        'current_part': current_part,
        'next_part': next_part,
        'prev_part': prev_part,
    })
def short_stories_list(request):
    stories = ShortStory.objects.all().order_by('-created_at')
    slides = get_story_slides(stories)
    # for story in stories:
    #     for i in story.categories.all():
    #         print(i)
    return render(request, 'short_stories_list.html', {
        'stories': stories,
        'slides': slides
    })


def short_story_detail(request, slug):
    story = get_object_or_404(ShortStory, slug=slug)
    return render(request, 'short_story_detail.html', {'story': story})

def movie_ideas_list(request):
    ideas = MovieIdea.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    # FILTER
    category_id = request.GET.get('category')

    if category_id:
        ideas = ideas.filter(categories__id=category_id)

    return render(request, 'movie_ideas_list.html', {
        'ideas': ideas,
        'categories': categories
    })


def movie_idea_detail(request, slug):
    idea = get_object_or_404(MovieIdea, slug=slug)
    return render(request, 'movie_idea_detail.html', {'idea': idea})

