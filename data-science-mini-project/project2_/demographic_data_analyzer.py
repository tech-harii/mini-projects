import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # 3. Percentage with Bachelors
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / len(df)) * 100, 1)

    # 4. Advanced education (Bachelors, Masters, Doctorate)
    higher_edu = df[
        (df['education'] == 'Bachelors') |
        (df['education'] == 'Masters') |
        (df['education'] == 'Doctorate')
    ]

    lower_edu = df[
        (df['education'] != 'Bachelors') &
        (df['education'] != 'Masters') &
        (df['education'] != 'Doctorate')
    ]

    # Rich people (>50K)
    higher_edu_rich = round(
        (len(higher_edu[higher_edu['salary'] == '>50K']) / len(higher_edu)) * 100,
        1
    )

    lower_edu_rich = round(
        (len(lower_edu[lower_edu['salary'] == '>50K']) / len(lower_edu)) * 100,
        1
    )

    # 5. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. People who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_min_workers = min_workers[min_workers['salary'] == '>50K']

    rich_percentage = round(
        (len(rich_min_workers) / len(min_workers)) * 100,
        1
    )

    # 7. Country with highest % of rich people
    countries = df['native-country'].unique()

    highest_earning_country = ""
    highest_percentage = 0

    for country in countries:
        country_df = df[df['native-country'] == country]
        rich = country_df[country_df['salary'] == '>50K']

        percentage = len(rich) / len(country_df)

        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_earning_country = country

    highest_earning_country_percentage = round(highest_percentage * 100, 1)

    # 8. Most popular occupation in India for >50K
    india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich %:", higher_edu_rich)
        print("Lower education rich %:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }