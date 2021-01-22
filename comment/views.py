from rest_framework.viewsets import ModelViewSet

from .serializers import CommentSerializer
from .models import Comment
from .permissions import IsCommentAuthor
from main.permissions import ProductPermission


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ProductPermission, ]
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [IsCommentAuthor, ]
        return [permission() for permission in permissions]
