### 2.ChatCompletion.create API使用方法及参数解释

#### 2.1 ChatCompletion.create函数使用简例

&emsp;&emsp;接下来，我们尝试调用OpenAI的Chat类模型，并详细解释模型API参数。和调用Completion模型需要使用Completion.create函数类似，若要调用Chat类大模型，则需要使用ChatCompletion.create函数。由于Chat模型本身是基于Completion模型的、专门用于处理对话类任务的模型，因此ChatCompletion.create的使用方法和Completion.create非常类似，整体函数使用流程和核心参数都非常类似，这里我们直接对Chat模型提问“什么是机器学习？”提问和获取结果流程如下：


```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
```


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "请问，什么是机器学习？"}
  ]
)
```


```python
response
```




    <OpenAIObject chat.completion id=chatcmpl-7aMK1Zr3sFfDrvScu0rGRShzbjNsI at 0x2e70127e980> JSON: {
      "id": "chatcmpl-7aMK1Zr3sFfDrvScu0rGRShzbjNsI",
      "object": "chat.completion",
      "created": 1688899969,
      "model": "gpt-3.5-turbo-0613",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "\u673a\u5668\u5b66\u4e60\u662f\u4e00\u79cd\u4eba\u5de5\u667a\u80fd\u9886\u57df\u7684\u6280\u672f\uff0c\u901a\u8fc7\u8ba9\u8ba1\u7b97\u673a\u7cfb\u7edf\u6839\u636e\u5927\u91cf\u6570\u636e\u81ea\u52a8\u5b66\u4e60\u548c\u6539\u8fdb\uff0c\u4ece\u800c\u5b9e\u73b0\u7279\u5b9a\u4efb\u52a1\u7684\u80fd\u529b\u3002\u7b80\u800c\u8a00\u4e4b\uff0c\u673a\u5668\u5b66\u4e60\u662f\u6307\u8ba1\u7b97\u673a\u7cfb\u7edf\u5229\u7528\u7edf\u8ba1\u5b66\u548c\u7b97\u6cd5\u6765\u4f7f\u81ea\u8eab\u83b7\u5f97\u4ece\u6837\u672c\u6570\u636e\u4e2d\u5b66\u4e60\u7684\u80fd\u529b\uff0c\u5e76\u5229\u7528\u5b66\u4e60\u5230\u7684\u77e5\u8bc6\u8fdb\u884c\u9884\u6d4b\u3001\u51b3\u7b56\u6216\u6267\u884c\u7279\u5b9a\u4efb\u52a1\u3002\u5b83\u6d89\u53ca\u8bb8\u591a\u7b97\u6cd5\u548c\u6280\u672f\uff0c\u4f8b\u5982\u76d1\u7763\u5b66\u4e60\u3001\u65e0\u76d1\u7763\u5b66\u4e60\u3001\u5f3a\u5316\u5b66\u4e60\u7b49\u3002\u673a\u5668\u5b66\u4e60\u5728\u5404\u79cd\u9886\u57df\u4e2d\u5f97\u5230\u4e86\u5e7f\u6cdb\u5e94\u7528\uff0c\u5982\u81ea\u7136\u8bed\u8a00\u5904\u7406\u3001\u56fe\u50cf\u8bc6\u522b\u3001\u63a8\u8350\u7cfb\u7edf\u7b49\u3002"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 20,
        "completion_tokens": 204,
        "total_tokens": 224
      }
    }



能够看出，和Completion.create非常明显的一个区别在于，ChatCompletion.create函数的调用不再需要prompt参数，而是换成了messages参数，并且，不同于prompt参数对象是以简单的字符串形式呈现，messages参数则是一个基本构成元素为字典的列表，其内每个字典都代表一条独立的消息，每个字典都包含两个键值（Key-value）对，其中第一个Key都是字符串role（角色）表示某条消息的作者，第二个key为content（内容）表示消息具体内容。可以说messages参数是ChatCompletion.create函数最重要的参数之一，能够看出比简单的prompt参数格式要更加复杂。更多关于message的参数设置方法稍后介绍，总的来看，这里的messages就可以简单理解为输入给模型的信息，而模型接收到message之后也会输出对应的回答信息，当然也是以message形式呈现：


```python
# 返回对象类型和Completion.create函数返回对象类型一致
type(response)
```




    openai.openai_object.OpenAIObject




```python
# 可以通过索引的方式索引出文本部分内容
response["choices"]
```




    [<OpenAIObject at 0x2017fa89ea0> JSON: {
       "finish_reason": "stop",
       "index": 0,
       "message": {
         "content": "\u673a\u5668\u5b66\u4e60\u662f\u4e00\u79cd\u4eba\u5de5\u667a\u80fd\u7684\u5206\u652f\u9886\u57df\uff0c\u5b83\u7814\u7a76\u5982\u4f55\u4f7f\u8ba1\u7b97\u673a\u7cfb\u7edf\u6839\u636e\u6570\u636e\u548c\u7ecf\u9a8c\u81ea\u52a8\u6539\u5584\u548c\u9002\u5e94\uff0c\u800c\u65e0\u9700\u660e\u786e\u5730\u8fdb\u884c\u7f16\u7a0b\u3002\u673a\u5668\u5b66\u4e60\u7684\u76ee\u6807\u662f\u901a\u8fc7\u6784\u5efa\u6a21\u578b\u548c\u7b97\u6cd5\uff0c\u8ba9\u8ba1\u7b97\u673a\u80fd\u591f\u4ece\u5927\u91cf\u6570\u636e\u4e2d\u5b66\u4e60\uff0c\u5e76\u4e14\u53ef\u4ee5\u4ece\u4e2d\u53d1\u73b0\u6a21\u5f0f\u3001\u505a\u51fa\u9884\u6d4b\u548c\u505a\u51fa\u76f8\u5e94\u7684\u51b3\u7b56\u3002\u673a\u5668\u5b66\u4e60\u6280\u672f\u88ab\u5e7f\u6cdb\u5e94\u7528\u4e8e\u56fe\u50cf\u548c\u8bed\u97f3\u8bc6\u522b\u3001\u81ea\u7136\u8bed\u8a00\u5904\u7406\u3001\u63a8\u8350\u7cfb\u7edf\u3001\u6570\u636e\u6316\u6398\u7b49\u9886\u57df\uff0c\u4ee5\u89e3\u51b3\u590d\u6742\u95ee\u9898\u548c\u6539\u8fdb\u4eba\u5de5\u667a\u80fd\u7cfb\u7edf\u7684\u6027\u80fd\u3002",
         "role": "assistant"
       }
     }]




```python
# 也可以通过属性调用的方式查看choices
response.choices
```




    [<OpenAIObject at 0x2017fa89ea0> JSON: {
       "finish_reason": "stop",
       "index": 0,
       "message": {
         "content": "\u673a\u5668\u5b66\u4e60\u662f\u4e00\u79cd\u4eba\u5de5\u667a\u80fd\u7684\u5206\u652f\u9886\u57df\uff0c\u5b83\u7814\u7a76\u5982\u4f55\u4f7f\u8ba1\u7b97\u673a\u7cfb\u7edf\u6839\u636e\u6570\u636e\u548c\u7ecf\u9a8c\u81ea\u52a8\u6539\u5584\u548c\u9002\u5e94\uff0c\u800c\u65e0\u9700\u660e\u786e\u5730\u8fdb\u884c\u7f16\u7a0b\u3002\u673a\u5668\u5b66\u4e60\u7684\u76ee\u6807\u662f\u901a\u8fc7\u6784\u5efa\u6a21\u578b\u548c\u7b97\u6cd5\uff0c\u8ba9\u8ba1\u7b97\u673a\u80fd\u591f\u4ece\u5927\u91cf\u6570\u636e\u4e2d\u5b66\u4e60\uff0c\u5e76\u4e14\u53ef\u4ee5\u4ece\u4e2d\u53d1\u73b0\u6a21\u5f0f\u3001\u505a\u51fa\u9884\u6d4b\u548c\u505a\u51fa\u76f8\u5e94\u7684\u51b3\u7b56\u3002\u673a\u5668\u5b66\u4e60\u6280\u672f\u88ab\u5e7f\u6cdb\u5e94\u7528\u4e8e\u56fe\u50cf\u548c\u8bed\u97f3\u8bc6\u522b\u3001\u81ea\u7136\u8bed\u8a00\u5904\u7406\u3001\u63a8\u8350\u7cfb\u7edf\u3001\u6570\u636e\u6316\u6398\u7b49\u9886\u57df\uff0c\u4ee5\u89e3\u51b3\u590d\u6742\u95ee\u9898\u548c\u6539\u8fdb\u4eba\u5de5\u667a\u80fd\u7cfb\u7edf\u7684\u6027\u80fd\u3002",
         "role": "assistant"
       }
     }]




```python
# 查看第一个返回结果
response.choices[0]
```




    <OpenAIObject at 0x2017fa89ea0> JSON: {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "\u673a\u5668\u5b66\u4e60\u662f\u4e00\u79cd\u4eba\u5de5\u667a\u80fd\u7684\u5206\u652f\u9886\u57df\uff0c\u5b83\u7814\u7a76\u5982\u4f55\u4f7f\u8ba1\u7b97\u673a\u7cfb\u7edf\u6839\u636e\u6570\u636e\u548c\u7ecf\u9a8c\u81ea\u52a8\u6539\u5584\u548c\u9002\u5e94\uff0c\u800c\u65e0\u9700\u660e\u786e\u5730\u8fdb\u884c\u7f16\u7a0b\u3002\u673a\u5668\u5b66\u4e60\u7684\u76ee\u6807\u662f\u901a\u8fc7\u6784\u5efa\u6a21\u578b\u548c\u7b97\u6cd5\uff0c\u8ba9\u8ba1\u7b97\u673a\u80fd\u591f\u4ece\u5927\u91cf\u6570\u636e\u4e2d\u5b66\u4e60\uff0c\u5e76\u4e14\u53ef\u4ee5\u4ece\u4e2d\u53d1\u73b0\u6a21\u5f0f\u3001\u505a\u51fa\u9884\u6d4b\u548c\u505a\u51fa\u76f8\u5e94\u7684\u51b3\u7b56\u3002\u673a\u5668\u5b66\u4e60\u6280\u672f\u88ab\u5e7f\u6cdb\u5e94\u7528\u4e8e\u56fe\u50cf\u548c\u8bed\u97f3\u8bc6\u522b\u3001\u81ea\u7136\u8bed\u8a00\u5904\u7406\u3001\u63a8\u8350\u7cfb\u7edf\u3001\u6570\u636e\u6316\u6398\u7b49\u9886\u57df\uff0c\u4ee5\u89e3\u51b3\u590d\u6742\u95ee\u9898\u548c\u6539\u8fdb\u4eba\u5de5\u667a\u80fd\u7cfb\u7edf\u7684\u6027\u80fd\u3002",
        "role": "assistant"
      }
    }




```python
# 查看第一个返回结果的message
response.choices[0].message['content']
```




    '机器学习是一种人工智能的分支领域，它研究如何使计算机系统根据数据和经验自动改善和适应，而无需明确地进行编程。机器学习的目标是通过构建模型和算法，让计算机能够从大量数据中学习，并且可以从中发现模式、做出预测和做出相应的决策。机器学习技术被广泛应用于图像和语音识别、自然语言处理、推荐系统、数据挖掘等领域，以解决复杂问题和改进人工智能系统的性能。'



可以说，在获取对话结果的过程中，除了ChatCompletion.create返回结果最终是保存在message属性中（Completion.create返回结果是保存在text属性中），其他方面ChatCompletion.create的返回结果和Completion.create返回结果完全一致。而文本补全模型需要输入“prompt”，输出结果是“text”；而对话模型需要输入“message”，返回也是“message”，可以说这种文本交互形式确实非常符合人类在进行聊天时的问答习惯。

&emsp;&emsp;最后需要注意的是，和Completion模型一样，Chat模型我们同样也可以在返回结果的usage中查看本次对话所占用的token数量，其中"prompt_tokens"表示提示词占用token数量，"completion_tokens"则表示返回结果所占用token数量，而"total_tokens"则是二者相加，代表本次对话总共占用token数量。


```python
response.usage
```




    <OpenAIObject at 0x2e70131fb50> JSON: {
      "prompt_tokens": 20,
      "completion_tokens": 464,
      "total_tokens": 484
    }




```python
response.usage["total_tokens"]
```




    484



#### 2.2 ChatCompletion.create函数参数解释

&emsp;&emsp;而关于ChatCompletion.create函数的详细参数解释，可以在官网相关页面查阅：https://platform.openai.com/docs/api-reference/chat/create 。能够发现，和Completion.create函数相比，ChatCompletion.create函数的参数结构发生了以下变化：     
- 用messages参数代替了prompt参数，使之更适合能够执行对话类任务；
- 新增functions和function_call参数，使之能够在函数内部调用其他工具的API，该功能为0613新增功能；
- 其他核心参数完全一致，例如temperature、top_p、max_tokens、n、presence_penalty等参数的解释和使用方法都完全一致，且这些参数具体的调整策略也完全一致，例如如果希望具备更有创造力的对话，则可以调高temperature且降低presence_penalty，而如果希望获得更加严谨的问答结果，则可以降低temperature并且提高presence_penalty取值；
- 剔除了best_of参数，即Chat模型不再支持从多个答案中选择一个最好的答案这一功能；

需要注意的是，两个函数相同的参数在Ch.2的Completion.create函数参数介绍中均有详细介绍，此处不再赘述。接下来我们围绕ChatCompletion.create不同的三个参数，即messages参数、functions和function_call参数进行详细解释。

### 3.messages参数详解

#### 3.1 message参数结构及功能解释

&emsp;&emsp;接下来我们来看ChatCompletion.create函数非常重要的参数——messages使用方法。总的来说，messages是一种用于描述ChatCompletion模型和用户之间通信信息的高级抽象，从表示形式上来说，一个messages是一个列表，包含多个字典，而每个字典都是一条消息，其中，一条消息由包含两个键值对（即每个字典都包含两个键值对），第一个键值对用于表示消息发送者，其中第一个Key为字符串'role'，Value为参与对话的角色名称，或者可以理解为本条消息的作者或消息发送人名称，第二个键值对表示具体消息内容，Key为字符串'content'，Value为具体的消息内容，用字符串表示。

> 实际上，根据官网的说明，更严谨的说法是role是content的作者，而content的作者并不一定是content的发送方，发送方的角色更多是用于消息传递而非消息创作。但在实际使用过程中我们发现，ChatCompletion模型的role几乎可以完全看成是消息发送方，这么理解也会更加便于我们对消息结构的掌握和解读。

例如上述示例中的messages就总共包含一条信息，即一个一个名为user的角色发送了一条名为'请问什么是机器学习？'的消息：


```python
messages=[
    {"role": "user", "content": "请问什么是机器学习？"}
]
```

而同时，返回的message结果也是一个“字典”，并且也包含了信息的发送方和具体信息内容，不难看出，此时返回的message发送方是一个名为'assistant'的角色，而具体内容则是一段关于什么是机器学习的描述：


```python
response.choices[0].message
```




    <OpenAIObject at 0x2017fa89d10> JSON: {
      "content": "\u673a\u5668\u5b66\u4e60\u662f\u4e00\u79cd\u4eba\u5de5\u667a\u80fd\u7684\u5206\u652f\u9886\u57df\uff0c\u5b83\u7814\u7a76\u5982\u4f55\u4f7f\u8ba1\u7b97\u673a\u7cfb\u7edf\u6839\u636e\u6570\u636e\u548c\u7ecf\u9a8c\u81ea\u52a8\u6539\u5584\u548c\u9002\u5e94\uff0c\u800c\u65e0\u9700\u660e\u786e\u5730\u8fdb\u884c\u7f16\u7a0b\u3002\u673a\u5668\u5b66\u4e60\u7684\u76ee\u6807\u662f\u901a\u8fc7\u6784\u5efa\u6a21\u578b\u548c\u7b97\u6cd5\uff0c\u8ba9\u8ba1\u7b97\u673a\u80fd\u591f\u4ece\u5927\u91cf\u6570\u636e\u4e2d\u5b66\u4e60\uff0c\u5e76\u4e14\u53ef\u4ee5\u4ece\u4e2d\u53d1\u73b0\u6a21\u5f0f\u3001\u505a\u51fa\u9884\u6d4b\u548c\u505a\u51fa\u76f8\u5e94\u7684\u51b3\u7b56\u3002\u673a\u5668\u5b66\u4e60\u6280\u672f\u88ab\u5e7f\u6cdb\u5e94\u7528\u4e8e\u56fe\u50cf\u548c\u8bed\u97f3\u8bc6\u522b\u3001\u81ea\u7136\u8bed\u8a00\u5904\u7406\u3001\u63a8\u8350\u7cfb\u7edf\u3001\u6570\u636e\u6316\u6398\u7b49\u9886\u57df\uff0c\u4ee5\u89e3\u51b3\u590d\u6742\u95ee\u9898\u548c\u6539\u8fdb\u4eba\u5de5\u667a\u80fd\u7cfb\u7edf\u7684\u6027\u80fd\u3002",
      "role": "assistant"
    }




```python
response.choices[0].message['content']
```




    '机器学习是一种人工智能的分支领域，它研究如何使计算机系统根据数据和经验自动改善和适应，而无需明确地进行编程。机器学习的目标是通过构建模型和算法，让计算机能够从大量数据中学习，并且可以从中发现模式、做出预测和做出相应的决策。机器学习技术被广泛应用于图像和语音识别、自然语言处理、推荐系统、数据挖掘等领域，以解决复杂问题和改进人工智能系统的性能。'



由此不难看出，对话Chat模型的每个对话任务都是通过输入和输出message来完成的。

#### 3.2 messages中的角色划分

- user role和assistant role

&emsp;&emsp;那么接下来的问题就是，在实际调用Chat模型进行对话时，messages中的role应该如何设置呢？从上述极简的对话示例中能够看出，一个最简单的对话就是我们扮演user（用户）这个角色（'role':'user'），然后在content中输入我们的问题并等待模型回答。而模型在实际回答过程中，也会扮演一个名为assistant（助手）这个角色（'role':'assistant'）进行回答，这里的user和assistant是具有明确含义的字符串，即如果一条信息的role是user，则表明这是用户向模型发送的聊天信息，相当于是Completion模型中的prompt，而如果一条信息的role是assistant，则表示这是当前模型围绕某条用户信息做出的回应，相当于是相当于是Completion模型中的text。需要注意的是，在messages参数中，我们是不能给自己或者模型自定义其他名称的。

&emsp;&emsp;很明显，基于这样的一个定义的规则，最简单的Chat模型的调用方法就是在messages参数中设置一条role为user的参数，在content中输入聊天的内容，而模型则会根据这条用户输入给模型的消息进行回答，类似于此前我们向模型提问“请问什么是机器学习？”这种提问方式:


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "请问什么是机器学习？"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '机器学习是一种人工智能的分支，通过使用数学和统计方法来自动分析和理解数据，并使计算机能够自主学习和改进性能。它是通过从数据中学习模式和规律，而不是通过明确编程来实现任务的一种方法。机器学习可以帮助计算机系统通过从大量数据中提取规律来预测结果、进行分类、聚类、识别图像和语音、自动驾驶等。'



不过需要注意的是，尽管一个messages可以包含多条信息，但模型只会对于最后一条用户信息进行回答，例如：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "请问什么是机器学习？"},
    {"role": "user", "content": "请问什么是决策树算法？"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '决策树算法是一种用于分类和回归的机器学习算法，它基于树形结构来进行决策。决策树可以看作是一个由节点和有向边组成的树，每个节点表示一个特征属性，每条边表示一个特征属性取值或决策的结果。决策树的根节点表示最重要的特征，而叶子节点表示分类或回归结果。\n\n决策树算法的特点包括易于理解和解释、能够处理非线性关系、不需要对数据进行特征预处理、可以处理多输出问题等。算法的核心思想是通过反复分割数据集，使得每个子集中的样本都属于同一类别（或拥有相似的回归结果）。分割的决策依据是选择最佳的划分特征，通常使用各种不纯度指标（例如基尼系数或熵）来衡量每个特征的纯度。\n\n决策树算法包括很多变种和优化方法，如CART（Classification and Regression Trees）、ID3、C4.5、随机森林等。决策树算法在实际应用中广泛使用，可以用于分类问题（如垃圾邮件分类、医学诊断等）和回归问题（如房价预测、股票趋势预测等）。'



也就是说，assistant消息和role消息是一一对应的，而且在一般情况下，assistant消息只会围绕messages参数中的最后一个role信息进行回答。

- system role用于身份设定

&emsp;&emsp;不过，值得一提的是，user和assistant的这种提问方式尽管足够清晰，但往往形式上不够丰富，例如在实践中人们发现，给聊天机器人进行一个身份设置，其实是非常有效的引导模型创作我们想要的结果的方法，例如如果我们希望获得一个关于“什么是机器学习？”更加严谨且丰富的答案，我们可以以“假设你是一名资深的计算机系大学教授”为模型进行身份设置，例如我们可以以如下方式向模型进行提问：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "假设你是一名资深的计算机系大学教授，请帮我回答，什么是机器学习？"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '机器学习是一门研究如何使计算机系统通过大量数据和经验自动学习和改进性能的领域。它利用算法和数学模型，使计算机能够自动发现数据中的模式和规律，并利用这些模式来进行预测、分类、优化等任务。\n\n在机器学习中，计算机系统并不需要明确地编写具体规则或指令，而是通过从数据中学习，从而提高自己的性能和准确性。它依赖于大数据、统计学和计算机科学等领域的技术，包括数据预处理、特征提取、模型选择和评估等步骤。\n\n机器学习广泛应用于各个领域，如自然语言处理、计算机视觉、推荐系统、金融预测等。它的目标是从数据中发现隐藏的模式和知识，以提供高效的决策支持和智能化的解决方案。'



不难看出，此时模型的回答就变得更加详细和严谨，更像一名“大学教授”的语气风格，也同时说明我们对模型进行的身份设定是切实有效的。

&emsp;&emsp;而在ChatCompletion.create函数中，还有另外一种非常便捷的对模型进行身份设置的方法，即使用system role，即我们可以使用如下方式为模型进行“大学教授”身份设定：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一名资深的计算机系大学教授"},
    {"role": "user", "content": "请问什么是机器学习？"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '机器学习是一种人工智能的分支领域，它致力于研究和开发能够从数据中自动学习和改进的算法和模型。机器学习使计算机可以通过分析大量数据并自动发现数据中隐藏的模式和规律，从而使计算机能够作出预测或做出决策。\n\n机器学习的主要任务包括分类、回归、聚类和推荐等。分类任务是将数据分为不同的类别，回归任务是预测数据的数值，聚类任务是将相似的数据分组，推荐任务是根据用户的个人偏好为其推荐物品。\n\n机器学习算法可以分为监督学习、无监督学习和强化学习。监督学习是通过已标记的训练数据进行学习，无监督学习是利用未标记的数据进行学习，而强化学习则是通过与环境的交互来进行学习。\n\n机器学习在许多领域中都有广泛的应用，例如图像识别、语音识别、自然语言处理、金融预测和医学诊断等。通过机器学习，计算机可以从大量的数据中学习，并提供更准确、高效的解决方案。'



&emsp;&emsp;能够看出，这里我们在原有消息之前，新增一条消息{"role": "system", "content": "你是一名资深的计算机系大学教授"}，也能起到设定模型身份的作用。而这条消息的实际含义是，以system的身份发送一条消息，消息内容为“你是一名资深的计算机系大学教授”。这里的system就是messages参数的role可以选取的第三个字符串，意为该消息为一条系统消息。相比用户消息，系统消息有以下几点需要注意，其一是系统消息的实际作用是给整个对话系统进行背景设置，不同的背景设置会极大程度影响后续对话过程中模型的输出结果，例如如果系统设置为“你是一位资深医学专家”，那么接下来系统在进行回答医学领域相关问题时则会引用大量医学术语，而如果系统设置为“你是一位资深喜剧演员”，那么接下来系统进行的回答则会更加风趣幽默：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一名资深的喜剧演员"},
    {"role": "user", "content": "请问什么是机器学习？"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '哈哈，这是一个有趣的问题！机器学习是一种人工智能的分支，它通过让计算机系统自动学习和改进，而无需明确的编程指令。简单来说，机器学习是让机器具备从数据中学习和预测的能力。就像我在喜剧表演中学习和改进我的技巧一样，机器学习通过分析大量的数据，找到模式和规律，从而使机器能够做出智能的决策和预测。不过相比我，机器学习更加准确和高效！话不多说，让我们继续我的喜剧表演吧！'



&emsp;&emsp;而第二方面需要注意的则是，当messages中只包含一条system消息时，系统会围绕system进行回答，只不过此时系统的assistant的应答消息则更像是一个completion的过程，即围绕system的prompt进行进一步的文本补全：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一名资深的喜剧演员"},
  ]
)
```


