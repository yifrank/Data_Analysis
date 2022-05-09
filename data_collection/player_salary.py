from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import sqlite3  # 进行SQLite数据库操作
import csv

# URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向服务器发送消息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"
    }  # 用户代理：表示告诉目标服务器，我们是什么类型的机器；浏览器：本质上告诉服务器，我们能够接受什么水平的内容
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 球员薪资
findSalary = re.compile(r'<b>(本年薪金\：.*)</b>')


def getData(baseurl):
    datalist = []
    teamslist = ['grizzlies','mavericks','spurs','rockets','pelicans','warriors','suns','clippers','lakers','kings',
                  'jazz','nuggets','timberwolves','blazers','thunder','nets','76ers','celtics','raptors','knicks',
                  'heat','wizards','hornets','hawks','magic','bulls','bucks','cavaliers','pacers','pistons']
    for i in teamslist:
        url = baseurl + str(i)
        html = askURL(url)

        # 2、逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('table', class_="players_table"):   # 查找符合要求的字符串，形成列表
            # print(item)   #测试：查看球员item全部信息
            data = []  # 保存每一位球员的所有信息
            item = str(item)

            salary = []
            salarylist = re.findall(findSalary,item)
            for salarys in salarylist:
                #print(salary)
                salary.append(salarys)
            # print(salary)
            sala = []
            sa = []
            for str1 in salary:
                str2 = str1.split('：')[1]
                money = str2.replace('万美元','')
                sala.append(money)
            for str4 in sala:
                if str4 == '':
                    str4 = '0'
                sa.append(str4)
            data.append(sa)  # 添加本年薪金
            # print(data)

            for d in range(len(data[0])):
                l =[]
                for s in range(len(data)):
                    l.append(data[s][d])
                datalist.append(l)   # 把处理好的信息放入datalist
            print(len(datalist))
    return datalist


def writeData(dataList):
    #写入数据
    with open('1.csv','w',encoding='utf-8-sig',newline='')as f:
        write = csv.writer(f)
        for each in dataList:
            write.writerow(each)



if __name__ == "__main__":
    baseurl = "https://nba.hupu.com/players/"
    # 1、爬取网页
    datalist = getData(baseurl)
    writeData(datalist)