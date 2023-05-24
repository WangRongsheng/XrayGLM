import json
from tqdm import tqdm

with open('openi-zh.json') as f:
    data = json.load(f)

data_info = []
for i in tqdm(range(len(data['annotations']))):
    img = data['annotations'][i]['image_id']
    prompt = '通过这张胸部X光影像可以诊断出什么？'
    label = data['annotations'][i]['caption']
    json_data = {
                'img': './data/Xray/'+str(img)+'.png',
                'prompt': prompt,
                'label': str(label)
                }
    data_info.append(json_data)

with open('openi-zh-prompt.json', 'w+') as f1:
    json.dump(data_info, f1)
    