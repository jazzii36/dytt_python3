import requests
import re


url="https://www.dytt8.net/html/gndy/index.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39","Referer":"https://www.baidu.com/link?url=IQ05fej4Js4l11-E2fAHuhPRwKsqi9nNmCfIAy9Bs5eMPmR82SimMLvRORE7KljfwZujfYkMi_ay6YDvTqpl9K&wd=&eqid=d0eb6a820008f174000000046279ee09"}
html=requests.get(url=url,headers=headers)
html.encoding="gb2312"
p=html.text


dimoin="https://www.dytt8.net"


pattern1=".*国内电影</a>]<a href='(.*)'>(.*)</a><br/>"
pattern2=".*日韩影片</a>]<a href='(.*)'>(.*)</a><br/>"
pattern3=".*欧美影片</a>]<a href='(.*)'>(.*)</a><br/>"

doc1=re.findall(pattern=pattern1,string=p)
doc2=re.findall(pattern=pattern2,string=p)
doc3=re.findall(pattern=pattern3,string=p)


#域名组装
# 国内电影
doc1new=list()
for data in doc1:
    data=list(data)
    data[0]=dimoin+data[0]
    doc1new.append(data)
# 日韩电影
doc2new=list()
for data2 in doc2:
    data2 = list(data2)
    data2[0] = dimoin + data2[0]
    doc2new.append(data2)
# 欧美电影
doc3new=list()
for data3 in doc3:
    data3 = list(data3)
    data3[0] = dimoin + data3[0]
    doc3new.append(data3)

#获取影片的种子地址
moviename1=list()
moviefile1=list()
for url in doc1new:
    html2=requests.get(url=url[0])
    html2.encoding="gb2312"
    pattern4='<br /><br /><br /><a target="_blank" href="(.*)"><strong><font'
    mag=re.findall(pattern=pattern4,string=html2.text)
    moviename1.append(str(url[1]))
    moviefile1.append(str(mag[0]))

moviename2=list()
moviefile2=list()
for url in doc2new:
    html2=requests.get(url=url[0])
    html2.encoding="gb2312"
    pattern4='<br /><br /><br /><a target="_blank" href="(.*)"><strong><font'
    mag=re.findall(pattern=pattern4,string=html2.text)
    moviename2.append(str(url[1]))
    moviefile2.append(str(mag[0]))

moviename3=list()
moviefile3=list()
for url in doc3new:
    html2=requests.get(url=url[0])
    html2.encoding="gb2312"
    pattern4='<br /><br /><br /><a target="_blank" href="(.*)"><strong><font'
    mag=re.findall(pattern=pattern4,string=html2.text)
    moviename3.append(str(url[1]))
    moviefile3.append(str(mag[0]))


#组装输出值
dict1new=dict(zip(moviename1,moviefile1))
dict2new=dict(zip(moviename2,moviefile2))
dict3new=dict(zip(moviename3,moviefile3))

#打包种子文件
dict=dict()
dict.update(dict1new)
dict.update(dict2new)
dict.update(dict3new)


file=open(file="今日更新电影.txt",mode="w",encoding='utf-8')
file.write(str(dict))
file.close()