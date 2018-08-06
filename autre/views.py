from django.shortcuts import render
from django.views import generic
from .models import Article
from . import monkey_patching
from .forms import ArticleForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.



class IndexView(generic.ListView):
    template_name = 'autre/index1.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class DetailView(generic.DetailView):
    template_name = 'autre/detail1.html'
    model = Article


class AjouterArticleView(generic.FormView):
    form_class = ArticleForm
    success_url = '.'
    template_name = 'autre/ajouter_article1.html'
    
    def form_valid(self, form):
        titre = self.request.POST['titre']
        contenu = self.request.POST['contenu']
        photo = self.request.FILES['photo']
        nouvel_article = Article(photo=photo, titre=titre,
        contenu=contenu, auteur=self.request.user)
        nouvel_article.save()
        return super().form_valid(form)


ajouter_article = login_required(AjouterArticleView.as_view())
