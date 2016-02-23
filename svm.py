from data_parse import Parser
from sklearn import cross_validation
from sklearn import svm

svm_clf = svm.SVC()

data_instances = []
classification = []

attribute_list = ["age", "gender", "first_affiliate_tracked"]
classification = "country_destination"

#Read in the training data
parser_train = Parser('folds/train_users_fold.csv')
data_instances = parser_train.get_data(attribute_list)
classification = parser_train.get_class(classification)

#Train the classifier with the data instances and their classification
svm_clf = svm_clf.fit(data_instances, classification)

#Read in the testing data
parser_test = Parser('folds/test_users_fold.csv')

test_data 	= []
test_class	= []

test_data	= parser_test.get_data(attribute_list)
test_class	= parser_test.get_class(classification)
test_id		= parser_test.get_class("id")

#Classifiy the test data
ids 	 = parser_test.convert_id(test_id, 'id')

svm_values = parser_train.convert_id(svm_clf.predict(test_data), 'country_destination')
for x in range(len(svm_values)):
	svm_values[x] = [ids[x],svm_values[x]]
parser_train.output_csv('svm.csv', ["id","country"], svm_values)
