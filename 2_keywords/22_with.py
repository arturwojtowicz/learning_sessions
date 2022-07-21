# with
print("----------- with -----------")
with open("c:\\Users\\arwojtow\\Documents\\PythonBootCampInternal\\1\\2_keywords\\2_true_false.py", 'r') as f:
    print(f.read())

print("Without Context Manager")
x = open("c:\\Users\\arwojtow\\Documents\\PythonBootCampInternal\\1\\2_keywords\\2_true_false.py", 'r')
y = x.read()
x.close()
print(y)
