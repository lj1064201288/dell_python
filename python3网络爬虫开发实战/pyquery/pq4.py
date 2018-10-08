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
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(str(li))

# 多个节点遍历:调用items()方法后,会得到一个生成器,遍历一下,就可以逐个得到li节点对象了
print("***" * 50)
doc = pq(html)
lis = doc('li').items()
print(type(lis))
print(lis)
for li in lis:
    print(li, type(li))

