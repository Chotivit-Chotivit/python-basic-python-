#ระบบ login ง่ายๆ
def login():
    name = input('please your name :')
    if name == 'hacked':
        print('Login ok ----> Go!!')#ถ้าถูกจะเเสดงLogin ok ----> Go
    else:
        print('Login fall !! กากหมา')#ถ้าผิดจะเเสดง'Login fall !! กากหมา
        login()
login()


