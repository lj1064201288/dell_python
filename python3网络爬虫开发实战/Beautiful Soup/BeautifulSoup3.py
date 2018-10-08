from bs4 import BeautifulSoup

html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-smail" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
# find_all:查询所有符合条件的元素,给她传入一些属性或文本,就可以得到符合条件的元素,它的功能十分强大,返回的是一个列表类型
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

# attrs根据节点名查询,我们也可以传入一些属性来查询
print("***" * 50)
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

# 查询id为list-1的节点,可以直接传入id这个参数
print('***' * 50)
print(soup.find_all(id="list-1"))
# 因为class是python里面的关键词,所有使用的时候需要加上下划线进行区分
print(soup.find_all(class_="element"))

# text()参数用来匹配节点的文本,传入的形式可以是字符串,可以是正则表达式
import re

html = '''
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
print("***" * 50)
print(soup.find_all(text=re.compile('link')))


# find()返回单个元素,也就是第一个匹配的元素,find()与find_all()查询方法都是一样的,只不过查询的范围不同而已
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-smail" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""

soup = BeautifulSoup(html, 'lxml')

print("***" * 50)
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