```python
response.choices[0].message
```




    <OpenAIObject at 0x2017fa96590> JSON: {
      "content": "\u6211\u4f1a\u7ed9\u89c2\u4f17\u5e26\u6765\u6b22\u4e50\u548c\u5feb\u4e50\u7684\u7b11\u58f0\uff01\u6211\u64c5\u957f\u5851\u9020\u4e30\u5bcc\u591a\u6837\u7684\u89d2\u8272\uff0c\u8fd0\u7528\u5938\u5f20\u7684\u8868\u6f14\u6280\u5de7\u548c\u5e7d\u9ed8\u7684\u53f0\u8bcd\uff0c\u8ba9\u89c2\u4f17\u6367\u8179\u5927\u7b11\u3002\u6211\u559c\u6b22\u6311\u6218\u81ea\u5df1\uff0c\u5c1d\u8bd5\u4e0d\u540c\u7684\u559c\u5267\u98ce\u683c\uff0c\u4f8b\u5982\u60c5\u666f\u559c\u5267\u3001\u559c\u5267\u7535\u5f71\u3001Stand-up\u559c\u5267\u7b49\u7b49\u3002\u901a\u8fc7\u4ee4\u4eba\u96be\u5fd8\u7684\u8868\u6f14\uff0c\u6211\u5e0c\u671b\u80fd\u591f\u7559\u4e0b\u6df1\u523b\u7684\u5370\u8c61\uff0c\u5e76\u8ba9\u89c2\u4f17\u5fd8\u8bb0\u751f\u6d3b\u4e2d\u7684\u70e6\u607c\uff0c\u4eab\u53d7\u4e00\u6bb5\u6b22\u4e50\u7684\u65f6\u5149\uff01",
      "role": "assistant"
    }




