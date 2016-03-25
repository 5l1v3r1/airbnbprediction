from clf import Classifier

booked_attributes 	= [
	'age',
	'engage_level',
	'unique_actions',
	'engage_actions',
	'action_count',
	'seconds_count',
	'device_count',
]

booked_layer = Classifier(
	"../data/test_sessions.csv",
	"../data/train_sessions.csv",
	"country_destination",
	booked_attributes,
	"rf"
)

booked_layer.output_csv()
