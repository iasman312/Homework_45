from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),
                  ('done', 'Сделано')]


class Task(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    status = models.CharField(max_length=150, choices=status_choices,
                              default="new")
    up_to = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.id}. {self.title}: {self.status}'
