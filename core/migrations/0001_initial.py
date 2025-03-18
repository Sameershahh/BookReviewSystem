# Generated by Django 5.1.7 on 2025-03-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.IntegerField(unique=True)),
                ('genre', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Sci-Fi', 'Science Fiction'), ('Mystery', 'Mystery'), ('Fantasy', 'Fantasy')], max_length=200)),
                ('publication_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]
