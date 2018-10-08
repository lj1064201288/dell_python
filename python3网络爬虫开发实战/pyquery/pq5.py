from pyquery import PyQuery as pq

html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""

# 使用attr()方法获取属性
doc = pq(html)
a = doc(".item-0.active a")
print(a, type(a))
print(a.attr('href'))

# 使用attr属性来获取属性
print(a.attr.href)

# 如果需要选中的是多个元素,调用attr()方法
print("***" * 50)
a = doc('a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

# 如果需要调取全部标签,这里就需要使用到items()方法了
print("###" * 50)
doc = pq(html)
a = doc('a')
for item in a.items():
    print(item.attr.href)

# 获取文本:获取节点之后的另一个主要操作就是其内部的文本了,此时可以调用text()方法来实现
print("***" * 50)
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())

# 如果想要获取这个节点内部的HTML文本,就要用html()方法了
print("***" * 50)
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())

# 如果选中的结果是多个节点,text()返回的内容是所有节点内部的纯文本,中间用一个空格分割开的,返回的结果是一个字符串
# 而html()方法返回的是第一个指定的节点内部的html文本
print("***" * 50)
doc = pq(html)
li = doc('li')
print(li.html())
print(type(li.html()))
print(li.text())
print(type(li.text()))