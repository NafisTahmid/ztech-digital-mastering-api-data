from requests import get
letters = 'abcd'
pages = {}
for letter in letters:
    page_url = f"https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages"
    res = get(page_url)
    data = res.json()
    pages[letter] = data.get('page_count')
    print(f"{letter} is scraped")
print(pages)