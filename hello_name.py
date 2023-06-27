import gradio as gr
# 関数を定義
def greet(name): 
  return "Hello " + name + "!"
# Webアプリを作成
app = gr.Interface(fn=greet, inputs="text", outputs="text")
# Webアプリを起動
app.launch(share=True, auth=("userA", "passwordA"))
