# Generated by Django 4.2.4 on 2023-10-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_remove_historicaltaskdependency_created_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="dependencies",
            field=models.ManyToManyField(related_name="tasks", to="api.dependency"),
        ),
        migrations.AlterField(
            model_name="task",
            name="job",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="api.job",
            ),
        ),
    ]
