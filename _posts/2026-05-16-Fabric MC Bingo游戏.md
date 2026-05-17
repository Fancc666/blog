---
title: Fabric MC Bingo游戏
date: 2026-05-16 21:38
tags: [mc,java,服务器]
categories: [研究]
---

## 前言

听舍友说一直在和初中同学玩一个mc整合包，叫`Yet Another Bingo`，玩法就是系统每局发放5*5的棋盘，玩家分了组，每个组的玩家都要尽可能多的收集到这些物品，最先完成任务的组获胜。

于是我想试试看能不能搭一个这样的服务器和舍友一起玩，有了此篇研究。

## 下载服务端

### 安装Java

<a href="https://www.oracle.com/cn/java/technologies/downloads/#java21" target="_blank">https://www.oracle.com/cn/java/technologies/downloads/#java21</a>

推荐下载jdk21，比较新也比较稳定。

![Img](https://qnhdpic.twt.edu.cn/download/origin/4a213861d114c7e1fde48fe27e7c7f32.png)

由于我是在Windows10下面开服，所以选了Windows的x64 Installer下载。

下载完一路下一步即可，使用`java --version`检查安装状态。

### 下载MC服务端

由于bingo游戏只能跑在Fabric服务器下，我们要先下载Fabric MC的服务端。

<a href="https://fabricmc.net/use/server/" target="_blank">https://fabricmc.net/use/server/</a>

![Img](https://qnhdpic.twt.edu.cn/download/origin/f978123bc27c069f361a35957edc1cd2.png)

我这里以1.21.10版本为例，点击下载`.jar`文件。这里下载的时候可能会把源代码下载下来，是一个`.zip`文件，非常奇怪。如果遇到这个问题，我们得修正一下url地址，把问号后查询字符串都删掉，再进行下载，我在macOS下是没有这个问题的。

<a href="https://meta.fabricmc.net/v2/versions/loader/1.21.10/0.19.2/1.1.1/server/jar" target="_blank">https://meta.fabricmc.net/v2/versions/loader/1.21.10/0.19.2/1.1.1/server/jar</a>

### 下载Bingo插件

玩Bingo游戏那肯定得下载一个Bingo游戏的插件，这个插件还依赖一个Fabric API插件，两个都得下载，以下是下载地址。

**Fabric API**

<a href="https://modrinth.com/mod/fabric-api" target="_blank">https://modrinth.com/mod/fabric-api</a>

点击Download，一定记得选好版本。

![Img](https://qnhdpic.twt.edu.cn/download/origin/f13561db26a754383527f88b537fbf5b.png)

**Yet Another Bingo**

<a href="https://modrinth.com/mod/yet-another-minecraft-bingo" target="_blank">https://modrinth.com/mod/yet-another-minecraft-bingo</a>

![Img](https://qnhdpic.twt.edu.cn/download/origin/a5827fe73d733949377258a33fd7b716.png)

## 启动服务端

我们需要先运行游戏jar构建下载整个目录，我们新建一个`start.bat`文件，里面填写

```bat
@echo off
java -Xmx8G -Xms8G -jar fabric-server-mc.1.21.10-loader.0.19.2-launcher.1.1.1.jar
pause
```

双击启动，然后等待一会，会弹出一个eula提示，然后打开目录下的`eula.txt`，把false改成true来同意eula协议。

```text
#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://aka.ms/MinecraftEULA).
#Sun May 10 17:07:29 CST 2026
eula=true
```

然后你的目录应该长这样。

![Img](https://qnhdpic.twt.edu.cn/download/origin/cd781227a0110cd9a5b17de21ce6b8b3.png)

接下来把两个下载的插件放进`mods`目录。

![Img](https://qnhdpic.twt.edu.cn/download/origin/c962b61d798bbd45fe96fb276563b17d.png)

这样应该就可以了，我们再次运行`start.bat`。

![Img](https://qnhdpic.twt.edu.cn/download/origin/9dac7d9eb37cbd8ea8cbc2f31787b01a.png)

弹出这个界面就是启动成功了，我们可以顺便把自己设成服主，使用以下命令。

```text
/op [username]
```

一些其他更复杂的网络设置，请参看[开始游戏](#开始游戏)板块。

## 客户端（可选）

这个Yet Another Bingo即使不安装客户端整合包，用1.21.10原版mc也是可以游玩的，但是体验不如安装了整合包，那为了更好的游戏体验我还是建议安装一下客户端整合包。

这个整合包是在玩家客户端安装的，千万别搞混了，服务端上那个叫*插件Mods*，客户端这个叫*整合包ModPacks*，这里我们使用`Yet Another Bingo: Ultimate`。

<a href="https://modrinth.com/modpack/yet-another-bingo-ultimate" target="_blank">https://modrinth.com/modpack/yet-another-bingo-ultimate</a>

依旧要选择好版本

![Img](https://qnhdpic.twt.edu.cn/download/origin/1680046dfe8b20851b58fff9444a01b3.png)

然后下载完是一个`.mrpack`文件，里面记录了整合包的所有插件和他们的版本，我和同学使用`.zip`安装的，不过`.mrpack`好像也可以。直接把这个文件拖进你的启动器就好，PCL和HMCL都可以。

## 开始游戏

服务端可能需要修改一些配置获得更好的游戏体验，这里不赘述了。

都配置好，启动服务端就可以开始游戏了！在多人联机里输入服务器地址加端口号，或者你给ip绑定一个dns的a记录，在srv记录里面写好端口，具体配置如下。（这个域名配置是可选的，不是必须弄，但是你的公网ip是必须的）

![Img](https://qnhdpic.twt.edu.cn/download/origin/d9550df0fd7b4b02c253943b42834ec4.png)

![Img](https://qnhdpic.twt.edu.cn/download/origin/b598bb9ded7199fb114b10de41cb6294.png)

注意这个SRV记录，一定得是`_minecraft._tcp.你的域名`（是二级域名就得写二级域名）。还得注意我写的`55565`是端口，你需要根据自己实际情况修改。

进入游戏，开始愉快的玩耍吧！另外如果你想和我们一起玩mc bingo游戏，也随时欢迎联系我。玩家数量才是多人游戏好玩的关键。

附游戏截图，我使用的是HMCL启动器。

选择`Yet Anothor Bingo`实例

![Img](https://qnhdpic.twt.edu.cn/download/origin/d83e17adc093ef2c0ae6bad3f2d582c7.png)

游戏界面

![Img](https://qnhdpic.twt.edu.cn/download/origin/4bc8fe550c68fb1f145e5306ef8f9d53.png)

多人游戏

![Img](https://qnhdpic.twt.edu.cn/download/origin/6860e8163e7d9ecd848ae6770ee1d6ef.png)

Bingo Lobby

![](https://qnhdpic.twt.edu.cn/download/origin/ee3f161ee1d1aa22254fef8aad38d4c5.png)

游玩愉快！
