from clf import Classifier

booked_attributes 	= [
	'male',
	'female',
	'other',	
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
	'late_tod',
	'pop_dest',
	'weekday',
	'PR_NDF',
	'PR_GB',
	'PR_DE',
	'PR_FR',
	'PR_other',
	'PR_ES',
	'PR_PT',
	'PR_NL',
	'PR_US',
	'PR_AU',
	'PR_IT',
	'PR_CA'
]

booked_layer = Classifier(
	"../data/test_pr.csv",
	"../data/train_pr.csv",
	"country_destination",
	booked_attributes,
	"xgb"
)

#print booked_layer.cross_validate()
#booked_layer.output_csv()
booked_layer.xgb_predict()
