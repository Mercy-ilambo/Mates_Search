# Generated by Django 4.0.5 on 2022-06-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('birth_date', models.DateTimeField(verbose_name='date of birth')),
            ],
        ),
    ]
