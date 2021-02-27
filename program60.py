# meta characters

import re
# . er jaygay jekono kicu hote pare
pattern1 = r"colo.r"
if re.match(pattern1, "colour"):
    print("Matched!")
else:
    print("Not matched")

# ^ means start obossoi colo diye hote hbe and last e r thaka lagbe
pattern2 = r"^colo..r$"
if re.match(pattern2, "colouur"):
    print("Matched!")
else:
    print("Not matched")

# * means 0 or more a thakte pare
pattern3 = r"a*"
if re.match(pattern3, "colouur"):
    print("Matched!")
else:
    print("Not matched")

# + means 1 or more a thakte pare surute
pattern4 = r"a+"
if re.match(pattern4, "colouuraaa"):
    print("Matched!")
else:
    print("Not matched")

# ? means 0 or 1 bar hote pare
pattern5 = r"ice(-)?cream"
if re.match(pattern5, "icecream"):
    print("Matched!")
else:
    print("Not matched")

# {limit start,limit end}
pattern6 = r"a{1,3}$"
if re.match(pattern6, "aaa"):
    print("Matched!")
else:
    print("Not matched")
