# Generated by Django 4.1.7 on 2023-02-27 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_author_name_remove_recipe_book_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_image.svg', upload_to='recipes'),
        ),
    ]