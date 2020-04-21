# Generated by Django 3.0.5 on 2020-04-21 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=200, verbose_name='用户名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('phone_number', models.CharField(default='', max_length=200, verbose_name='手机号')),
                ('Email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=200, null=True, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]