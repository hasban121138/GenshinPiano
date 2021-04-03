**版本：0.9b**

**作者：**[此号已封12138](https://space.bilibili.com/40358750)

**注意：**

``` 
由于是按键模拟器,无法保证完全安全,请谨慎使用
```



**使用说明：**

<u>**使用管理员身份运行**</u>

```

在输入框中输入字符，点击开始即可弹奏
使用括号(英文)表示和弦
例如:(AE)表示同时按下AE
延迟为每个音符的停顿时长，单位:毫秒
请尽可能不要输入奇怪的东西防止出现Bug
```



**Packages：**

```
PyQt5
pynput(1.6.8)
pyinstaller
```

**运行**

```Python
安装python3.7和包
Python 环境下：
	直接运行src下GenshinPiano.py
build可运行exe
	在src下运行pyinstaller -F -D -w -i ./../img/hutao.ico GenshinPiano.py
```

**后续更新**

```
1.每个按键的单独时间
2.多个窗口
3.UI优化
```

