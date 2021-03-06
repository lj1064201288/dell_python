# 非关系型数据库存储
- NoSQL,全称Not Only SQL, 意为不仅仅是SQL,泛指非关系型数据库.
- NoSQL是基于键值对的,而且不需要经过SQL层的解析,数据之间没有耦合性,性能非常高
- 非关系型数据库可以分为:
    - 键值存储数据库: 代表的有Redis, Voldemort和Orace BDB等
    - 列存储数据库: 代表的有Cassandra, HBase等等
    - 文档型数据库: 代表的有CouchDB和MongoDB等等
    - 图形数据库: 代表的有Neo4J, InfoGrid和Infinite Graph等等
- 对于爬虫的数据存储来说,一条数据可能存在某些字段提取失败而缺失情况,而且数据可能随时调整,另外,数据之间还存在嵌套关系
- 如果使用关系型数据库,一是需要提前建表,二是如果存在数据嵌套关系的话,需要进行序列化操作才可以存储,这非常不方便
- 如果用了关系型数据库,就可以避免一些麻烦,更简单高效
- MongoDB存储
    - MongoDB是由C++语言编写的非关系型数据库,是一个基于分布式文件存储的开源数据库系统,其内容存储形式类似于json对象
    - 它的字段值可以包含其它文档,数组及文档数组,非常灵活
    - 准备工作
        - 需要安装MongoDB并启动服务,并且需要安装好Python的PyMongo库
    - 连接MongoDB
        - 连接MongoDB时，需要使用pymongo库里面的MongoClient
        - 一般来说,传入MongoDB的IP端口即可其中第一个参数为地址host，第二个参数为端口port(如果不传递参数,默认参数是27017)
        - 案例: 连接MongoDB.py
    - 指定数据库
        - MongoDB中可以建立多个数据库
    - 指定集合
        -MongoDB的每个数据库又包含许多集合collection,他们类似与关系型数据库的表
    - 插入数据
        - 在MongoDB中,每条数据其实都有一个_id属性来唯一标示,如果没有显示指明该属性,MongoDB会自动产生一个ObjectId类型的_id属性,insert()方法会在执行后返回_id值
    - 查询
        - 插入数据后,我们可以利用find_one()或者find()方法进行查询,其中find_one()查询得到的是单一的结果,find()则返回一个生成器对象
        - 但是这里的大于查询不再是运算符查询:
               $lt   -- 小于
               #gt   -- 大于
               #lte  -- 小于等于
               #gte  -- 大于等于
               #ne   -- 不等于
               #in   -- 在范围内
               #nin  -- 不在范围内
        - 而且还可以使用re正则表达式进行匹配,使用$regex
        - 还可以使用功能符号查询
                    $exists   --属性是否存在
                    $type     --类型判断
                    $mod      --数字摸操作
                    $text     --文本查询
                    $where    --高级条件查询
    - 计数
        - 要统计查询结果有多少条数据,可以调用count()方法
        - 运行结果是一个数值,值符合条件的数据条数
                    