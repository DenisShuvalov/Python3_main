duration = int(input("введите количество секунд "))

days = duration // 86400
days_left = duration % 86400
hours = days_left // 3600
hours_left = days_left % 3600
minutes = hours_left // 60
minutes_left = hours_left % 60
seconds = minutes_left

print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
# //-челоч
# print(duration)
# print(days)
# print(days_left)
# print(hours)
# print(hours_left)
# print(minutes)
# print(minutes_left)
# print(seconds)
