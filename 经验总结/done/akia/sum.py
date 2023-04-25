
inputs = [-1, 1, 0, 2, -2, -2]
target = 0
outputs = [(-1, 1), (-2, 2)]

# [(-1, 0, 1), (-2, 0, 2)]

# bucket = {value: [(x, y)]}
# -num in bucket 

from collection import defaultdict
def sol():

	res = []
  bucket = defualtdict(int)
  
  for num in inputs:
    if num in bucket and bucket[num] > 0:
      res.append((num, target - num))
      bucket[num] -= 1 # { 1: 0, 0: 1, -2: 1}
    else:
      bucket[target - num] += 1 
    
	return res    
    

  
def sol2():

	res = []
  bucket = defualtdict(list)
  
  for i in range(len(inputs)):
    for j in range(i+1, len(inputs)):
      bucket[-(inputs[i] + inputs[j])].append((i, j))
  
  for h in range(len(inputs)):
    num = inputs[h]
    if num in bucket:
      for combo in bucket[num]:
        if h not in combo:
      		res.append((num, inputs[combo[0]], inputs[combo[1]]))
					
    
	return res    
    
  
def sol3(inputs):
  res = []
  inputs.sort()
  
  if len(inputs) < 2:
    return []
  s_ptr, e_ptr = 0, len(inputs)
  
  for final_prt in range(len(inputs), -1, -1):
    for e_ptr in range(i, -1, 0):
      while s_ptr < e_ptr:
        acc = sum(inputs[s_ptr],inputs[e_ptr],inputs[final_prt])
        if target == acc:
          res.append((inputs[s_ptr], inputs[e_ptr], inputs[final_prt]))
          e_ptr -= 1
        elif target > acc:
          s_ptr += 1
        else:
          e_ptr -= 1
    
    return res

  
  
  
  
  
  
  
  
  