#!/usr/bin/env python
# coding: utf-8

# In[47]:


#create 5 people cv using dictionaries
cv_1 = {"CV" : ["Ali", "Duman", "23", "01.05.1997","0541234567","Ankara", "Python"]}
cv_2 = {"CV" : ["Veli", "Ay", "25", "22.12.1995","05057654321","Hatay", "Java"]}
cv_3 = {"CV" : ["Osman", "Kara", "30", "16.04.1990","05041291275","Adana", "C"]}
cv_4 = {"CV" : ["Merve", "Beyaz", "20", "19.08.2001","05041232091","Konya", "Javascript"]}
cv_5 = {"CV" : ["Zeynep", "Yildiz", "24", "02.09.1996","05041238625","Izmir", "PHP"]}


# In[49]:


#print cv of 5 people
print("CV\tName\tSurname\tAge\tBirthday\tPhone\t\tCity\tProgramming Language")
print("1\t", '\t'.join([str(i) for i in cv_1["CV"]]))
print("2\t", '\t'.join([str(i) for i in cv_2["CV"]]))
print("3\t", '\t'.join([str(i) for i in cv_3["CV"]]))
print("4\t", '\t'.join([str(i) for i in cv_4["CV"]]))
print("5\t", '\t'.join([str(i) for i in cv_5["CV"]]))

