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

# addClass和removeClass方法:
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('avtive')
print(li)
li.addClass('active')
print(li)

# attr()方法: 这个方法只传一个参数的属性名,则是获取这个属性值,如果传入第二个参数，就可以修改属性值
# text()和html()方法:这两个方法如果不传入参数,则获取节点内纯文本和HTML文本,如果传入参数，则进行赋值
print("***" * 50)
html = """
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a><li>
</ul>
"""

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# remove()方法
html = '''
<.div class="wrap">
Hello,World
<p>This is a paragraph.</p>
</div>

'''

print("***" * 50)
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

