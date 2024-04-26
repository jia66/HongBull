import gradio as gr
from service import *

with gr.Blocks() as demo:
    gr.Markdown("小红书AI Agent-内容生成V0.1")
    with gr.Row():
        with gr.Column():
            product = gr.Textbox(label="产品：", value="云养宠动物追踪手链")
            common_key = gr.Textbox(label="常规关键词：", value="手链,追踪,野生动物,云领养,领养野生动物,环保时尚,礼物推荐")
            hot_key = gr.Textbox(label="爆款词：", value="五一送礼")
        out = gr.Textbox(label="种草文案：")
        #promt_test = gr.Textbox(label="提示词测试：")
    btn = gr.Button("生成文案")
    btn.click(fn=genContent, inputs=[product,common_key,hot_key], outputs=out)

    

demo.launch()


#增加动态调试提示词功能
#palyground 同时测试多个提示词
# 开源promt tools 
# 提示词测试