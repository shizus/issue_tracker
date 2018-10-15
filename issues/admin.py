from django.contrib import admin

# Register your models here.
from django.db.models import Avg, Min, Max

from .models import Issue, IssueStatus


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):

    list_display = ('submitter', 'solver', 'created', 'finished', 'status', 'category')
    list_filter = ('submitter', 'solver', 'created', 'finished', 'status', 'category')
    search_fields = [
        'submitter__first_name',
        'submitter__last_name',
        'submitter__username',
        'submitter__email',
        'solver__first_name',
        'solver__last_name',
        'solver__username',
        'solver__email',
        'description',
                     ]

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        issues = Issue.objects.all().aggregate(Avg('duration'), Min('duration'), Max('duration'))

        extra_context['duration'] = {
            'min': 'No data available' if not issues['duration__min'] else issues['duration__min'],
            'avg': 'No data available' if not issues['duration__avg'] else issues['duration__avg'],
            'max': 'No data available' if not issues['duration__max'] else issues['duration__max']
        }

        return super().changelist_view(
            request, extra_context=extra_context,
        )
