f = open("C:/doit/new_file.txt", 'a')
for i in range(11, 20):
    data = "This is line %d.\n" %i
    f.write(data)
f.close()