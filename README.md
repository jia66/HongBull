# HongBull
小红书自动内容生成AIAgent


## 安装

1. 配置key

复制`.envconfig`文件另存为`.env`，根据选用的大模型配置对应key
```txt
ZHIPUAI_API_KEY=
OPENAI_API_KEY=
```

2. 安装依赖
```
pip install -r requirements.txt
```


## 运行

```
python webui.py
```

如果需要开启调试热重载模式，改用gradio命令运行：
```
gradio webui.py
```
    
## 扩展功能

### 爬虫

爬虫模块基于[MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)项目进行修改。因为MediaCrawler项目的开源协议不允许商用，为避免一些麻烦，整体的实现方案是fork这个项目，在这个项目的基础上封装了一层简单的rpc服务。通过独立部署并远程调用这个rpc服务，来实现爬虫功能。

MediaCrawler rpc服务部署步骤：

1. clone封装后的MediaCrawler项目到本地
```shell
git clone -b rpc https://github.com/qinxiandiqi/MediaCrawler.git
```

2. 创建python 3.9的虚拟环境并激活，推荐使用conda
```shell
conda create -n crawler python=3.9
conda activate crawler
```

3. cd到MediaCrawler的目录，安装依赖
```shell
cd ${your path to MediaCrawler}
pip install -r requirements.txt
playwright install
```

4. 启动服务
```shell
python rpc.py
```

5. 首次启动需要扫码和通过图形验证码登录小红书。登录后，即可通过rpc远程调用MediaCrawler的爬虫服务

6. MediaCrawler rpc服务的使用例子，可以参考test.py