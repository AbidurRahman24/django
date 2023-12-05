from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.AutoField(primary_key= True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    address = models.TextField()
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    date_field = models.DateField(default='2023-01-01')
    # binary_field = models.BinaryField()
    boolean_field = models.BooleanField(default=True)
    datetime_field = models.DateTimeField(default=timezone.now)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    duration_field = models.DurationField(default=timedelta(days=1))
    email_field = models.EmailField(default='niloy@gmail.com')
    float_field = models.FloatField(default=23.9)
    # file_field = models.FileField(upload_to='files/')
    generic_ip_address_field = models.GenericIPAddressField(default='0.0.0.0')
    null_boolean_field = models.BooleanField(null=True)
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # null_boolean_field = models.NullBooleanField()
    url_field = models.URLField(default='https://example.com')
    
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    




    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'