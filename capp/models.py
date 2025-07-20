from django.db import models

class UsrSubmission(models.Model):
    mode = models.CharField(max_length=100)
    abstract = models.BooleanField(default=False)
    temp = models.FloatField(default=1.0)
    keepit = models.BooleanField(default=True)
    usrinput = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} - mode={self.mode}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if not (0.0 <= self.temp <= 2.0):
            raise ValidationError({'temp': "Temperature must be between 0.0 and 2.0."})


class DialogHistory(models.Model):
    prompt = models.JSONField(default=list)
    usr = models.JSONField(default=list)
    assistant = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DialogHistory {self.id} ({len(self.usr)} exchanges)"
