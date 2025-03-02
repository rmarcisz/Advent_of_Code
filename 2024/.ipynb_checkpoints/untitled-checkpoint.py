containers = [[2, 2], [3, 3], [4, 4], [5, 5]]
index = 0
for container in containers:  
  for item in container:
    if index == 3:
      print(item)      
  index = index + 1