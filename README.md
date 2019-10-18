# ArTools

**为方便日常计算机操作而写的一些小工具**

## jre信任证书注册

**依赖: python3、PyUserInput-可以通过pip直接安装**

path: src/main/code/org/ar/artools/pytools/cerregister/

link: link/cerregister(双击快捷方式运行，记得修改快捷方式的启动参数)
    parameters: 
        alias 注册别名
        filepath 证书路径

function: 注册jre对https网站的信任证书

## 一键截屏

**依赖: python3、PyHook3、pywin32**

path: src/main/code/org/ar/artools/pytools/screenshots/

link: link/cutshot(双击快捷方式运行，按PrtSc键截屏)

function: 一键截取全屏，并以当前时间.png的形式保存在src\main\resources\screenshots\pictures中

**note: 直接pip安装的pyHook在操作界面中有中文时会出bug，这里使用的是PyHook3-1.6.1**
