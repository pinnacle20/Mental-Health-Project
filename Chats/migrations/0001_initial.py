# Generated by Django 4.1.2 on 2023-03-25 19:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('sno', models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_receiver', to='Authentication.person')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_sender', to='Authentication.person')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('sno', models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2023, 3, 26, 1, 27, 54, 380245))),
                ('receiver', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='Authentication.person')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='Authentication.person')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Thread',
            fields=[
                ('sno', models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False)),
                ('last_message', models.DateTimeField(default=datetime.datetime(2023, 3, 26, 1, 27, 54, 379244))),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='Authentication.person')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Authentication.person')),
            ],
        ),
    ]