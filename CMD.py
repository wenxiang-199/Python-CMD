import time

print('wanxiang bulb[版本:0.424134]')
user_input = input("a:\>") 
if user_input == 'dir':
    print('<dir> user')
    print('<dir> bulb')
    print('      st32.dll')
    user_input = input("a:\>") 
    if user_input == 'cd /user':
        user_input = input("a:\\user\\>")
        if user_input == 'dir':
            print('这些文件是隐藏的，如果想继续浏览请输入:1')
            user_input = input("a:\\user\\>")
            if user_input == '1':
                print('<dir> bulb 4 SP2')
                user_input = input('a:\\user\\>')
                if user_input == 'cd /bulb 4 SP2':
                    print('要是要继续访问，请使用‘安全选项卡’')
                    time.sleep(3)
          
    if user_input == 'cd /bulb':
        print('要是要继续访问，请使用‘安全选项卡’')
        time.sleep(3)
       
    if user_input == 'st32.dll':
        print('无法直接执行.dll文件，你可以找到此文件的关联程序运行')
        time.sleep(3)
        
if user_input == 'bulb':
    print('bulb版本:bulb 4 SP2 专业版')
    time.sleep(3)

if user_input == 'cmd':
    print('由玩想科技有限公司研发，用于bulb上')
    time.sleep(3)
    
if user_input == 'python':
    print('本项目使用python开发')
    time.sleep(3)

if user_input == 'cd /user':
        user_input = input("a:\\user\\>")
        if user_input == 'dir':
            print('这些文件是隐藏的，如果想继续浏览请输入:1')
            user_input = input("a:\\user\\>")
            if user_input == '1':
                print('<dir> bulb 4 SP2')
                user_input = input('a:\\user\\>')
                if user_input == 'cd /bulb 4 SP2':
                    print('要是要继续访问，请使用‘安全选项卡’')
                    time.sleep(3)
        if user_input == 'cd /bulb 4 SP2':
                    print('要是要继续访问，请使用‘安全选项卡’')
                    time.sleep(3)

if user_input == 'cd /user/bulb 4 SP2':
     print('这些文件是隐藏的，如果想继续浏览请输入：1')
     user_input = input("a:")
     if user_input == '1':
          print('要是要继续访问，请使用‘安全选项卡’')
          time.sleep(3)

if user_input == 'unlock dir':
     print('<dir> user')
     print('<dir> users')
     print('<dir> bulb')
     print('      st32.dll')
     user_input = input('a:\\')
     if user_input == 'cd /user':
        user_input = input("a:\\user\\>")
        if user_input == 'dir':
            print('这些文件是隐藏的，如果想继续浏览请输入:1')
            user_input = input("a:\\user\\>")
            if user_input == '1':
                print('<dir> bulb 4 SP2')
                user_input = input('a:\\user\\>')
                if user_input == 'cd /bulb 4 SP2':
                    print('要是要继续访问，请使用‘安全选项卡’')
                    time.sleep(3)
     if user_input == 'cd /bulb':
        print('要是要继续访问，请使用‘安全选项卡’')
        time.sleep(3)
     if user_input == 'st32.dll':
        print('无法直接执行.dll文件，你可以找到此文件的关联程序运行')
        time.sleep(3)
     if user_input == 'cd /users':
         print('⚠无法继续操作，你应该有administrator的权限...')
         time.sleep(3)

if user_input == 'Unlock the Security tab':
    print('命令执行成功，但只可以定位到带有‘安全选项卡’的文件夹并只可以一键定位（部分可用）')
    user_input = input('a:\\')
    if user_input == 'cd /user':
        print('此文件夹的内容：')
        print('<dir> administrator')
        user_input = input('a:\\user\\')
        if user_input == 'cd /administrator':
            print('部分可用')
            time.sleep(3)
    else:
        print('只可以定位到带有‘安全选项卡’的文件夹并只可以一键定位（部分可用）')

if user_input == 'update':
    print('正在检查更新')
    print('*-------------------')
    time.sleep(1)
    print('*****---------------')
    time.sleep(1)
    print('**************------')
    time.sleep(1)
    print('********************')
    print('检查失败，没有lnternet连接')
    time.sleep(1)

if user_input == 'c:':
    user_input = input('c:\\')
    if user_input == 'dir':
        print('<dir> .')
        time.sleep(3)
    else:
        print('无法定位...')
        time.sleep(3)

if user_input == 'temp':
    print('缓存文件')
    print('117个文件，共1.57GB按Y清理')
    user_input = input('c\\')
    if user_input == 'Y':
        print('清理完成!')
        time.sleep(3)

if user_input == 'ping baidu.com /t':
    print('正在 Ping baidu.com [39.156.66.10] 具有 32 字节的数据:')
    print('无法访问目标主机')
    time.sleep(3)

if user_input == 'ping baidu.com':
    print('正在 Ping baidu.com [39.156.66.10] 具有 32 字节的数据:')
    print('无法访问目标主机')
    time.sleep(3)

if user_input == 'ping':
    print('ping的用法：')
    print('-t 一直发送请求包')
    time.sleep(3)

if user_input == 'bulb 4':
    print('bulb 4 SP2专业版')
    time.sleep(3)

if user_input == 'CPU':
    print('中央处理器的详细信息：i9-13100K')
    time.sleep(3)

if user_input == 'cmd_1.py':
    print('你怎么知道？？？')
    time.sleep(3)

if user_input == 'bulb OS':
    print('hello world!')
    print('bulb OS就是当前系统版本')
    time.sleep(3)

else:
    print (f"{user_input}这是不是一个可用的驱动器或命令和可执行程序...")
    time.sleep(3)
    
