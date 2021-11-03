import urllib3
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor,as_completed,wait, ALL_COMPLETED
import time
class Spider:
    _data=[]
    _max_worker=5
    def __init__(self,e_url="",e_decode='utf-8',**kargs):
        self.e_decode=e_decode
        self.e_url=e_url
        if ("Hearders" in kargs.keys()):
            self.headers = kargs['Hearders']
        else:
            self.headers={
            "accept": "*/*",
            "accept - language": "zh - CN, zh;q = 0.9, en;q = 0.8, en - GB;q = 0.7, en - US;q = 0.6",
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            "user - agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 95.0.4638.54 Safari / 537.36 Edg / 95.0.1020.40"
            }
    def ReadAll(self):
        http=urllib3.PoolManager(3.0)
        response=http.request("GET",self.e_url,headers=self.headers)
        HtmlText=response.data.decode(self.e_decode)
        response.release_conn()
        return HtmlText

    def download(self,links:list,**kargs):
        if ("Hearders" in kargs.keys()):
            self.headers = kargs['headers']
        if("Cookie" in kargs.keys()):
            self.headers["Cookie"]=kargs['Cookie']
        executor = ThreadPoolExecutor(max_workers=self._max_worker)
        self.http = urllib3.PoolManager()
        i=0
        tasks=[]
        for link in links:
            tasks.append(executor.submit(self.requestFile,link,i))
            i+=1
        wait(tasks, return_when=ALL_COMPLETED)
        return self._data
    def requestFile(self,link,count):
        response = self.http.request("GET",link,headers=self.headers)
        print("download statue:"+response.status+">>>"+link)
        self._data.append(response.data)
        response.release_conn()


