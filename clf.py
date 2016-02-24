import sys, getopt
from data_parse import Parser
from sklearn import cross_validation

from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

def parse_args(argv):

	try:
		opts, args = getopt.getopt(argv,"hov",["train=","test=","class=","attributes=","classifier="])
	except getopt.GetoptError:
		print 'clf.py --train <train file> --test <test_file> --attributes <example,example2,example3> --classifier <classifier> --class <predict class>'
		print '-o argument'
		print '\t\tOutputs csv files'
		print '-v argument'
		print '\t\tOutputs the cross validation score'
		sys.exit(2)

	output 	= False
	cv 		= False

	for opt, arg in opts:
		if opt == '-h':
			print 'clf.py --train <train file> --test <test_file> --attributes <example,example2,example3> --classifier <classifier> --class <predict class>'
			sys.exit()
		elif opt in ("--test"):
			testfile = arg
		elif opt in ("--train"):
			trainfile = arg
		elif opt in ("--class"):
			predict_class = arg
		elif opt in ("--attributes"):
			attribute_list = arg.split(',')
		elif opt in ("-o"):
			output = True
		elif opt in ("-v"):
			cv = True
		elif opt in ("--classifier"):
			if arg == 'gnb':
				clf = GaussianNB()
			elif arg == 'bnb':
				clf = BernoulliNB()
			elif arg == 'mnb':
				clf = MultinomialNB()
			elif arg == 'svm':
				clf = svm.SVC()
			elif arg == 'rf':
				clf = RandomForestClassifier(max_depth=len(attribute_list), n_estimators=5, max_features=len(attribute_list))
			elif arg == 'dt':
				clf = tree.DecisionTreeClassifier()

	main(output, cv, testfile, trainfile, predict_class, clf, attribute_list)

def main(output, cv, testfile, trainfile, predict_class, clf, attribute_list):

	parser_train 	= Parser(trainfile)
	data_instances 	= parser_train.get_data(attribute_list)
	classification 	= parser_train.get_class(predict_class)
	
	
	if cv:
		data_train, data_test, target_train, target_test = cross_validate(data_instances, classification)
		clf = clf.fit(data_train, target_train)

		print "Score for " + str(clf) + " classifier:"
		print clf.score(data_test, target_test)
	else:
		clf = clf.fit(data_instances, classification)

		parser_test = Parser(testfile)

		test_data	= parser_test.get_data(attribute_list)
		test_class	= parser_test.get_class(predict_class)
		test_id		= parser_test.get_class("id")

		if output:
			write_csv(parser_test, parser_train, clf, predict_class, test_data)

def write_csv(parser_test, parser_train, clf, predict_class, test_data):
	test_id	= parser_test.get_class("id")
	ids 	= parser_test.convert_id(test_id, 'id')
	values 	= parser_train.convert_id(clf.predict(test_data), predict_class)

	for index in range(len(values)):
		values[index] = [ids[index], values[index]]
	parser_train.output_csv('output.csv', ["id","country"], values)

def cross_validate(data, target):
	data_train, data_test, target_train, target_test = cross_validation.train_test_split(
		data, target, test_size=0.4, random_state=0
	)
	return data_train, data_test, target_train, target_test

#output.csv file created here
def ouput_csv(parser, clf):
	
	ids 	= parser_test.convert_id(test_id, 'id')
	values 	= parser.convert_id(clf.predict(test_data), 'country_destination')
	
	for x in range(len(g_values)):
		g_values[x] = [ids[x],g_values[x]]
	
	parser_train.output_csv('output.csv', ["id","country"], g_values)

if __name__ == "__main__":
   parse_args(sys.argv[1:])
