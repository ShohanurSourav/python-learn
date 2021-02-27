# search & replace

import re
pattern = r"color"
text1 = "My favourite color is Green, I love Blue color  as well"
text2 = re.sub(pattern, "colour", text1)
# text2 = re.sub(pattern, "colour", text1, count=2)
print(text2)
