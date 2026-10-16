from django.db import models

# Create your models here.
"""
Schema : QuestionsDb
Fields : title, language, notes, difficulty_level, sample_input, sample_output,
         topic, published_date, is_active            
"""

class QuestionDb(models.Model):
    title = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ("python", "Python"),
        ("java", "Java"),  
        ("javascript", "JavaScript"), 
    )
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default="python")

    DIFFICULTY_CHOICES = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default="easy")

    notes = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    topic = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)