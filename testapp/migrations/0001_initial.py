# Generated by Django 4.0.3 on 2022-03-29 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EbookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('year', models.DateField(default=django.utils.timezone.now)),
                ('publisher', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='covers/')),
                ('books_pdf', models.FileField(upload_to='pdfs/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]