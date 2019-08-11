from django.db import models

from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(
        max_length=200
    )
    pub_date = models.DateTimeField(
        verbose_name=_('Publish Date')
    )

    def __str__(self):
        return f'({self.id}) {self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(
        max_length=200,
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'({self.id}) Question ({self.question_id}) {self.choice_text}'
