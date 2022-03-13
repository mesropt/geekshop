# Generated by Django 3.2.12 on 2022-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("mainapp", "0006_product_is_active")]

    operations = [
        migrations.AlterField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(db_index=True, default=True, verbose_name="категория активна"),
        )
    ]
