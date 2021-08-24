from django.core import validators
from django.db import models
import django.core.validators as val
import uuid
import os
# Create your models here.


def get_image_path(instance, filename: str):
    return os.path.join("images", str(instance.id), filename)


def get_pdf_path(instance, filename: str):
    return os.path.join("pdf", str(instance.id), filename)


class Claims(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          verbose_name="Claim ID")

    name = models.CharField(max_length=128)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=11,
                                 verbose_name="HP Number",
                                 help_text="</br>Input with this format: 01XXXXXXXX")

    vehicle_year_make = models.PositiveSmallIntegerField(
        default=2021,
        validators=[val.MaxValueValidator(2021),
                    val.MinValueValidator(1950)])

    vehicle_model = models.CharField(max_length=128)
    vehicle_no = models.CharField(max_length=10)

    date_accident = models.DateField(verbose_name="Date of Accident")
    time_accident = models.TimeField(verbose_name="Time of Accident",
                                     help_text="<br/>HH:MM am/pm")
    location = models.CharField(max_length=128,
                                verbose_name="Location of Accident")
    LOSS_CHOICES = [("OD", "Own Damage"),
                    ("KfK", "Knock for Knock"),
                    ("WD", "Windscreen Damage"),
                    ("Th", "Theft")]
    type_loss = models.CharField(default="OD",
                                 max_length=3,
                                 choices=LOSS_CHOICES,
                                 verbose_name="Accident Type")
    desc_of_loss = models.TextField(verbose_name="Description")

    BOOL_CHOICE = [('Y', 'Yes'), ('N', 'No')]
    is_report_lodged = models.CharField(
        default='Y',
        max_length=1,
        choices=BOOL_CHOICE,
        verbose_name="Are any reports lodged?")
    is_any_injured = models.CharField(
        default='Y',
        max_length=1,
        choices=BOOL_CHOICE,
        verbose_name="Is anyone injured in the accident?")

    photo = models.ImageField(verbose_name="Images of Accident",
                              upload_to=get_image_path)
    pdf_insurance_cover = models.FileField(
        validators=[val.FileExtensionValidator(["pdf"])],
        upload_to=get_pdf_path,
        verbose_name="Insurance Cover",
        help_text="Supported Formats: pdf")

    CLAIM_STATUS = [("IP", "In Progress"),
                    ("AC", "Accepted")]
    claim_status = models.CharField(default="IP",
                                    max_length=2,
                                    choices=CLAIM_STATUS)
