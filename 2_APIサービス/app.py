import streamlit as st
import requests
import pandas as pd

API_URL =""

# Model
def get_report(key_word):
    if key_word == "":
        data = '[{"id":0, "report" : "キーワードを入れて下さい。"}]'
    elif "%" in key_word:
        data = '[{"id":0, "report" : "キーワードに「％」は使えません。"}]'
    else:
        query = '/api?key_word=' + key_word
        url = API_URL + query
        try:
            data = requests.get(url).json()
        except:
            data = '[{"id":0, "report" : "エラーが発生しました。"}]'
    if data == "[]":
        data = '[{"id":0, "report" : "該当する報告書はありません。"}]'
    df_out = pd.read_json(data)
    df_out = df_out[['id', 'report']]
    return df_out[::-1].head(20)

# View
st.title("委託調査報告書検索")
key_word = st.text_input("キーワード：", value='')
st.table(get_report(key_word))