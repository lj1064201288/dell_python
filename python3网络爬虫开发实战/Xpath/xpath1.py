# 导入lxml库的etree模块
from lxml import etree

# 声明一段HTML文本
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactve"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
<ul>
</div>
'''
# 调用HTML类进行初始化,这样就成功构造了一个XPath解析对象
html = etree.HTML(text)
# 调用tostring()方法即可输出修正后的HTML代码,但是结果是butes类型
result = etree.tostring(html)
#　这里利用decode()方法将其装成str类型
print(result.decode('utf-8'))

html = etree.parse('./text.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
