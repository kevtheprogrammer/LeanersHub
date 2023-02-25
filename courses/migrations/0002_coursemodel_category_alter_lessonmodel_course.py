# Generated by Django 4.1.7 on 2023-02-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursemodel",
            name="category",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="courses.coursecategorymodel",
            ),
        ),
        migrations.AlterField(
            model_name="lessonmodel",
            name="course",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course",
                to="courses.coursemodel",
            ),
        ),
    ]