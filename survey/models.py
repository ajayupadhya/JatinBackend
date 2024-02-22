from django.db import models

# Create your models here.


class SurveyQuestionModal(models.Model):
    question = models.TextField()
    

    
class SurveyAnswerModal(models.Model):
    question = models.ForeignKey(SurveyQuestionModal , on_delete = models.CASCADE)
    answer = models.TextField()
    files = models.FileField()
    


class Client(models.Model):
    title = models.CharField(max_length=255)
    client_url = models.CharField(max_length=255)
    timeline = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="jatin/images", null=True , blank=True , default="")
    imageMobile = models.ImageField( upload_to="jatin/images", null=True , blank=True , default="")
    link = models.CharField(max_length=255, default="")
    
    
    # To see name after adding something in Django it changes Client object (1) to title
    def __str__(self):
        return self.title
    
class SinglePage(models.Model):  
    title = models.ForeignKey(Client , on_delete=models.CASCADE , default="")  
    slug = models.CharField(max_length = 255)
    overview = models.TextField()
    challenges = models.TextField()
    approach = models.TextField()
    solution = models.TextField()
    strong_word = models.TextField()
    results = models.TextField()
    
    def __str__(self):
        return self.title
    