from pydaisi import Daisi
import time
import logging

#No config needed, code is directly deployed from the GitHub repo

logging.getLogger().setLevel(logging.ERROR)

t = time.time()

d = Daisi("Hello (vs. Lambda)")

#Friendly interface to call the remote function
response = d.hello()


#No deserialization or data conversion needed
print(response.value)



print(time.time() - t)