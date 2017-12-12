# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:52:59 2017

@author: GLee
"""


from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://shopee.tw/')
ck = ';'.join(['{}={}'.format(item.get('name'), item.get('value')) for item in driver.get_cookies()]) #把從COOKIE抓到的NAME 做成字串,再把結果放到LIST中
tok = [item.get('value') for item in driver.get_cookies() if item.get('name') == 'csrftoken'][0]

import requests
import json

jd = json.loads('{"item_shop_ids":[{"itemid":153014542,"shopid":11318369,"logisticid":[30006,39304,30005,39303]},{"itemid":453346309,"shopid":11318369,"logisticid":[39303,30001,39304,30005]},{"itemid":181231589,"shopid":9986870,"logisticid":[30006,39304,30005]},{"itemid":706142766,"shopid":2725500,"logisticid":[30006,30005]},{"itemid":511783966,"shopid":16964695,"logisticid":[39303]},{"itemid":745482064,"shopid":3273172,"logisticid":[30005,30006,30007]},{"itemid":739700713,"shopid":37432969,"logisticid":[39304]},{"itemid":735466444,"shopid":25372675,"logisticid":[39304]},{"itemid":730913844,"shopid":15846664,"logisticid":[39304,30001]},{"itemid":729945682,"shopid":13932848,"logisticid":[30007,30005,30006]},{"itemid":729037254,"shopid":30346572,"logisticid":[39303,30001]},{"itemid":727352997,"shopid":16113066,"logisticid":[30006,30005]},{"itemid":720062771,"shopid":14959544,"logisticid":[30001]},{"itemid":718068307,"shopid":14959544,"logisticid":[30001]},{"itemid":714331212,"shopid":11423753,"logisticid":[30005]},{"itemid":712731824,"shopid":9362398,"logisticid":[30001]},{"itemid":707461806,"shopid":28152118,"logisticid":[30005,30006]},{"itemid":699962468,"shopid":7318926,"logisticid":[39303,30001]},{"itemid":696488376,"shopid":16877974,"logisticid":[39304]},{"itemid":692298147,"shopid":22663013,"logisticid":[39304]},{"itemid":676139414,"shopid":2501243,"logisticid":[30005,30006,30007]},{"itemid":676127219,"shopid":2501243,"logisticid":[30006,30007,30005]},{"itemid":674430759,"shopid":2695501,"logisticid":[39303]},{"itemid":656194288,"shopid":8776825,"logisticid":[30005,30006,39303,39304]},{"itemid":645754787,"shopid":26610914,"logisticid":[30005,39303,39304,30001]},{"itemid":634867768,"shopid":14192623,"logisticid":[39304]},{"itemid":631753554,"shopid":9986870,"logisticid":[39304]},{"itemid":628476573,"shopid":5139293,"logisticid":[30006,39304]},{"itemid":618419556,"shopid":6579828,"logisticid":[30007,30005,30006]},{"itemid":618320110,"shopid":6579828,"logisticid":[30005,30006,30007]},{"itemid":617761453,"shopid":3503005,"logisticid":[30001]},{"itemid":612954214,"shopid":7961395,"logisticid":[39303]},{"itemid":600955778,"shopid":18319742,"logisticid":[30005]},{"itemid":600299623,"shopid":16964695,"logisticid":[39303]},{"itemid":589066668,"shopid":3165104,"logisticid":[39303]},{"itemid":584357032,"shopid":4020578,"logisticid":[30007,30005,30006]},{"itemid":584354214,"shopid":4020578,"logisticid":[30005,30006,30007]},{"itemid":580483516,"shopid":16514758},{"itemid":577160244,"shopid":2571728,"logisticid":[30006,39304,30005]},{"itemid":568534177,"shopid":7924711,"logisticid":[39303,30001]},{"itemid":566684791,"shopid":7924711,"logisticid":[30001,39303]},{"itemid":538107601,"shopid":19705633,"logisticid":[39304,39303]},{"itemid":518079394,"shopid":19320041,"logisticid":[30006,30007,39304,30005,39303]},{"itemid":518077025,"shopid":19320041,"logisticid":[30005,39303,30006,30007,39304]},{"itemid":514117944,"shopid":26166698,"logisticid":[30007,30005,30006]},{"itemid":503576735,"shopid":26081965,"logisticid":[30001]},{"itemid":502381382,"shopid":12066784,"logisticid":[39304,30001]},{"itemid":490601506,"shopid":2004966,"logisticid":[30005,30006,30001]},{"itemid":476365712,"shopid":7961395,"logisticid":[39303]},{"itemid":474983678,"shopid":26081965,"logisticid":[30001]}]}')
#res = requests.post('https://shopee.tw/api/v1/items/', json = jd)#嘗試抓取資訊，發現 403 錯誤:抓不到資源
#發現缺少Header，所以開始加入一些資訊來嘗試
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',#判斷是由人來瀏覽網頁
    #'x-csrftoken':'JDk5bADKtwHszPE0qLn6RlrsjHtnmzBZ',
    'x-csrftoken': tok,#用變數代替
    'referer':'https://shopee.tw/search/?keyword=%E4%BA%8C%E6%89%8B%E9%9B%BB%E8%85%A6&subcategory',#從何處導過來的資訊
    'cookie': ck, #用變數代替
    #'cookie':'SPC_F=stlvph8QsrC86eOoJjSwfjNfzZwimjmr; REC_T_ID=8acaaad8-b58d-11e7-b993-1866da92ead7; __BWfp=c1510110441051x9914a0bc1; __utma=88845529.853388662.1508500522.1510329554.1510411779.3; __utmz=88845529.1510110474.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _atrk_siteuid=kb6fk3GkSV3GOfsL; SPC_IA=-1; SPC_EC=-; SPC_T_ID="OTmszC20QfXDrRjAixRdpbrPPnFLEDBFGc6+j9bLBgNqeHty/HXnBnWs5ht1pQsUlxAVz+haW9l2WAt0d1FL53gxhjj4eLYerZSwgpBNkaU="; SPC_U=-; SPC_T_IV="Q3srBbbcYLfd+084jrCyAg=="; _gat=1; csrftoken=JDk5bADKtwHszPE0qLn6RlrsjHtnmzBZ; bannerShown=true; SPC_SC_TK=; UYOMAPJWEMDGJ=; SPC_SC_UD=; _ga=GA1.2.853388662.1508500522; _gid=GA1.2.718423720.1512978261; _gac_UA-61915057-6=1.1508500522.Cj0KCQjwvabPBRD5ARIsAIwFXBl4npQTtlSkWFbL-RdXbqLlpO6at40qfZtYsUXP1UOfyq_WgjxrbzQaAiYFEALw_wcB; SPC_SI=lqwctsy9ooci6qe2rka5u5tz5nk5yo2i',
}
res = requests.post('https://shopee.tw/api/v1/items/', json = jd, headers = headers)

import pandas
df = pandas.DataFrame(res.json())
