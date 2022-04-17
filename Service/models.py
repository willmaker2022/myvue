from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from productplan.models import Productplan
#为了删除图片
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Service(models.Model):
    # 订单
    orderid = models.ForeignKey(
        Productplan,
        null=True,
        blank=True,
        verbose_name="订单号",
        on_delete=models.CASCADE,
        related_name='order',
        primary_key=False
    )
    #操作者
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='user_service'
    )
    # 报告类型
    style_choice = (
        ('servicein', "保内维修"),
        ('serviceout', "保外维修"),
        ('production', "工艺改进")
    )
    style = models.CharField(
        max_length=10,
        choices=style_choice ,
        default='servicein',
        verbose_name="报告类型",
    )

    description = models.TextField(default="", null=True, blank=True, verbose_name="问题描述")
    actions = models.TextField(default="", null=True, blank=True, verbose_name="操作内容")
    created = models.DateTimeField(default=timezone.now, null=True,verbose_name='创建时间')
    pictures = models.ImageField(upload_to='service_pictures/%Y%m%d/', blank=True)
    # 备注
    remark = models.TextField(default="",verbose_name="备注")

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "维修记录"

@receiver(pre_delete, sender=Service)
def delete(sender, instance, **kwargs):
    instance.pictures.delete(False)

