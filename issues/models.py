
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timezone

from django.db.models.signals import pre_save
from django_enumfield import enum


class IssueStatus(enum.Enum):
    OPENED = 0
    SOLVED = 1
    ON_PROGRESS = 2


class IssueCategory(enum.Enum):
    BUG = 0
    ENHANCEMENT = 1
    DOCUMENTATION = 2


# Create your models here.
class Issue(models.Model):
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='submitter', null=True)
    solver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='solver', null=True)
    description = models.CharField(max_length=200)
    status = enum.EnumField(IssueStatus, default=IssueStatus.OPENED)
    category = enum.EnumField(IssueCategory, default=IssueCategory.BUG)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    finished = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return '{}'.format(self.description[0:10])

    @property
    def duration(self):
        if self.created is not None and self.finished is not None:
            return self.finished - self.created
        else:
            return datetime.now(timezone.utc) - self.created

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        # created = kwargs.get('created')
        if instance.status == IssueStatus.SOLVED:
            instance.finished = datetime.now()
        else:
            instance.finished = None

pre_save.connect(Issue.post_save, sender=Issue)
