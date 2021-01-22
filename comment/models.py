from django.db import models
from account.models import User
from main.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='commentaries')
    text = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author_id


