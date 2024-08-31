pages = {'a': 3106, 'b': 2109, 'c': 3121, 'd': 1779}

with open("urls.txt", "w+") as file:
    for letter, total_pages in pages.items():
        for page_num in range(1, total_pages+1):
            url = f"https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages/{page_num}"
            file.write(url + '\n')