# Generated by Django 3.1.5 on 2021-04-18 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('blog', '0005_auto_20210417_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.author'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
