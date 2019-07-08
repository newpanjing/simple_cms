# simple cms

手机版URL：
> localhost:8000/mobile

PC版URL：
> localhost:8000

## 初始化项目

```
git clone git@github.com:newpanjing/simple_cms.git
```

## 安装依赖包

```
pip install -r requirements.txt
```

## 配置数据库
找到项目中的settings.py文件，替换数据库的host和用户名密码，在执行以下步骤

## 执行迁移

### 生成迁移文件
```
python manage.py makemigrations
```

### 执行迁移
```
python manage.py migrate
```

## 创建超级用户

```
python manage.py createsuperuser
```

## 启动查看

```
python manage.py runserver 8000
```

## 访问地址

### 前台地址

```
http://localhost:8000
```

### 后台地址

```
http://localhost:8000/admin
```

用户名密码创建步骤请看：[创建超级用户](创建超级用户)


# 注意事项

本程序开放源码，但是不提供任何技术支持，有问题请自行百度。