f = open('session/train_data_sessions_pop.csv', 'r')

f.readline()

booked_array = []
for line in f.readlines():
    line = line.strip().split(',')
    booked = (line[len(line)-5] != 'NDF')

    if booked:
        booked_array.append(1)
    else:
        booked_array.append(0)
    
f = open('session/train_data_sessions_pop.csv', 'r')
f_new = open('session/new_train_data_sessions_pop_2.csv', 'w')
f.readline()

for value in booked_array:
    f_new.write(f.readline().strip()+','+str(value)+'\n')
 
