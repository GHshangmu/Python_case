import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/70.0.3538.102 Safari/537.36"
}


def get_url():
    for page in range(1, 2):
        url = 'http://www.nipic.com/design/wenyi/chuantong/index.html?page=' + str(page)
        response = requests.get(url, headers=headers)
        time.sleep(0.2)
        # 设置编码格式
        response.encoding = 'utf-8'
        html = etree.HTML(response.text)  # 初始化生成一个XPath解析对象
        img_url = html.xpath('//*/ul/li/a/@href')
        for i in img_url:
            if i.find('http') != -1:
                yield i


def get_img_url():
    for i in get_url():
        resp = requests.get(i)
        html2 = etree.HTML(resp.text)  # 初始化生成一个XPath解析对象
        item_name = html2.xpath('//*[@id="J_worksBigImg"]/div/text()')
        item_url = html2.xpath('//*[@id="J_worksBigImg"]/img/@src')
        item_info = list(zip(item_name, item_url))
        yield item_info


def download_img():
    for item_info in get_img_url():
        try:
            print('downloading')
            res = requests.get(item_info[0][1], headers=headers)
            with open(r'C:\Users\m_sha\Desktop\图片\\' + item_info[0][0]+'.jpg', 'wb') as f:
                f.write(res.content)
                print('finish')
        except Exception as e:
            print(item_info[0][0] + " error")


if __name__ == '__main__':
    download_img()

