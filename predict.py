import pickle

filename = "model.sav"

#モデルデータを読みこんで、予測した結果配列で返す
def get_result(X_test):
    loaded_model = pickle.load(open(filename,'rb'))
    result = loaded_model.predict_proba(X_test)
    result = result.argmax(axis=1)
    return result[0]