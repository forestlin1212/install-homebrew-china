# -*- coding:  utf-8 -*-
import os
import sys,shutil
from subprocess import PIPE, STDOUT, Popen
from pathlib import Path

curFileDir = os.path.dirname(__file__)
ustcSource = 'mirrors.ustc.edu.cn'
installShFileName = 'install.sh'

def runCommand(command, endOutpuptStr=""):
    """
    执行一个命令，实时打印命令的输出。直到命令执行结束。
    command格式: eg. ls -all, 则传入数组 ["ls","-all"]
    如果输出了endOutpuptStr开头的文字，则终止命令。
    返回是否执行成功。
    """
    isSucess = True
    with Popen(command, stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True) as pipe:
        for line in pipe.stdout:
            print(line, end='')
            if endOutpuptStr != "" and line.startswith(endOutpuptStr):
                print('强制结束命令')
                pipe.kill()
                break

        if pipe.wait() > 0:
            isSucess = False

    return isSucess

def runCommandSerial(command, endOutpuptStr=""):
    """
    执行一个命令，实时打印命令的输出。直到命令执行结束。
    command格式: eg. ls -all, 则传入数组 ["ls","-all"]
    如果输出了endOutpuptStr开头的文字，则终止命令。
    如果最终命令执行失败，则退出程序。
    """
    isSucess = runCommand(command, endOutpuptStr)
    if not isSucess:
        exit()

def getCurrentShellName():
    """
    获取当前shell是zsh还是bash
    """
    pipe = Popen("echo $SHELL", shell=True, stdin=PIPE, stdout=PIPE)
    (outData , errData) = pipe.communicate()
    shellStr = outData.decode().strip()
    if shellStr.endswith("zsh"):
        return "zsh"
    elif shellStr.endswith("bash"):
        return "bash"
    else:
        return "other"

#给install.sh加权限
print('给' + installShFileName + '加执行权限，需要输入电脑密码: ')
runCommandSerial(["sudo", "chmod", "+x", curFileDir + "/" + installShFileName])

#运行install.h，到“Cloning into”时，停止。
print('开始运行' + installShFileName)
runCommandSerial(["sh", curFileDir + "/" + installShFileName],
           endOutpuptStr="Cloning into")

#手动运行git clone命令
print('把homebrew-core 运行git clone到本地')
corePathStr = "/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core"
corePath = Path(corePathStr)
if corePath.exists():
    print("删除已有的homebrew-core目录")
    shutil.rmtree(corePathStr, ignore_errors=True)

runCommandSerial([
    "git", "clone", "git://" + ustcSource + "/homebrew-core.git/",
    corePathStr, "--depth=1"
])

#更换shell的bottles
print('更换bottles')
shellName = getCurrentShellName()
if shellName == "zsh":
    runCommandSerial([
        "echo",
        "\'export HOMEBREW_BOTTLE_DOMAIN=https://" + ustcSource + "/homebrew-bottles\'",
        ">>", "~/.zshrc"
    ])
elif shellName == "bash":
    runCommandSerial([
        "echo",
        "\'export HOMEBREW_BOTTLE_DOMAIN=https://" + ustcSource + "/homebrew-bottles\'",
        ">>", "~/.bash_profile"
    ])
else:
    print('你的shell不是zsh，也不是bash。无法更换国内bottles源！！！')



#更换brew源
print('更换brew源')
runCommandSerial(["cd", "\"$(brew --repo)\""])
runCommandSerial([
    "git", "remote", "set-url", "origin", "https://" + ustcSource + "/brew.git"
])

#更换homebrew-core源
print('更换homebrew-core源')
runCommandSerial(["cd", "\"$(brew --repo)/Library/Taps/homebrew/homebrew-core\""])
runCommandSerial([
    "git", "remote", "set-url", "origin",
    "https://" + ustcSource + "/homebrew-core.git"
])

print('完成，输入brew update，试试')
