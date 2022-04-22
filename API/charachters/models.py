from enum import unique
from django.db import models

# Create your models here.
#JsonField only python 3.9+ or install json1
#model for out rick and morty characters
class Character(models.Model):
    
    CHARACTER_STATUS_CHOICES = (
        ('Alive', 'Alive'),
        ('Dead', 'Dead'),
        ('unknown', 'unknown')
    )
    
    CHARACTER_GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('unknown', 'unknown'),
        ('Genderless', 'Genderless')
    )
    
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10,choices=CHARACTER_STATUS_CHOICES,default='unknown')
    species = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True)
    
    gender = models.CharField(max_length=10,choices=CHARACTER_GENDER_CHOICES,default='unknown')
    origin = models.JSONField(null=True) # object	Name and link to the character's origin location.
    location = models.JSONField(null=True) # object	Name and link to the character's last known location endpoint.
    image = models.TextField() #link for image
    episode = models.JSONField() # (urls) will be list stored
    url = models.TextField() #character url
    created = models.DateTimeField()
  
    """
        our equal magic function to compare with other characters
        checking if have in common episodes or same species,gender,status
    """
    def __eq__(self, other):  
        if (len(set(self.episode) & set(other.episode)) > 0 or (self.status == other.status and 
            self.species == other.species and self.type == other.type and self.gender == other.gender)):
              print(len(set(self.episode) & set(other.episode))) # for myself to check
              return True
        
        return False
  
  
#model for results

class Result(models.Model):
      
      RESULT_CHOICES = (
        (True, True),
        (False, False)
      )
      
      result = models.BooleanField(choices=RESULT_CHOICES, default=False) # if characters are identical or not
      characters = models.JSONField(unique=True) # store id for characters have been in compare
    