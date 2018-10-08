from lxml import etree

html = etree.parse('text.html', etree.HTMLParser())

# 这里代表匹配li标签下的所有a标签
result = html.xpath('//li/a')
print(result)

# 注意:这里如果使用//ul/a就无法匹配到信息,因为a标签不是ul的子节点,而是子孙节点,所以使用//进行全部查找
result = html.xpath('//ul//a')
print(result)