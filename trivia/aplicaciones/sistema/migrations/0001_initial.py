# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'fotos/', blank=True)),
                ('correo', models.EmailField(max_length=70, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
