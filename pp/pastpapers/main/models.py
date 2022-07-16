from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Paper(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.IntegerField()

    def __str__(self):
        return f"{self.subject}'s Paper {self.name}"



class Topic(models.Model):
    paper = models.ForeignKey(Paper,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name}'s Paper {self.paper.name} {self.name}"


class Question(models.Model):
    paper = models.ManyToManyField(Paper)
    subject = models.ManyToManyField(Subject)
    topic = models.ManyToManyField(Topic)
    marks = models.IntegerField()
    date = models.CharField(max_length=100)
    question_no = models.IntegerField()
    picture = models.ImageField()
    

    def __str__(self):
        return self.date+" "+self.question_no

    
class Answer(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE)
    picture = models.ImageField()
    

    def __str__(self):
        return "Answer of "+self.question

    
 