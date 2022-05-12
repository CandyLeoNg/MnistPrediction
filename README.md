# mnistPredict
创建一个基于Django的mnist手写题识别项目
```
命令：python manage.py runserver 127.0.0.1:3333
```

```
网址：http://127.0.0.1:3333/login/
```

# 步骤

- 首先，在conda环境下安装Django
```
pip install Django
```

- 在某个盘下创建Django项目
```
django-admin startproject 项目名
```

- 创建完成后，用pycharm -点击open - 项目名


- 在虚拟环境下创建应用程序文件
```
python manage.py startapp mnistMain
```
![image](https://user-images.githubusercontent.com/63994835/163525519-115b1592-6dbc-453f-b9df-34a2ebe6eb8f.png)

- 在setting中的INSTALLED_APPS 的列表中添加 创建好的应用程序名字

![image](https://user-images.githubusercontent.com/63994835/163525540-d804d298-ac89-4186-8f4c-5bebe410377d.png)

- 在应用程序mnistMain中的view添加自己需要添加的功能方法

![image](https://user-images.githubusercontent.com/63994835/163525659-cc7b2b7e-c96d-403b-a061-f6e6226ecaf2.png)

- urls.py中导入方法

![image](https://user-images.githubusercontent.com/63994835/163525708-9bc4a115-7a45-416c-8740-d746adcef7c0.png)

- 开启服务

在终端输入以下命令：
```
python manage.py runserver 127.0.0.1:3333
```
访问 http://127.0.0.1:3333/login/ 即可

![image](https://user-images.githubusercontent.com/63994835/168125654-8810ab3e-4a02-4f85-a227-a8333ac0789d.png)




