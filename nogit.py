import requests

cookies = {
    'JSESSIONID': '5F5D3973685E2FB5033DAC3AE78B5259',
    'JAVAFIXATION': 'yEFf8k4Fm0Tzpugqf0FFfRnrhaySFJ36',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://upbhulekh.gov.in/public/public_ror/Public_ROR.jsp',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://upbhulekh.gov.in',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=5F5D3973685E2FB5033DAC3AE78B5259; JAVAFIXATION=yEFf8k4Fm0Tzpugqf0FFfRnrhaySFJ36',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

data = 'kcn=450&act=sbksn&vcc=209519&fasli-code-value=999&fasli-name-value=^%^E0^%^A4^%^B5^%^E0^%^A4^%^B0^%^E0^%^A5^%^8D^%^E0^%^A4^%^A4^%^E0^%^A4^%^AE^%^E0^%^A4^%^BE^%^E0^%^A4^%^A8+^%^E0^%^A4^%^AB^%^E0^%^A4^%^B8^%^E0^%^A4^%^B2^%^E0^%^A5^%^80'

response = requests.post(
    'https://upbhulekh.gov.in/public/public_ror/action/public_action.jsp',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)



data = 'khata_number=2095190450000012&district_name=%E0%A4%B5%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%B8%E0%A5%80&district_code=197&tehsil_name=%E0%A4%B8%E0%A4%A6%E0%A4%B0&tehsil_code=00996&village_name=%E0%A4%85%E0%A4%B5%E0%A4%B2%E0%A5%87%E0%A4%B6%E0%A4%AA%E0%A5%81%E0%A4%B0&village_code=209519&pargana_name=+%28%E0%A4%A6%E0%A5%87%E0%A4%B9%E0%A4%BE%E0%A4%A4+%E0%A4%85%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%A4%29&pargana_code=00827&fasli_code=999&fasli_name=%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%A4%E0%A4%AE%E0%A4%BE%E0%A4%A8+%E0%A4%AB%E0%A4%B8%E0%A4%B2%E0%A5%80'
response = requests.post('https://upbhulekh.gov.in/public/public_ror/action/public_action.jsp',data=data,headers=headers)

print(response.status_code)
print(response.text)