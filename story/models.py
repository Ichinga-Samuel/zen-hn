from django.db import models
from django.contrib.auth import get_user_model

from base.models import Item

class Story(Item):
    by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='stories')
    title = models.TextField()
    url = models.URLField(blank=True, default="https://news.ycombinator.com/")
    text = models.TextField(blank=True, default="")

    class Meta:
        permissions = [
            ("can_read", "can read a story"),
            ("can_edit", "can edit a story"),
        ]

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'story'


class Comment(Item):
    by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments', null=True, default=None)
    reply = models.ManyToManyField('self', related_name='replies', symmetrical=False, blank=True)

    def __str__(self):
        return f"by_{self.by.username}"

    class Meta:
        db_table = 'comment'
