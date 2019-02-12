import json

#字符串和dic、list的互相转换: loads  dumps
str = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(str)
print(list_data)

obj = [{"name": "张三", "age": 20}, {"name": "李四", "age": 18}]
str_data = json.dumps(obj)
print(str_data)


#文件对象和 dict list转换: dump load
# 需要将json对象先转换成字符串写入到文件中
obj = [{"name": "张三", "age": 20}, {"name": "李四", "age": 18}]
str_obj = json.dumps(obj)
with open('json_test.json', 'w') as f:
    f.write(str_data)

#但是json模块提供了直接将json对象直接写入文件的方法
json.dump(obj, open('json_test2.json', 'w'))

#那么反过来读取json文件，就是这样写了
json_obj = json.load(open('json_test2.json','r'))
print('读取文件：'+ json.dumps(json_obj))

