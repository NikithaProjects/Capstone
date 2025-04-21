from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category_name

class Question(BaseModel):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = Answer.objects.filter(question=self)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'uid': answer_obj.uid,
                'answer': answer_obj.answer,
                'rep_system': answer_obj.rep_system
            })
        return data

class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    # Representation system this answer corresponds to
    REP_SYSTEM_CHOICES = [
        ('V', 'Visual'),
        ('A', 'Auditory'),
        ('K', 'Kinesthetic'),
        ('O', 'Olfactory'),
        ('G', 'Gustatory'),
        ('AD', 'Auditory Digital')
    ]
    rep_system = models.CharField(max_length=2, choices=REP_SYSTEM_CHOICES)
    
    def __str__(self) -> str:
        return f"{self.answer} ({self.get_rep_system_display()})"

class QuizResult(BaseModel):
    visual_count = models.IntegerField(default=0)
    auditory_count = models.IntegerField(default=0)
    kinesthetic_count = models.IntegerField(default=0)
    olfactory_count = models.IntegerField(default=0)
    gustatory_count = models.IntegerField(default=0)
    auditory_digital_count = models.IntegerField(default=0)
    
    def get_dominant_system(self):
        counts = {
            'Visual': self.visual_count,
            'Auditory': self.auditory_count,
            'Kinesthetic': self.kinesthetic_count,
            'Olfactory': self.olfactory_count,
            'Gustatory': self.gustatory_count,
            'Auditory Digital': self.auditory_digital_count
        }
        return max(counts, key=counts.get)
    
    def get_all_counts(self):
        return {
            'Visual': self.visual_count,
            'Auditory': self.auditory_count,
            'Kinesthetic': self.kinesthetic_count,
            'Olfactory': self.olfactory_count,
            'Gustatory': self.gustatory_count,
            'Auditory Digital': self.auditory_digital_count
        }
