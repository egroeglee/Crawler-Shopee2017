# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:52:59 2017

@author: GLee
"""


from Selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://shopee.tw/')

import requests

import json
jd = json.loads('{"item_shop_ids":[{"itemid":20087240,"shopid":3617056},{"itemid":12881421,"shopid":2698155},{"itemid":19338928,"shopid":3617056},{"itemid":10658620,"shopid":2698155},{"itemid":10533325,"shopid":2698155},{"itemid":11032358,"shopid":2698155},{"itemid":10662647,"shopid":2698155},{"itemid":11149608,"shopid":2698155},{"itemid":22571492,"shopid":2698155},{"itemid":12483544,"shopid":3617056},{"itemid":12767696,"shopid":2698155},{"itemid":14043348,"shopid":2698155},{"itemid":9902675,"shopid":3617056},{"itemid":10209201,"shopid":3617056},{"itemid":10672062,"shopid":2698155},{"itemid":10837523,"shopid":2698155},{"itemid":10217180,"shopid":3617056},{"itemid":11037502,"shopid":2698155},{"itemid":10665919,"shopid":2698155},{"itemid":12961395,"shopid":2698155},{"itemid":10209995,"shopid":3617056},{"itemid":9885946,"shopid":3617056},{"itemid":10831164,"shopid":2698155},{"itemid":12962175,"shopid":2698155},{"itemid":12485661,"shopid":3617056},{"itemid":6273136,"shopid":2698155},{"itemid":12488152,"shopid":3617056},{"itemid":10937063,"shopid":2698155},{"itemid":11892577,"shopid":2698155},{"itemid":12958045,"shopid":2698155},{"itemid":10211261,"shopid":3617056},{"itemid":10937071,"shopid":2698155},{"itemid":20088766,"shopid":3617056},{"itemid":9882308,"shopid":3617056},{"itemid":10833104,"shopid":2698155},{"itemid":12479887,"shopid":3617056},{"itemid":13143524,"shopid":2698155},{"itemid":12439415,"shopid":3022167},{"itemid":12485841,"shopid":3617056},{"itemid":16552891,"shopid":3617056},{"itemid":10967786,"shopid":2698155},{"itemid":11655454,"shopid":3617056},{"itemid":11670484,"shopid":1686644},{"itemid":4978896,"shopid":2292850},{"itemid":12484031,"shopid":3617056},{"itemid":8919568,"shopid":2273965},{"itemid":19325422,"shopid":3617056},{"itemid":10659434,"shopid":2698155},{"itemid":30188251,"shopid":1273184},{"itemid":30301130,"shopid":6080885}]}')
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
'x-csrftoken':'7wWOLqv2lJHF42rPn8CnkkoAeHUX2zCq',
'referer':'https://shopee.tw/%E5%AE%B6%E9%9B%BB%E5%BD%B1%E9%9F%B3-cat.71',
'cookie':'SPC_F=stlvph8QsrC86eOoJjSwfjNfzZwimjmr; REC_T_ID=8acaaad8-b58d-11e7-b993-1866da92ead7; __BWfp=c1510110441051x9914a0bc1; __utma=88845529.853388662.1508500522.1510329554.1510411779.3; __utmz=88845529.1510110474.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _atrk_siteuid=kb6fk3GkSV3GOfsL; SPC_IA=-1; SPC_EC=-; SPC_T_ID="OTmszC20QfXDrRjAixRdpbrPPnFLEDBFGc6+j9bLBgNqeHty/HXnBnWs5ht1pQsUlxAVz+haW9l2WAt0d1FL53gxhjj4eLYerZSwgpBNkaU="; SPC_U=-; SPC_T_IV="Q3srBbbcYLfd+084jrCyAg=="; csrftoken=7wWOLqv2lJHF42rPn8CnkkoAeHUX2zCq; _gat=1; SPC_SC_TK=; UYOMAPJWEMDGJ=; SPC_SC_UD=; _ga=GA1.2.853388662.1508500522; _gid=GA1.2.943461500.1512541987; _gac_UA-61915057-6=1.1508500522.Cj0KCQjwvabPBRD5ARIsAIwFXBl4npQTtlSkWFbL-RdXbqLlpO6at40qfZtYsUXP1UOfyq_WgjxrbzQaAiYFEALw_wcB; SPC_SI=kym1n3zp78ynuieh6v5j6gurzp4ibti3',
}        
                  
res = requests.post('https://shopee.tw/api/v1/items/', json = jd, headers = headers)
res.text
