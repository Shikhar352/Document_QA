import torch
import gradio as gr
from transformers import pipeline
model_path=r"D:\Gen_AI project\documents_QA\models--deepset--roberta-base-squad2\snapshots\adc3b06f79f797d1c575d5479d6f5efe54a9e3b4"
question_answer = pipeline("question-answering", model=model_path)
def read_file_content(file_obj):
    try:
        with open(file_obj.name, 'r') as file:
            context=file.read()
            return context
    except Exception as e:
        return f"an error occured:{e}"
    
def get_answer(file, question):
    context=read_file_content(file)
    answer=question_answer(question=question, context=context)
    return answer['answer']

demo = gr.Interface(fn=get_answer,
                    inputs=[gr.File(label="Upload your file"), gr.Textbox(label="Input your question",lines=1)],
                    outputs=[gr.Textbox(label="Answer text",lines=1)],
                    title="Document Q & A",
                    description="THIS APPLICATION WILL BE USED TO ANSER QUESTIONS BASED ON CONTEXT PROVIDED.")

demo.launch(share=True)

