# Generated by Django 4.1.2 on 2023-03-24 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0006_alter_chat_thread_last_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_thread',
            name='last_message',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 25, 5, 22, 59, 214831)),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 25, 5, 22, 59, 214831)),
        ),
    ]
