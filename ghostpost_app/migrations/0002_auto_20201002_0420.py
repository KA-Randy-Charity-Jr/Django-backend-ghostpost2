# Generated by Django 3.1.1 on 2020-10-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='boasts',
        ),
        migrations.RemoveField(
            model_name='ghostpost',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='ghostpost',
            name='post_date',
        ),
        migrations.RemoveField(
            model_name='ghostpost',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='isboast',
            field=models.CharField(choices=[('BOAST', 'BOAST'), ('ROAST', 'ROAST')], default='BOAST', max_length=5),
        ),
    ]
