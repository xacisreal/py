
dic1={'apple':1,'banana':2,'cherry':3}
sort_as=dict(sorted(dic1.items(),))
print("Ascending order: ", sort_as)
sort_des=dict(sorted(dic1.items(),reverse=True))
print("Descending order: ",sort_des)
dic2={'date':4,'eagle':5}
merge={**dic1,**dic2}
print("Merged dic: ",merge)