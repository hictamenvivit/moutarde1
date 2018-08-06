from django import forms


class ArticleForm(forms.Form):
    titre = forms.CharField(label='titre', max_length=100)
    contenu = forms.CharField(label='contenu', max_length=200, widget=forms.Textarea)
    photo = forms.FileField()
