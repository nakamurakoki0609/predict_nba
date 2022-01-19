import tweepy
import os
from dotenv import load_dotenv

#.envにあるAPIキー等の取得
load_dotenv()
API_KEY = os.environ['API_KEY']
API_SECRET_KEY = os.environ['API_SECRET_KEY']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET_TOKEN = os.environ['ACCESS_SECRET_TOKEN']

def makeAPI():
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
    return tweepy.API(auth)

def make_status(result,gameDay,opp_name,per_correct):
    
    #result=1勝つと予測した時の処理 
    if result == 1:
        STATUS ="Yes! WIN! Based on the score through halftime, the program predicted we would WIN the " + opp_name +" game on" +" "+ gameDay + " current correct:" +per_correct+"%" + " #DubNation"
        return STATUS
    #result=0負けると予測した時の処理
    else:
        STATUS = "No..., lose, Based on the score by halftime, the program predicted we would LOSE " + opp_name + " on " + gameDay + " current correct:" +per_correct +"%"+ " #DubNation"
        return STATUS

def send_tweet(result,gameDay,opp_name,per_correct):
    STATUS = make_status(result,gameDay,opp_name,per_correct)
    makeAPI().update_status(STATUS)