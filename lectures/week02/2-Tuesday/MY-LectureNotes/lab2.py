import corona #object

most_recovered = corona.data[0]['recovered'] 
least_recovered = corona.data[0]['recovered']

state_mr = ''
state_lr = ''

for i in range(len(corona.data)):
    print(corona.data[i]['state'])
    print(f"cases: {corona.data[i]['cases']}")
    print(f"recovered: {corona.data[i]['recovered']}")
    print(f"active: {corona.data[i]['active']}\n")
    
for j in range(len(corona.data)):
    if corona.data[j]['recovered'] >= most_recovered:
        state_mr = corona.data[j]['state']
    if corona.data[j]['recovered'] <= least_recovered:
        state_lr = corona.data[j]['state']
    
print(state_mr)
print(state_lr)
    
    
    

