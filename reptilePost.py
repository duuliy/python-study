import requests        #导入requests包
import json
def get_translate_date(word=None):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    From_data={
      'from': 'zh',
      'to': 'en',
      'query': '我爱中国',
      'transtype': 'realtime',
      'simple_means_flag': '3',
      'sign': '731618.1034963',
      'token': 'c3ee7b9fac0e17692b0224d49a61f963',
      'domain': 'common'
      }
    #请求表单数据
    response = requests.post(url,data=From_data)
    # 将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    #打印翻译后的数据
    # print(content['translateResult'][0][0]['tgt'])
if __name__=='__main__':
    get_translate_date('我爱中国')