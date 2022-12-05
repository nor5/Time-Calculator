def add_time(start, duration, day = "Monday"):

    numberDay = 0

   
    startTime = start.split()[0]
    clockSystem = start.split()[1]
    startHour = startTime.split(":")[0]
    startMinut = startTime.split(":")[1]
    durationHour = duration.split(":")[0]
    durationMinut = duration.split(":")[1]
##    print(f"startTime :{startTime}, clockSystem :{clockSystem }, startHour :{startHour},startMinut:{startMinut}")
##    print(f"durationHour: {durationHour}, durationMinut :{durationMinut}")

    if int(durationHour) >= 24:
        numberDay =  int(durationHour)  // 24
        durationHour = int(durationHour)  - (( int(durationHour)  // 24) * 24)
##        print(durationHour)
        resultHour = durationHour + int( startHour )
##        print(resultHour, numberDay, durationHour) 

    resultHour = int(startHour) + int(durationHour)
    resultMinut = int(startMinut) + int(durationMinut)
    if  resultMinut >=60:
      resultHour = resultHour+ (resultMinut // 60)
      resultMinut = resultMinut - ((resultMinut // 60)*60)

        
    if  resultHour >= 12 and resultHour < 24:
         resultHour =  resultHour - 12
         if  resultHour == 0:
             resultHour = 12
         if  clockSystem == "PM":
             clockSystem = "AM"
             numberDay  = numberDay  +1
         else:
             clockSystem = "PM"
##    print(resultHour,resultMinut, clockSystem , numberDay)        
         
    new_time = str(resultHour) +" :    "+ str(resultMinut )+"  "+ str(clockSystem) +"   "+ str(numberDay) + "days"
    print(new_time)

        


    return new_time

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
