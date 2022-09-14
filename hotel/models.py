from django.db import models

class hotel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    star=models.IntegerField()
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.id , self.name

