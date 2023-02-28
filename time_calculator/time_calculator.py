import math

def calculate_day(day, dayLapse):
  days = [
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday"
  ]

  dayIndex = days.index(day.lower())
  newDayIndex = dayIndex + dayLapse
  newDayIndex = newDayIndex if newDayIndex <= 6 else math.floor(newDayIndex %
                                                                7)
  return days[newDayIndex].capitalize()

def add_time(start, duration, day=None):
  currentTime = start.split()

  hourTime = currentTime[0].split(':')
  meridiem = currentTime[1].lower()

  hour = int(hourTime[0])
  base24Hour = int(hourTime[0]) if meridiem == "am" else int(hourTime[0]) + 12
  minute = int(hourTime[1])


  addHourTime = duration.split(':')
  addHour = int(addHourTime[0])
  addMinute = int(addHourTime[1])

  totalMinute = minute + addMinute
  totalHour = hour + addHour

  minuteLapse = math.floor(totalMinute / 60)
  newMinute = totalMinute if totalMinute < 60 else totalMinute % 60
  newMinute = str(newMinute)
  newMinute = newMinute if len(newMinute) > 1 else "0" + newMinute

  totalHour += minuteLapse
  
  hourLapse = math.floor(totalHour / 12)
  newHour = totalHour if totalHour < 12 else totalHour % 12
  if (newHour == 0):
    newHour = 12
  newHour = str(newHour)

  if (hourLapse % 2 != 0):
    meridiem = "am" if meridiem == "pm" else "pm"

  meridiem = meridiem.upper()

  newTime = newHour + ":" + newMinute + " " + meridiem

  totalBase24Hour = base24Hour + addHour + minuteLapse
  dayLapse = math.floor(totalBase24Hour / 24)

  if (day is not None):
    newDay = calculate_day(day, dayLapse)
    newTime += ", " + newDay

  if (dayLapse == 1):
    newTime += " (next day)"
  elif (dayLapse > 1):
    newTime += " (" + str(dayLapse) + " days later)"

  return newTime
