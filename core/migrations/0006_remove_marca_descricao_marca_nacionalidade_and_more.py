# Generated by Django 5.0.6 on 2024-07-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_marca"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marca",
            name="descricao",
        ),
        migrations.AddField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="marca",
            name="nome",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
