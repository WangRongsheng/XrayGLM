import json
from tqdm import tqdm


with open('./openi-en.json') as f:
    data = json.load(f)

markdown_content = ''
for i in tqdm(range(len(data['annotations']))):
    # 获取字典对象
    #img = data['annotations'][i]['image_id']
    annotation = data['annotations'][i]['caption']
    markdown_content = markdown_content + str(annotation) + '\n\n'

with open('openi-en-md.md', 'w') as f1:
    f1.write(markdown_content)

print(len(data['annotations']))