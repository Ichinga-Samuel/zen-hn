from django.db import models
from django.conf import settings

from base.models import Item



class Poll(Item):
    by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='polls')
    title = models.TextField()


class PollOption(Item):
    by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='options')
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
