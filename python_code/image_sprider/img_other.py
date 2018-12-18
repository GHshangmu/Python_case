import re
import requests


def get_url():
    img_url_list = []
    url = 'https://shimo.im/docs/cUkqzHiy1zYs2eUu'
    response = requests.get(url)
    response.encoding = 'utf-8'
    rule = re.compile("contentUrl\":\"(.*?)\"")
    second_url = re.findall(rule, response.text)
    second_res = requests.get(second_url[0].replace("\\u0026", "&"))

    jsom_data = second_res.json()
    print(len(jsom_data))
    for i in jsom_data:
        if isinstance(i[1], dict):
            img_url = i[1].get("gallery")
            if img_url:
                img_url_list.append(img_url)
    return img_url_list


def download_img():
    img_list = get_url()
    for index, item_info in enumerate(img_list):
        try:
            print('downloading')
            res = requests.get(item_info)
            with open(r'C:\Users\m_sha\Desktop\图片\\' + str(index) + '.jpg', 'wb') as f:
                f.write(res.content)
                print('finish')
        except Exception as e:
            print(item_info + " error")


if __name__ == '__main__':
    download_img()

