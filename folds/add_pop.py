updated_file = open("train_users_fold.csv", 'r')
new_file	 = open("train_users_fold_pop.csv", 'w')

new_file.write(updated_file.readline())

for line in updated_file:
	values 	= line.strip('\n').split(',')
	gender 	= values[4]
	age		= values[5]

	if gender == '-unknown-':
		country = 'NDF'
	else:
		pop_dest	 = open("pop_dest.csv", 'r')
		pop_dest.readline()
			
		for row in pop_dest:
			values 		= row.strip('\n').split(',')
			row_gender 	= values[1]
			row_age 	= values[0]
			row_country = values[2]

			if gender == row_gender:
				if age[:-2] == row_age:
					country = row_country
	new_file.write(line.strip('\n')+','+country+'\n')
