# Generated by Django 2.0.6 on 2018-07-18 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
