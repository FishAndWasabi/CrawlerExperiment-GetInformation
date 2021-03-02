from tqdm import tqdm
import pandas as pd
import requests
import time


class Crawler:
    def __init__(self):
        self.type_url = "https://searchapi.energylabelrecord.com/record/clist.do"
        self.list_url = "https://searchapi.energylabelrecord.com/record/list.do"
        self.detail_url = "https://searchapi.energylabelrecord.com/record/get.do"
        self.models = {}
        self.result = pd.DataFrame()
        self.data = {'pageNum': 1, 'pageSize': 10}
        self.types = {'备案号': 'recordNo', '产品型号': 'markingTitle'}

    @staticmethod
    def get(url, data):
        response = requests.get(url, data, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response

    def __get_total(self):
        response = self.get(self.type_url, {'_': int(time.time())})
        self.models = {_['text']: _['value'] for _ in response.json()}

    def __get_products(self):
        return self.get(self.list_url, self.data).json()

    def run(self, model, type_, typeValue):
        self.__get_total()
        ec_model_no = self.models[model]
        self.data['ec_model_no'] = ec_model_no
        self.data['type'] = self.types[type_]
        self.data['typeValue'] = typeValue
        self.data['_'] = time.time()
        products = self.__get_products()
        for product in tqdm(products):
            response = self.get(self.detail_url, {'uid': product['uid'], '_': int(time.time())}).json()
            params_list = {param['desc'].replace(' ', ''): param['value'].replace(' ', '') for param in response['paramslist']}
            response = dict(response,**params_list)
            self.result = self.result.append(pd.DataFrame().from_dict({0: response}).T, ignore_index=True)
        try:
            self.result.rename(columns={'cname': '类型名称',
                                        'level': '级别',
                                        'model': '型号',
                                        'pubdate': '发布时间',
                                        'recordno': '备案号码',
                                        'recordtype': '备案类型',
                                        'unit': '单位'}, inplace=True)
            self.result.drop(columns=['producer', 'paramslist', 'cid', '依据国家标准'], inplace=True)
            self.result.set_index('uid', inplace=True)
            self.result = self.result[['型号', '级别', '类型名称', '发布时间', '备案类型', '备案号码', '生产者名称', '单位', '24h固有能耗系数(ε)', '热水输出率(μ)']]
        except Exception as err:
            print(str(err))


if __name__ == "__main__":
    crawler = Crawler()
    crawler.run('储水式电热水器 2008版', '产品型号', 'bbb')
    print(crawler.result)
    crawler.result.to_csv('result.csv',encoding='gbk',index=False)
