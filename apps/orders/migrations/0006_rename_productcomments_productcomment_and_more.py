# Generated by Django 4.1.3 on 2023-02-12 04:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_productcomments_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductComments',
            new_name='ProductComment',
        ),
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
        migrations.AlterModelOptions(
            name='productcomment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={},
        ),
    ]
