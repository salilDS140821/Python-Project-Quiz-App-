#!/usr/bin/env python
# coding: utf-8

# In[10]:


nameslist=[]
listofemail=[]
users_list=[nameslist,listofemail]

class TestTaker:
    def __init__(self):
        pass
        
    def register(self):
        name=self.name()
        mail_ID=self.email()
        
    
    def name(self):
        name=input("Enter name:")
        self.name=name
        nameslist.append(name)
           
    def email(self):
        email_id= input("Enter the mail address")
        
        import re
        if(re.search("^[a-Z]+[0-9]+.*@gmail.com$",email_id)):
            listofemail.append(email_id)
            self.email=email_id
        else:
            print("emailID must start with an alphabet, then it should have one or more digit and should have a domain @gamil.com")

from questionbank import Question

question_prompts = ["What is the capital of Odisha?\na. Cuttack\nb. Balesore\nc. Bhubaneshwar\nd. Berhampur\n\n",
                    "Who is the Chief Minister of Odisha?\na. Biju Patnaik\nb. Pradeep Maharana\nc. R.K Sighdeo\nd. Naveen Patnaik\n\n",
                    "In which city of Odisha, SAIL plant is situated?\na. Rourkela\nb. Anugul\nc. Dhenkanal\nd. Jagatsinghpur\n\n",
                    "Which instrument measure and records the relative humidity of air?\na. Hydrometer\nb. Hygrometer\nc. Lactometer\nd. Barometer\n\n",
                    "What is the shape of or milkyway?\na. Elliptical\nb. Spiral\nc. Circular\nd. None of the above\n\n",
                    "What is the fundamental scientific priciple in te operation of battery?\na. Acid-Base interaction\nb. Dialysis\nc. Dissociation of electrolytes\nd. Oxidation-Reduction\n\n"]
questions = [
        Question(question_prompts[0], 'c'),
        Question(question_prompts[1], 'd'),
        Question(question_prompts[2], 'a'),
        Question(question_prompts[3], 'b'),
        Question(question_prompts[4], 'a'),
        Question(question_prompts[5], 'c')
        ]

def run_quiz(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=10
    print("Your score is "+ str(score)+"/"+str(len(questions)*10)+"correct")
    
    for question in questions:
                print("The correct answers are "+ question.answer)
            
            
run_quiz(questions)


# In[ ]:




