from functools import partial
import requests
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def getJson(url):
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    response = requests.get(url,headers=headers)
    json_data = json.loads(response.text)
    return json_data


def  getData(json_data):
    playerList=[]
    for item in json_data['payload']['teams']:
        player_dataDict={}
        #球队名字
        name=item['profile']['displayAbbr']
        #东西部
        part=item['profile']['displayConference']
        #场数
        games=item['statAverage']['games']
        #命中
        fgm=item['statAverage']['fgpct']
        #三分命中
        tpm=item['statAverage']['tppct']
        #罚球命中
        ftm=item['statAverage']['ftpct']
        #进攻篮板
        offRebs=item['statAverage']['offRebsPg']
        #防守篮板
        defRebs=item['statAverage']['defRebsPg']
        #场均得分
        points=item['statAverage']['pointsPg']
        #场均篮板
        rebs=item['statAverage']['rebsPg']
        #场均助攻
        assists=item['statAverage']['assistsPg']
        #失误
        turnovers=item['statAverage']['turnoversPg']
        #场均抢断
        steals=item['statAverage']['stealsPg']
        #场均盖帽
        blocks=item['statAverage']['blocksPg']
        #犯规
        fouls=item['statAverage']['foulsPg']
        #命中
        fgmt=item['statTotal']['fgm']
        #出手
        fgat=item['statTotal']['fga']
        #三分命中
        fpmt=item['statTotal']['tpm']
        #三分出手
        fpat=item['statTotal']['tpa']        
        #罚球命中
        ftmt=item['statTotal']['ftm']
        #罚球出手
        ftat=item['statTotal']['fta']
        #总进攻篮板
        offRebst=item['statTotal']['offRebs']
        #总防守篮板
        defRebst=item['statTotal']['defRebs']
        #总得分
        pointst=item['statTotal']['points']
        #总篮板
        rebst=item['statTotal']['rebs']
        #总助攻
        assistst=item['statTotal']['assists']
        #总抢断
        stealst=item['statTotal']['steals']
        #总盖帽
        blockst=item['statTotal']['blocks']
        #总失误
        turnoverst=item['statTotal']['turnovers']
        #总犯规
        foulst=item['statTotal']['fouls']



        player_dataDict['球队']=name
        player_dataDict['赛区']=part
        player_dataDict['场次']=games
        player_dataDict['命中率']=fgm
        player_dataDict['三分命中率']=tpm
        player_dataDict['罚球命中率']=ftm
        player_dataDict['进攻篮板']=offRebs
        player_dataDict['防守篮板']=defRebs
        player_dataDict['场均得分']=points
        player_dataDict['场均篮板']=rebs
        player_dataDict['场均助攻']= assists
        player_dataDict['失误']=turnovers
        player_dataDict['场均抢断']=steals
        player_dataDict['场均盖帽']=blocks
        player_dataDict['犯规']=fouls
        player_dataDict['命中']=fgmt
        player_dataDict['出手']=fgat
        player_dataDict['三分命中']=fpmt
        player_dataDict['三分出手']=fpat
        player_dataDict['罚球命中']=ftmt
        player_dataDict['罚球出手']=ftat
        player_dataDict['总进攻篮板']=offRebst
        player_dataDict['总防守篮板']=defRebst
        player_dataDict['总得分']=pointst
        player_dataDict['总篮板']=rebst
        player_dataDict['总助攻']= assistst
        player_dataDict['总抢断']=stealst
        player_dataDict['总盖帽']=blockst
        player_dataDict['总失误']=turnoverst
        player_dataDict['总犯规']=foulst   

        print(player_dataDict)
        playerList.append(player_dataDict) 
    return playerList


def writeData(playerList, filename):
    #写入数据
    with open(filename,'w',encoding='utf-8-sig',newline='')as f:
        write=csv.DictWriter(f, fieldnames=['球队','赛区','场次','命中率','三分命中率','罚球命中率',
                                            '进攻篮板','防守篮板','场均得分','场均篮板','场均助攻',
                                            '失误','场均抢断','场均盖帽','犯规','命中','出手','三分命中','三分出手','罚球命中',
                                            '罚球出手','总进攻篮板','总防守篮板','总得分','总篮板','总助攻',
                                            '总抢断','总盖帽','总失误','总犯规'])
        write.writeheader()
        for each in playerList:
            write.writerow(each)


if __name__ == "__main__":

    for i in range(1996,2022):
        url='https://china.nba.cn/stats2/league/teamstats.json?conference=All&division=All&locale=zh_CN&season=' + str(i) + '&seasonType=4'
        filename='team_'+str(i)+'_'+str(i+1)+'.csv'
        json_data = getJson(url)
        playerList=[]
        playerList += getData(json_data)
        writeData(playerList, filename)


    

