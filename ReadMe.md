# 原神自动弹奏工具

## 关于

当前版本：0.9.1b

作者：[此号已封12138](https://space.bilibili.com/40358750)



## 使用说明：

<u>**注意：由于是按键模拟器,无法保证完全安全,请谨慎使用**</u>

<u>**使用管理员身份运行**</u>

在输入框中输入字符，点击开始即可弹奏

使用括号(英文)表示和弦，例如:(AE)表示同时按下AE

延迟为每个音符的停顿时长，单位:毫秒

编辑->启用单音延迟开启单音延迟功能，$表示延迟的单位时长

例如：

​	A$B 表示按下A延迟1个单位时间后按下B

​	$$$ 表示延长3个单位时间

​	$3 表示延长3个单位时间，同$$$

请尽可能不要输入奇怪的东西防止出现Bug



## 更新

**0.9.1b**

​	添加单音延迟

​	添加文件功能

**0.9b**

​	添加自动弹奏功能

​	添加全局延迟



## 后续更新

UI优化



## Packages

```
PyQt5
pynput(1.6.8)
pyinstaller
```



## 运行

```Python
安装python3.7和包
Python 环境下：
	直接运行src下GenshinPiano.py
build可运行exe
	在src下运行pyinstaller -F -D -w -i ./../img/hutao.ico GenshinPiano.py
```



## License

MIT