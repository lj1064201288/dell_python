'''
项目实战:爬取猫眼电影排行榜
1. 需要获取的是电影名称,演员,上映时间,评分
2. 使用re正则提取里面的数据,保存到一个文件当中
'''
import re
import requests

if __name__ == '__main__':
    # 1.获取猫眼电影的网址
    url = "http://maoyan.com/board"

    # 2.构建请求头
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Connection":"keep-alive"
    }

    # 3.向猫眼网址发送请求
    rep = requests.get(url, headers=headers)
    html = rep.text

    # 4.提取猫眼电影中我们需要的数据
    s = r"<dd>(.*?)</dd>"
    film = re.compile(s,re.S)
    films = film.findall(html)

    # 5.提取电影的名称
    names = []
    for f in films:
        #print(type(f))
        #print(f)
        r = r'<a.*?title="(.*?)"'
        p = re.compile(r)
        ps = p.findall(f)[0]
        names.append(ps)

    # 6.提取演员的列表
    actors = []
    for a in films:
        r = r'<p.*?class="star">(.*?)</p>'
        p = re.compile(r, re.S)
        actor = p.findall(a)[0]
        actors.append(actor.strip())
        # for i in actor:
        #     actors.append(i.strip())

    # 7.提取上映的时间
    shows = []
    for s in films:
        r = r'<p.*?class="releasetime">(.*?)</p>'
        p = re.compile(r)
        show = p.findall(s)[0]
        shows.append(show)

    # 8.提取电影评分
    scores = []
    for price in films:
        r = r'<p.*?class="score"><i.*?class="integer">(.*?)</i><i.*?class="fraction">(.*?)</i>'
        p = re.compile(r)
        score = p.findall(price)
        scores.append(score[0][0]+score[0][1])
    #print(scores)

    files = {}
    # 9.把数据制作成一个字典s
    for i in range(len(names)):
        files["排名"+str(i+1)] = names[i] + "\n" + actors[i] + "\n" + shows[i] + "\n评分:" + scores[i]

    # 10.把数据存入文档
    js = str(files)
    print(type(js))
    print(js)
    with open("猫眼电影.json", 'w') as f:
        f.write(js)
    # for i in range(len(names)):
    #     print(names[i] + "---" + actors[i])
    #     print(shows[i])
    #     print("评分:" + scores[i])
    #     print("*" * 20)
    #     print()


        # print(type(actor))
        # print(actor)
        # for i in actor:
        #     print(i)


    # #for f in films:
    #     print("*" * 20)
    #     r = '<a.*?title="(.*?)"'
    #     name = re.compile(r)
    #     names = name.findall(f)
    #     print(names)

