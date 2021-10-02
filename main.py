import pandas as pd
import streamlit as st

"""
ヘルメットの位置を探します
"""
names = [['田上', '永尾'],
         ['広瀬', '山口']]

dataframe = pd.DataFrame(names)

who = st.text_input(label='検索したいひとの名前を入れてください', value='例：田上')


def search_for_name(who_to_search):
    for index, name in enumerate(names):
        for index2, name2 in enumerate(name):
            if name2 == str(who_to_search):
                print(index, index2, name2)
                return index, index2, name2


def cell_style(value):
    if value == who:
        return "background-color: gray; color: white"
    else:
        return ""


# dataframe.style.applymap(cell_style)
st.table(dataframe.style.applymap(cell_style))
st.write('input: ', search_for_name(who))
