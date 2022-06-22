from django.db import models
from django.contrib.auth import get_user_model


class Fact(models.Model):
  date = models.DateField()
  FLAGS = (('c','Civil'),('v','Voting'),('s','Slavery'),('z','Citizenship'))
  flags = models.CharField(max_length=1, choices=FLAGS)
  fact = models.CharField(max_length=256)
  source = models.URLField(blank=True)
  progress = models.BooleanField(blank=True)
  verified = models.BooleanField(default=False)
  contributor = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

  def __str__(self) -> str:
    return self.fact