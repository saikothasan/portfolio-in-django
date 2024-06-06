# Generated by Django 3.1.7 on 2021-07-02 19:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=150)),
                ('section_description', models.CharField(max_length=255)),
                ('services_name', models.CharField(max_length=150)),
                ('services_description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=150)),
                ('section_description', models.CharField(max_length=255)),
                ('testimonials_name', models.CharField(max_length=150)),
                ('testimonials_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('testimonials_image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
