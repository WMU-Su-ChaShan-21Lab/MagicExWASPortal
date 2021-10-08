# 项目说明

## 项目目的


## 项目主要功能


## 安装虚拟环境

* 选择 `pipenv` 进行安装
    * 先安装`pipenv`:`pip install pipenv`
    * 根据系统中使用的python版本的不同，请先修改`Pipfile`文件中最后一行python的版本
    * 使用IDE
        * 设置->项目->python解释器->在三个点点处点击添加->在左边选择使用 pipenv *新建虚拟环境*
        * pipenv会自动选择根目录下的pipenv和pipenv.lock下载需要的库
        * 有的老版本的IDE可能不支持pipenv创建，可以自己安装pipenv在终端使用，或者换用 `virtual environment` 的方法
    * 使用终端
        * 生产环境：`pipenv install`
        * 开发环境：`pipenv install -d`
* 使用 `virtual environment` 进行安装
    * 使用`Pycharm`
        * 设置->项目->python解释器->在三个点点处点击添加->在左边选择使用 virtual environment *新建虚拟环境*
        * 创建之后会自动选择虚拟环境的解释器，之后进入终端执行
            * `pip install -r requiremnets.txt`
            * 或者手动安装包 `pip install flask`
    * 使用终端
        * 需要安装 virtual environment的包
            * `pip install virtualenv`
        * 确定终端进入根目录后，在终端执行`python -m venv venv`
        * 启动和退出虚拟环境
            * 先进入虚拟环境 venv 文件夹（`cd 文件夹名称`）
            * Mac
                * 启动：`source bin/activate`
                * 退出：`deactivate` #这个是全局的命令，任何路径下执行都行
            * Windows
                * 启动：在Scripts文件夹里，使用 `activate` 命令
                * 退出：任意地方使用 `deactivate` 命令
        * 如果后续更换了 `pycharm`
            * 设置->项目->python解释器->在三个点点处点击添加->在左边选择使用 virtual environment *添加已经存在的虚拟环境*
* 有可能遇到的问题
    * 安装的时候找不到包或者对应版本
        * 如果未换源的话大概率是网络问题
            * 可以在终端代理后用命令行安装
            * 可以先在根环境下安装之后，在安装虚拟环境的时候会从根环境调用包过来
        * 如果换源之后就确实有可能这个包找不到了，具体可能是撤回或者小版本
            * 建议直接安装最新版或者手动安装一些其他的老版本
            * 然后在requirements.txt文件中删除对应的一行
            * pipenv由于现在未配置，大多数都是默认安装最新的版本
    * 安装失败
        * 先查看pip和setuptools的版本是不是最新的
        * 如果pip是最新的，需要vc++说明是c编译的包，可以装visual studio
            * 如果不想装那么大的visual studio，可以安装windows10的SDK和2015版本的c++生成工具
            * 还不想装，那就去[这个网站](http://www.lfd.uci.edu/~gohlke/pythonlibs/)找对应python和操作系统版本的whl文件手动安装
                * 下载后到对应的文件夹输入命令：`pip install ***.whl`，卸载将`install`改为`uninstall`
        * 还有一种可能是包卸载不干净，最简单方法就是直接删除环境重新创建
            * 老版本的pycharm可能装的pip包比较老，更新的pip后指向不对，但是可以用，建议安装后应该直接删除老版本文件，再次重新执行更新pip的命令
            * 不想操作的建议直接更新最新版本的pycharm
    * 源码编译方法
        * 有一些包不需要vc++，但是也不在pypi官网上发布，就需要自己手动安装
        * 先进入下载下来的包的文件夹：`python setup.py install`

## 项目启动

* 先配置.env环境变量

```dotenv
# 示例，在真实的生产环境中请不要加中文注释，因为pipenv的gbk问题至今未解决
# 存储包含敏感信息的环境变量，不提交到git仓库
SECRET_KEY='35JN7GFaUFNeriObUj93bQpavYWsGPOp6I4BDoe-U6Q'
SECURITY_PASSWORD_SALT='120426439174435924094353414614255850770'
# MySQL数据库URL
# 格式为DATABASE_URL='mysql+pymysql://username:password@host/databasename'
DATABASE_URL='mysql+pymysql://username:password@host/databasename'
```

* 启动pipenv虚拟环境(千万注意.env文件中不要有中文注释)：`pipenv shell`
* 启动MySQL(需要额外安装这个软件)
    * 初始化
        * 配置数据的管理员和密码
        * 创建和`.env`配置中相应的数据库
    * 记得需要配置环境变量
        * 提醒：如果密码中含有特殊字符，请手动配置`app/setting.py`文件，使用URL编码进行处理
    * *数据库源文件较大，不好上传，建议自己保存到`app/models/myopia/source`文件夹下，并重新保存为xlsx文件*
    * 在终端初始化数据库表：`flask db-init`
    * 初始化表数据：`flask data-init`
        * 输入`p`或者`production`代表生产环境
        * 输入`d`或者`development`代表开发环境