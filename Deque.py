''''
    Assignment 2
    Leslie N. Kodjoe
'''
import random
class Deque:

    MaxArraySize =20
    def __init__(self):
        self.items=[0]*Deque.MaxArraySize
        self.size=0
        self.front=-1
        self.rear=-1


    def isFull(self):

        if (self.front == 0 and self.rear ==len(self.items)-1) or (self.front == self.rear+1):
           return True

        else:
            return False

    def isEmpty(self):
        if (self.front==-1 and self.rear == -1):
            return True

        else:
            return False
            

    def Insertfront(self,data):

        if(self.isFull()):
            print("The Array is maxed out")
            print("Cannot insert %d"%data)
        else:
            if(self.isEmpty()):
                self.front = 0
                self.rear = 0
            elif(self.front == 0):
                self.front = len(self.items)-1
            else:
                self.front-=1
        self.items[self.front]=data

    def Insertrear(self,data):
        if(self.isFull()):
            print("The Array is maxed out")
            print("Cannot insert %d"%data)
        else:
            if(self.isEmpty()):
                self.front =0
                self.rear=0
            elif(self.rear==len(self.items)-1):
                self.rear=0
            else:
                self.rear+=1
        self.items[self.rear]=data

    
    def Removefront(self):
        if(self.isEmpty()):
            print("The Array is Empty")
        else:
            if(self.front==self.rear): #When there is only one element
                self.front=-1
                self.rear=-1
            elif(self.front==len(self.items)-1):
                self.front=0
            else:
                self.front+=1
        self.getFront()
        self.display()
        

    def Removerear(self):
        if(self.isEmpty()):
            print("The Array is Empty")
        else:
            if(self.front==self.rear):
                self.front=-1
                self.rear=-1
            elif(self.rear ==0):
                self.rear=len(self.items)-1
            else:
                self.rear-=1
        self.getRear()
        self.display()

    def display(self):
        i = self.front
        print("Current Size:")
        while(i!=self.rear):
            print("%d" %self.items[i],end=",")
            i=(i+1)%len(self.items)
        print("%d" %self.items[self.rear])

    def getFront(self):
        print("The Current Front element is: %d " %self.items[self.front])

    def getRear(self):
        print("The Current Rear element is: %d " %self.items[self.rear])

##    def Simulation(self):
##        prob = random.random()
##        if(prob <=0.1):
##            for i in range(0,10):
##                data = random.randint(1,100)
##                self.Insertfront(data)
##            self.display()
####        if(prob<=0.2):
####            self.Removefront()
####        if(prob<=0.1):
####            for i in range(0,100):
####                data=random.randint(1,100)
####                self.Insertrear(data)
####        if(prob<=0.6):
####            self.Removerear()
####        
##        else:
##            print("Error")
##        self.display()
        

Deck = Deque()
Deck.Insertfront(2)
Deck.Insertfront(3)
Deck.display()
Deck.getFront()
Deck.Removefront()
            
        


        
