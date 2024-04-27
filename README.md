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
    