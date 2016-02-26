from clf import Classifier
import itertools

data_file 	= open("statistics.txt", 'a')
test_count 	= 4
test_number	= 0

attributes 	= [
	'gender', 'age_bkt', 'secs_elapsed', 'pop_dest'
]


Classifier(
	"session/test_data_sessions_pop.csv",
	"session/train_data_sessions_pop.csv",
	"country_destination",
	attributes,
	"rf",
	True,
	False
).output_csv()

'''

Classifiers	= ["rf", "dt", "pr", "mnb", "gnb", "bnb", "svm"]

data_file.write("\nNew Test\n")

for L in range(4, 5):
	for subset in itertools.combinations(attributes, L):
		for classifier in Classifiers:
			score = Classifier(
				"session/test_data.csv",
				"session/session_train.csv",
				"country_destination",
				attributes,
				classifier,
				True,
				False
			).cross_validate()
			
			data_file.write(classifier)
			data_file.write("\t")
			data_file.write(str(subset))
			data_file.write("\t")
			data_file.write(str(score))
			data_file.write("\n")
			test_number += 1
			print str((float(test_number)/test_count)*100)+'% \done '
'''