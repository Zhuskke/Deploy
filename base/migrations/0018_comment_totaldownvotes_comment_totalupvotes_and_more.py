# Generated by Django 5.0.2 on 2024-04-17 05:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_worksheet_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='totalDownvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='totalUpvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(max_length=10)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'comment')},
            },
        ),
    ]
