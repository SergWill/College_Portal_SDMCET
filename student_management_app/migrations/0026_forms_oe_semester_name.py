# Generated by Django 4.0.3 on 2022-06-27 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0025_remove_forms_oe_semester_name_forms_oe_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms_oe',
            name='semester_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student_management_app.semester_oe'),
        ),
    ]
