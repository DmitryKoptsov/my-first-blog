from django.conf import settings
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='Название блога')
    text = models.TextField(max_length=300,verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_date']
        verbose_name = "Блоги"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name="Блог",
        db_index=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title