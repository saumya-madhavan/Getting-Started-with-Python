# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data=yaml.load(f)
f.close()    

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
print (data.keys())
#for key,val in data.items():
#    print(key,val)
print (data['info']['city'])
print (data['info']['venue'])

# Which are all the teams that played in the tournament ? How many teams participated in total?
print ("vs ".join(data['info']['teams']))

# Which team won the toss and what was the decision of toss winner ?
print (data['info']['toss']['winner'])
print (data['info']['toss']['decision'])

# Find the first bowler and first batsman who played the first ball of the first inning
print (data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
print (data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])


# How many deliveries were delivered in first inning ?
print (len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print (len(data['innings'][1]['2nd innings']['deliveries']))


# Which team won and how ?
print (data['info']['outcome']['winner'])
print (data['info']['outcome']['by']['runs'])




