# Install Homebrew in China
国内安装Homebrew速度非常慢，网上很多更换国内源的方法，但是按那些步骤操作大部分时候还是失败。这里整理了一份比较清楚的操作流程。

经测试，国内的几个源，中科大的效果最好。所以本方法是使用中科大的源。

过几天，把这个流程用Python封装自动化一下。



##安装Homebrew
***如果你已经按官方的方式安装了Homebrew，那么直接更换源，未必有效果。请先删除已下载的Homebrew。***

***删除 `/usr/local/Homebrew` 目录即可。***



先给`install.h`加上执行权限

```shell
sudo chmod +x xxx/xxx/install.h
```

运行`install.h`，提示”Cloning into....“的时候，会卡住。此时关闭命令行窗口，重新打开。

手动输入git clone命令

```shell
git clone git://mirrors.ustc.edu.cn/homebrew-core.git/ /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core --depth=1
```




##更换成中科大的源

更换bottles源，打开用户根目录下的~/.zshrc 文件，加入以下代码:

```shell
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
```



给brew更换源

```shell
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
```



给homebrew-core更换源

```shell
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
```



完成，测试一下

```shell
brew update
```



##安装cask(可选)

如果需要的话，可安装cask。

```
brew tap homebrew/cask
```

提示”Cloning into....“的时候，会卡住。此时关闭命令行窗口，重新打开。

手动输入git clone命令

```shell
git clone git://mirrors.ustc.edu.cn/homebrew-cask.git/ /usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask --depth=1
```

