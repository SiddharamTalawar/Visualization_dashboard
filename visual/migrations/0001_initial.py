# Generated by Django 4.2.1 on 2023-06-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=100, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=100, null=True)),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('insight', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.TextField(blank=True, max_length=550, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True)),
                ('start_year', models.CharField(blank=True, max_length=100, null=True)),
                ('impact', models.CharField(blank=True, max_length=100, null=True)),
                ('added', models.CharField(blank=True, max_length=100, null=True)),
                ('published', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.TextField(blank=True, max_length=500, null=True)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
