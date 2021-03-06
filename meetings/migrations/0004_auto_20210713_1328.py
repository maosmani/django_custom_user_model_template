# Generated by Django 3.2.4 on 2021-07-13 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_meetings_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='about_meeting',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='meetings',
            name='zoom_url',
            field=models.URLField(),
        ),
    ]
