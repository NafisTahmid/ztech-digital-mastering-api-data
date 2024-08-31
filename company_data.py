from requests import get
import csv

url = "https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/entity/6645e6252eda850001b83591"
res = get(url)
data = res.json()
with open("new_file.txt", "r", encoding="utf-8") as file:
    urls = file.readlines()



with open('company_information.csv', "a+", newline='', encodings="utf-8") as csvfile:
    fieldnames = [
        'company_name',
        'logo',
        'website_url',
        'phone_number',
        'social_links_linkedin',
        'location'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for url in urls:
        company_data = {}
        res = get(url.strip())
        data = res.json()
        company_data['company_name'] = data.get("name")
        company_data['logo'] = data.get("logo_url")
        company_data['website_url'] = data.get("website_url")
        company_data['phone_number'] = data.get("phone_number")
        location_city = data.get("location").get("city")
        location_state = data.get("location").get("state")
        location_country = data.get("location").get("country")
        company_data['social_links_linkedin'] = data.get("social_links").get("linkedin_url")
        company_data['location'] = f"{location_city} {location_state} {location_country}"
        writer.writerow(company_data)