a = "i like python and i like ai"

b = a.split()

result = {}

for ch in b:
    if ch not in result :
        result[ch] = 1
    else :
        result[ch] += 1 
print(result)           

