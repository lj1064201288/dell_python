from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

# 如果属性当中有多个值,可以使用contains()方法提取数据
result = html.xpath('.//li[contains(@class, li)]/a/text()')
print(result)