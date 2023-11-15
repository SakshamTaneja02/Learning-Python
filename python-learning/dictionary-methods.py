info = {"name":"Luffy", "age":19, "work":"pirate"}
info.update({"age":20})
info.update({"work":"pirate_king"})
info.update({"food":"meat","vice-captain":"Zoro"})
print(info)

ep2 = {1:23,2:23}
# del ep2 
ep2.clear()
print(ep2)

info.pop("vice-captain")
print(info)

info.popitem()
print(info)
