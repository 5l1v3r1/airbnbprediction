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
data_instances = parser_train.get_data(["age", "gender"])
classification = parser_train.get_class("country_destination")

#Train the classifier with the data instances and their classification
g_clf = g_clf.fit(data_instances, classification)
m_clf = m_clf.fit(data_instances, classification)
b_clf = b_clf.fit(data_instances, classification)

#Read in the testing data
parser_test = Parser('folds/test_users_fold.csv')

test_data 	= []
test_class	= []

test_data	= parser_test.get_data(["age", "gender"])
test_class	= parser_test.get_class("country_destination")
test_id		= parser_test.get_class("id")

#Classifiy the test data
ids 	 = parser_test.convert_id(test_id, 'id')

g_values = parser_train.convert_id(g_clf.predict(test_data), 'country_destination')
for x in range(len(g_values)):
	g_values[x] = [ids[x],g_values[x]]
parser_train.output_csv('g_nb.csv', ["id","country"], g_values)

m_values = parser_train.convert_id(m_clf.predict(test_data), 'country_destination')
for x in range(len(m_values)):
	m_values[x] = [ids[x],m_values[x]]
parser_train.output_csv('m_nb.csv', ["id","country"], m_values)

b_values = parser_train.convert_id(b_clf.predict(test_data), 'country_destination')
for x in range(len(b_values)):
	b_values[x] = [ids[x],b_values[x]]
parser_train.output_csv('b_nb.csv', ["id","country"], b_values)
