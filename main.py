import pandas as pd
import streamlit as st

# Todo ヘルメットの位置を更新
# todo 複数人の検索

'''
ヘルメットの位置を探します
'''

names = \
    [['藤井', '原田', '奥田', '田中', '向中野', '山本', '平野', '高間', '吉澤', '三矢', '西海', '中', '宇野', '井沢', '中島', '中山', '松本', '高村', '井上',
      '松浦'],
     ['安藤', '平川', '張', '?', '星子', '大志民', '志田', '島田', ' 横田', '水沢', '津村', '高坂', '吉田(研)', '白川', '戸田(克)', '片山(博)', '望月',
      '深澤', '馬場', '角谷'],
     ['古城', '米山', '小澤', '佐藤(尚)', '牛島', '北原', '鍋島', '佐藤(伸)', '吉田(周)', '柏原(拓)', '杉本', '千葉', '安東', '加藤(博)', '古田', '竹田',
      '横山', '菅野', '植木', '黒田'],
     ['篠崎', '吉田(可)', '石井', '川口', '坂本', '新堀', '戸田(庸)', '片山(慶)', '本藤', '松原', '山本(雅)', '山口', '小澤', '永易', '旗手', '深澤(音)',
      '小保方', '佐藤(大史)', '畔柳', '金城'],
     ['島村', '村上', '鈴木(満)', '照井', '松下', '戸田(彩)', '永尾', '五十嵐', '川崎', '弘瀬', '徳平(剛)', '杉江', '津田', '永易', '新田', '横須賀', '熊谷',
      '砂押', '出口'],
     ['加来', '井本', '小野口', '田上', '石橋', '上田', '金子', '近藤', '早川', '宮園', '坂下', '伊藤', '村上(一)', '宮之原', '青木', '?', '平', '?',
      '前田', '吉田直斗']]

dataframe = pd.DataFrame(names)

who = st.text_input(label='検索したい人の名前を入れてください', value='田上')


def search_for_name(who_to_search):
    for index, name in enumerate(names):
        for index2, name2 in enumerate(name):
            if name2 == str(who_to_search):
                # print(index, index2, name2)
                return index, index2, name2


def cell_style(value):
    if value == who:
        return "background-color: gray; color: white"
    else:
        return ""


st.dataframe(dataframe.style.applymap(cell_style))
st.write('input: ', search_for_name(who))

'''
2021/10/3 ver1公開！ 一人だけ検索できるようになりました。
'''
