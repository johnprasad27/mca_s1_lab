dict1={"banana":6,"mango":1,"apple":2}
sorted_dict=dict(sorted(dict1.items()))
print("ascending",sorted_dict)
sorted_dict=dict(sorted(dict1.items(),reverse=True))
print("descending",sorted_dict)