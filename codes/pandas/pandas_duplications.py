from pymongo import MongoClient

# MongoDB 서버에 연결 : Both connect in case local and remote
client = MongoClient('mongodb://192.168.0.135:27017/')

# 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
db = client['mydatabase']

# 'users' 컬렉션 find
collection_users = db['users_collecting']
users_source = collection_users.find({})

# 중복 처리
import pandas as pd
df_data = pd.DataFrame(list(users_source))
df_users_source = df_data.drop_duplicates(subset = ['name'])

# users_target insert
collection_target = db['users_target']
collection_target.insert_many(df_users_source.to_dict("records"))

pass
