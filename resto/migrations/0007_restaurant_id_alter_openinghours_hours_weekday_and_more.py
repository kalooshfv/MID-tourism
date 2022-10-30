# Generated by Django 4.1 on 2022-10-25 23:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0006_auto_20221025_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123456, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='hours_weekday',
            field=models.IntegerField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='resto_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
