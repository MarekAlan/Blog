# Generated by Django 4.0.3 on 2022-03-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]