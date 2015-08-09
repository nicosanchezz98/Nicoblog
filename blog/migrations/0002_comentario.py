# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=50, verbose_name=b'publicado por:')),
                ('contenido', models.TextField(max_length=500, verbose_name=b'Ahi lo anoto')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha')),
                ('post', models.ForeignKey(to='blog.Entrada')),
            ],
        ),
    ]
