from django.db import models

# Create your models here.
class User(models.Model):
 ID = models.AutoField(primary_key=True)
 Username = models.CharField(max_length = 100)
 Email = models.EmailField(max_length = 100)
 Password = models.CharField(max_length = 100) #must be hashed

 def __str__(self):
     return self.Username

class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length = 100)
    Content = models.TextField()
    Category = models.CharField(max_length = 100)
    Date_Published = models.DateField()
    def __str__(self):
        return self.Title

class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE) #check if it's related to post ID
    User = models.ForeignKey(User, on_delete=models.CASCADE) #check
    Content = models.TextField()
    Date_Posted = models.DateField()

    def __str__(self):
        return f"Comment by {self.User.Username}"

class Category(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length = 100)

    def __str__(self):
        return self.Name








