import gzip #ライブラリの読み込み
import re
import codecs
import string

from pykakasi import kakasi #日本語をアルファベットに変換する準備
kakasi = kakasi()
kakasi.setMode('H', 'a') #ひらがな→アルファベット

kakasi.setMode('K', 'a') #カタカナ→アルファベット

kakasi.setMode('J', 'a') #漢字→アルファベット

conv = kakasi.getConverter()






base = 'えんしょういわちひろ' #押韻したい文字列

lower = -2 #許容範囲
upper = 2

basetxt = re.sub(r'[^aiueo]','',conv.do(base)) #母音の抽出

with gzip.open('jawiki-20230720-all-titles-in-ns0.gz','rb') as f: #辞書より押韻候補を表示
    reader = codecs.getreader("utf_8")

    title = reader(f)

    for comp in title:

        jpn = comp.translate(str.maketrans('','',string.printable)) #アルファベットと記号を除いて判定

        if (base not in comp) and (comp not in base) and (len(jpn) > 0):

            comptxt = re.sub(r'[^aiueo]','',conv.do(jpn))

            if (basetxt in comptxt) and (lower < (len(comptxt) - len(basetxt)) < upper):

                print(comp)    