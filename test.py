import easygui

file = open(easygui.fileopenbox(),'w+')
file.write(str(input()))
data = file.read()
file.close()

print(data)	