from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content=models.TextField()

    image=models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )

    created_at=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username


class Comment(models.Model):

    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text=models.TextField()

    created_at=models.DateTimeField(
        auto_now_add=True
    )


class Like(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together=('user','post')