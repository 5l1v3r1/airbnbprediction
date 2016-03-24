f = open('train_data_sessions_pop.csv','r')
f_new = open('booked_train.csv', 'w')

f_new.write(f.readline())

for line in f.readlines():
    feat = line.strip().split(',')

    if int(feat[len(feat)-1]):
        f_new.write(line)

