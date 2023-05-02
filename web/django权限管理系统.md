## Django权限管理

对于后台系统来说，权限管理是必不可少的一个环节。

### 权限管理系统的三大要素

分别是账号、角色和权限

![img](https://pic1.zhimg.com/v2-180a3a716fb544c5f4a83dc42362e050_b.png)

账号：是整个权限管理的基础，也就是因为账号把用户分为了三六九等。

角色：角色是搭建在账号与权限之间的一道桥梁。

权限：权限可分为三类：数据权限、操作权限和页面权限。我这里把权限理解为资源。所谓的权限就是对于资源的增删查改，对应于后端来说就是请求方法和请求路径

### RBAC模型

（1）定义

RBAC（Role-Based Access Control）意思是基于角色的权限控制，有别于传统模型中的直接把权限赋予账号，增加了“角色”的概念，把权限赋予角色，再将角色赋予账号。提高了账号管理效率，降低了出错的概率。

例如：当有多个账号需要配置相同的权限时，有了角色后便不需要给每个账号挨个配置权限，只需要在角色上配置权限，再把角色配置到账号上。如果想批量调整账号的权限，只需要调整账号对应的角色的权限，无需对每个账号进行调整。

（2）类型

RBAC模型根据设计需要，可分为RBAC0、RBAC1、RBAC2、RBAC3四种类型。其中RBAC0是基础，另外三种是RBAC0的升级。产品经理在进行权限系统设计时，可以结合实际情况来选择使用的RBAC模型的类型。

具体细节自行百度

### 具体需求

#### 需求一

rpa开放sass平台，用户以公司为单位进行注册，要求用户可以根据公司为单位进行注册，同个公司用户分为admin，updater，creator分别对应的权限为

admin: 作为公司中的最高权限拥有者，可以对于流程的任意增删查改

updator: 可以查看，修改同公司下的任何流程以及创建流程

creator: 可以创建和查看，没有修改权限

#### 需求二

公司之间可以开放权限给其他公司进行流程的修改和查询

### 解决思路

关于需求一可以简单理解为用户，权限、角色、部门四种类型，就是典型的rbac权限模型

用户可以根据部门和角色拥有对于的权限，可以对于数据进行各种操作。

那么需求二中公司之间可以开放权限给其他公司进行流程的修改和查询该如何做呢？用户和部门角色有关目前已有的数据库模型无法满足。

没有方法就使用`中间件`

这里采用的为增加一个群组的概念，群组和权限、用户关联

查询到用户的群组，找到对应的权限进行操作

#### 基本思路

##### 需求一

- 创建用户表，权限表，角色表，部门表，用户部门表，部门角色表，角色权限表，其中权限表是对于着请求方法，请求路径进行解析
- 根据用户查到部门，部门查到角色，角色查到权限从而达到用户和权限之间的关系
- 自定义权限验证方法，判断用户是否有权限处理数据

##### 需求二

- 

#### 代码实现

一、创建model类

```python
# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : models.py
# Time       ：2023/5/1 22:12
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

from django_celery_demo.libs.base_model import BaseModel


class Users(AbstractUser):
    name = models.CharField(max_length=20, default='', blank=True, verbose_name='真实姓名')
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True, default=None, verbose_name='手机号码')
    image = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', blank=True, verbose_name='头像')
    roles = models.ManyToManyField('Roles', db_table='users_to_roles', blank=True, verbose_name='角色')
    department = models.ForeignKey('Departments', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='部门')
    group_owner = models.BooleanField(default=False, verbose_name='是否为群组owner')
    groups = models.ManyToManyField('SystemGroup', db_table='users_to_groups', blank=True, verbose_name='群组')

    class Meta:
        db_table = 'oauth_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username

    def _get_user_permissions(self):
        # 获取用户权限
        permissions = list(filter(None, set(self.roles.values_list('permissions__sign', flat=True))))
        if 'admin' in self.roles.values_list('name', flat=True):
            permissions.append('admin')
        return permissions

    def _get_group_permissions(self):
        # 获取群组信息
        permissions = list(filter(None, set(self.groups.values_list('permissions__sign', flat=True))))
        return permissions

    def get_user_info(self):
        # 获取用户信息
        user_info = {
            'id': self.pk,
            'username': self.username,
            'name': self.name,
            'avatar': '/media/' + str(self.image),
            'email': self.email,
            'permissions': self._get_user_permissions(),
            'department': self.department.name if self.department else '',
            'mobile': '' if self.mobile is None else self.mobile,
            'groups': self._get_group_permissions(),

        }
        return user_info


class SystemGroup(BaseModel):
    name = models.CharField(max_length=64, verbose_name='群组')
    permissions = models.ManyToManyField('Permissions', db_table='group_to_permissions', blank=True, verbose_name='权限')
    desc = models.CharField(max_length=50, blank=True, default='', verbose_name='描述')
    owner = models.ForeignKey('Users', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='群组owner')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'system_group'
        verbose_name = '群组'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Permissions(BaseModel):
    """
    权限
    """
    method_choices = (
        (u'POST', u'增'),
        (u'DELETE', u'删'),
        (u'PUT', u'改'),
        (u'PATCH', u'局部改'),
        (u'GET', u'查')
    )

    name = models.CharField(max_length=30, verbose_name='权限名')
    sign = models.CharField(max_length=30, unique=True, verbose_name='权限标识')
    menu = models.BooleanField(verbose_name='是否为菜单')  # True为菜单,False为接口
    method = models.CharField(max_length=8, blank=True, default='', choices=method_choices, verbose_name='方法')
    path = models.CharField(max_length=200, blank=True, default='', verbose_name='请求路径正则')
    pid = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父权限')
    desc = models.CharField(max_length=30, blank=True, default='', verbose_name='权限描述')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'system_permissions'
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Roles(BaseModel):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name='角色')
    permissions = models.ManyToManyField('Permissions', db_table='roles_to_permissions', blank=True, verbose_name='权限')
    desc = models.CharField(max_length=50, blank=True, default='', verbose_name='描述')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'system_roles'
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        ordering = ['id']


class Departments(BaseModel):
    """
    组织架构 部门
    """
    name = models.CharField(max_length=32, unique=True, verbose_name='部门')
    pid = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父部门')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'system_departments'
        verbose_name = '部门'
        verbose_name_plural = verbose_name
        ordering = ['id']

```



#### 二、定义序列化类

详情和参见代码`src/oauth/serializers`

#### 三、定义验证方法

```python
# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : rbac_permission.py
# Time       ：2023/5/1 22:35
# Author     ：blue_moon
# version    ：python 3.7
# Description：
"""
import json
import re

from django.conf import settings
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission

from django_celery_demo.libs.redis_permissions_storage import redis_storage_permissions
from oauth.models import Permissions
from oauth.serializers.permission import PermissionsResourceSerializer


class UserLock(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '用户已被锁定,请联系管理员'
    default_code = 'not_authenticated'


class RbacPermission(BasePermission):
    """
    自定义权限认证
    """

    @staticmethod
    def pro_uri(uri):
        base_api = settings.BASE_API
        uri = '/' + base_api + '/' + uri + '/'
        return re.sub('/+', '/', uri)

    def has_permission(self, request, view):
        # 验证用户是否被锁定
        if not request.user.is_active:
            raise UserLock()
        request_url = request.path
        # 如果请求url在白名单，放行
        for safe_url in settings.WHITE_LIST:
            if re.match(settings.REGEX_URL.format(url=safe_url), request_url):
                return True
        # admin权限放行
        conn = get_redis_connection('user_info')
        if not conn.exists('user_permissions_manage'):
            redis_storage_permissions(conn)
        if conn.exists('user_info_%s' % request.user.id):
            user_permissions = json.loads(conn.hget('user_info_%s' % request.user.id, 'permissions').decode())
            if 'admin' in user_permissions:
                return True
        else:
            if 'admin' in request.user.roles.values_list('name', flat=True):
                return True
        # 根据rbac设置权限
        rbac_permission = self.rbac_permission_validate(request)
        return any([rbac_permission, ])

    @staticmethod
    def rbac_permission_validate(request):
        """rbac和群组权限验证，这里为了简单没有加部门的关联"""
        # 获取用户的所有权限
        user_info = request.user.get_user_info()
        permissions = user_info.get('permissions', [])
        groups = user_info.get('groups', [])
        permissions = permissions + groups
        # 获取具体的method和url
        permissions_info = Permissions.objects.filter(sign__in=permissions).all()
        permissions_info = PermissionsResourceSerializer(permissions_info, many=True).data
        # 判断请求方法和请求路径是否符合权限配置的路径
        permissions_info = [dict(item) for item in permissions_info]
        for permission in permissions_info:
            if request.method == permission.get('method') and request.path == permission.get('path'):
                return True
        return False

```



#### 四、修改配置类

```python
# 第一处修改REST_FRAMEWORK
REST_FRAMEWORK = {
   ...
    # 权限验证
    'DEFAULT_PERMISSION_CLASSES': (
        'django_celery_demo.libs.middleware.rbac_permission.RbacPermission'  # 自定义权限认证
    ),
   ...
}
# 第二处修改AUTH_USER_MODEL
# 自定义users
AUTH_USER_MODEL = "oauth.Users"
```

#### 五、修改admin.py

```python
from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from oauth.models import Permissions, Roles, Departments, SystemGroup

Users = get_user_model()

# Register your models here.
admin.site.register(Users)
admin.site.register(Permissions)
admin.site.register(Roles)
admin.site.register(Departments)
admin.site.register(SystemGroup)
```



### 问题

#### 一、关于flask 的权限管理应该怎么做？

其实原理都是一样的，不过是数据库的模型类不一样而已

在哪里写权限验证方法呢

`before request`这里是没有请求过来之后的第一个入口，可以在这里进行权限验证



