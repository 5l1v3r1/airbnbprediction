from data_parse import Parser
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

g_clf = GaussianNB()
m_clf = MultinomialNB()
b_clf = BernoulliNB()

data_instances = []
classification = []

#Read in the training data
parser_train = Parser('folds/train_users_fold.csv')

for data in parser_train.get_data(["age", "gender", "country_destination"]):
	data_instances.append(data[:len(data)-1])
	classification.append(data[len(data)-1])

#Train the classifier with the data instances and their classification
g_clf = g_clf.fit(data_instances, classification)
m_clf = m_clf.fit(data_instances, classification)
b_clf = b_clf.fit(data_instances, classification)

#Read in the testing data
parser_test = Parser('folds/test_users_fold.csv')

test_data 	= []
test_class	= []

for data in parser_test.get_data(["age", "gender", "country_destination"]):
	test_data.append(data[:len(data)-1])
	test_class.append(data[len(data)-1])

#Classifiy the test data
print "GaussianNB Score:"
print g_clf.score(test_data, test_class)
print "MultinomialNB Score:"
print m_clf.score(test_data, test_class)
print "BernoulliNB Score:"
print b_clf.score(test_data, test_class)
