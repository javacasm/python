import json
  
details = {'Name': "Bob",
          'Age' :28}
  
with open('convert.txt', 'w') as convert_file:
     convert_file.write(json.dumps(details))
26
>>> with open('convert.txt','r') as f:
    data = f.read()
    
>>> type(data)
<class 'str'>
>>> js = json.loads(data)
>>> js
{'Name': 'Bob', 'Age': 28}
>>> 