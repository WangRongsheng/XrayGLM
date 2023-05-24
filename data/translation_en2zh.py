import json 
import openai
import time
from tqdm import tqdm

# 设置 OpenAI API 账户信息
openai.api_key = "xxx"

# 定义翻译函数
def translate_text(text):
    # 请翻译成中文，你可以适当润色翻译的内容，但是要保证整句话通顺并且原意不变：
    prompt = "Translate the following English text to Chinese"+str(text)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个非常优秀的中英文翻译器。"},
        {"role": "user", "content": prompt}
    ]
    )
    #print(completion.choices[0].message['content'])
    return str(completion.choices[0].message['content'])

with open('./openi-en.json') as f:
    data = json.load(f)

for i in tqdm(range(len(data['annotations']))):
    # 获取字典对象
    annotation = data['annotations'][i]['caption']

    translation = translate_text(annotation)
    #print(translation)
    data['annotations'][i]['caption'] = str(translation)

# 写入json文件
with open('openi-zh.json', 'w') as f1:
    json.dump(data, f1)