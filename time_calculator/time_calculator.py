import math

def time_in_str(timeInt):
  timeStr = str(timeInt)
  timeStr = timeStr if len(timeStr) > 1 else "0" + timeStr
  return timeStr


def calculate_day(day, dayLapse):
  days = [
    "sunday", "monday", "tuesday", "wednesday", "thurday", "friday", "saturday"
  ]

  dayIndex = days.index(day.lower())
  newDayIndex = dayIndex + dayLapse
  newDayIndex = newDayIndex if newDayIndex <= 6 else newDayIndex - 6

  return days[newDayIndex].capitalize()


def add_time(start, duration, day=None):
  currentTime = start.split()

  hourTime = currentTime[0].split(':')
  meridiem = currentTime[1].lower()

  hour = int(hourTime[0])
  minute = int(hourTime[1])

  addHourTime = duration.split(':')
  addHour = int(addHourTime[0])
  addMinute = int(addHourTime[1])

  totalMinute = minute + addMinute
  totalHour = hour + addHour

  minuteLapse = math.floor(totalMinute / 60)
  newMinute = totalMinute if totalMinute < 60 else totalMinute - 60
  newMinute = time_in_str(newMinute)

  totalHour += minuteLapse
  hourLapse = math.floor(totalHour / 12)
  newHour = totalHour if totalHour < 12 else totalHour - 12
  newHour = time_in_str(newHour)

  if (hourLapse % 2 != 0):
    meridiem = "am" if meridiem == "pm" else "pm"

  meridiem = meridiem.upper()

  newTime = newHour + ":" + newMinute + " " + meridiem

  dayLapse = math.floor(totalHour / 24)

  if (day is not None):
    newDay = calculate_day(day, dayLapse)
    newTime += " " + newDay

  if (dayLapse == 1):
    newTime += " (next day)"
  elif (dayLapse > 1):
    newTime += " (" + dayLapse + " days later)"

  return newTime
