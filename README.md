# keyboard_monitor_python
Monitor keyboard using python

## main fun()
```
def getKey():
    if os.name == 'nt':
      return msvcrt.getch()   # 识别键盘功能键

    fd = sys.stdin.fileno()
    # fd--文件描述符。文件描述符是一个低级概念，它是一个整数，每个打开的文件都有一个唯一的文件描述符。0-标准输入；1-标准输出；2-标准错误
    tty.setraw(fd)
    #将文件描述符fd的模式更改为raw。raw和cbreak函数模式都可以禁止行缓冲(按键直接作用，不需要回车和换行指令)，raw模式在(CTRLC)和(CTRLZ)字符下不回显
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    # select函数阻塞进程，监控inputs中的套接字(带fileon()方法的文件句柄)，当其中有套接字满足可读的条件（第一个参数为可读，第二个参数可写），则把这个套接字返回给rs，然后程序继续运行。
    # 当套接字缓冲区大于1byte时，就被标记为可读。当套接字收到客户端发来的数据，变成可读，然后select就会把这个套接字取出来，进入下一步程序。

    if rlist:
        key = sys.stdin.read(1) # 最多读取一个字节，以字符串的形式返回
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    # termios:该模块提供了一个用于tty I/O控制的POSIX调用的接口
    # tcsetattr:从属性设置文件描述符fd的tty属性，将终端属性设置为原先的标准模式
    # 参数二: 确定属性何时发生更改。TCSANOW立即更改，TCSADRAIN在传输所有排队输出后更改，TCSAFLUSH在传输所有排队输出并丢弃所有排队输入后更改

    return key
```
