import os
class SaveFile:
    def __init__(self,path,FileName):
        if(os.path.isdir(path)):
            if(not os.path.exists(path)):
                os.mkdir(path)
            self.path=path
            self.FileName=FileName
        else:
            raise Exception("Not A Path","Error")

    def save(self,data):
        file = open(self.path+"\\"+self.FileName,"wb")
        file.write(data)
        file.close()
        return True