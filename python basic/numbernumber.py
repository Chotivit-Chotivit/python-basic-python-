#PythonList คลังเก็บข้อมูล

#################################################################
for lists in ชื่อตัวเเปร :
        print("Number :",lists)
        #เป้นคำส่งเรียกข้อมูล
################################################################


#number =[1,2,3,4,5,6,7,8] #ตรงนี้คือข้อมูลหรือตะกร้า
for lists in number :     #เราทำการเรียกข้อมูลในlistsหรือในnumberให้เเสดงผลออกมา
    print("Number :",lists)  #อันนี้เป็นตัวเลข

########################################################################
#การใช้append
bag = ["pen","pencii","int"]

name =["dd","sss"] #อันนี้เป็นการเพิ่มลงไปในlists

########################################################
#การเอาตะกร้าหรือข้อมูลมารวมกัน การใช้extend
bag = ["pen","pencii","int"]

name =["dd","sss"]

bag.extend(name)#เอาตะกร้าหรือข้อมูลของbagเเละname มารวมกัน (ตำส่ง)

############################################################
#อันนี้เป็นการใช้คำส่งลบ การใช้pop

bag = ["pen","pencii","int"]
bag.pop() #คำส่ง

################################################################
#อันนี้เป็นการนับจำนวนของ
bag = ["pen","pencii","int"]
 #ใช้คำสั่งชื่อ ชื่อตัวเเปรตะกร้า.count(ชื่อของในlists)
######################################################################
#การ insert
bag = ["pen","pencii","int"]

bag.insert(3,"asjdkha") #เป็นการเเทรกข้อความให้ถูกเรียงในตำเเหน่งที่เท่าไร
#####################################################################

#การลบข้อความที่ต้องการลบ
bag = ["pen","pencii","int"]

bag.remove("pen")

#############################################################
#มันคือการreverse
bag = ["pen","pencii","int"]

bag.reverse()
########################################
#การเรียกลำดับข้อมูล sort
bag = ["apen","zpencii","xint"]
bag.sort()

