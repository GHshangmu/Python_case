import requests
from lxml import etree

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/52.0.2743.116 Safari/537.36', 'Accept-Language': 'zh-CN,zh;q=0.8'}

try:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    result = html.xpath('//div[contains(@id,"qiushi_tag")]')
    print(result)

    for site in result:
        item = {}
        imgUrl = site.xpath('./div/a/img/@src')[0]
        username = site.xpath('./div/a/h2/text()')[0].strip()
        content = site.xpath('.//div[@class="content"]/span/text()')[0].strip()
        # 投票次数
        vote = site.xpath('.//i')[0].text
        # 评论信息
        comments = site.xpath('.//i')[1].text

        print(imgUrl, username, content, vote, comments)

except Exception as e:
    print(e)
