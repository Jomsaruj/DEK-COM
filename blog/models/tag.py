from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=15, default='')
    post_num = models.BigIntegerField(default=1)

    def post_add_tag(self):
        self.post_num += 1
        self.save()

    def post_delete_tag(self):
        self.post_num -= 1
        self.save()

    def __str__(self):
        return self.name
