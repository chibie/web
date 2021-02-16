# Generated by Django 2.2.4 on 2021-02-03 06:46

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0170_auto_20210202_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('addr', models.GenericIPAddressField(db_index=True, null=True)),
                ('comments', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(help_text='Is the block active?')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]