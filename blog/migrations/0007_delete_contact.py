# Generated by Django 5.0.1 on 2024-05-14 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]