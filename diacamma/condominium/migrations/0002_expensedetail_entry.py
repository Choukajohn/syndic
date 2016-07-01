# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.utils import translation
from django.conf import settings

from lucterios.CORE.models import PrintModel


def printer_model(*args):
    translation.activate(settings.LANGUAGE_CODE)
    PrintModel().load_model("diacamma.condominium", "Owner_0001")


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_add_param'),
        ('condominium', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': [
                '-date'], 'verbose_name': 'expense', 'verbose_name_plural': 'expenses'},
        ),
        migrations.AddField(
            model_name='expensedetail',
            name='entry',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.EntryAccount', verbose_name='entry'),
        ),
        migrations.AddField(
            model_name='owner',
            name='information',
            field=models.CharField(
                default='', max_length=200, null=True, verbose_name='information'),
        ),
        migrations.RunPython(printer_model),
    ]
