''''
    Assignment 2
    Leslie N. Kodjoe
'''
import random
class Deque:

    MaxArraySize =20  # default array size
    def __init__(self):
        self.items=[0]*Deque.MaxArraySize
        self.size=0
        self.front=-1  #front of the array
        self.rear=-1   #back of the arrray


#Funtion to check if the array is full
    def isFull(self):
        #Instances for when there is no more space in the array
        if (self.front == 0 and self.rear ==len(self.items)-1) or (self.front == self.rear+1):
           return True

        else:
        #returns false when there is space
            return False

#Function to check if the array is empty
    def isEmpty(self):
        #when they all still point to their intial initialization returns the empty array
        if (self.front==-1 and self.rear == -1):
            return True

        else:
            return False
            

    def Insertfront(self,data):
        if(self.isFull()): #Calls the function
            print("The Array is maxed out")
            print("Cannot insert %d"%data)
        else:
            if(self.isEmpty()):
                self.front = 0 #Points to the first index
                self.rear = 0
            elif(self.front == 0):
                self.front = len(self.items)-1 #When inputting, next index will begin from the end of the array
            else:
                self.front-=1 #Subtracts from the index
        self.items[self.front]=data #Assigns the data into the array


    def Insertrear(self,data):
        if(self.isFull()):
            print("The Array is maxed out")
            print("Cannot insert %d"%data)
        else:
            if(self.isEmpty()): #Calls the function
                self.front =0 #Points to the first index
                self.rear=0
            elif(self.rear==len(self.items)-1): #Starts inputting from the last index of the array
                self.rear=0
            else:
                self.rear+=1 #Adds 1 to index
        self.items[self.rear]=data #Assigns the data into the array

    
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
            print("%d" % self.items[i],end=",")
            i=(i+1)% len(self.items)
        print("%d" % self.items[self.rear])

    #Function that return the current front element
    def getFront(self):
        print("The Current Front element is: %d " %self.items[self.front])
    
    #Function that return the current front element
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
        
#Creates an Object
Deck = Deque()
#Shows insertion into deque
Deck.Insertfront(2)
Deck.Insertfront(3)
Deck.Insertfront(5)
Deck.Insertfront(10)
Deck.Insertfront(6)
#Displays current size of deque
Deck.display()
#Get front and rear
Deck.getFront()
Deck.getRear()

#Deletes from front and rear
Deck.Removefront()
Deck.Removerear()
            
        


        
