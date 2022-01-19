import result_csv
import day
import boxscore
import predict
import csv
from tweet import send_tweet

import sys

def main():
    updateDay = day.get_updateDay()
    df_stats = boxscore.access_to_site(updateDay)
    result = predict.get_result(df_stats)
    gameDay = boxscore.get_gameDay(updateDay)
    opp_name = boxscore.get_opp_name(gameDay)
    
    correct = boxscore.compare_correct_predictions(result, gameDay)
    result_csv.add_result(result,correct)
    per_correct = result_csv.percent_correct()
    day.change_updateDay(gameDay)
    send_tweet(result,gameDay,opp_name,per_correct)
    
    print('finish')
main()
