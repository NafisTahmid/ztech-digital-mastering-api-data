from requests import get
letters = 'abcd'
pages = {}
for letter in letters:
    base_url=f"https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages"
    res = get(base_url)
    data = res.json()
    pages[letter] = data.get('page_count')
    print(f"{letter} is scraped")

print(pages)