from data import read_data

from ages import get_all_ages, get_the_oldest_age, get_the_youngest_age
from cities import get_all_cities
from countries import get_all_countries
from emails import get_all_emails
from nats import get_all_nats
from phone_numbers import get_all_numbers
from pictures import get_all_pictures_url
from streets import get_all_streets


data = read_data('Data/randomusers.json')

def main():
    ages = get_all_ages(data)
    olest_age = get_the_oldest_age(ages)
    print(olest_age)

main()

# DRY - Don't Repeat Yourself