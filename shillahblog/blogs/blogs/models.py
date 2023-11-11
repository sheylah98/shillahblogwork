from django.db import models

class Author(models.Model):
    GENDER_OPTIONS = [
        ("M","Male"),
        ("F","Female"),

    ]
    name= models.CharField(max_length=50,verbose_name="Author Name")
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    birth_date=models.DateField(auto_now=False,auto_now_add=False)
    no_of_articles=models.IntegerField()
    address=models.CharField(max_length=100, null=True,blank=True,default="N/A")
    gender=models.CharField(max_length=2,choices=GENDER_OPTIONS)

    class Article(models.Model):
        title=models.CharField(max_length=150)
        summary=models.TextField(max_length=250)
        author=models.ForeignKey(Author,on_delete=models.CASCADE)
        publish_date=models.DateTimeField(auto_now=False)
        is_published=models.BooleanField(default=False)

