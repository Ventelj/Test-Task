#!/usr/bin/env python
# coding: utf-8

# In[9]:


import json
with open('file1.json','r') as a:
    data1 = a.read()
obj1 = json.loads(data1)
with open('file2.json','r') as a:
    data2 = a.read()
obj2 = json.loads(data2)
dlt = {i: obj1[i] for i in obj1 if i in obj2 and obj1[i] != obj2[i]}
if len(dlt):
    print ("Есть различие!\nJSON 1 | JSON 2")
    for key, value in dlt.items():
        print (key, "->", value, '|',key, "->", obj2[key])


# In[ ]:




