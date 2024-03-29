# Generated by Django 5.0.1 on 2024-01-26 16:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('memo', models.TextField(verbose_name='Description')),
                ('priority', models.IntegerField(choices=[(0, 'Faible'), (1, 'Moyen'), (2, 'Elevé'), (3, 'Critique')], verbose_name='Priority')),
                ('duedate', models.DateField(verbose_name='Due date')),
                ('status', models.IntegerField(choices=[(0, 'A faire'), (1, 'En cours'), (2, 'Terminé'), (3, 'Annulé'), (4, 'En attente'), (5, 'En pause'), (6, 'En attente de validation')], verbose_name='Status')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ['-priority'],
            },
        ),
    ]
