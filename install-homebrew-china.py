# -*- coding:  utf-8 -*-
import os,sys,subprocess
curFileDir = os.path.dirname(__file__)
installShFileName = 'install222.sh'

#给install.sh加权限
# print('给' + installShFileName + '加执行权限，需要输入电脑密码: ')
# pipe = subprocess.Popen("sudo chmod +x " + curFileDir + "/" + installShFileName, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# (outData , errData) = pipe.communicate()
# if pipe.returncode <= 1:
#     print('OK')
#     print(outData.decode())
# else:
#     print(errData.decode())


#运行install.sh
def runInstallSh() :
    print('开始运行'+installShFileName)
    pipe = subprocess.Popen(["sh", curFileDir + "/" + installShFileName], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    # while(True):
    #     # returns None while subprocess is running
    #     retcode = pipe.poll() 
    #     line = pipe.stdout.readline()
    #     yield line    
    #     if retcode is not None:
    #         break

    (outData , errData) = pipe.communicate()
    if pipe.returncode <= 1:
        print('OK')
        print(outData.decode())
    else:
        print(errData.decode())


runInstallSh()