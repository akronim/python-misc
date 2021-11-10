course = "Python for Beginners"
print(len(course))      # 20

print(course.upper())   # PYTHON FOR BEGINNERS

print(course.lower())   # python for beginners

print(course.find('P'))     # 0 >>> index of P (case sensitive)
print(course.find('Beginners'))     # 11 >>> index of B

print(course.index("B"))    # 11

print(course.replace('Beginners', 'Absolute Beginners'))    # Python for Absolute Beginners

print('Python' in course)       # true
print('python' in course)       # false

print(course[11].isupper())     # True
