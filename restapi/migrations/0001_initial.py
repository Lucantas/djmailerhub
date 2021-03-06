# Generated by Django 3.2.5 on 2021-08-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=253)),
            ],
        ),
        migrations.CreateModel(
            name='MailConf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(null=True)),
                ('host', models.CharField(max_length=253)),
                ('port', models.CharField(max_length=20)),
                ('sender', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('reply_to', models.CharField(max_length=255)),
                ('plain_password', models.BooleanField()),
                ('use_ssl', models.BooleanField()),
                ('purge_date', models.DateTimeField(blank=True, null=True)),
                ('body', models.TextField()),
                ('subject', models.CharField(max_length=998)),
                ('allowed_hosts', models.ManyToManyField(related_name='allowed_hosts', to='restapi.Host')),
                ('copies', models.ManyToManyField(blank=True, related_name='copy_receivers', to='restapi.Email')),
                ('receivers', models.ManyToManyField(related_name='mail_receivers', to='restapi.Email')),
            ],
            options={
                'verbose_name': 'mail configuration',
                'verbose_name_plural': 'mail configurations',
            },
        ),
    ]
