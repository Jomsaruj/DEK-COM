from django.db import models


class IdCode(models.Model):
    """The code for each id."""

    code = models.CharField(max_length=6, default='')

    def __str__(self):
        """Return the string."""
        return self.code
