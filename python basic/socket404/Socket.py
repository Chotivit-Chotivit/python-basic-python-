import socket #นำเข้าโมดูลsocket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #ให้socketไปเรยกใช้socket (socket.INET=โฮสต์ม,socket.SOCK_STEAM = ports)
mysock.connect(('jibbering.com',443)) #ตรงนี้ให้ตัวเเปรmysockไปเชื่อมต่อกับเว็บที่เราใสไปไปอย่างในโค้คเราให้mysockไปconnectกับ(('jibbering.com',443))ตัวเลขด้านหลังคือports443หรือก็คือhttps
html = 'GET https://webserv.kmitl.ac.th/socialblog/text.txt HTTP/1.0\n\n'.encode() #ตรงนี้เราประกาศให้htmlเก็บค่าgetตามด้วยเว็บที่จะเปิดเเล้วก็ตามด้วยportsเเล้วก็ตามด้วยเวอร์ชันตามด้วย\n\nเเล้วก็ต้องมี encode()ปิดท้ายเสมอ
mysock.send(html)#เอาค่าออกมา

while True: #ส่งให้loopไปเรื่อยๆ
	data = mysock.recv(500) #ตรงนี้มีrecvหรือก็คือให้serverตอบกลับมาตรง500คือตัวหนังสือที่ให้มีมากสุดกี่บรรทัด
	if(len(data)<1): #ถ้าจำนวนdataมันน้อยกว่า1จะทำการbreakหรือหยุดทำงานเเต่ก้าdataมากว่า1มันจะเเสดงข้อมูลออกมา
		break #กรณีที่if data < 1
	print(data.decode()) #เเสดงdataออกมาในกรณีที่ if data > 1
mysock.close() #ปิดการทำงาน

#การrunคำส่งเข้าไปในServerที่จะใช้getเรียกต้องมี encode() ปิดท้ายเสมอ
