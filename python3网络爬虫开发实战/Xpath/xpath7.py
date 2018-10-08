from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)