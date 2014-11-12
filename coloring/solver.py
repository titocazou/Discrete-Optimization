#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import collections
import time

class GraphColoring:
    
    def __init__(self,Edges,Node_count,Edge_count):
        self.edges=Edges
        self.node_count=Node_count
        self.edge_count=Edge_count
        self.nodes=[None]*Node_count
        self.colorPanel=[0]
        self.solution=[None]*Node_count
        self.colorCount=[0]
   
    def Initialize(self):
        # Create a list of node objects
        for i in range(0,self.node_count):
            self.nodes[i]=self.Node(i)
        
        # set the list of neighbors for each node
        for i in range (0,len(self.edges)):
            self.nodes[self.edges[i][0]].neighbors.append(self.edges[i][1])
            self.nodes[self.edges[i][1]].neighbors.append(self.edges[i][0])

        for i in range(0,self.node_count):
            self.nodes[i].num_neighbors=len(self.nodes[i].neighbors)
            
 
        
                        
            
    def RandomSolve(self):
        templist=list(self.nodes)
        random.shuffle(templist) 
        templist=self.AssignColors(templist)

        poto=5;
        self.RearrangeList(templist)
    

        
    def AssignColors(self,templist):
        arrangedList=list(self.nodes)
    
        for i in range(0,self.node_count):
            node=templist[i]
            
            neighborCheck=False
            k=0;
         
            while neighborCheck==False:
                check=0;
                node.color=self.colorPanel[k]
                for j in range(0,node.num_neighbors):
                    if arrangedList[node.neighbors[j]].color!=node.color:
                        check+=1
                    else:
                        break
                if check == node.num_neighbors:
                    neighborCheck=True
                    self.colorCount[k]+=1
                else:
                    k=k+1
                    if k > self.colorPanel[-1]:
                       self.colorPanel.append(self.colorPanel[-1]+1)
                       self.colorCount.append(0)                      

                templist[i]=node
        return templist

    def RearrangeList(self,templist):

        for i in range(0,self.node_count):
            node=templist[i]
            self.nodes[node.node]=node;
            self.solution[node.node]=node.color;

    def ArrangeSolutionByColor(self):

        templist=list(self.nodes);
        arrangedList=[None]*self.node_count;
        colorCount=list(self.colorCount);
        nodesToVisit=range(0,self.node_count);

        visitedColors=[0]*len(self.colorCount)
        l=0;

        while len(nodesToVisit)>=1 :
          
            minNumColors=10000;
            for j in range (0,len(colorCount)):
                if colorCount[j] < minNumColors and visitedColors[j]==0:
                    minNumColors= colorCount[j]
                    smallestColorIndex=j;
            visitedColors[smallestColorIndex]=1;         
        
            
            p = len(nodesToVisit)
            m=0;
            for k in range (0,p):
                if templist[nodesToVisit[k-m]].color==smallestColorIndex:
                    arrangedList[l]=templist[nodesToVisit[k-m]].node;
                    nodesToVisit.pop(k-m)
                    l+=1;
                    m+=1;

        arrangedList = sorted(self.nodes, key=lambda x: x.color, reverse=True)

        return arrangedList
        poto=5;

    def Reset (self):
        self.colorPanel=[0]
        self.colorCount=[0]

        for j in range (0,self.node_count):
            self.nodes[j].color=-1
           
    class Node:
        def __init__(self,node):
            self.node=node
            self.color=-1;
            self.neighbors=[]
            self.num_neighbors=0



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))


    gc=GraphColoring(edges,node_count,edge_count)
    gc.Initialize()
    gc.RandomSolve()

    minColor=gc.colorPanel[-1]+1;
    bestSol=list(gc.solution);
    t=0
    while minColor > 16:
        t=t+1
        for i in range(0,5):
            sol = gc.ArrangeSolutionByColor()
        
            gc.Reset()
            for j in range (0,gc.node_count):
                sol[j].color=-1


            sol = gc.AssignColors(sol)
            gc.RearrangeList(sol)
     
        if gc.colorPanel[-1]+1 < minColor :

            minColor=gc.colorPanel[-1]+1
            bestSol=list(gc.solution);
        else:
            gc.Reset()
            gc.RandomSolve()
        print ""
        print "Iteration number:",t
        print "current colors: " ,gc.colorPanel[-1]+1
        print "Current Minimum:", minColor
        print ""
        #print "Iteration number:",i
        #print "Solution colors:" ,gc.colorPanel[-1]+1 
        #print  "Solution:", gc.solution
    
    solution=bestSol;
    print bestSol
    print minColor

    
    
    # prepare the solution in the specified output format
    output_data = str(minColor) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, bestSol))

    f = open('solution', 'r+')
    f.write(output_data)
    return output_data
    

import sys

if __name__ == '__main__':
    sys.argv.append("data\\gc_50_1");

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

