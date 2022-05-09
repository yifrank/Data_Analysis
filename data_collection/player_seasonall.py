import requests
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
# url='https://china.nba.cn/stats2/league/playerstats.json'

def getJson(url):
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    response = requests.get(url,headers=headers)
    json_data = json.loads(response.text)
    return json_data
def  getData(json_data):
    playerdata=[]
    for item in json_data['payload']['player']['stats']['regularSeasonStat']['playerTeams']:
        player_dataDict={}
        #球员
        name = json_data['payload']['player']['playerProfile']['displayNameEn']
        #赛季
        year = item['seasonDisplay']
        #所在球队
        if item['profile'] != None:
            team = item['profile']['nameEn']
        else:
            team = 'none'
        #出场次数
        count = item['statAverage']['games']
        #先发次数
        count1 = item['statAverage']['gamesStarted']
        #场均时间
        timeshow = item['statAverage']['minsPg']
        #投篮命中率
        fgpct = item['statAverage']['fgpct']
        #三分命中率
        tppct = item['statAverage']['tppct']
        #罚球命中率
        ftpct = item['statAverage']['ftpct']
        #场均得分
        points = item['statAverage']['pointsPg']
        #场均助攻
        assists = item['statAverage']['assistsPg']
        #场均抢断
        steals = item['statAverage']['stealsPg']
        #场均盖帽
        blocks = item['statAverage']['blocksPg']
        #场均篮板
        rebs = item['statAverage']['rebsPg']
        #平均防守篮板
        defrebs = item['statAverage']['defRebsPg']
        #平均进攻篮板
        offrebs = item['statAverage']['offRebsPg']
        #失误
        turnovers = item['statAverage']['turnoversPg']
        #犯规
        fouls = item['statAverage']['foulsPg']
        
        player_dataDict['球员'] = name
        player_dataDict['赛季']=year
        player_dataDict['所在球队']=team
        player_dataDict['场次']= count
        player_dataDict['先发']= count1
        player_dataDict['出场时间']=timeshow
        player_dataDict['投篮命中率'] = fgpct
        player_dataDict['三分命中率']=tppct
        player_dataDict['罚球命中率']=ftpct
        player_dataDict['进攻篮板']=offrebs
        player_dataDict['防守篮板']=defrebs
        player_dataDict['篮板']=rebs
        player_dataDict['助攻']= assists
        player_dataDict['抢断']=steals
        player_dataDict['盖帽']=blocks
        player_dataDict['失误']=turnovers
        player_dataDict['犯规']=fouls
        player_dataDict['得分']=points
        playerdata.append(player_dataDict) 
    
    return playerdata

def writeData(playerList):
    #写入数据
    with open(r'./player_dataall.csv','w',encoding='utf-8-sig',newline='')as f:
        write=csv.DictWriter(f, fieldnames=['球员','赛季','所在球队','场次','先发','出场时间','投篮命中率','三分命中率','罚球命中率',
                                            '进攻篮板','防守篮板','篮板','助攻',
                                            '抢断','盖帽','失误','犯规','得分'])
        write.writeheader()
        for each in playerList:
            write.writerow(each)
if __name__ == "__main__":
    code = pd.read_csv(r'./now_player_persondata.csv')
    player = code['球员编号']
    playerList=[]
    for i in player:
        if i == 'yves_pons':
            continue
        if i == 'tyrell_terry':
            continue
        url = f'https://china.nba.cn/stats2/player/stats.json?ds=career&locale=zh_CN&playerCode={i}'
        json_data = getJson(url)
        print(i)
        playerList += getData(json_data)
    writeData(playerList)

