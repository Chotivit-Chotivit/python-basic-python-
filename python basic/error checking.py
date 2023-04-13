#การตรวจสอบข้อผิดพลาด ถ้าจะตรวจสอบต้องมีtry:เสมอ
try:
   x = int(input("Enter your number :"))
except ValueError:
   print("Not number") #ถ้าใส่ไปเเล้วมันไม่ใช่ตัวเลขมันจะขึ้น not number จะไม่ขึ้นValueErrorอีก
else:
    print(x)

################################
#การตรวจสอบตัวหารเป็น0
try:
   result = 2/0
except ZeroDivisionError:
    print("division by zero!!!")
###########################################
#ตรวจสอบค่าx y
try:
    x= int(input("Enter your name x:"))
    y= int(input("Enter your name y:"))
    result =x/y
except ValueError:
    print("not number") #ถ้าไม่ใช้ตัวเลข
except ZeroDivisionError:
    print("ตัวหารเป็น0!!") #ถ้าตัวหารเป็น0
else:
    print("result  =",result)
