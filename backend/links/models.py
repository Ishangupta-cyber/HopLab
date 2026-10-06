from django.db import models


class Link(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=12, unique=True, null=True, blank=True)
    click_count = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"