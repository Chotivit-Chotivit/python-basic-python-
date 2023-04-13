from socket import* #อันนี้เป็นimportโดยที่เรานำโค้คทั้งหมดของsocketมาโดยใช้form socket import

def ip_connect(x,y):
   x = gethostbyname(y) #gethostbynameเป็นฟังก์ชั่นของform socket import
   print("ip web",web,"is:",x)

web = input("Website :")
ip_connect(web,web)