from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.conf import settings


class Category(models.Model):
    name = models.CharField(
        max_length=50
    )


class Tag(models.Model):
    name = models.CharField(
        max_length=50
    )


class Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    body = models.TextField(
        default='',
        blank=True,
    )
    published = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        blank=True,
    )
    image = models.ImageField(
        blank=True,
        default=''
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    body = models.TextField()


class ButtonAction(models.Model):
    """
    like or dislike
    """
    LIKE = 'like'
    DISLIKE = 'dislike'
    ACTION_TYPES = (
        (LIKE, _('Like')),
        (DISLIKE, _('Dislike')),
    )
    action_type = models.CharField(
        max_length=10,
        choices=ACTION_TYPES
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [
            'post', 'user'
        ]
