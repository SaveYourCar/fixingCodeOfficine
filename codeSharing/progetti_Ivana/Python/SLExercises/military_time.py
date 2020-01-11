time_12h=input()

def time_24h(time_12h):

    if "AM" in time:
        time_24h=time_12h[:-3]
    elif "PM" in time_12h:
        hour= time_12h.split(":")[0]
        time_24h=time_12h[:-3].replace(hour,str(int(hour)+12), 1)
    else:
        return "Invalid input!"
    return time_24h

print(time_24h(time_12h))
