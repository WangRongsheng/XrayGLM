import xml.etree.ElementTree as ET
import os
import shutil
from tqdm import tqdm

for i in tqdm(range(1,4000)):
    file_path = 'ecgen-radiology/'+str(i)+'.xml'
    # 判断文件存在
    if not os.path.isfile(file_path):
        continue
    else:
        # 解析XML文件内容
        tree = ET.parse(file_path)
        root = tree.getroot()
        # 遍历XML文件中所有的<url>标签
        num = 1
        for url in root.findall('.//url'):
            s = str(url.text)
            filename = s.split("/")[-1].split(".")[0]
            src_file = './NLMCXR_png/'+str(filename)+'.png'
            # 新建images文件夹
            dst_file = './images/'+str(i)+'_'+str(num)+'.png'
            shutil.copy(src_file, dst_file)
            num = num+1