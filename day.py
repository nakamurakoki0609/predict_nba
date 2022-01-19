
path = "./update_date.txt"
#最後の更新日の取得
def get_updateDay():

    text = open(path, 'r')
    update_day = text.read()
    text.close()
    
    return update_day

#更新日の更新
def change_updateDay(gameDay):
    text = open(path, 'w+')
    text.write(gameDay)
    text.close()
    
