'''
writing a file
'''

file = open("student.txt", "w")
file = open("student1.txt", "w")

file.write("\nSourav - CSE")


file1 = open("student.html", "w")
file1.write("<h1>This is a html code</h1>")
file.close()
file1.close()
