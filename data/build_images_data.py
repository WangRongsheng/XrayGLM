import json
import shutil
from tqdm import tqdm

with open('openi-en.json') as f:
    data = json.load(f)

#print(len(data['annotations']))
#print(data['annotations'][0]['image_id'])

for i in tqdm(range(len(data['annotations']))):
    img_name = data['annotations'][i]['image_id']
    src_file = './images/'+str(img_name)+'.png'
    # 新建images2文件夹
    dst_file = './images2/'
    shutil.copy(src_file, dst_file)