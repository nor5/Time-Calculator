#def add_time(start, duration, day = "Monday"):
start = "3:30 AM"
duration = "10:00"
# Returns: 6:10 PM
startTime = start.split()[0]
clockSystem = start.split()[1]
startHour = startTime.split(":")[0]
startMinut = startTime.split(":")[1]
durationHour = duration.split(":")[0]
durationMinut = duration.split(":")[1]
print(f"startTime :{startTime}, clockSystem :{clockSystem }, startHour :{startHour},startMinut:{startMinut}")
print(f"durationHour: {durationHour}, durationMinut :{durationMinut}")
resultHour = int(startHour) + int(durationHour)
resultMinut = int(startMinut) + int(durationMinut)
if  resultMinut >=60:
  resultHour = resultHour+ (resultMinut // 60)
  resultMinut = resultMinut - ((resultMinut // 60)*60)

if  resultHour >12:
     resultHour =  resultHour - 12
     if  clockSystem == "PM":
         clockSystem = "AM"
     else:
         clockSystem = "PM"
print(resultHour,resultMinut, clockSystem)        
     


##resultClockSystem
##resultDay  

##regexp = "(\d{1,4})([-\+])(\d{1,4}$)"
##match = re.match(regexp, p)
    


       #  return new_time
