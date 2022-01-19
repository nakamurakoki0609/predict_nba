from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import sys

#最初にデータを取得するサイトを読み込む
home_url = "https://www.basketball-reference.com/teams/GSW/2022/gamelog/" 
res = urllib.request.urlopen(home_url)
soup = BeautifulSoup(res.read(),features="lxml")

#最後の更新日から最新の試合日を比較し以降の処理を行うか判断する
def access_to_site(updateDay):
    date_games = soup.find_all(attrs={'data-stat':'date_game'})
    for date in date_games:
        date = date.find('a')
        if date is not None and string_to_datetime(updateDay) < string_to_datetime(date.get_text()):
            game_url = date.get('href')
            df_stats = get_boxscore(game_url)
            return df_stats
    
    sys.exit()

#日にちで比較を行えるようにする
def string_to_datetime(string):
    return  datetime.datetime.strptime(string, "%Y-%m-%d")

#halfTimeまでのboxscoreの取得
def get_boxscore(game_url):
    base_url = "https://www.basketball-reference.com"
    score_url = base_url + game_url
    
    score_res = urllib.request.urlopen(score_url)
    soup = BeautifulSoup(score_res.read(),features='lxml')
    table = soup.find(attrs = {"id": "box-GSW-h1-basic"})
    foot = table.find('tfoot')
    
    stats = []
    stats_columns = ['fg','fga','fg_pct','fg3','fg3a','fg3_pct','ft','fta','ft_pct','orb','drb','trb','ast','stl','blk','tov','pf','pts']
    
    for column in stats_columns:
        stats.append(foot.find(attrs={'data-stat':column}).get_text())
        
    df_stats = pd.DataFrame([stats],columns = stats_columns)
    df_stats.fillna(0,inplace=True)
    return df_stats
    

#試合の行われた日の取得
def get_gameDay(updateDay):
    
    date_games = soup.find_all(attrs={'data-stat':'date_game'})
    for date in date_games:
        date = date.find('a')
        if date is not None and string_to_datetime(updateDay) < string_to_datetime(date.get_text()):
            game_day = date.get_text()
            return game_day

def get_opp_name(game_day):
    elems = soup.find("a",text =game_day)
    #game_dayを利用して親属性から対戦相手の名前の要素を出す
    opp_elems = elems.parent.parent.find( attrs = {'data-stat':'opp_id'})
    opp_a = opp_elems.find('a')
    opp_name = opp_a.get_text()
    return opp_name

def compare_correct_predictions(result,game_day):
    elems = soup.find("a",text =game_day)
    #game_dayを利用して親属性から対戦相手の名前の要素を出す
    result_elems = elems.parent.parent.find( attrs = {'data-stat':'game_result'})
    game_result = result_elems.get_text()
    if result == 1 and game_result =="W":
        return True
    elif result == 0 and game_result=="L":
        return True
    else:
        return False