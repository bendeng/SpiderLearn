#pip install redis
#pip show redis

import redis
# 1.链接数据库 key--value。默认链接数据库是0
client = redis.StrictRedis(host='127.0.0.1', port=6379)

# 2.设置key
key = 'pyredis'

# 3.string  增加
result = client.set(key, "1")

# 4.删 1, 0
result = client.delete(key)


# 5.改
result = client.set(key,'2')


# 6.查--bytes
result = client.get(key)

# 查看所有的键
result = client.keys()

print(result)