import uuid
import base64
import uuid
from Dao import idtoencoding,sourcenametoidaccess


class facialrecogition:
    def  __init__(self):
            self.idtoencoding=idtoencoding()
            self.idtoname=sourcenametoidaccess()
            pass
    def runalgorith(self,base6,lat,long):
            #save base64 file to a folder
            imgdata=base64.b64decode(base64)
            filename = lat+long+str(uuid.uuid4()) # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
            #send the path and the location data to the algorithm function to  get the encoding vector
            a=algorithmfunction(filename,lat,long)
            list=[]
            #check the the list of encodings  and check the one closest
            for x in self.idtoencoding.findall('{}'):
                if a-x['encoding']<0.5:
                    list.append(x)




def algorithmfunction(filepath,lat,long):
        return 1
def differencebtwencoding(a,b):
        return a-b



