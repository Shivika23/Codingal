def test(l):
    result = {}
    for item in l:
        result[item[0]] = item[1:]
    return result

students = [[1,"Shivika","8"],[2,"Rose","9"],[3,"Harry","8"],[4,"Hermoine","8"],[5,"Ron","8"]]
print("Original List: ",students)

print(test(students))
