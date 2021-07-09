import sqlite3
import json
import sys

# def getTest():
#   return 666
def getUser():
    searchId=sys.argv[1]
  # 查询记录：
    # conn = sqlite3.connect('/test.db')#根据自己的数据库地址进行填写
    conn = sqlite3.connect('../../test.db')#根据自己的数据库地址进行填写
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from user where id=?', searchId)
    # 获得查询结果集:
    data = cursor.fetchall()
    # print(data)

    # test=getTest()
    sys.stdout.write(json.dumps(data))
    sys.stderr.write(json.dumps(data))
    # print(sys.stderr)
    # print(json.dumps(data, ensure_ascii=False, indent=4))

    # return json.dumps(data, ensure_ascii=False, indent=4)
#  content = json.loads(response.text)
if __name__ == '__main__':
    getUser()