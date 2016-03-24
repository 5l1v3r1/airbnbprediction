from clf import Classifier

booked_attributes 	= [
	'age', 'gender', 
	'action_count', 'secs_elapsed', 'pop_dest'
]

booked_layer = Classifier(
	"session/test_data_sessions_pop.csv",
	"session/train_data_sessions_pop.csv",
	"country_destination",
	booked_attributes,
	"rf"
)

booked_layer.output_csv()
