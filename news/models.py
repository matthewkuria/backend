from django.db import models
from django.contrib.auth import get_user_model

class NewsCategory(models.Model):
    """Model to categorize news articles (e.g., Match News, Player News, Club Announcements)."""
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class News(models.Model):
    """Main model for news articles."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)  # For SEO-friendly URLs
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)  # Short summary for previews
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, related_name='news')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='news_articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)  # Schedule publish date
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Optional news image
    tags = models.CharField(max_length=255, blank=True, null=True)  # Comma-separated tags

    # Additional fields to improve user engagement
    view_count = models.PositiveIntegerField(default=0)  # Track how many times an article was viewed
    is_featured = models.BooleanField(default=False)  # Flag for featured articles

    class Meta:
        ordering = ['-published_date']  # Latest news first

    def __str__(self):
        return self.title

    def increment_view_count(self):
        """Method to increment the view count each time the article is viewed."""
        self.view_count += 1
        self.save()

    def get_tags_list(self):
        """Returns tags as a list of strings."""
        return [tag.strip() for tag in self.tags.split(',')] if self.tags else []

    