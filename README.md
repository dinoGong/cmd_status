##
用github透过网关来控制内网硬件。

本例子用的是罗技的摄像头，主板选用nanopi，系统为dietpi（基于armbian），兼容debian/ubuntu。

调用摄像头用的是fswebcam，因此需要安装fswebcam：

```
sudo apt install fswebcam
```

之后，需要配置任务，比如2分钟执行一次。

这样，每隔2分钟，就会调用checkCMD.py一次。
其中，关键代码为：
```
return_text=system("git pull |grep cmd.json")
```

意思是如果cmd.json有变化，才会进行后面的处理。至于代码中的256作为判断关键字是怎么来的，我并不清楚，只是测试时发现如果没有更新cmd.json，返回的是256。

谁若知道，欢迎赐教。

这个项目，用于远程查看我写字台上的热带鱼。

220v接入小米智能开关，用APP可以远程控制。小米智能开关上面插上usb充电器连接nanopi或树梅派。这样，APP遥控开关打开时，树梅派因为上电自动开启。这时，我想git仓库写入一个命令：
```
{
"cmd":"take-a-pic",
"time":"22：00"
}
```
每隔2分钟，程序见擦一次，发现cmd.json有变化，则执行相应的命令。（time上写的22：00是发出指令的时间，但并不做判断的依据，只是用来让cmd.json呈现可以提交的状态）


ps:定时配置

crontab -e

*/1 * * * * /usr/bin/python /你的路径/checkCMD.py

sudo service cron start
