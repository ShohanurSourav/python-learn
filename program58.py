# regular expression

import re
pattern = r"Green"
if re.match(pattern, "Green is a color, I love green color"):
    print("Match")
else:
    print("Not Matched!")

pattern1 = r"color"
if re.search(pattern1, "Green is a color, I love green color"):
    print("Found")
else:
    print("Not Found!")

pattern2 = r"color"
print(re.findall(pattern2, "Green is a color, I love green color"))

pattern3 = r"is"
text = "My favourite color is Green."
match = re.search(pattern3, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
