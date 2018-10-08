from lxml import etree


html = etree.parse('./text.html', etree.HTMLParser())

# 这里的*代表的是匹配所有的节点,也就是整个HTML文本中的所有节点都会被获取.
result = html.xpath('//*')
print(result)

#　这里的li代表的是匹配所有的li节点
result = html.xpath('//li')
print(result)
print(result[0])