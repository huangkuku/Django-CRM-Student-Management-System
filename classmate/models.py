from django.db import models

# Create your models here.
class Classmate(models.Model):
    student_number = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50) # 國小 國中
    grade = models.FloatField()
    chinese_score = models.PositiveIntegerField()
    math_score = models.PositiveIntegerField()
    english_score = models.PositiveIntegerField()
    def __str__(self):
        return f'Student Info: name: {self.first_name} {self.last_name}, grade and level: {self.grade}, {self.field_of_study}'
