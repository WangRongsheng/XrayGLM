import json
from tqdm import tqdm

# 读取data.md文件，获取每行非空内容的列表
with open('data_ch.md', 'r', encoding='utf-8') as f:
    data_lines = [line.strip() for line in f if line.strip()]

print(len(data_lines))

with open('./filter_cap.json') as f:
    data = json.load(f)

print(len(data['annotations']))

for i in tqdm(range(len(data['annotations']))):
    data['annotations'][i]['caption'] = data_lines[i]

with open('data_ch.json', 'w') as f1:
    json.dump(data, f1)

with open('./data_ch.json') as f2:
    data2 = json.load(f2)

print(len(data2['annotations']))