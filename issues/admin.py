from django.contrib import admin

# Register your models here.

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
        issues = Issue.objects.all()

        max(issues, key=lambda item: item.duration)

        durations = [issue.duration.seconds for issue in issues]
        solved_issues = Issue.objects.filter(status=IssueStatus.SOLVED)

        durations_solved = [issue.duration.seconds for issue in solved_issues]

        extra_context['duration'] = {
            'min': 'No data available' if len(durations_solved) == 0 else min(durations_solved),
            'avg': 'No data available' if len(durations) == 0 else sum(durations) / float(len(durations)),
            'max': 'No data available' if len(durations) == 0 else max(durations)
        }

        return super().changelist_view(
            request, extra_context=extra_context,
        )
