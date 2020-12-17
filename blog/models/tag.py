from django.db import models


class Tag(models.Model):
    """Tag for all the blogs."""
    name = models.CharField(max_length=15, default='')
    post_num = models.BigIntegerField(default=1)

    @property
    def get_tags(self):
        """Get the tags."""
        return self.tags.all()

    def __str__(self):
        """Return the string of the tag."""
        return self.name
