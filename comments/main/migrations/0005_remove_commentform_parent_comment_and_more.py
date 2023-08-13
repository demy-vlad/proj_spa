# Generated by Django 4.2.4 on 2023-08-13 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_parent_comments_commentform_parent_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentform',
            name='parent_comment',
        ),
        migrations.AddField(
            model_name='commentform',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.commentform'),
        ),
    ]
