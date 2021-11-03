from bs4 import BeautifulSoup
import re
class FindTarget:
    def __init__(self,e_HtmlCode,e_target_reg='^.*'):
        self.e_HtmlCode=e_HtmlCode
        self.bs=BeautifulSoup(self.e_HtmlCode,'html.parser')
        #输出格式化HTML
        #print(self.bs.prettify())
        self.reg_par=re.compile(e_target_reg)
    def find(self,**kargs):
            if("id" in kargs.keys()):
                e_id=kargs['id']
                raw_target=self.bs.find_all(id=e_id)
                return self._RegularMatch(raw_target)
            if("class_" in kargs.keys()):
                e_class = kargs['class_']
                raw_target = self.bs.find_all(class_=e_class)
                return self._RegularMatch(raw_target)
    def findAllTag(self,TagType):
        return self.bs.find_all(TagType)
    def _RegularMatch(self,rawList):
        result=[]
        aaa=0
        for i in rawList:
            finds=self.reg_par.findall(str(i))
            result.append(finds)
            aaa += 1
        return  result
    def setHtmlCode(self,htmlcode):
        self.e_HtmlCode=htmlcode
        self.bs = BeautifulSoup(self.e_HtmlCode, 'html.parser')
    def setReg(self,reg):
        self.reg_par=re.compile(reg)

    def getTagAttr(self,Tags,Attr,**kargs):
        result=[]
        ii=0
        for i in Tags:
            i=str(i)
            bs_temp=BeautifulSoup(i, 'html.parser')
            result.append(bs_temp.img.attrs[Attr])
        return result

