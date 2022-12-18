from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    # whenever you make a new table in your database Django automatically 
    # addes a column to the database named "id"
    title = models.CharField(max_length=254, null = False, blank = False)

    # when you are using the ForeignKey you will get the id of the 
    # foreign key but not the actuall foreign key data.
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    content = models.TextField() # TEXT
    author = models.CharField(max_length=100, null=False) # VARCHAR
    image = models.ImageField(null = True, blank = False, upload_to = "blog")  # Varchar
    video = models.FileField(null = True, blank = True, upload_to = "blog_video")  # Varchar

    def __str__(self):
        return self.title
