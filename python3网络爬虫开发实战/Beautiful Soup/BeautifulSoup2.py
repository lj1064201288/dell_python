from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's stiry</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sister; and their names were
<a href="http:example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http:example.com/elsie" class="sister" id="link2">Lacie</a> and
<a href="http:example.com/elsie" class="sister" id="link3">Title</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')

# 选择元素
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 提取信息
# 获取名称:可以利用name属性获取节点的名称
print(soup.title.name)
# 获取属性:可以调用attrs获取所有的属性
# attrs返回的结果是字典类型的,他把选择的节点的所有属性值组合成一个字典
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 也可以不用写attrs直接在节点元素后面中括号传入属性名也可以获取属性值
# 注意:一个标签种可能包含多个class属性,所以返回的是一个列表
print(soup.p['name'])
print(soup.p['class'])
#　获取内容: 可以利用string属性获取节点元素包含的文本内容
print(soup.p.string)
print("===" * 50)
# 嵌套元素
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择:在做选择的时候,有时候不能做到一步就宣导想要的节点元素,需要先选中某一个节点元素,然后以它为基准在选择它的子节点,父节点,兄弟节点
# 子节点和子孙节点:选取元素之后,如果想要获取它的直接子节点,可以调用contents属性
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sister; and their names were
    <a href="http://example.com/elsie", class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/title" class="sister" id="link3">Title</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
# 使用contents获取节点中所有的子节点以及内容,然后以列表的方式进行显示
print("===" * 50)
soup = BeautifulSoup(html, "lxml")
print(soup.p.contents)

# 使用cheildren属性,返回结果是生成器类型
print("===" * 50)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 使用descendants实行得到所有子孙节点
print("===" * 50)
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 父节点和祖先节点,可以调用parent属性
print("===" * 50)
print(soup.a.parent)
print()
print(soup.a.parents)
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 兄弟节点: next_sibling下一个节点兄弟元素,previous_sibling上一个兄弟元素,返回的结果都是生成器
print("****" * 50)
print('Next Sibling', soup.a.next_sinling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Sinling', list(enumerate(soup.a.previous_siblings)))

# 提取信息
print("***" * 50)
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parets))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])







