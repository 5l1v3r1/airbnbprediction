from clf import Classifier

booked_attributes 	= [
	'gender',
	'age',
	'signup_method',
	'signup_flow',
	'language',
	'affiliate_channel',
	'affiliate_provider',
	'first_affiliate_tracked',
	'signup_app',
	'first_device_type',
	'first_browser',
	'engage_level',
	'unique_actions',
	'engage_actions',
	'action_count',
	'seconds_count',
	'device_count',
	'apple_device',
	'android_device',
	'other_device',
	'tablet',
	'desktop',
	'early_tod',
	'mid_tod',
	'evening_tod',
	'late_tod'
]

booked_layer = Classifier(
	"../data/test_sessions_tod.csv",
	"../data/train_sessions_tod.csv",
	"country_destination",
	booked_attributes,
	"gbc"
)

#print booked_layer.cross_validate()
booked_layer.output_csv()
#booked_layer.xgb_predict()
