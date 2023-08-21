当然可以，以下是一个简单的示例函数，用于实现多轮对话的功能：

```python
def chat_with_model(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": "您是一位客户"},
        {"role": "user", "content": prompt}
    ]
    
    while True:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        
        # 获取模型回答
        answer = response.choices[0].message['content']
        print(f"模型回答: {answer}")

        # 询问用户是否还有其他问题
        user_input = input("您还有其他问题吗？(输入退出以结束对话): ")
        if user_input == "退出":
            break

        # 记录用户回答
        messages.append({"role": "user", "content": user_input})

chat_with_model("请问，什么是机器学习？")
```

在该示例函数中，用户可以连续地进行提问，并通过输入"退出"来结束对话。每一轮对话中，用户与模型的交互都会被记录在`messages`列表中，并传递给`ChatCompletion.create`函数进行模型回答。模型的回答会打印在控制台上，并循环询问用户是否还有其他问题。

请注意，由于目前 gpt-3.5 系列模型对于system消息的长期关注性较低，在多轮对话时可能会出现由于上下文的丢失导致模型回答的问题。