from requests import get
with open("urls.txt", "r") as file:
    urls_list = file.readlines()

with open("new_file.txt","w+", encoding="utf-8") as file:
    for url in urls_list:
        res = get(url.strip())
        data = res.json()
        for company in data:
            company_id = company.get("id")
            company_url = f"https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/entity/{company_id}"
            print(company_url)
            file.write(company_url + "\n")
