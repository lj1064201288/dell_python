from lxml import etree

html = etree.parse('./text.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)


result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

result = html.xpath('//li[@class="item-0"]//text()')
print(result)