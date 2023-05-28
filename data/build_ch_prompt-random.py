import json
from tqdm import tqdm
import random

with open('openi-zh.json') as f:
    data = json.load(f)

data_info = []
for i in tqdm(range(len(data['annotations']))):
    prompt_temp = ['通过这张胸部X光影像可以诊断出什么？',
                   '这张图片的背景里有什么内容？',
                   '详细描述一下这张图片',
                   '看看这张图片并描述你注意到的内容',
                   '请提供图片的详细描述',
                   '你能为我描述一下这张图片的内容吗？'
                    ]
    img = data['annotations'][i]['image_id']
    prompt = random.choice(prompt_temp)
    label = data['annotations'][i]['caption']
    json_data = {
                'img': './data/Xray/'+str(img)+'.png',
                'prompt': prompt,
                'label': str(label)
                }
    data_info.append(json_data)

with open('openi-ch-prompt.json', 'w+') as f1:
    json.dump(data_info, f1)
    