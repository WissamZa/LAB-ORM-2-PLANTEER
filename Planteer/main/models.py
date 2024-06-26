from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
   class category_choices(models.TextChoices):
      Fruit = "Fruit"
      Vegetables = "Vegetables"
      Flawer = "Flower"
      Herb = "Herb"
      Mushroom = "Mushroom"

   name = models.CharField(max_length=20)
   about = models.TextField()
   used_for = models.TextField()
   image = models.ImageField(upload_to="images/plant/")
   category = models.CharField(max_length=10,
                               choices=category_choices.choices,
                               default=category_choices.Fruit)
   is_edible = models.BooleanField(null=False)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['name']

   def __str__(self) -> str:
      return self.name


class Contact(models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   email = models.EmailField()
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['-created_at']

   def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}"


class Comment(models.Model):
   plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
   user: User = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   comment_date = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['-comment_date']

   def __str__(self) -> str:
      return f"{self.user_name.username} {self.plant.name}"


def plant_count():

   return Plant.objects.all().values_list('id')
