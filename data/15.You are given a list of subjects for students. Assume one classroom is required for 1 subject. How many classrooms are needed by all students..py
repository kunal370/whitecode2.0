"""
15	You are given a list of subjects for students.
Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
"""


sub=["python","java","C++","python","javascript","java","python","java","C++","C"]
set1=set(sub)
print("classrooms are needed: ",len(set1))