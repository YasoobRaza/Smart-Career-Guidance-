from experta import *
import pandas as pd
from tkinter import *
import os


df=pd.read_csv("departments1.csv",index_col=0,encoding="cp1252")


class CareerAdvisor(KnowledgeEngine):

    def __init__(self,departments):
        self.departs=departments        
        KnowledgeEngine.__init__(self)

    def increment(self,list):
        self.departs.loc[list,"points"]+=1

    def increment_except(self,list):
        exclude_mask=self.departs.index.isin(list)
        self.departs.loc[~exclude_mask, 'points'] += 1

    def eval_question(self,option):
        operations = {'inc': self.increment,
                      '~inc': self.increment_except}
                      
        if option[0] in operations:
            operations[option[0]](option[1])
        else:
            print("Invalid function")


    #code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        print("""
        This is a Smart Career Guidance Expert System

        Note:
        answer a series of questions to determine best suited career path for you

        """)
        yield Fact(action="find_career")

    # BASE QUESTION 1
    @Rule(Fact(action="find_career"),salience=4)
    def studybackground(self):
        print( """what is your intermediate background 
                    a)pre_engineering
                    b)pre_medical
                    c)commerce
                    d)computer science
                    
                    """)
        ans= input("ans => ")
        self.declare(Fact(Q1=ans))
        
        a = ("~inc",["BSDS","BSEG","BSEC","BSMG"])
        b = ("inc",["BEBM","BSIC","BSDS","BSEG","BSPH","BSMG"])
        c = ("inc",["BSEC","BSDS","BSCF","BSEG","BSMG"])
        d = ("inc",["BESE","BECS","BSCT","BSCF","BSIC","BSDS","BSEG","BSPH","BSMG"])
        self.eval_question(eval(ans))
        
        

    # PRE-ENGG 1
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg1(self):
        print("""Q. What are your current interests and hobbies?
                    a) Coding and programming
                    b) Building and fixing machines
                    c) Designing and creating things
                    d) Experimenting with different ingredients
                    e) none of these   """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BESE","BSCT","BECS"])
        b = ("inc",["BEME","BEIM","BEAU","BEEE"])
        c = ("inc",["BECE","BECN","BEUE","B.Arch","BETE"])
        d = ("inc",["BECH","BSPH","BEMY","BSIC","BEPP","BEMM"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-ENGG 2
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg2(self):
        print("""Q. Which of the following subjects do you enjoy the most?
                    a) Computer Science
                    b) Physics
                    c) Mathematics
                    d) Chemistry      
                    e) none of these  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BESE","BSCT","BECS"])
        b = ("inc",["BEME","BEIM","BEAU","BEEE","BEEL","BETC","BSPH","BETE","BEMM","BECE","BEUE","BECN"])
        c = ("inc",["BSCF","BSEC","BSCF"])
        d = ("inc",["BECH","BEMY","BSIC","BEPP","BETE","BEMM"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-ENGG 3
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg3(self):
        print("""What type of work environment do you see yourself in?
                    a) In front of a computer, writing code
                    b) In a lab, working with electronics
                    c) In an office, analyzing data
                    d) In a workshop, designing and building physical systems
                    e) at a construction site building infrastructure 
                    f) none of these  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BESE","BSCT","BECS"])
        b = ("inc",["BEEE","BETC","BECS","BEEL"])
        c = ("inc",["BSCF","BSEC","BSEG"])
        d = ("inc",["BEME","BEAU","BEIM","BEMY","BETE"])
        e = ("inc",["BECE","BEUE","BECN","B.Arch"])
        f = ("inc",[])
        self.eval_question(eval(ans))
    
    # PRE-ENGG 4
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg4(self):
        print("""2) Which of the following best describes your experience and skills?
                    a) Proficient in programming languages such as Java, C++, and Python
                    b) Experienced in circuit design and electronic systems
                    c) Knowledgeable in the principles of thermodynamics and heat transfer
                    d) Skilled in statistical analysis and data visualization
                    e) none of these   """)
        ans = input("ans=> ").lower()

        a = ("inc",["BESE","BSCT","BECS"])
        b = ("inc",["BEEE","BETC","BECS","BEEL"])
        c = ("inc",["BEME","BEAU","BEIM","BEMY","BETE"])
        d = ("inc",["BSCF","BSEC"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-ENGG 5
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg5(self):
        print("""1) Which of the following best describes your career goals?
                    a) Developing new materials and products 
                    b) Improving and optimizing manufacturing processes
                    c) Designing and building transportation systems
                    d) Analyzing and interpreting data to make policy recommendations
                    e) none of these  """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BECH","BEMY","BSIC","BETE"])
        b = ("inc",["BEME","BEAU","BEIM","BEMY"])
        c = ("inc",["BECE","BEUE","BECN","B.Arch"])
        d = ("inc",["BSCF","BSEC","BSDS","BSMG"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-ENGG 6
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg6(self):
        print("""1) Which of the following would you prefer more?
                    a) designing new inovative infrastructure designs  
                    b) inspection and supervising constuctions
                    c) Designing road maps and urban infrastucture
                    d) none of these """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BECE","B.Arch"])
        b = ("inc",["BECE","BECN"])
        c = ("inc",["BECE","BEUE"])
        d = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-ENGG 7
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=3)
    def pre_engg7(self):
        print("""Q. which of these capture your interest more ?
                    a) Designing and developing vehicles
                    b) Designing and developing mechanical systems
                    c) Optimizing industrial processes
                    d) none of these """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BEAU"])
        b = ("inc",["BEME"])
        c = ("inc",["BEIM"])
        d = ("inc",[])
        self.eval_question(eval(ans))
    
    # PRE-ENGG 8
    @Rule(AND(Fact(action="find_career"),Fact(Q1="a")),salience=2)
    def pre_engg8(self):
        print("""if you are given a chance to work on any one one these projects.What would it be ?
                    a) developing fabrics that could conduct electricty like metals 
                    b) developing an AI tool to make images from textual descriptions
                    c) building a fully functional formula-1 racing car
                    d) designing and modeling of a detachable buildings
                    e) building drones that can communicate and syncronize with eachother
                    f) none of these  """)
        ans = input("ans=> ").lower()
        self.declare(Fact("end"))

        a = ("inc",["BECH","BEMY","BSIC","BEPP","BETE","BEMM","BSPH"])
        b = ("inc",["BESE","BSCT","BECS"])
        c = ("inc",["BEME","BEAU","BEIM","BEMY"])
        d = ("inc",["BECE","BEUE","BECN","B.Arch"])
        e = ("inc",["BEEE","BECS","BEEL","BETC"])
        f = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-MED 1
    @Rule(AND(Fact(action="find_career"),Fact(Q1="b")),salience=3)
    def pre_med1(self):
        print("""Which of the following subjects do you enjoy the most?
                    a) Biology
                    b) Economics
                    c) Physics
                    d) Linguistics
                    e) Chemisrty  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BEBM"])
        b = ("inc",["BSEC","BSDS","BSMG"])
        c = ("inc",["BSPH"])
        d = ("inc",["BSEG"])
        e = ("inc",["BSIC"])
        self.eval_question(eval(ans))

    # PRE-MED 2
    @Rule(AND(Fact(action="find_career"),Fact(Q1="b")),salience=3)
    def pre_med2(self):
        print("""Q.if given an opportunity where would you prefer to work?
                    a) work as an English teacher at school 
                    b) work as an Financial Analyst in bank
                    c) work in an organizations as project manager
                    d) work in labortary performing experiments 
                    e) none of these   """)
        ans = input("ans=> ").lower()

        a = ("inc",["BSEG"])
        b = ("inc",["BSEC"])
        c = ("inc",["BSMG","BSDS"])
        d = ("inc",["BSIC","BSPH"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # PRE-MED 3
    @Rule(AND(Fact(action="find_career"),Fact(Q1="b")),salience=3)
    def pre_med3(self):
        print("""Which of the following topics do you find most fascinating?
                    a) Understanding and applications of chemical reactions in industry 
                    b) Applications of physics in engineering and technology
                    c) Global development and sustainable development 
                    d) Strategic management and organizational behavior
                    e) Analyzing data to understand economic trends  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BSIC"])
        b = ("inc",["BSPH"])
        c = ("inc",["BSDS"])
        d = ("inc",["BSMG"])
        e = ("inc",["BSEC"])
        self.eval_question(eval(ans))

    # PRE-MED 4
    @Rule(AND(Fact(action="find_career"),Fact(Q1="b")),salience=2)
    def pre_med4(self):
        print("""What type of problems do you want to solve?
                    a) Business and organizational issues
                    b) health and medical issues 
                    c) Social and economic issues
                    d) Environmental and sustainability issues  
                    e) none of these """)
        ans = input("ans=> ").lower()
        self.declare(Fact("end"))

        a = ("inc",["BSMG","BSDS"])
        b = ("inc",["BEBM",])
        c = ("inc",["BSMG","BSEC"])
        d = ("inc",["BSIC","BSPH"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # COMMERCE 1 
    @Rule(AND(Fact(action="find_career"),Fact(Q1="c")),salience=3)
    def commerce1(self):
        print("""Which of the following best describes your career goals?
                    a) Developing and implementing mathematical models for financial markets
                    b) Conducting research on economic policy and forecasting
                    c) Teaching or researching in the field of linguistics
                    d) Working in international development organizations
                    e) Advising or managing in the business sector""")
        ans = input("ans=> ").lower()

        a = ("inc",["BSCF"])
        b = ("inc",["BSEC"])
        c = ("inc",["BSEG"])
        d = ("inc",["BSDS"])
        e = ("inc",["BSMG"])
        self.eval_question(eval(ans))

    # COMMERCE 2 
    @Rule(AND(Fact(action="find_career"),Fact(Q1="c")),salience=3)
    def commerce2(self):
        print("""Which of the following do you enjoy reading about?
                    a) Advanced mathematical concepts related to finance
                    b) Economic trends and news
                    c) The history and structure of the English language
                    d) Global issues such as poverty, inequality, and sustainable development
                    e) Business strategies and case studies  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BSCF"])
        b = ("inc",["BSEC"])
        c = ("inc",["BSEG"])
        d = ("inc",["BSDS"])
        e = ("inc",["BSMG"])
        self.eval_question(eval(ans))

    # COMMERCE 3
    @Rule(AND(Fact(action="find_career"),Fact(Q1="c")),salience=3)
    def commerce3(self):
        print("""Which of the following do you find most appealing?
                    a) Using data and technology to understand financial markets
                    b) Analyzing data to understand economic trends
                    c) Understanding the intricacies of language and communication
                    d) Examining ways to create a more just and equitable world
                    e) Strategic management and organizational behavior.  """)
        ans = input("ans=> ").lower()

        a = ("inc",["BSCF"])
        b = ("inc",["BSEC"])
        c = ("inc",["BSEG"])
        d = ("inc",["BSDS"])
        e = ("inc",["BSMG"])
        self.eval_question(eval(ans))

    # COMMERCE 4
    @Rule(AND(Fact(action="find_career"),Fact(Q1="c")),salience=2)
    def commerce4(self):
        print("""Which of the following best describes your area of interest?
                    a) Understanding and modeling financial markets and their risks
                    b) Analyzing and interpreting economic data
                    c) Studying the structure and use of the English language
                    d) Examining issues related to global development and poverty
                    e) Examining issues related to business and management""")
        ans = input("ans=> ").lower()
        self.declare(Fact("end"))

        a = ("inc",["BSCF"])
        b = ("inc",["BSEC"])
        c = ("inc",["BSEG"])
        d = ("inc",["BSDS"])
        e = ("inc",["BSMG"])
        self.eval_question(eval(ans))

    # COMPUTER 1
    @Rule(AND(Fact(action="find_career"),Fact(Q1="d")),salience=3)
    def comp1(self):
        print("""Q. What are your current interests and hobbies?
                    a) Coding and programming
                    b) reading books and literature
                    c) Designing and making circuits
                    d) Experimenting with different materials
                    e) none of these   """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BESE","BSCT","BECS"])
        b = ("inc",["BSEG"])
        c = ("inc",["BEEL","BECS","BETC"])
        d = ("inc",["BSPH"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # COMPUTER 2
    @Rule(AND(Fact(action="find_career"),Fact(Q1="d")),salience=3)
    def comp2(self):
        print("""Which type of projects do you prefer more?
                    a) Web development
                    b) embedded systems development
                    c) software development
                    d) networks development
                    e) none of these  """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BESE","BSCT"])
        b = ("inc",["BEEL","BECS",])
        c = ("inc",["BESE","BSCT","BECS"])
        d = ("inc",["BECS","BETC"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # COMPUTER 3
    @Rule(AND(Fact(action="find_career"),Fact(Q1="d")),salience=3)
    def comp3(self):
        print(""" If given a topic for Research which topic would you most likely pick? 
                    a) Cloud computing 
                    b) Augmented reality 
                    c) Internet of things 
                    d) Block chain
                    e) none of these  """)
        ans = input("ans=> ").lower()
        self.declare(Fact("end"))
        
        a = ("inc",["BESE","BSCT"])
        b = ("inc",["BEEL","BECS",])
        c = ("inc",["BEEL","BETC","BECS"])
        d = ("inc",["BECS","BETC"])
        e = ("inc",[])
        self.eval_question(eval(ans))

    # COMPUTER 4
    @Rule(AND(Fact(action="find_career"),OR(Fact(Q1="d"),Fact(Q1="a"))),salience=3)
    def comp4(self):
        print("""what type of topics you enjoy studying? 
                    a) computer architecture
                    b) computer communications
                    c) software development cycle
                    d) probability and statistics
                    e) none of these  """)
        ans = input("ans=> ").lower()
        
        a = ("inc",["BECS","BEEL"])
        b = ("inc",["BETC","BSCT","BECS"])
        c = ("inc",["BESE","BSCT"])
        d = ("inc",["BSCF"])
        e = ("inc",[])
        self.eval_question(eval(ans))


    # FINAL QUESTION
    @Rule(Fact("end"),salience=1)
    def eval_result(self):
        grade = int(input("Enter your percentage => "))
        test_score = int(input("Enter your test score => "))
        merit = (grade*0.5)+(test_score*0.5)
        result = self.departs[self.departs["merits"]<=merit]
        result=result.sort_values(["points","merits"],ascending=[False,False])
        

        print("")
        print("best suited field of study for you will be:",result["name"].iloc[0])
        print("")
        print("________________________________________Field Description_____________________________________")
        print(result["info"].iloc[0])
        print("")
        print("")
        print(result)        
        
engine = CareerAdvisor(df)
engine.reset()
engine.run()
        

