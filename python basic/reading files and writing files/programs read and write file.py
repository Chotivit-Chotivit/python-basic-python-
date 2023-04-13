fname = input("Enter your filename :")#ส่วนนี้เป็นการป้อนค่าชื่อไฟล์เเล้วจะเเก้ไขหรือเขียนไฟล์โดยไม่จำเป้นต้องเขียนเรียกชื่อไฟล์ในโค้ดเเต่ให้โปรเกรมหาให้เลย
file = open(fname,"w")
file.write("this is name database\n") #เเบบป้อนชื่อไฟล์หลังrunโปรเเกรม
for name in range(1,10):
    aaa = input("Enter your name :")
    file.write(aaa+"\n")
file.close()
################################################
file =open("chotivit","w")
file.write("this is name database\n") #เเบบเขียนชื่อไฟล์ในโค้ดเลย
for name in range(1,10):
    aaa = input("Enter your name :")
    file.write(aaa+"\n")
file.close()

