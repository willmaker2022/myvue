from django.contrib.auth.models import User
from datetime import timezone
from django.db import models
# Create your models here.


class CommonInfo(models.Model):

    # 开始时间 auto_now_add=True,
    startday = models.DateField(verbose_name="下单时间", null=True)
    # 结束时间
    endday = models.DateField(verbose_name="交货时间", null=True)
    # 备注
    remark = models.TextField(default="",verbose_name="备注")

    status_choice = (
        ('pending',"未开始"),
        ('process',"进行中"),
        ('finish',"已完成")
    )
    status = models.CharField(
        max_length=10,
        choices=status_choice,
        default='pending',
        verbose_name="订单状态",
    )

    class Meta:
        abstract = True

class Productplan(CommonInfo):
    # 订单号
    orderid = models.CharField(max_length=10,verbose_name="订单号")
    #订单分类
    category_choice = (
        ('std',"标准"),
        ('unstd',"非标")
    )
    category = models.CharField(
        max_length=5,
        choices=category_choice,
        default='std',
        verbose_name="订单类型",
    )
    # 型号
    productid = models.CharField(max_length=10,verbose_name="产品型号")
    # 序列号
    serial = models.CharField(max_length=10,verbose_name="序列号")
    # 用户
    customer = models.CharField(max_length=20,verbose_name="用户")
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer + "_SN"+ self.serial

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "订单管理"

class ProcessElPrepare(CommonInfo):
    orderid = models.OneToOneField(
        Productplan,
        on_delete=models.CASCADE,
        related_name='proel',
        primary_key=True
    )
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "电路板准备"


class ProcessMePrepare(CommonInfo):
    orderid = models.OneToOneField(
        Productplan,
        on_delete=models.CASCADE,
        related_name='prome',
        primary_key=True
    )
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "机械件准备"


class ProcessScPrepare(CommonInfo):
    orderid = models.OneToOneField(
        Productplan,
        on_delete=models.CASCADE,
        related_name='prosc',
        primary_key=True
    )
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "干涉仪准备"


class ProcessAssemble(CommonInfo):
    orderid = models.OneToOneField(
        Productplan,
        on_delete=models.CASCADE,
        related_name='proas',
        primary_key=True
    )
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "装配中"

class ProcessTesting(CommonInfo):
    orderid = models.OneToOneField(
        Productplan,
        verbose_name="订单号",
        on_delete=models.CASCADE,
        related_name='prots',
        primary_key=True
    )
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = "测试中"

    def __str__(self):
        return self.orderid.customer

class ProductHistory(models.Model):
    #操作者
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='user'
    )
    # 订单
    orderid = models.ForeignKey(
        Productplan,
        verbose_name="订单号",
        on_delete=models.CASCADE,
        related_name='product_history',
        primary_key=False
    )
    # 操作项目
    proitem = models.CharField(max_length=10, verbose_name="操作项目")
    # 新内容
    newcontent = models.CharField(max_length=10, verbose_name="新内容")
    # 操作时间
    operateday = models.DateTimeField(verbose_name="操作时间", null=True)

    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural="订单历史"

    def __str__(self):
        return self.orderid.customer