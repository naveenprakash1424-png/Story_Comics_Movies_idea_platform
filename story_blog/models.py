from django.db import models
from django.utils.text import slugify 

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class Story(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='stories/', blank=True, null=True)  # ✅ NEW


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title 

class StoryPart(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='parts')
    part_number = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='story_parts/', blank=True, null=True)  # ✅ NEW

    class Meta:
        ordering = ['part_number']

    def __str__(self):
        return f"{self.story.title} - Part {self.part_number}"
class Slide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='slides/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='comic_images/')
    categories = models.ManyToManyField('Category', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ComicPart(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='parts')
    part_number = models.IntegerField()
    image = models.ImageField(upload_to='comic_parts/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['part_number']

    def __str__(self):
        return f"{self.comic.title} - Part {self.part_number}"

class ShortStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # the short story text
    image = models.ImageField(upload_to='short_stories/', blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while ShortStory.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
# models.py

class MovieIdea(models.Model):
    title = models.CharField(max_length=200)
    concept = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_ideas/', blank=True, null=True)

    categories = models.ManyToManyField('Category', blank=True)  # ✅ ADD THIS

    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title