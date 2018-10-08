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

# 子节点:查找自己点的时候,需要用到find()方法,此时传入的参数是CSS选择器,find()方法查找的范围是所有的子孙节点.
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

# children()方法:可以只是查找子节点
print("***" * 50)
lis = items.children()
print(type(lis))
print(lis)
lis = items.children('.active')
print(type(lis))
print(lis)

# 父节点: 使用parent()方法来获取某个节点的父节点
print("***" * 50)
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# 祖先节点:使用parents()方法来获取节点的祖先节点
print("***" * 50)
parents = items.parents()
print(type(parents))
print(parents)
parent = items.parents('.wrap')
print(parent)

# 兄弟节点:使用siblings()方法
print("***" * 50)
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())
li = doc('.list .item-0.active')
print(li.siblings('.active'))