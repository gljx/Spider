import urllib3
from bs4 import BeautifulSoup
import json
from EasySpider.Spider import Spider
from EasySpider.FindTargetUtils import FindTarget
from FileUtils.SaveFile import SaveFile
def main():
    #需要爬的网站
    spider= Spider("https://www.nipic.com/")
    code=spider.ReadAll()
    findT=FindTarget(code)
    #筛选出ID 或者 class
    reslut=findT.find(class_="newIndex-hotpic")
    strings=str(reslut).replace(",","")
    findT.setHtmlCode(strings)
    Alltags=findT.findAllTag('img')
    links=findT.getTagAttr(Alltags,'src')
    download_and_save(links)
def download_and_save(links):
    spider = Spider()
    data=spider.download(links)
    count=0
    for i in data:
        sf = SaveFile("D:\\test", str(count)+".jpg")
        sf.save(i)
        count+=1
    print("finished")
if __name__ == '__main__':
    main()
