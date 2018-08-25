
# git常用指令

## 一般配置
git --version   //查看git的版本信息
git config --global user.name   //获取当前登录的用户
git config --global user.email  //获取当前登录用户的邮箱

## 登陆git
/* 如果刚没有获取到用户配置，则只能拉取代码，不能修改  要是使用git，你要告诉git是谁在使用*/
 
git config --global user.name 'userName'    //设置git账户，userName为你的git账号，
git config --global user.email 'email'
## 创建一个文件夹
mkdir nodejs    //创建文件夹nodejs
cd nodejs       //切换到nodejs目录下
##初始化git仓库
git init //在nodejs文件夹下初始化一个仓库，此时文件里会到一个.git的隐藏文件夹
##创建忽略文件 ##
touch .gitignore    //不需要服务器端提交的内容可以写到忽略文件里
    /*
        .git
        .idea
    */
## 查看目录
ls -al

##创建文件并写入内容
echo "hello git" > index.html
//单个>箭头表示写入， >>表示追加
##查看文件内容
cat index.html
## 增加到缓存中
git add index.html
git add -A // 全部添加到缓存中
## 增加到版本库中
git commit -m "备注信息"
## 查看版本
git log --oneline
##比较差异
比较的是暂存区和工作区的差异
git diff
比较的是暂存区和历史区的差异
git diff --cached
比较的是历史区和工作区的差异（修改）
git diff master
撤回内容
(如果修改了工作区的文件后发现改错了，可以用暂存区或者版本库里的文件替换掉工作区的文件)
##用暂存区中的内容或者版本库中的内容覆盖掉工作区
git checkout index.html
##取消增加到暂存区的内容（添加时）
git reset HEAD index.html
##显示目录的状态 有没有添加或者修改文件
git status
##删除本地文件
rm filename
##删除缓存区
保证挡墙工作区没有index.html
git rm index.html --cached
使用--cached 表示只删除缓存区中的内容
##回滚版本
回滚最近的一个版本 git log
git reset --hard HEAD/commit_id
## 回滚到未来 ##
git reflog
#分支管理
##创建分支
git branch dev
##切换分支
git checkout dev
##创建分支并切换分支
git checkout -b dev
##删除分支
git brach -d dev
##在分支上提交新的版本
git commit -a -m 'dev1'
##合并分支
git merge dev
##分支的合并并显示log
git log --oneline --graph --decorate
##在分支开发的过程中遇到其他问题需要切换到其他分支
保留写好的内容在切换到主干
保留内容
git stash
##在次切换分之后需要应用一下保留的内容
git stash apply
##丢掉保存的内容
git stash drop
##使用并丢掉
git stash pop
#最佳分支
-有的时候开发需要合并指定的内容，而不是合并所有的提交，所以我们需要挑选最好的，自己生产版本

合并分支把树杈掰到主干上
git rebase
##添加远程的仓库
push -u
git push origin master -u   //获取最新代码
##连接远程仓库
git remote add origin 仓库的地址
##查看远程仓库
git remote -v
##删除远程仓库
git remote rm origin


#git常用命令

##安装及配置：
- Ubuntu下安装：sudo apt-get install git
- 配置用户名：git config --global user.name "你的名字"
- 配置e-mail：git config --global user.email "你的邮箱@xx.com"

##与添加有关的：
- 将当前目录变为仓库：git init
- 将文件添加到暂存区：git add 文件名 [可选：另一个文件名]
- 将暂存区提交到仓库：git commit –m "描述"

##与查询有关的：
- 查询仓库状态：git status
- 比较文件差异（请在git add之前使用）：git diff 文件名
- 查看仓库历史记录(详细)：git log
- 查看仓库历史记录(单行)：git log --pretty=online 或 git log --online
- 查看所有版本的commit ID：git reflog

