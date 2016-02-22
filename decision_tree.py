from sklearn import tree
from data_parse import Parser
from sklearn import cross_validation

tree_clf = tree.DecisionTreeClassifier()

data_instances = []
classification = []

#Read in the training data
parser_train = Parser('folds/train_users_fold.csv')
data_instances = parser_train.get_data(["age", "gender"])
classification = parser_train.get_class("country_destination")

#Train the classifier with the data instances and their classification
tree_clf = tree_clf.fit(data_instances, classification)

#Read in the testing data
parser_test = Parser('folds/test_users_fold.csv')

test_data 	= []
test_class	= []

test_data	= parser_test.get_data(["age", "gender"])
test_id		= parser_test.get_class("id")

#Classifiy the test data
ids 	 = parser_test.convert_id(test_id, 'id')

tree_values = parser_train.convert_id(tree_clf.predict(test_data), 'country_destination')
for x in range(len(tree_values)):
	tree_values[x] = [ids[x],tree_values[x]]
parser_train.output_csv('tree.csv', ["id","country"], tree_values)
