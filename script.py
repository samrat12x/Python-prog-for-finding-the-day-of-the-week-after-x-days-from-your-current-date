'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

         
print('\t\t\t read carefully')
print ('Hello user, if you tell this program , what day is today . ')
print('then this prog will tell you what day will be , x days later \n')
curr_day=input('what day is today?\n')
curr_day=curr_day.lower()


day_gap=int(input('enter x\n'))
remainder=day_gap%7
projected_day='nan'


class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None
   
   
   def listprint(self) :
     global remainder  #so that i can use this var inside this class func
     global projected_day
     printval = self.headval
      
      
        
        #goal of this  while loop is too make printval stop at node whose dataval is equals to curr day
     while printval.dataval != curr_day:
          #print(printval.dataval)
          printval = printval.nextval
          
     #print('value of printval after inner while gets executed',printval.dataval)
        #goal of this while loop is make 'remainder' jumps from the curr_day
     while remainder !=0:
         printval = printval.nextval
         remainder=remainder-1 
        
          
     #print('value of printval after outer while gets executed',printval.dataval)
     projected_day=printval.dataval
         
list1 = SLinkedList()
list1.headval = Node('monday')
e2 = Node('tuesday')
e3 = Node("wednesday")
e4 = Node('thursday')
e5 = Node('friday')
e6= Node('saturday')
e7= Node('sunday')
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=list1.headval
#over all created a circular list
list1.listprint()
print('\n\nafter',day_gap,'days ,it will be',projected_day)
