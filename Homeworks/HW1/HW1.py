#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create odd and even lists
odd_list = [1,3,5,7,9,11,13,15,17]
even_list = [0,2,4,6,8,10,12,14,16]

#merge two lists
merge_list = even_list + odd_list

#multiple by 2 all values in merge list using list comprehension
multiple_list = [x * 2 for x in merge_list]

#use loop to print data type of all values
for i in range (len(multiple_list)):
    print(multiple_list[i], type(multiple_list[i]))


# In[ ]:




