from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get posts from users that the current user follows
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
