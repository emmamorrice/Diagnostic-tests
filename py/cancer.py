#importing the libraries needed
import pandas as pd

#identifying the source data
#source: https://www.opendata.nhs.scot/dataset/drug-and-alcohol-treatment-waiting-times
cancer31day= pd.read_csv("https://www.opendata.nhs.scot/dataset/11c61a02-205b-43f6-9297-243679103617/resource/58527343-a930-4058-bf9e-3c6e5cb04010/download/cwt_31_day_standard.csv")
cancer61day= pd.read_csv("https://www.opendata.nhs.scot/dataset/11c61a02-205b-43f6-9297-243679103617/resource/23b3bbf7-7a37-4f86-974b-6360d6748e08/download/cwt_62_day_standard.csv")
HBnames= pd.read_csv("https://www.opendata.nhs.scot/dataset/9f942fdb-e59e-44f5-b534-d6e17229cc7b/resource/652ff726-e676-4a20-abda-435b98dd7bdc/download/hb14_hb19.csv")

#merging datasets
merge1= pd.merge(cancer31day, HBnames, left_on='HBT', right_on='HB')
merge2= pd.merge(cancer61day, HBnames, left_on='HBT', right_on='HB')

cancer31dayfinal = merge1.drop(columns=['HBTQF','CancerTypeQF', 'NumberOfEligibleReferrals31DayStandardQF', 'NumberOfEligibleReferralsTreatedWithin31DaysQF', 'HB_y', 'HBDateEnacted'])
cancer62dayfinal = merge2.drop(columns=['HBQF','CancerTypeQF', 'NumberOfEligibleReferrals62DayStandardQF', 'NumberOfEligibleReferralsTreatedWithin62DaysQF', 'HB_y', 'HBDateEnacted', 'HBDateArchived'])

#saving the final dataset as a csv
cancer31dayfinal.to_csv(r'data/cancer31day.csv')
cancer62dayfinal.to_csv(r'data/cancer62day.csv')
