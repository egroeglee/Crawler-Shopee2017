# Crawler-Shopee2017
    
    參考資料https://www.youtube.com/watch?v=jV6eHoLzD2
    蝦皮的抓取方法必須先找到放在XHR 的請求連結，接下來必須連同json 格式的參數
    一同透過POST做傳輸，方能送出正確的請求出去。但是如果今天發出請求後，如何都
    拿不到正確回應時，便要思考是不是有少帶哪些標頭(Headers)資訊，此時只要一一
    嘗試，總會找到一個正確的組合取得商品資訊。當然，有些標頭資訊是很難以取得的
    ，此時再搭配Selenium 取得正確Cookie，任何難解的網站都可以迎刃而解!


1. 首先我想要搜尋的是二手電腦，因為金費不夠買新的XD
2. 搜尋後點選F12並選擇XHR-->PREVIEW-->ITEM 確定相關的資料確實存在這裡
3. 再點選Headers看到一個POST的連結，複製連結貼上PYTHON
4. 但又發現資料卻是JASON的型態，所以點選VIEW SOURCE把資料複製在PYTHON貼上
5. jd = jason.loads()
6. res = request.post(link_,json = jd)
7. RUN之後發現報錯403
8. 403表示要讀出這些資料還需要HEADER，所以要去找出一個個的HEADERS
9. 找出來後
10. headers ={agent,cookie,token,referer}
11. 確定可以取得資訊
