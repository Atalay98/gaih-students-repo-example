#!/usr/bin/env python
# coding: utf-8

# In[34]:


#create function for getting grade from user
def getGrade(student, exam):
    grade = input("Enter {}'s {} grade: ".format(student,exam))
    result = 0
    try:
        result = float(grade)
    except ValueError:
        print("Enter a grade with numerical")
        return -1
    
    if(result>100):
        print("Grade can not greater than 100")
        return -1
    elif(result<0):
        print("Grade can not smaller than 0")
        return -1
    else:
        return result

#create dictionary for keep students name as key, students grades as value
grades = {}

for i in range(5):
    student = input("Enter {}. student's name: ".format(i+1))
    check = False
    mid = 0
    project = 0
    final = 0
    #check value controls that the user has entered a correct grade
    #if user doesn't enter appropriate grade, program will ask again
    while check == False:
        mid = getGrade(student, "midterm")
        if mid != -1:
            check = True
    
    check = False
    while check == False:
        project = getGrade(student, "project")
        if project != -1:
            check = True
            
    check = False
    while check == False:
        final = getGrade(student, "final")
        if final != -1:
            check = True
        
    passingGrade = (mid * 0.3) + (project * 0.3) + (final * 0.4)
    grades[student] = [mid, project, final, passingGrade]


# In[35]:


#declare final grades list
finalGrades = []

#add students final grade to a list from dictionary
for k,v in grades.items():
    finalGrades.append(v[-1])

# In[36]:


#sort the grades lowest to highest
finalGrades.sort()


# In[37]:


#then reverse the list and we get the grades highest to lowest
finalGrades.reverse()
print(finalGrades)

