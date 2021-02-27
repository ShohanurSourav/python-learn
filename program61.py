# character class

import re
pattern1 = r"[aeiou]"
if re.match(pattern1, "ecoli"):
    print("Matched!")
else:
    print("Not matched")

pattern2 = r"[A-Z][a-z][0-9]"
if re.match(pattern2, "Aa1ecolour"):
    print("Matched!")
else:
    print("Not matched")