##与撤销有关的：
- 撤销工作区的修改：git checkout -文件名
- 撤销暂存区的修改：git reset HEAD 文件名
- 回退到历史版本：git reset --hard 该版本ID
- 回退到上个版本：git reset --hard HEAD^
- 上上版本是HEAD^^，也可用HEAD~2表示，以此类推

##与标签有关的：
- 为当前版本打标签：git tag 标签名
- 为历史版本打标签：git tag 标签名 该版本ID
- 指定标签说明：git tag –a 标签名 –m "标签说明" [可选：版本ID]
- 查看所有标签：git tag
- 查看某一标签：git show 标签名
- 删除某一标签：git tag –d 标签名
- 删除远端的标签名:git push origin --delete 标签名

##分支
- git branch, 查看当前分支
- git checkout -b 分支名, 切换到指定分支
- git push -u origin 分支名,  推送本地分支跟踪远程分支
- git checkout master/dev 切换到master主分支/子分支
- git merge 分支A, 合并指定分支A到主分支中

##多人操作:
- git clone 地址, 克隆远程的代码到本地
- git push, 推送到远程仓库
- git config --global  credential.helper cache 十五分钟有效期
- git config  credential.helper 'cache --timeout==3600' 一个小时有效期
- git config --global credential.helper store 长期有效
- git pull ,拉取远程代码到本地目录

#与GitHub有关的：
先有本地- 库，后有远程库，将本地库push到远程库
- 
- 关联本地仓库和GitHub库：git remote add origin 网站上的仓库地址
- 第一次将本地仓库推送到GitHub上：git push –u origin master
- 
- 先有远程库，后有本地库，从远程库clone到本地库
- 
- 从远程库克隆到本地：git clone 网站上的仓库地址
- 
- 网站地址可以选择HTTPS协议（https://github.com...）、SSH协议（git@github.com...）。
- 如果选择SSH协议，必须将Ubuntu的公钥添加到GitHub上。见下一步
- 
#SSH Key

- 生成SSH Key：ssh-keygen –t rsa –C "你的邮箱@xx.com"
- 生成Key时弹出选项，回车选择默认即可。
- Key保存位置：/root/.ssh
- 登陆GitHub，创建new SSH key，其内容为/root/.ssh/id_rsa.pub中文本
- 
- 已经有了本地库和远程库，二者实现同步
- 
- 本地库的改动提交到远程库：git push origin master
- 更新本地库至远程库的最新改动：git pull


# 第二篇 #
- 初始化参数
- $ git config --global user.name "你的名字"
- $ git config --global user.email "你的邮箱地址"
- 
- 因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。
-  注意git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。
- 
- 初始化本地仓库
- $ git init
- 
- SSH key生成
- $ ssh-keygen -t rsa -C "你的邮箱地址"
- 
- clone代码
- // 克隆master分支
- $ git clone <版本库的网址>
- // 指定克隆的分支名
- $ git clone -b <分支名> <版本库的网址>
- 
- .gitignore生效办法
- // 先把本地缓存删除（改变成未track状态）
- $ git rm -r --cached .
- // 然后再提交
- $ git add .
- $ git commit -m 'update .gitignore'
- 
- 查看各种状态
- // 查看当前状态（分支名，有哪些改动，有哪些冲突，工作区暂存区中的内容，几个commit等等）
- $ git status
- // 查看本地仓库的提交历史
- $ git log
- // 查看本地仓库的提交历史，简洁版
- $ git log --pretty=oneline
- // 查看命令历史
- $ git reflog
- 
- 分支
- // 查看分支：
- $ git branch -a
- // 创建本地分支：
- $ git branch <分支名>
- // 切换本地分支：

----------

----------

