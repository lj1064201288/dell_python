# 使用pyquery
- 初始化pyquery的时候,需要传入HTML文本来初始化一个PyQuery对象,它的初始化方式有多种,比如直接传入字符串,传入URL,传入文件名
- 初始化:
    - 案例:pq1
- 基本CSS选择器
    - 案例:pq2
- 查找节点
    - 案例:pq3
- 遍历
    - pyquery的选择结果可能是多个节点,也可能是单个节点,类型都是PyQuery类型,并没有返回的是list
    - 对于单个节点来说,可以直接打印输出,也可以直接转成字符串
    - 案例:pq4
- 获取信息
    - 提取到节点之后,然后就是提取节点所包含的信息了,比较重要的有两条
        - 一是获取属性
        - 二是获取文本
    - 案例:pq5
- 节点操作
    - pyquery提供了一系列方法来对接点进行动态修改,比如说为某个几点添加一个class,移除某个节点等,这些操作有使用会为提取信息带来极大的便利
    - addClass: 添加一个class属性
    - removeClass:删除一个class属性
    - pq6
 - 伪类选择器
    - CSS选择器之所以强大,还有一个很重要的原因,那就是它支持多种多样的伪类选择器
    - 例如选择第一个节点,最后一个节点,奇偶数节点,包含魔偶以文本的节点等
    - 案例:pq7