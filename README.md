# Crawler-Shopee2017
    
    抓取方法: 原本找到XHR的連結，連同json的參數透過POST做傳輸，才可送出正確的請求出去。
    但如果今天發出請求後，無論如何都得不到回應時，應該是少了某些(Headers)，此時要一個一個
    的把HEADERS都加入來嘗試，直到找到正確的組合並取得商品資訊。
    某些HEADER無法直接用網頁的明細內找到，所以需要搭配Selenium 取得正確Cookie即可!

動作:
1. 首先我想要搜尋的是二手電腦，因為"金"費不夠買新的XD
2. 搜尋後點選F12並選擇XHR-->PREVIEW-->ITEM 確定相關的資料確實存在這裡

![image](https://github.com/egroeglee/pictures/blob/master/CrawlerSshopee/1.png)

3. 再點選Headers看到一個POST的連結，複製連結貼上PYTHON
![image](https://github.com/egroeglee/pictures/blob/master/CrawlerSshopee/2.png)

4. 但又發現資料卻是JASON的型態，所以點選VIEW SOURCE把資料複製在PYTHON貼上
5. jd = jason.loads()
6. res = request.post(link_,json = jd)
7. RUN之後發現報錯403
8. 403表示要讀出這些資料還需要HEADER，所以要去找出一個個的HEADERS
9. 找出來後
10. headers ={agent,cookie,token,referer}
![image](https://github.com/egroeglee/pictures/blob/master/CrawlerSshopee/3.png)

11. 確定可以取得資訊
12. 輸入res.json()可以得到資料，代表沒問題
13. 利用Selenium來抓取cookie and token 成為參數 ck & tok
14. 再把參數加入headers
15. 此時資料應該就可以抓取到了
16. 可以利用Pandas把資料分配的比較方便查看
