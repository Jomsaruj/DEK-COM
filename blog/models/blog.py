from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils import timezone
from django.contrib.auth.models import User

from .tag import Tag


class Blog(PolymorphicModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now())
    id_code = models.CharField(max_length=6, default='')
    tags = models.ManyToManyField(Tag)

    def get_tags(self):
        return self.tags.all()

    def __str__(self):
        return self.topic

    
