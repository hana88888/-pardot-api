#wrapperをインストールする
pip install pypardot4

#PardotAPIを簡単に使うためのimport
from pypardot.client import PardotAPI

#jsonを処理するためのimport
import pandas as pd
import json

#認証のための変数を入れる
p = PardotAPI(
    email ='自分のメールアドレス',
    password ='自分のパスワード',
    user_key='自分のuser_key'
)

#認証する
p.authenticate()

#昨日以降に作成されたプロスペクトを抽出
prospects = p.prospects.query(created_after='yesterday')
total = prospects['total_results']
#1名ずつ名前を抽出
for prospect in prospects['prospect']:
    print(prospect.get('first_name'))
 
