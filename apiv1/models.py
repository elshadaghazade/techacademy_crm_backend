from django.db import models
from django.http import HttpResponse, JsonResponse

class Lead(models.Model):
    STATUS_LEAD = 1
    STATUS_CALL = 2
    STATUS_RECALL = 3
    STATUS_MEETING = 4
    STATUS_BLOCK = 5

    status_choices = (
        (STATUS_LEAD, "leads"),
        (STATUS_CALL, "calls"),
        (STATUS_RECALL, "recalls"),
        (STATUS_MEETING, "meetings"),
        (STATUS_BLOCK, "blocks")        
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    social = models.CharField(max_length=20)
    status = models.IntegerField(choices=status_choices, default=STATUS_LEAD)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname} | type: {dict(self.status_choices)[self.status]}"


class LeadInteraction(models.Model):
    CALL_STATUS_PENDING = 0
    CALL_STATUS_ANSWERED = 1
    CALL_STATUS_UNANSWERED = 2
    CALL_STATUS_RESCHEDULED = 6
    CALL_STATUS_RECALL_PENDING = 3
    CALL_STATUS_RECALL_ANSWERED = 4
    CALL_STATUS_RECALL_UNANSWERED = 5
    CALL_STATUS_RECALL_RESCHEDULED = 7

    MEETING_STATUS_PENDING = 1
    MEETING_STATUS_DONE = 2
    MEETING_STATUS_RESCHEDULED = 3
    MEETING_STATUS_CANCELED = 4

    call_status_choices = (
        (CALL_STATUS_PENDING, "Call pending"),
        (CALL_STATUS_ANSWERED, "Call answered"),
        (CALL_STATUS_UNANSWERED, "Call unanswered"),
        (CALL_STATUS_RESCHEDULED, "Call rescheduled"),
        (CALL_STATUS_RECALL_PENDING, "Recall pending"),
        (CALL_STATUS_RECALL_ANSWERED, "Recall answered"),
        (CALL_STATUS_RECALL_UNANSWERED, "Recall unanswered"),
        (CALL_STATUS_RECALL_RESCHEDULED, "Recall rescheduled")
    )

    meeting_status_choices = (
        (MEETING_STATUS_PENDING, "Meeting pending"),
        (MEETING_STATUS_DONE, "Meeting accomplished"),
        (MEETING_STATUS_RESCHEDULED, "Meeting rescheduled"),
        (MEETING_STATUS_CANCELED, "Meeting canceled")
    )

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    call_date = models.DateTimeField(null=True, blank=True)
    call_status = models.IntegerField(choices=call_status_choices, null=True, blank=True)
    called_at = models.DateTimeField(blank=True, null=True)
    meeting_date = models.DateTimeField(blank=True, null=True)
    meeting_status = models.IntegerField(choices=meeting_status_choices, null=True, blank=True)
    met_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.lead} | call date: {self.call_date} | call status: {dict(self.call_status_choices).get(self.call_status)} | called at: {self.called_at} | meeting date: {self.meeting_date} | meeting status: {dict(self.meeting_status_choices).get(self.meeting_status)} | met at: {self.met_at}"
