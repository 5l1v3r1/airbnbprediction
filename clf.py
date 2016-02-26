import sys, getopt
from data_parse import Parser
from sklearn import cross_validation

from sklearn import svm
from sklearn import tree
from sklearn import linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB



'''
Main function
'''
class Classifier():
	def __init__(self, testfile, trainfile, predict, attributes, classifier, cv=False, output=False):
		self.output 		= output
		self.cv 			= cv 
		self.testfile 		= testfile
		self.trainfile  	= trainfile
		self.predict		= predict
		self.attributes 	= attributes 
		self.clf 			= self.get_classifier(classifier)

	def get_classifier(self, classifier):
		if classifier == 'gnb':
			return GaussianNB()
		elif classifier == 'bnb':
			return BernoulliNB()
		elif classifier == 'mnb':
			return MultinomialNB()
		elif classifier == 'svm':
			return svm.SVC(decision_function_shape='ovr')
		elif classifier == 'rf':
			return RandomForestClassifier(max_depth=len(self.attributes), n_estimators=len(self.attributes), max_features=len(self.attributes))
		elif classifier == 'dt':
			return tree.DecisionTreeClassifier()
		elif classifier == 'ls':
			return linear_model.LinearRegression()
		elif classifier == 'pr':
			return linear_model.Perceptron(fit_intercept=False, n_iter=10, shuffle=False)
		elif classifier == 'kr':
			return KernelRidge(alpha=1.0)

	def cross_validate(self):
		parser_train 	= Parser(self.trainfile)
		data_instances 	= parser_train.get_data(self.attributes)
		classification 	= parser_train.get_class(self.predict)

		data_train, data_test, target_train, target_test = self.c_v(data_instances, classification)
		clf = self.clf.fit(data_train, target_train)

		return clf.score(data_test, target_test)

	def c_v(self, data, target):

		data_train, data_test, target_train, target_test = cross_validation.train_test_split(
			data, target, test_size=0.4, random_state=0
		)

		return data_train, data_test, target_train, target_test

	def output_csv(self):
		parser_train 	= Parser(self.trainfile)
		data_instances 	= parser_train.get_data(self.attributes)
		classification 	= parser_train.get_class(self.predict)
		clf 			= self.clf.fit(data_instances, classification)

		parser_test = Parser(self.testfile)

		test_data	= parser_test.get_data(self.attributes)
		test_class	= parser_test.get_class(self.predict)
		test_id		= parser_test.get_class("id")

		self.write_csv(parser_test, parser_train, clf, self.predict, test_data)

	def write_csv(self, parser_test, parser_train, clf, predict_class, test_data):
		test_id	= parser_test.get_class("id")
		ids 	= parser_test.convert_id(test_id, 'id')
		values 	= parser_train.convert_id(clf.predict(test_data), predict_class)

		for index in range(len(values)):
			values[index] = [ids[index], values[index]]
		parser_train.output_csv('output.csv', ["id","country"], values)

