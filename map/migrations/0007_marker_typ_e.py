# Generated by Django 4.0.3 on 2023-02-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_typemarker'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='typ_e',
            field=models.ManyToManyField(related_name='type_marker', to='map.typemarker'),
        ),
    ]
