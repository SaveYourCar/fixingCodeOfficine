import re

def alarm(casino_layout):
    secure = re.search(r"(\$|T)([xG])*(G+)([xG])*(T|\$)", casino_layout)
    if not secure:
        return "ALARM"
    else:
        return "quiet"

print(alarm(input()))