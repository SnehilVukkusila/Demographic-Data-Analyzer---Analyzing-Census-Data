import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read in the data from the CSV file
  data = pd.read_csv('census_data.csv')

  # How many people of each race are represented in this dataset?
  race_counts = data['race'].value_counts()

  # What is the avege age of men?
  average_age_men = data[data['sex'] == 'Male']['age'].mean()

  # What is the percentage of people who have a Bachelor's degree?
  bachelors_count = len(data[data['education'] == 'Bachelors'])
  total_count = len(data)
  percentage_bachelors = (bachelors_count / total_count) * 100

  # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
  higher_education = data[data['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate'])]
  higher_education_rich = len(
    higher_education[higher_education['salary'] == '>50K'])
  percentage_higher_education_rich = (higher_education_rich /
                                      len(higher_education)) * 100

  # What percentage of people without advanced education make more than 50K?
  lower_education = data[~data['education'].
                         isin(['Bachelors', 'Masters', 'Doctorate'])]
  lower_education_rich = len(
    lower_education[lower_education['salary'] == '>50K'])
  percentage_lower_education_rich = (lower_education_rich /
                                     len(lower_education)) * 100

  # What is the minimum number of hours a person works per week?
  min_work_hours = data['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
  num_min_workers = len(data[data['hours-per-week'] == min_work_hours])
  rich_percentage = len(data[(data['hours-per-week'] == min_work_hours)
                             & (data['salary'] == '>50K')]) / num_min_workers

  # What country has the highest percentage of people that earn >50K and what is that percentage?
  highest_earning_country = (
    data[data['salary'] == '>50K']['native-country'].value_counts() /
    data['native-country'].value_counts()).idxmax()
  highest_earning_country_percentage = (
    data[data['salary'] == '>50K']['native-country'].value_counts() /
    data['native-country'].value_counts()).max() * 100

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = data[(data['salary'] == '>50K') & (
    data['native-country'] == 'India')]['occupation'].value_counts().idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }