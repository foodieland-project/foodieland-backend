# Generated by Django 4.0.4 on 2022-04-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='comments',
            field=models.ManyToManyField(
                blank=True, related_name='recipe_comment', to='core.comment'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