```python
response.choices[0].message['content']
```




    '我会给观众带来欢乐和快乐的笑声！我擅长塑造丰富多样的角色，运用夸张的表演技巧和幽默的台词，让观众捧腹大笑。我喜欢挑战自己，尝试不同的喜剧风格，例如情景喜剧、喜剧电影、Stand-up喜剧等等。通过令人难忘的表演，我希望能够留下深刻的印象，并让观众忘记生活中的烦恼，享受一段欢乐的时光！'




```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你好，请问"},
  ]
)
```


```python
response.choices[0].message['content']
```




    '有什么可以帮助您的吗？'



当然，借助completion过程也是可以进行提问的，例如：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "请问什么是机器学习？"},
  ]
)
```


```python
response.choices[0].message['content']
```




    '机器学习是一种人工智能的分支，它通过使用计算机算法和模型，让机器自动从数据中学习，并从中提取规律和模式，以做出预测和决策。它的主要目标是使机器能够从经验中学习，提高预测能力和自动化任务。机器学习在许多领域都有广泛应用，包括自然语言处理、图像识别、数据挖掘和智能推荐系统等。'



不过这么做意义并不大，还是建议以user角色进行提问。

&emsp;&emsp;第三方面需要注意的是，如果我们需要根据system系统信息对系统进行设置，然后再提问，那么先system消息再user消息的顺序就变得非常重要，例如还是上面的例子，还是希望以喜剧演员的身份介绍机器学习，但我们调换了system消息和user消息的顺序，那么会发现，system消息的作用就会失效：


```python
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "请问什么是机器学习？"},
    {"role": "system", "content": "你是一名资深的喜剧演员"}
  ]
)
```


```python
response.choices[0].message['content']
```




    '机器学习是一门人工智能领域的研究，旨在让计算机系统通过学习和改进经验，不需要明确的程序指导下，自动完成特定任务。它利用统计学和算法来使计算机能够从数据中学习并进行预测和决策。机器学习可以应用于各种领域，如图像识别、语音识别、自然语言处理、推荐系统等。通过训练模型，机器学习可以帮助计算机系统能够从数据中识别模式，做出预测，并根据反馈不断改进自己的表现。'



此时会发现，模型还是能解答“请问什么是机器学习？”这个问题，但却没有正确接受“你是一名资深喜剧演员”这个设定。

&emsp;&emsp;最后还有一点需要注意的是，根据OpenAI官网说明，截至目前，gpt-3.5系列模型仍然无法对system提供的系统消息保持长期关注，即在多轮对话中，模型极有可能逐渐忘记自己的身份设定。根据长期使用情况来看，gpt-4模型对system设置的长期关注要好于gpt-3.5系列模型。
