def Second():
    second =int(input('second :'))
    Day = 86400
    secondDay = second / Day

    hour = 3600
    secondhour =  second / hour

    minute = 60
    secondminute = second / minute

    print(secondDay,'Day')
    print(secondhour,'Hour')
    print(secondminute,'minute')
    print(second)
Second()