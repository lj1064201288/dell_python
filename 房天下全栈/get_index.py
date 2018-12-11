# 导入全国的城市
import get_citys
# 导入爬虫
import crawl_infos


def carwl_newhouse(citys, chengshi, write_type):

    if chengshi in citys.keys():
        new_href = citys[chengshi].split('.')
        new_href.insert(1, 'newhouse')
        new_url = '.'.join(new_href) + 'house/s/b91/'
        house = crawl_infos.new_house(chengshi, new_url, write_type)
        house.get_page()
        house.carwl_newhouse()

    elif chengshi == "全国":
        for city, href in citys.items():
            new_href = href.split('.')
            new_href.insert(1, "newhouse")
            new_url = '.'.join(new_href) + "house/s/b91/"
            house = crawl_infos.new_house(city, new_url, write_type)
            house.get_page()
            house.carwl_newhouse()
    elif chengshi not in citys.keys():
        print("请输入正确的城市")
        print(citys.keys())

        #new_house(city, href)

def carwl_esf(citys, chengshi, write_type):

    if chengshi in citys.keys():
        # 将城市的url分成列表
        new_href = citys[chengshi].split('.')
        # 对url里面插入esf
        new_href.insert(1, 'esf')
        # 构建新的初始页面
        new_url = '.'.join(new_href) + 'house/i31/'
        house = crawl_infos.esf_house(chengshi, new_url, write_type)
        house.run()

    elif chengshi == "全国":
        for city, href in citys.items():
            new_href = href.split('.')
            new_href.insert(1, "esf")
            new_url = '.'.join(new_href) + "house/i31/"
            house = crawl_infos.esf_house(city, new_url, write_type)
            house.run()
    elif chengshi not in citys.keys():
        print("请输入正确的城市")
        print(citys.keys())

def carwl_zf(citys, chengshi, write_type):

    if chengshi in citys.keys():
        # 将城市的url分成列表
        new_href = citys[chengshi].split('.')
        # 对url里面插入esf
        new_href.insert(1, 'zu')
        # 构建新的初始页面
        new_url = '.'.join(new_href) + 'house/i31/'
        house = crawl_infos.zf_house(chengshi, new_url, write_type)
        house.run()
    # 如果数输入全国，那么全部获取
    elif chengshi == "全国":
        for city, href in citys.items():
            new_href = href.split('.')
            new_href.insert(1, "zu")
            new_url = '.'.join(new_href) + "house/i31/"
            house = crawl_infos.zf_house(city, new_url, write_type)
            house.run()
    elif chengshi not in citys.keys():
        print("请输入正确的城市")
        print(citys.keys())

def User_select():
    # 赋值给对象
    item = get_citys.citys()
    citys = item.parse_citys()
    if citys:
        # 获取想要的类型
        house = input('请输入要获取的类型:')
        # 获取城市
        chengshi = input("请输入你要获取的城市(输入全国全部获取):")
        writes = {
            '1': 'csv',
            '2': 'MongoDB'
        }
        # 遍历存储方式进行选择
        for k, v in writes.items():
            print("{0}: {1}".format(k, v))
        write = input('请输入存储方式:')
        write_type = writes[write]

        # 楼盘信息
        if house == "楼盘":
            carwl_newhouse(citys, chengshi, write_type)
        # 二手房信息
        elif house == "二手房":
            carwl_esf(citys, chengshi, write_type)
         # 租房信息
        elif house == "租房":
            carwl_zf(citys, chengshi, write_type)

        else:
            print('没有这个选项...')
    else:
        print("获取城市失败...")



if __name__ == '__main__':
    try:
        User_select()
    except Exception as e:
        print('输入错误，请重新输入...', e.args)
        User_select()



