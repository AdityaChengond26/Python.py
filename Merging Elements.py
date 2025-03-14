def merged_list(list1,list2):
   newlist=list(set(list1+list2))
   return newlist
list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
print(merged_list(list1,list2))
