import random
import uuid
from datetime import date, datetime

import requests
from faker import Faker

faker = Faker()
session = requests.Session()

firefox_version = random.randint(50, 90)
firefox_date = faker.date_between_dates(date_start=date(2008, 1, 1), date_end=datetime.now()).strftime("%Y%m%d")

r = session.post(
	url="https://www.microsoft.com/en-US/api/controls/contentinclude/html",
	params={
		"pageId": "6e2a1789-ef16-4f27-a296-74ef7ef5d96b",
		"host": "www.microsoft.com",
		"segments": "software-download,windows11",
		"query": "",
		"action": "getskuinformationbyproductedition",
		"sessionId": str(uuid.uuid4()).upper(),
		"productEditionId": "0",
		"sdVersion": "2",
	},
	headers={
		"Referer": "https://www.microsoft.com/software-download/windows11",
        "User-Agent": f"Mozilla/5.0 (X11; Linux i586; rv:{firefox_version}.0) Gecko/{firefox_date} Firefox/{firefox_version}.0",
	},
)
print(r, r.url)
print(r.text)