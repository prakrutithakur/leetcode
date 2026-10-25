# obj={

# }
# all_keys=obj.keys()
# print(all_keys)
# obj={
#     "obj_1": "hello",
#     "obj_2": "hello"
# }
# all_keys=obj.keys()
# print(len(all_keys))


from collections import defaultdict

possible_counts = defaultdict(list)
possible_counts={
    1:[1,2],
    2:[3,5]
}

possible_counts[4]=[3,4]
list1=[]
list1.extend(possible_counts[4])
list1.extend(possible_counts[1])
print(list1)
