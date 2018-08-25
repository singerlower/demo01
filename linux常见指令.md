#linux 操作

## apt-get
Advanced Package Tool（高级包管理工具），又名apt-get，是一款适用于Unix和Linux系统的应用程序管理器

apt-get命令一般需要root权限执行，所以一般跟着sudo命令
### 安装一个新软件包
apt-get install packagename

### 卸载一个已安装的软件包（保留配置文档）
apt-get remove packagename

###卸载一个已安装的软件包（删除配置文档）
apt-get autoremove packagename

###删除包及其依赖的软件包+配置文件，比上面的要删除的彻底一点
dpkg --force-all --purge packagename
有些软件很难卸载，而且还阻止了别的软件的应用，就能够用这个，但是有点冒险

###定期运行这个命令来清除那些已卸载的软件包的.deb文档。通过这种方式，您能够释放大量的磁盘空间。
apt-get autoclean

## su
SU：( Switch user切换用户)，可让一个普通用户切换为超级用户或其他用户，并可临时拥有所切换用户的权限，切换时需输入欲切换用户的密码；也可以让超级用户切换为普通用户，临时以低权限身份处理事务，切换时无需输入欲切换用户的密码。
###实例
假设一个普通用户trunk，首先以trunk登陆：
####su root 
临时切换到root用户，需要输入密码，切换后环境变量不变，取得root的部分权限，且只能使用trunk用户path路径中的命令，不能使用root用户path路径中的独有命令。
####su - root
切换为root用户，需要输入密码，切换后环境变量改变，几乎可以不受限制的做任何事。
####su - trunk
从root切换回普通用户，无需输入密码，切换后只拥有trunk权限。

## sudo
sudo是linux系统管理指令，是允许系统管理员让普通用户执行一些或者全部的root命令的一个工具，如halt，reboot，su等等。这样不仅减少了root用户的登录 和管理时间，同样也提高了安全性。sudo不是对shell的一个代替，它是面向每个命令的。

###sudo与su之间的关系
一般用户管理系统的方式是利用su切换为超级用户。但是使用su的缺点之一在于必须要先告知超级用户的密码。

sudo使一般用户不需要知道超级用户的密码即可获得权限。
###范例
1. sudo -l 列出目前的权限
若用户不在sudoers中会提示不能运行sudo命令，存在则会显示详细的权限。
2. sudo -V 列出 sudo 的版本资讯
3. 指令名称:sudoers（在fc5下显示不能找到此命令，但用man可以查到其用法。）用来显示可以使用sudo的用户