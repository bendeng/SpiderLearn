#pip install pymysql
import pymysql

try:
    # 1.链接 数据库  链接对象 connection()
    conn = pymysql.Connect(
        host="localhost",
        port=3306,
        db='test',
        user='root',
        passwd="",
        charset='utf8'
    )
    # 2. 创建 游标对象 cursor()
    cur = conn.cursor()

    # 增加一条数据 科目表--GO语言
    #insert_sub = 'insert into subjects values(0,"GO语言")'
    #result = cur.execute(insert_sub)

    # 修改
    #update_sub = 'update subjects set title="区块链" where id=1'
    #result = cur.execute(update_sub)

    # 删除
    #delete_sub = 'delete from  subjects  where id=1'
    #result = cur.execute(delete_sub)

    search_sub = 'select * from subjects where id=1'
    cur.execute(search_sub)
    #result = cur.fetchall()
    result = cur.fetchone()
    print(result)

    # for res in result:
    #
    #     print(result)

    # 提交事务
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()

except Exception as e:
    print(e)


