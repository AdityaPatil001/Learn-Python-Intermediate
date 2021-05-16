list_org = ["banana", "cherry", "apple"]

list_copy = list_org

list_copy.append(True)
print(list_copy)
print(list_org)

list_org = ["banana", "cherry", "apple"]

list_copy = list_org.copy()

list_copy.append(True)
print(list_copy)
print(list_org)