import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))

findalllist= re.findall(pattern, "eggspamsausagespam")
print(len(findalllist))

for spam in re.finditer(pattern, "eggspamsausagespam"):
    print("1spam")

pattern = r"pam"

match = re.search(pattern, "eggspdfpamsaupamsage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())

str = "My name is David. Hi David."
pattern = r"name"
newstr = re.sub(pattern, "friend", str)
print(newstr)

pattern = r"gr.y"

if re.search(pattern, "ghgreyh"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "grbiy"):
   print("Match 3")


pattern = r"^gr.y$"

if re.search(pattern, "fggreyh"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")

#find if a letter in the brackets is in the pattern
pattern = r"letter [aeiou] ok$"

if re.search(pattern, "letter a ok"):
   print("Match 1")

if re.search(pattern, "letter u ok"):
   print("Match 2")

if re.search(pattern, "the letter a ok"):
   print("Match 3")

pattern = r"[A-Za-z][a-z][0-9]"

if re.search(pattern, "sc9"):
   print("Match 1")

if re.search(pattern, "Es3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

pattern = r"[A-Za-z]([aeiou])*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspameie"):
   print("Match 2")

if re.match(pattern, "zoo"):
   print("Match 3")

pattern = r"[A-Za-z]+"

if re.match(pattern, "1g"):
   print("Match 1")

if re.match(pattern, "ggggggggggggsdssfEgg2"):
   print("Match 2")

if re.match(pattern, "a@bc"):
   print("Match 3")


pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.group(2))
   print(match.groups())

#find if one or the other letter in parethesis is in the pattern
pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")

pattern = r"(.+)\1"

match = re.match(pattern, "w w")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")

match = re.match(pattern, "rg1, 23, r456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

pattern = r"\b(cat)( )*(dog)\b"

match = re.search(pattern, "The catdog sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat dog tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We sdog cattered.")
if match:
   print ("Match 3")

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.search(pattern, "We sdo2-.g@sfr2.com cattered prova@mail.com.")
if match:
   print (match.group())

match = re.findall(pattern, "We sdo2-.g@sfr2.com cattered prova@mail.com.")
if match:
   print (match)