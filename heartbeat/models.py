from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

from django.db import models

# Create your models here.
class HeartBeat(models.Model):
    current_bpm=models.IntegerField(default=0)
    current_time=models.DateTimeField(' TIME ')
    
    def isOlderThan10(self):
        return self.current_time >= timezone.now() - datetime.timedelta(seconds=10)
    def __str__(self):
        return str(self.current_time)
