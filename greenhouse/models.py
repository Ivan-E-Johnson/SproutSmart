from django.db import models

# greenhouse/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="email_not_provided@email.com")
    id = models.AutoField(primary_key=True)
    # Add other fields as needed


class SensorReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    def __str__(self):
        return f"Sensor Reading (User: {self.user.username}, Value: {self.value})"
