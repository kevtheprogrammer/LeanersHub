# Generated by Django 4.1.7 on 2023-03-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assessments", "0004_remove_answermodel_qtype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answermodel",
            name="answer_text",
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]
