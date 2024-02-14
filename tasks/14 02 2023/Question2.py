# Print even length words in a string. 

# Sample String : ''I love coding" 

# Expected Result : “love, coding”


n="I love coding"

s=n.split(" ") 
for i in s:
  if len(i)%2==0: 
    print(i)