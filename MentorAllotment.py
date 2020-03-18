# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:55:24 2020

@author: Gokul Balachandran
"""


class person:
    def __init__(self):
        self.top=1
        self.SUB_STACK=[]
   
    def addStacks(self):
        self.SUBJECT=input("Enter the name of the course : ")
        self.SUB_STACK.append(self.SUBJECT)
        self.top=self.top+1
    
    def setMentorOrLearner(self):
        self.ROLE=input("Enter the role(mentor : M | learner : L) : ")
    
    def setAvailableTime(self):
        self.start_time=int(input("Start time (24 hr format [:00]) : "))
        self.end_time=int(input("End time (24 hr format [:00] ):  "))
    
    def getMentor(self,stime,etime,sub):
        if sub in self.SUB_STACK:
            if stime <= self.start_time and etime >= self.end_time :
                return 1
        else :
            return 0    
    def display(self,sub):
        print("SUB  : " + sub)
        print("time : ",self.start_time,":00 - ", self.end_time,":00")
            
        
        

P=person()
for i in range(0,5):
    P.addStacks()

P.setMentorOrLearner()
P.setAvailableTime()
#print(P.getMentor(11,2,'ML'))
if P.getMentor(11,14,"ML") == 1:
    P.display("ML")
else :
    print("Mentor not available at the specified duration !!")
