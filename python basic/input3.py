#Script ของ ฟังก์ชั่นและการป้อนค่า

print("hello my friend")
user =""  #ประกาศตัวเเปร
passwd = ""#ประกาศตัวเเปร

def username():
	return input("username : ") #โปรเเกรมจะข้ามไปก่อนเพราะยังไม่เห็นการเรียกใช้

def passwd():
	return input("passwd : ") #เมื่อโปรเเกรมเห้นการใช้ฟังก์ชั่นdefก็จะทำงานเเละจะถูกretureกลับไหที่ตัวเเปรที่เราประกาศไว้


user = username() #มันคืออันที่เราประกาศตัวเเปรไปเเล้วที่อยู่ด้านบน
passwd= passwd()  #เมื่อโปรเเกรมเห็นการเรียกใข้ฟังก์ชั่นมันจะกลับไปที่def

print("\n") #การเว้นบรรทัด
print("username :",user) #เเสดงusername
print("passwd :",passwd) #เเสดงpasswd