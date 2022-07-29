# Generated by Django 4.0.6 on 2022-07-29 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0009_pop_created_at_pop_pop_image_pop_save_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_who_commentlike',
            field=models.ManyToManyField(blank=True, related_name='user_who_commentlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pop',
            name='user_who_like',
            field=models.ManyToManyField(blank=True, related_name='user_who_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
