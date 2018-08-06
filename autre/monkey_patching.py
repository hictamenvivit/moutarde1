from django.contrib.auth.models import User
from .models import Article

def get_number_articles(self):
    return len(Article.objects.filter(auteur__id=self.id))
    
User.add_to_class("get_number_articles", get_number_articles)