# Generated by Django 5.1.3 on 2024-11-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wesite1', '0003_newsletter_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