- $ git checkout <分支名>
- // 创建+切换本地分支：
- $ git checkout -b <name>
- // 合并某分支到当前分支：
- $ git merge <要合并的分支>
- // 将本地分支推送到远程
- $ git push origin <要推送的本地分支名>
- // 以远程分支为基础，建一个本地分支
- $ git checkout -b <本地分支名> origin/<远程分支名>
- // 删除本地分支：
- $ git branch -d <本地分支名>
- // 删除远程分支。将本地空分支推送到远程分支,相当于删除远程分支
- $ git push origin  :<要删除的远程分支名>
- 
- 更新和提交代码
- 
- 一个新的文件,或改动.刚开始只存在你的工作区。当你使用git add的时候，Git就会缓存这个改动并且跟踪。当你使用git commit的时候就会把你的改动提交到仓库里。
- // 缓存所有改动
- $ git add --all
- // 缓存单个文件的改动
- $ git add <该文件的文件名，包含路径>
- // 提交至本地仓库
- $ git commit -m <提交备注>
- // 更新本地代码
- $ git pull origin <分支名>
- // 将本地commit推送至远端
- $ git push orign <分支名>
- 
- 撤销
- // 撤销工作区某个文件的更改
- $ git checkout [file]
- // 撤销工作区所有文件的更改
- $ git checkout .
- // 重置暂存区的指定文件，与上一次commit保持一致。但更改并没有消失，而是更改打回工作区
- $ git reset [file]
- // 重置暂存区与工作区，与上一次commit保持一致。
- $ git reset --hard <当前分支名>
- // 重置当前分支的指针为指定commit，同时重置暂存区。但更改并没有消失，而是更改打回工作区
- $ git reset [commit]  
- // 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致。
- $ git reset --hard [commit]
- // 重置当前HEAD为指定commit，但保持暂存区和工作区不变
- $ git reset --keep [commit]
- // 暂时将未提交的变化存入stash，稍后再弹出
- $ git stash
- $ git stash pop
- 
- git review
- 
- 代码评审使用gerrit系统，git中使用git review <分支名>(默认是master) 命令执行review操作。
- 
- 规则
- •提交reivew之前pull远程代码，保证提交以前是最新代码，有冲突需要本地合并处理。
- •一个单一的功能的变更放入一个commit中，提交一次reivew。
- 
- 特殊情况
- •review没有通过怎么办？
-  先回到要修改的那个commit
- $ git reset --soft  <要修改的那个commit的id>
- 
- 继续修改你要改的文件。修改后add缓存文件，并执行
- $ git commit --amend
- 
- 将刚生产的变更归并到上一次变更里，继续执行git review
- •已经做了多个提交commits怎么办？
-  如果多个提交是相关联的，请合并这个提交为一个提交
- // 查询最先提交的commit, 记住id.
- $ git log 
- // 进行变基操作
- $ git rebase -i  <上一步查到的id>
- // 弹出的界面上罗列了最先提交的commit到现在的所有提交记录
- //将每列开头的 'pick' 改成 's', 只保留第一列的 'pick'。
- //保存修改后系统会自动把这些commits合并成一个commit.
- // 如果遇到冲突需要手动解决。合并冲突后，继续变基， 直到所有commits都合并为止.
- $ git rebase --continue
- 
- 如果review中提交了多个commits，其中一个commit没review过怎么办(包括以前某个commit中没有生成change id)？一次commit对应生成一个review, 前一个review没通过的话，后面的review 通过了也提交不了。 必须把前面一个review 弄通过，后面的review才能提交。
- // 查询未通过的review对应的commit id(gerrit里有记录)
- // 回到这个commit的前一个节点，注意有个^
- $ 执行 git rebase -i  <未通过的review对应的commit id>^ 
- // 修改并缓存要提交的文件后
- $ git commit --amend
- // 返回head处
- $ git rebase --continue 
- // 提交对老review的更新
- $ git review
- 
- 特别提示
- 
- 如果git review <分支名>后提示缺失commit_id，可能是前面rebase操作造成的。
- // 现将rebase好的commit推回工作区
- $ git reset head^
- // 再重新add和commit，产生新的commit_id
- $ git add .
- $ git commit -m <备注信息>
- $ git review <分支名>
