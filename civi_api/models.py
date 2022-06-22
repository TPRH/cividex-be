from django.db import models
from django.contrib.auth import get_user_model


class Fact(models.Model):
  date = models.DateField()
  FLAGS = (('c','Civil'),('v','Voting'),('s','Slavery'),('z','Citizenship'))
  flags = models.CharField(max_length=1, choices=FLAGS)
  fact = models.CharField(max_length=256)
  progress = models.BooleanField()
  verified = models.BooleanField(default=False)
  contributor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.fact