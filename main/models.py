from django.db import models

# Create your models here.


class User(models.Model):
    """
        用户表
    """
    name = models.CharField(max_length=200, default='name', verbose_name=u'用户名')
    age = models.IntegerField(verbose_name=u'年龄')
    phone_number = models.CharField(max_length=200, verbose_name=u'手机号', default='')
    Email = models.EmailField(verbose_name=u'邮箱')
    password = models.CharField(max_length=200, verbose_name=u'密码', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
