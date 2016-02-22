import os.path

class Parser():
	def __init__(self, file_name):
		self.data 		= []
		self.file_name 	= ''
		self.format		= []

		if os.path.exists(file_name):
			self.file_name = file_name
		else:
			raise IOError('File not found')


		#Initialize format for CVS file

		data_file = open(self.file_name, "r")
		attributes = data_file.readline().strip("\n").split(",")

		#Create base attribute objects
		for attribute in attributes:
			self.format.append({
					"attribute_name":attribute,
					"numeric"		:True,
					"value_id"		:{},
					"id_value"		:{},
				})

		#Read data
		for line in data_file:
			line = line.strip("\n").split(",")
			data = []
			
			for index, value in enumerate(line):
				try: #Check if the value is numeric
					data.append(int(value))
				except ValueError:	#if the value is not numeric eg. a string
					#update attribute object 
					self.format[index]["numeric"] = False

					#assign an ID to the NAN value if unseen
					if value not in self.format[index]["value_id"]:
						value_id = len(self.format[index]["value_id"])
						self.format[index]["value_id"][value] 		= value_id
						self.format[index]["id_value"][value_id]	= value 
					else:
						value_id = self.format[index]["value_id"][value]

					data.append(value_id)

			self.data.append(data)

		data_file.close()	

	def get_data(self, attributes = []):
		if len(attributes):
			filtered_data	= []
			indices 		= []

			for index, attribute in enumerate(self.format):
				if attribute['attribute_name'] in attributes:
					indices.append(index)

			for data in self.data:
				new_data = []
				for index in indices:
					new_data.append(data[index])
				filtered_data.append(new_data)

			return filtered_data

		return self.data

	def get_class(self, class_name):
		class_instances	= []
		class_index		= 0

		for index, attribute in enumerate(self.format):
			if attribute['attribute_name'] == class_name:
				class_index = index

		for data in self.data:
			class_instances.append(data[class_index])

		return class_instances

	def convert_id(self, ids, class_name):
		values 			= []
		class_index 	= 0

		for index, attribute in enumerate(self.format):
			if attribute['attribute_name'] == class_name:
				class_index = index

		for Id in ids:
			values.append(self.format[class_index]["id_value"][Id])

		return values

	def output_csv(self, file_name, attributes, values):
		data_file = open(file_name, 'w')

		header_line = ''

		for index, attribute in enumerate(attributes):
			if index != 0:
				header_line += ','
			header_line += attribute
		header_line += '\n'
		
		data_file.write(header_line)

		for row in values:
			line = ''
			for index, value in enumerate(row):
				if index != 0:
					line += ','
				line += str(value)
			line += '\n'
			data_file.write(line)

		data_file.close()


