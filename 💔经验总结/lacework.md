
609， more focus on traversal file system, how to detect duplicates and h‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌ow to optimize runtime.



design car rental service. Major requirement as follow
1. reserve car
2. check out car
3. drop off car
4. Build data pipeline to process car reversation every day
#  more detailed requirements:
1. display reversation for a car, allow user to pick a date
2. allow different pick-up and drop-off location
3. allow over booking, assume some reservation will be cancelled
sys design 2
```
design music streaming platform:
users:
- music creator
- normal user listen to music
- internal admin user
Function requirement:
1) upload music
2) normal user
2.a) search music songs or collections
2.b) play songs
2.c) playlist management
2.d) recommondation
3) admin user‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌
3.a) censorship on upload, automate + manual
3.b) system operation to handle scalability, failure, etc
3.c) admin work, customer support about account issues



```py
# 

"""
Implement the dependency resolution algorithm for a simple build tool.

Our simple build tool uses simplified Makefile syntax, which has a list of targets,
in the following format: 

        target: dependencyA dependencyB dependencyC ...
                action
                
The input to the program is a Makefile and the name of a target to build.

The output should be a list of actions to execute, where the action for (e.g.)
"dependencyA" must be ordered before the action for "target".

NOTE: You can assume that the Makefile has already been parsed into an appropriate
data structure, so you do not need to implement the text parsing. Please define
the data structure you will use as part of the answer.


Example Makefile:

        foo.h: 
                protoc foo.proto
        
        foo.o: foo.h 
                gcc -c foo.c
        
        bar.o: bar.h foo.h 
                gcc -c bar.c
        
        main.o:
                gcc -c main.c
        
        main: foo.o bar.o main.o
                ld -o main foo.o bar.o main.o
        
make main
                
Example output for target "main" (N.B. other orders that respect the dependency
structure are valid):

        gcc -c main.c
        protoc foo.proto
        gcc -c foo.c
        gcc -c bar.c
        ld -o main foo.o bar.o main.o


        
main: A B C
     action_main
     
A: B
    action_A

B: 
    action_B
    
C:
   action_C
        

output:
      action_C
      action_B
      action_A
      action_main

2 rules:
  1 - dependencies must be processed first
  2 - don't do the work twice. Do not repeat "actions"       
      
"""

inputlst = [
    ['main', 'A', 'B', 'C'], ['A', 'B'], ['B'], ['C']];
    
mapping = {
    "main": "action_main",
    "A": "action_a",
    "B": "action_b",
    "C": "action_c",
}





from collections import defaultdict, deque

def sol2(inputlst, mapping, start = "main"):
    res = []
    
    def dfs(node):
        #if m[node] == []:
        #    res.append(mapping[node])
            
        for dep_n in m[node]:
            dfs(dep_n)
        
        res.append(mapping[node])
            
    m = defaultdict(list) # {target : dep nodes}
    indegree = defaultdict(int)
    
    for e in inputlst:
        target = e[0]
        dep = e[1: ] if len(e) >= 1 else []
        m[target] = dep
        
    dfs(start)
    return res
    
    
print (sol2(inputlst, mapping))

def sol1(inputlst, mapping):
    res = []
    
    m = defaultdict(list) # {target : dep nodes}
    indegree = defaultdict(int)
    for e in inputlst:
        target = e[0]
        dep = e[1: ] if len(e) >= 1 else []

        for dep_n in dep:
            m[dep_n].append(target)
        indegree[target] += len(dep)
        
    # indegree for dependency 
    
    
    q = deque(n for n in indegree if indegree[n] == 0)
    
    # loop through node 0 indegree
    #  indegree -1
    #  add to res
  
    while q:
        node = q.popleft()
        res.append(mapping[node])
        for dep_n in m[node]:
            indegree[dep_n] -= 1
            if indegree[dep_n] == 0:
                q.append(dep_n)
    
    return res

#print (sol1(inputlst, mapping))
    



```

