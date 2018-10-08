from pyquery import PyQuery as pq

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

# 字符串初始化
doc = pq(html)
print(doc('li'))

# URL初始化
doc = pq(url='http://www.baidu.com')
print(doc('title'))

# 文件初始化

doc = pq(filename='demo.html')
print(doc('li'))