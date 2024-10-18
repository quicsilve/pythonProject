calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = [len(stroka), stroka.upper(), stroka.lower()]
    count_calls()
    return result

def is_contains(string, list_to_search):
    stroka = str(string)
    spisok = list(list_to_search)
    baboling = bool
    for i in spisok:
        if i.lower() == stroka.lower():
            baboling = True
            break
        else:
            baboling = False
            continue
    count_calls()
    return baboling

print(string_info("Gigachat"))
print(string_info("Bimbambambum"))

print(is_contains("Cocodjambo", ["cocodJamBo", "Hola", "Chickchik"]))
print(is_contains("Love", ["JamBo", "Hola", "Chickchik"]))

print(calls)