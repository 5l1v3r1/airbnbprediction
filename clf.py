import sys, getopt
from data_parse import Parser
from sklearn import cross_validation




'''
Main function
'''
class Classifier():
	def __init__(self, testfile, trainfile, predict_class, attributes, classifier):
		self.testfile 		= testfile
		self.trainfile  	= trainfile
		self.predict_class	= predict_class
		self.attributes 	= attributes 
		self.clf 			= self.get_classifier(classifier)
		self.parser 		= Parser(self.trainfile)

	def get_classifier(self, classifier):
		if classifier == 'gnb':
			from sklearn.naive_bayes import GaussianNB
			print "Using GaussianNB classifier"
			return GaussianNB()
		elif classifier == 'bnb':
			from sklearn.naive_bayes import BernoulliNB
			print "Using BernoulliNB classifier"
			return BernoulliNB()
		elif classifier == 'mnb':
			from sklearn.naive_bayes import MultinomialNB
			print "Using MultinomialNB classifier"
			return MultinomialNB()
		elif classifier == 'svm':
			from sklearn import svm
			print "Using svm classifier"
			return svm.SVC(degree=2, cache_size=5000)
		elif classifier == 'sgd':
			print "Using SGD classifier"
			from sklearn.linear_model import SGDClassifier
			return SGDClassifier(loss="log", penalty="l2", n_iter=20, shuffle=True)
		elif classifier == 'rf':
			from sklearn.ensemble import RandomForestClassifier
			print "Using RandomForest classifier"
			return RandomForestClassifier(max_depth=len(self.attributes), n_estimators=len(self.attributes), max_features=len(self.attributes))
		elif classifier == 'gbc':
			from sklearn.ensemble import GradientBoostingClassifier
			print "Using GradientBoosting classifier"
			return GradientBoostingClassifier()
		elif classifier == 'dt':
			from sklearn import tree
			print "Using DecisionTree classifier"
			return tree.DecisionTreeClassifier()
		elif classifier == 'ls':
			from sklearn import linear_model
			print "Using LinearRegression classifier"
			return linear_model.LinearRegression()
		elif classifier == 'pr':
			from sklearn import linear_model
			print "Using Perceptron classifier"
			return linear_model.Perceptron(fit_intercept=False, n_iter=10, shuffle=False)
		elif classifier == 'cls':
			from sklearn import cluster
			print "Using cluster classifier"
			#return cluster.AgglomerativeClustering(init='random')
			return cluster.KMeans(n_clusters=11)
		elif classifier == 'kr':
			from sklearn.kernel_ridge import KernelRidge
			print "Using kernel_ridge classifier"
			return KernelRidge(alpha=1.0)

	def predict(self, test_data):
		temp = []
		for index, value in enumerate(test_data):
			try:
				if value is '':
					value = 0
				temp.append(int(float(value)))
			except:
				temp.append(self.parser.convert_value(value, self.attributes[index]))

		test_data 	= temp

		predictions = self.clf.predict(test_data)
		
		try:
			values 	= self.parser.convert_id(predictions, self.predict_class)
		except:
			values 	= predictions.tolist()
		
		return values

	def cross_validate(self):
		print "Begin Cross Validation"
		data_instances 	= self.parser.get_data(self.attributes)
		classification 	= self.parser.get_class(self.predict_class)

		data_train, data_test, target_train, target_test = self.c_v(data_instances, classification)

		clf = self.clf.fit(data_train, target_train)

		print "Finish Cross Validation"
		return clf.score(data_test, target_test)

	def c_v(self, data, target):

		data_train, data_test, target_train, target_test = cross_validation.train_test_split(
			data, target, test_size=0.4, random_state=0
		)

		return data_train, data_test, target_train, target_test

	def train(self):
		parser			= Parser(self.trainfile)
		data_instances 	= self.parser.get_data(self.attributes)
		classification 	= self.parser.get_class(self.predict_class)
		self.clf.fit(data_instances, classification)

	def output_csv(self, filename='output.csv'):
		self.train()

		parser_test = Parser(self.testfile)

		test_data	= parser_test.get_data(self.attributes)
		test_class	= parser_test.get_class(self.predict_class)
		test_id		= parser_test.get_class("id")
		
		self.write_csv(parser_test, test_data, filename)

	def write_csv(self, parser_test, test_data, filename):
		test_id		= parser_test.get_class("id")
		ids 		= parser_test.convert_id(test_id, 'id')
		predictions = self.clf.predict(test_data)
		
		try:
			values 	= self.parser.convert_id(predictions, self.predict_class)
		except:
			values 	= predictions.tolist()

		for index in range(len(values)):
			values[index] = [ids[index], values[index]]
		self.parser.output_csv(filename, ["id","country"], values)
