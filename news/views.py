from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import News, NewsCategory
from .serializers import NewsSerializer, NewsCategorySerializer

class NewsCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing News Categories."""
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow everyone to read, restrict write

class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for managing News articles."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow everyone to read, restrict write

    def perform_create(self, serializer):
        """Customize the creation process by automatically setting the author."""
        serializer.save(author=self.request.user)  # Set the author to the currently logged-in user

    def get_queryset(self):
        """Customize queryset to filter by published status or other criteria."""
        queryset = super().get_queryset()
        return queryset.filter(published_date__isnull=False)  # Only return published news
