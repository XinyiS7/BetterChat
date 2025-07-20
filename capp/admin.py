from django.contrib import admin
from .models import UsrSubmission, DialogHistory

@admin.register(UsrSubmission)
class UsrSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'mode', 'abstract', 'temp', 'keepit', 'created_at')
    search_fields = ('mode', 'usrinput')

@admin.register(DialogHistory)
class DialogHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    readonly_fields = ('prompt', 'usr', 'assistant')
