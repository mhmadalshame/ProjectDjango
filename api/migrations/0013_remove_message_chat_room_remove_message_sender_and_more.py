# Generated by Django 4.2.1 on 2024-01-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_purchaseinvoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat_room',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
