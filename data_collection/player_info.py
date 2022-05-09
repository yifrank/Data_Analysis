import requests
import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url='https://china.nba.cn/stats2/league/playerlist.json?locale=zh_CN'
def getJson(url):
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    response = requests.get(url,headers=headers)
    json_data = json.loads(response.text)
    return json_data
def  getData(json_data):
    playerList=[]
    for item in json_data['payload']['players']:
        player_dataDict={}
        #球员编号
        code =item['playerProfile']['code']
        #球员
        name=item['playerProfile']['displayNameEn']
        #国家
        country = item['playerProfile']['country']
        #身高
        height = item['playerProfile']['height']
        #选秀年
        draft_year = item['playerProfile']['draftYear']
        # 经历
        experience = item['playerProfile']['experience']
        #学校类型
        school_type = item['playerProfile']['schoolType']
        #位置
        position = item['playerProfile']['position']
        #体重
        weight = item['playerProfile']['weight']
        #城市
        city = item['teamProfile']['city']
        #球队
        teamname = item['teamProfile']['name']
        #赛区
        displayConference = item['teamProfile']['displayConference']
        #分区
        division = item['teamProfile']['division']

        player_dataDict['球员编号']=code
        player_dataDict['球员']=name
        player_dataDict['国家']=country
        player_dataDict['身高']=height
        player_dataDict['选秀年']=draft_year
        player_dataDict['经历时间']=experience
        player_dataDict['学校类型']=school_type
        player_dataDict['位置']=position
        player_dataDict['体重']=weight
        player_dataDict['城市']=city
        player_dataDict['球队']= teamname
        player_dataDict['赛区']=displayConference
        player_dataDict['分区']=division
        print(player_dataDict)
        playerList.append(player_dataDict) 
    return playerList
def writeData(playerList):
    #写入数据
    with open('now_player_persondata.csv','w',encoding='utf-8-sig',newline='')as f:
        write=csv.DictWriter(f, fieldnames=['球员编号','球员','国家','身高','选秀年','经历时间','学校类型',
                                            '位置','体重','城市','球队',
                                            '赛区','分区'])
        write.writeheader()
        for each in playerList:
            write.writerow(each)
if __name__ == "__main__":
    json_data = getJson(url)
    playerList=[]
    playerList += getData(json_data)
    writeData(playerList)

