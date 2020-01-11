import math

def time_for_license(name,agents,others):
    others_list = others.split(" ")
    if len(others_list) > 4 or len(others_list) < 4:
        return "The others costumers are 4"
    wating_list = others_list + [name]
    wating_list.sort(key=str.lower)
    print(wating_list)
    turns = math.ceil(5 / int(agents))
    print(turns)
    name_place = math.ceil((wating_list.index(name)+1)/int(agents))
    print(name_place)
    wating_time = 20 * name_place
    return wating_time


print("Insert a name, a number of agents, the names of the 4 costumers separeted by a space")
print(time_for_license(input(),input(),input()))