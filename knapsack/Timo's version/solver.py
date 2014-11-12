#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import collections
import random

Item = namedtuple("Item", ['index', 'value', 'weight','ratio'])

class KnapSack:

     def __init__(self,Item_count,Capacity,Items):
         self.item_count=Item_count
         self.capacity=Capacity
         self.items=Items
         self.MaxValue=0
         self.BestList=[0]*self.item_count
         self.Dic=collections.OrderedDict()
         self.counter=0
 

     def Greedy (self) :
         # use Greedy algorithm first to determine initial guess of max value
             value = 0
             weight = 0

             for item in self.items:
              if weight + item.weight <= self.capacity:
                 value += item.value
                 weight += item.weight
    
             self.MaxValue=value;

     def BranchAndBound (self):
         # Initialize first node #
         Initialnode=self.Node();
         Initialnode.level=0;
         Initialnode.value=0;
         Initialnode.weight=0;
         Initialnode.VisitedList=[0]*self.item_count;

         Initialnode.bound=self.DetermineBound(Initialnode)
         
         self.AddEntrySafely(Initialnode.bound,Initialnode)


         while len(self.Dic)>=1 :
             self.counter+=1
             # Pop out the node with the most potential from the list #
             FatherNode=self.PopOutMostValuable();

             print "Size of Queue:",len(self.Dic)
             print "Current Max value:", self.MaxValue
             print "Number of Nodes visited:", self.counter
             print "bound at this node:", FatherNode.bound
             print ""

             if FatherNode.bound > self.MaxValue :
             
                 # Go left first (pick the next object)
                 PickItem=self.Node()
                 PickItem.level=FatherNode.level+1;
                 PickItem.value=FatherNode.value+self.items[PickItem.level-1].value
                 PickItem.weight=FatherNode.weight+self.items[PickItem.level-1].weight
                 PickItem.VisitedList=FatherNode.VisitedList[:]
          
                 # Set the bound to the current value in the knapsack for now
                 PickItem.bound=PickItem.value;

                 # Continue with this item only if it does not exceed max knapsack capacity
                 if PickItem.weight <= self.capacity :

                     PickItem.VisitedList[self.items[PickItem.level-1].index]=1;
                     # If the this is not the last item, calculate the bound
                     if PickItem.level < self.item_count:
                        PickItem.bound=self.DetermineBound(PickItem)
                    
                     # Set the new max if the value is a new max
                     if PickItem.value >= self.MaxValue:
                         self.MaxValue=PickItem.value
                         self.BestList=PickItem.VisitedList[:]

                     # if the bound is higher than the current max, add this node to the queue
                     if PickItem.bound > self.MaxValue:
                         self.AddEntrySafely(PickItem.bound,PickItem)
                     
                 # Now go right (don't pick next object)
                 RejectItem=self.Node()
                 RejectItem.level=FatherNode.level+1;
                 RejectItem.value=FatherNode.value;
                 RejectItem.weight=FatherNode.weight;
                 RejectItem.VisitedList=FatherNode.VisitedList[:]
                
                 # Set the bound to the current value in the knapsack for now
                 RejectItem.bound=RejectItem.value;
                
                 # Continue with this item only if it does not exceed max knapsack capacity
                 if RejectItem.weight < self.capacity :

                      # If the this is not the last item, calculate the bound
                     if RejectItem.level < self.item_count:
                        RejectItem.bound=self.DetermineBound(RejectItem)

                     # if the bound is higher than the current max, add this node to the queue
                     if RejectItem.bound > self.MaxValue:
                        self.AddEntrySafely(RejectItem.bound,RejectItem)
       


     # Function to safely add an node to the queue by making sure all the keys are different
     def AddEntrySafely (self,Key,value):
         key=Key
         Keys=self.Dic.keys()
         for i in range (0, len(Keys)):
             if abs(key - Keys[i])<0.00000001 :
                 key+= random.random()/10
          #       key-= random.random()/10
          #       key+= random.random()/10
         self.Dic[key]=value
      

                
     # function to scan the search queue and pop out the most promising node
     def PopOutMostValuable (self):
         MostValuedKey=0.0;
         Keys=self.Dic.keys()

         for i in range (0, len(Keys)):
             if Keys[i]>MostValuedKey :
                 MostValuedKey=Keys[i]
         node=self.Dic.pop(MostValuedKey)
         return node
         

     # determine the bound of a given node
     def DetermineBound(self,node):
        lvl=node.level;
        wgt=node.weight;
        val=node.value;

        if wgt> self.capacity :
            print 'Go home you are drunk'
            return 0

        i=lvl;
        while wgt <= self.capacity and i<=self.item_count-1 :
            wgt += self.items[i].weight;
            val += self.items[i].value;
            i=i+1;
        if wgt > self.capacity:
          Bound=val - (wgt-self.capacity)/(float)(self.items[i-1].weight)*self.items[i-1].value;
        else:
          Bound=val


        return Bound
     
      
     class Node:
           def __init__(self):
            self.level = 0;
            self.value=0;
            self.weight=0;
            self.VisitedList=[];
            self.bound=0.0

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items=[];


    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]),float(parts[0])/float(parts[1])))

    # Sort Items in the initial List by density value
    items=sorted(items, key=lambda items: items[3], reverse=True) 


    knap= KnapSack(item_count,capacity,items)
    knap.Greedy();
    knap.BranchAndBound();
    print knap.BestList
    print knap.MaxValue

   # prepare the solution in the specified output format
    output_data = str(knap.MaxValue) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, knap.BestList))
    return output_data

  



import sys

if __name__ == '__main__':
    sys.argv.append("data\\ks_200_0");

    if len(sys.argv) >1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()

       # if (len(sys.argv) > 2):
       #     if (sys.argv[2] == "-v"):
        #        printOut = True;

        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

