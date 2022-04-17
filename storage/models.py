from django.contrib.auth.models import User
from django.db import models
from productplan.models import Productplan
# Create your models here.
from django.utils import timezone
import datetime


class Storage(models.Model):
    sId = models.CharField(max_length= 10, verbose_name='库存品代码')    #代码
    spartNumber = models.CharField(max_length=200, null=True, blank=True, verbose_name='物料号')       #物料号
    sName = models.CharField(max_length=20, null=True, verbose_name='品名')       #品名
    sDescription = models.TextField(max_length=100, null=True, blank=True, verbose_name='描述') #描述
    sCount = models.IntegerField(null=True, verbose_name='库存余量') #库存余量
    sUnit = models.CharField(max_length=5, null=True, verbose_name='单位')  #单位
    ssafeCount = models.IntegerField(null=True, verbose_name='安全库存') #安全库存
    sArea = models.CharField(max_length=10, null=True, verbose_name='存放区域') #存放区域
    sPosition = models.CharField(max_length=10, null=True, verbose_name='存放库位') #存放库位
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    remark = models.TextField(default="",  null=True, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "库存表"

    def __str__(self):

        if self.sName:
            return self.sName
        else:
            return "未命名"

#重写出入库记录
class InOutStorage(models.Model):
    #操作这
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='user_inout'
    )
    #库存品
    storage = models.ForeignKey(
        Storage,
        # null=True,
        # blank=True,
        on_delete=models.CASCADE,
        related_name='storage_inout'
    )
    #该库存给哪个订单的，默认为空，可为空，入库时为空
    product = models.ForeignKey(
        Productplan,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='product_inout'
    )
    #操作方向:入库还是出库
    direction_choice = (
        ('in',"入库"),
        ('out',"出库"),
        ('buy', "采购")
    )
    direction = models.CharField(
        max_length=5,
        choices=direction_choice,
        default='out',
        verbose_name="操作方向",
    )
    lCount = models.IntegerField(null=False,default=0,verbose_name='数量')
    operateday = models.DateTimeField(verbose_name="操作日期")
    remark = models.TextField(default="", null=True,blank=True, verbose_name="备注")

    class Meta:
        ordering = ('-operateday',)
        verbose_name_plural = "出入库记录"