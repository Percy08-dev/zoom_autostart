import webbrowser
import time
import datetime
import sys

#関数
#時刻を時限に変換(ここでは5分前から開始)
p = 0 #時限用変数
p1 = 9*60 + 30 - 5 #9:30
p2 = 11*60 + 10 - 5 #11:10
p3 = 13*60 + 30 - 5 #13:30
p4 = 15*60 + 10 - 5 #15:10
p5 = 16*60 + 50 - 5 #16:50
fin = 18*60

    #毎日終了する場合は#sys.exit()からコメントアウトから戻す
def period():
    r = -1
    now = datetime.datetime.now()
    t = now.hour * 60 + now.minute
    if fin <= t:
        #sys.exit()
        0
    elif p5 <= t:
        r = 5
    elif p4 <= t:
        r = 4
    elif p3 <= t:
        r = 3
    elif p2 <= t:
        r = 2
    elif p1 <= t:
        r = 1
    else:
        #sys.exit()
        0
        
    return r
        
#日時の取得
now = datetime.datetime.now()
date = now

#曜日 day of the week = dw
dw = date.weekday()

#時間割
sun = {
    0:0,
    1:0, 
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

mon = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

tue = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

wed = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

thu = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

fri = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

sat = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    -1:"終了",
}

#曜日ごとの予定を辞書型で定義
schedule = {0:sun,1:mon,2:tue,3:wed,4:thu,5:fri,6:sat}



#main
x=0
cnt = -1
while x == 0:
    p = period()
    today_s = schedule[dw]
    if p != -1:
        if cnt != p:
            url = today_s[p]
            webbrowser.open(url)
            cnt = p
    print(p)
    time.sleep(60)
    