## Data_Analysis
数据分析项目实验课代码

### 依赖
* python==3.8
* dgl==0.6.1
* torch==1.6.0
* 其余的依赖见requirement.txt


### 项目介绍
本项目通过爬虫收集NBA球员数据和比赛数据，并对其进行可视化，最后利用图卷积来预测球队的排名。

### 文件描述
* data_collection：该文件保存爬取NBA球员数据和比赛数据的代码，和相应爬取的数据。
* data_Visualizing: 该文件对数据进行可视化的代码以及相应的图片。
* data_mining：该文件是对爬取的数据进行挖掘，使用图卷积来预测球队的排名。
