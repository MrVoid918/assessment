# Generated by Django 3.2.6 on 2021-08-24 02:15

import claims.models
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_auto_20210823_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='claims',
            name='mobile_no',
            field=models.CharField(help_text='</br>Input with this format: 01XXXXXXXX', max_length=11, verbose_name='HP Number'),
        ),
        migrations.AlterField(
            model_name='claims',
            name='pdf_insurance_cover',
            field=models.FileField(help_text='Supported Formats: pdf', upload_to=claims.models.get_pdf_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Insurance Cover'),
        ),
        migrations.AlterField(
            model_name='claims',
            name='photo',
            field=models.ImageField(upload_to=claims.models.get_image_path, verbose_name='Images of Accident'),
        ),
        migrations.AlterField(
            model_name='claims',
            name='vehicle_year_make',
            field=models.PositiveSmallIntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(1950)]),
        ),
    ]