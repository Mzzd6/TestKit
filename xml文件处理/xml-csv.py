#coding:utf-8
import csv
from xml.etree import ElementTree as et
# version Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
def Get_ip(f_xml): #清洗xml数据
    file_xml=f_xml  #XML文件名
    sum=[]          #返回结果列表变量
    data=open(file_xml).read()
    root=et.fromstring(data)
    t1= root.findall("host") 

    for t2 in t1:
        #s2=[]  # s2[0] save hosts ip address, s2[1] save hosts status
        s2={"ip":"null","status":"null"} #存放主机IP地址和状态

        for t3 in t2:
            if(t3.tag=="status"):
               #s2.append(t3.attrib["state"]) # Get hosts status
               s2["status"]=t3.attrib["state"] #存放主机状态
            
            elif(t3.tag=="address"):
                if(t3.attrib["addrtype"]=="ipv4"):
                    #s2.append(t3.attrib["addr"])
                    s2["ip"]=t3.attrib["addr"] #存放主机IP地址
                    #sum.append(s2[::-1])    # Get hosts IP address,s2[::-1]:Reverse s2
                    sum.append(s2)  #将字典s2存入列表sum变量中

                                    
    return sum

def Write_csv(f_csv,datas): #写入csv文件中
    file_csv=f_csv     #csv文件名
    datas=datas        #需要写入文件的数据
    headers=["ip","status"]

    f=open(file_csv,"wb")
    writer = csv.DictWriter(f,fieldnames=headers)
    writer.writerows(datas)
    f.close()

if __name__ == '__main__':
    file_xml="1.xml" #需要清洗的xml文件
    file_csv="1.csv"  #需要保存到的csv文件

    s1=Get_ip(file_xml)
    Write_csv(file_csv,s1)

