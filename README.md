# ETL-project

This project has been divided into two sections: 

	The ETL process
	
	Exploratory Data Analysis

1.	The ETL process

Extract: 

For this project data was retrieved from Kaggle. The dataset includes over 67,000 employee reviews for Google, Amazon, Facebook, Microsoft, Apple and Netflix. This dataset consists of 17 columns. The full description of the data features can be found in a separate file: employee_reviews.csv

Transform: 

Data was processed and cleaned with Pandas (Python library). The process of data transformation can be found in rating_analysis notebook. The full description of clean data can be found in separate file: reviews.csv

Load: 

MongoDB was selected to load the data because data can be stored in BSON format – key, value pair and its capable of holding arrays. The loading process and code can be found in LoadDB notebook.


2.	Exploratory Data Analysis

The statistical analysis was done to compare the ratings of 6 corporations: Facebook, Google, Apple, Amazon, Microsoft and Netflix. These companies are compared based on the overall ratings, career opportunities, work-life balance, management, culture values and benefits ratings from an employee's perspective. The details can be found in rating_analysis notebook.

Findings:

Overall ratings: Median is the biggest for Google and Facebook. In general, overall ratings are pretty good for these companies.

Career opportunities: Facebook appears to provide better career opportunities followed by Google, Amazon, Microsoft, Apple, Netflix. Facebook is the winner with the highest possible median(5/5). Other companies have values around 4 while Netflix and apple have the least median(3/5) values.

Work-life balance: Comparision of work life balance among these companies indicates medians are highest for Facebook and Google. Other companies have median one point less. Marks less than 2 to 3 is unusal for all companies except Amazon.

Culture values: Facebook, Google and Apple have the high median values than other companies, Facebook at the top as the bad marks noticed rarely.

Management: The senior management appears to be best in facebook with biggest median, followed by goggle.

Benefits ratings: Comparision of the benefits ratings indicates that all of these companies are good in providing benefits although facebook is having biggest median value.



