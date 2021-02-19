subjects = ["C", "C++", "Java", "python", "BASIC"]
print(len(subjects))
subjects1 = [22, 11, 44, 33, 55, 77, 44, 44]

subjects.append("TOC")
print(subjects)

subjects.insert(2, "OS")
print(subjects)

subjects.remove("BASIC")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects2 = subjects.copy()
print(subjects2)

pos = subjects1.index(44)
print(pos)

pos = subjects1.count(44)
print(pos)