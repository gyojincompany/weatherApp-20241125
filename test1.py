weatherText = "맑음(낮) 체감온도 9°"

list1 = weatherText.split(" ")

print(list1)

weatherText2 = ""
for char in weatherText:
    if char == "(":
        break
    weatherText2 = weatherText2+char

print(weatherText2)






