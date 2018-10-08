from bs4 import BeautifulSoup

html = '''
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
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print()
print(soup.select('ul li'))
print()
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))


# 嵌套选择: select()方法同样支持嵌套选择
print("***" * 50)
for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性:节点类型都是Tag类型的
print("***" * 50)
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本:获取文本,还是可以用string属性,还有一个新的方法,就是get_text()
print("***" * 50)
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)