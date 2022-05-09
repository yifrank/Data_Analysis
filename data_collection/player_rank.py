from os import readlink
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import sqlite3
import csv 
import numpy as np 



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


def getLink(baseurl):
    player_link = []  
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

            item = str(item)

            # 获取到球员详情的链接
            linkHtmllist = soup.find_all("td", class_="td_padding")  #使用bs4获取链接
            for linkHtmls in linkHtmllist:
                player_link.append(linkHtmls.find('a').get('href'))

    return player_link


rankdata = re.compile(r'<b>(.*?)</b>')
def getData(urllist):
    playerlist = []
    ranklist=[]
    for url in urllist:
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")

        for item in soup.select('body > div.gamecenter_livestart > div.gamecenter_content > div.gamecenter_content_l > div.team_data > h2'):
            item = str(item)
            try:
                playerlist.append(item.split('（')[1].split('）')[0])
            except IndexError: 
                pass
            # playerlist.append(item.split('（')[0].split()[1].replace('-',' '))
            print(playerlist)
            print(len(playerlist))

        # for item in soup.select('body > div.gamecenter_livestart > div.gamecenter_content > div.gamecenter_content_l > div.team_data > div'):
        #     item = str(item)
        #     ranklist.append(re.findall(rankdata,item))
        #     print(ranklist)
        
    return playerlist,ranklist


def writeData(playerlist, ranklist):
    #写入数据
    # for i in range(len(playerlist)):
    #     ranklist[i].append(playerlist[i])
    # np.savetxt("rank_data.csv", ranklist, delimiter =",",fmt ='% s')
    np.savetxt("h:/360MoveData/Users/YZ/Desktop/Data Analysis/player_rank.csv", playerlist, delimiter =",",fmt ='% s')


if __name__ == "__main__":

    baseurl = "https://nba.hupu.com/players/"

    # 爬取球员链接
    linklist = getLink(baseurl)
    
    # 爬取球员信息
    playerlist, ranklist = getData(linklist)
    # writeData(playerlist, ranklist)

    
