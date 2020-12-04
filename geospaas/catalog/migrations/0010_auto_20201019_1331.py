# Generated by Django 3.0 on 2020-10-19 13:31

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201012_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='entry_id',
            field=models.TextField(default=uuid.uuid4, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_.-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]