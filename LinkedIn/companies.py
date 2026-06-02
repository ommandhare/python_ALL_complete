# import yfinance as yf

# company = yf.Ticker(".NS")

# info = company.info

# print(info['sector'])
# print(info['industry'])

import requests


headers = {
    "User-Agent": "Mozilla/5.0"
}


# =========================
# GET LABEL FROM ENTITY ID
# =========================

def get_entity_label(entityId):

    url = f"https://www.wikidata.org/wiki/Special:EntityData/{entityId}.json"

    response = requests.get(url, headers=headers)

    data = response.json()

    entity = data['entities'][entityId]

    try:
        return entity['labels']['en']['value']

    except:
        return entityId


# =========================
# SEARCH COMPANY
# =========================

company = "Google"

searchUrl = "https://www.wikidata.org/w/api.php"

searchParams = {
    "action": "wbsearchentities",
    "search": company,
    "language": "en",
    "format": "json"
}


response = requests.get(
    searchUrl,
    params=searchParams,
    headers=headers
)

searchData = response.json()

entityId = searchData['search'][0]['id']


# =========================
# GET FULL ENTITY
# =========================

entityUrl = f"https://www.wikidata.org/wiki/Special:EntityData/{entityId}.json"

response = requests.get(
    entityUrl,
    headers=headers
)

data = response.json()

companyData = data['entities'][entityId]


# =========================
# BASIC INFO
# =========================

print("\n===== BASIC INFO =====")

name = companyData['labels']['en']['value']

description = companyData['descriptions']['en']['value']

print("Name :", name)

print("Description :", description)


claims = companyData.get('claims', {})


# =========================
# EMPLOYEES
# =========================

print("\n===== EMPLOYEES =====")

if 'P1128' in claims:

    try:

        emp = claims['P1128'][0]

        empCount = emp['mainsnak']['datavalue']['value']['amount']

        print("Employees :", empCount)

    except:

        print("Employees Not Found")


# =========================
# FOUNDERS
# =========================

print("\n===== FOUNDERS =====")

if 'P112' in claims:

    try:

        founders = claims['P112']

        for founder in founders:

            founderId = founder['mainsnak']['datavalue']['value']['id']

            founderName = get_entity_label(founderId)

            print(founderName)

    except:

        print("Founder Not Found")


# =========================
# INDUSTRIES
# =========================

print("\n===== INDUSTRIES =====")

if 'P452' in claims:

    try:

        industries = claims['P452']

        for industry in industries:

            industryId = industry['mainsnak']['datavalue']['value']['id']

            industryName = get_entity_label(industryId)

            print(industryName)

    except:

        print("Industry Not Found")


# =========================
# WEBSITE
# =========================

print("\n===== WEBSITE =====")

if 'P856' in claims:

    try:

        website = claims['P856'][0]

        websiteUrl = website['mainsnak']['datavalue']['value']

        print(websiteUrl)

    except:

        print("Website Not Found")