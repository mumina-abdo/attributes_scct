# Generated by Django 5.0.6 on 2024-07-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('teachers_class', models.CharField(max_length=20)),
                ('teachers_course', models.CharField(max_length=20)),
                ('teacher_id', models.PositiveBigIntegerField()),
                ('account_number', models.CharField(max_length=20)),
                ('date_of_joining', models.DateField()),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
