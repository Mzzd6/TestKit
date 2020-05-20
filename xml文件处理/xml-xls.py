import xml.dom.minidom
import xml
import xlwt

#python3 xml-xls.py
dom = xml.dom.minidom.parse('1.xml')

root = dom.documentElement

hostlist = root.getElementsByTagName('host')

list1 = []

for i in hostlist:
	address = i.getElementsByTagName('address')[0].getAttribute('addr')
	portid = i.getElementsByTagName('port')[0].getAttribute('portid')
 	
	
	# state = i.getElementsByTagName('state')[0].getAttribute('state')
	

	port = i.getElementsByTagName('port')
	 # print(port)
	if port != []:
	
		for j in port:

			
			state = j.getElementsByTagName('state')
			c = j.getAttribute('portid')
		
			for m in state:
				a = m.getAttribute("state")

				service = j.getElementsByTagName('service')
				for n in service:
					b=n.getAttribute("name")
				if a == "open":				
					list1.append([address,c,b])



workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('sheet 1')

for d in range(len(list1)):
	for e in range(len(list1[d])):
		worksheet.write(d+1,e,list1[d][e])
			

workbook.save('1.xls')

		

