"""Let's break xfinity."""
import requests

fields = ["firstName", "lastName", "emailValidationInfo.contactEmail",
          "primaryEmail", "userName", "alternateEmail", "secretQuestion",
          "secretAnswer", "password", "passwordRetype"]
answ = ["first", "last", "random1%40gmail.com", "random1%40gmail.com", "", "",
        "What+is+your+favorite+movie%3F", "secret",
        "pa%24%24w0rd", "pa%24%24w0rd"]

craft = ""
for idx, item in enumerate(fields):
    craft = "{}{}={}&".format(craft, fields[idx], answ[idx])
craft = "{}{}{}".format(craft, "_eventId=", "submit")

compare = "firstName=first&lastName=last&emailValidationInfo.\
contactEmail=random1%40gmail.com&primaryEmail=random1%40gmail.com\
&userName=&alternateEmail=&secretQuestion=\
What+is+your+favorite+movie%3F&secretAnswer\
=secret&password=pa%24%24w0rd&passwordRetype=pa%24%24w0rd&_eventId=submit"

# print(craft == compare)
# print(craft)

# Host: idm.xfinity.com
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Referer: https://idm.xfinity.com/myaccount/create-uid?execution=e2s1
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 224
# DNT: 1
# Connection: keep-alive
# Cookie: SESSION=453471cd-2c16-4957-a89e-f2219353ca71; BIGipServerp_loginxf-wcdc-ipv4_443=2284148548.36895.0000; isAuth=0; BIGipServerp_loginxf-pdc-ipv4_443=859068228.36895.0000
# Upgrade-Insecure-Requests: 1
ol = requests.get("https://wifiondemand.xfinity.com/wod/#offerList")
print(ol.cookies)
print(ol.history)
print(ol.text)

offer = {"chosenCoupon": "null",
"chosenOfferId": "-1456637658",
"locale": "en",
"salesChannel": "CC"}

ol.post("https://wifiondemand.xfinity.com/wod/#offerList",
json=offer)
print(r.status_code, r.reason, r.headers, r.url)
print(r.text)


# ("https://wifiondemand.xfinity.com/wod/ecommerce/select-offer")

# https://wifiondemand.xfinity.com/wod/
# r = requests.post("https://idm.xfinity.com/myaccount/create-uid?execution=e2s1",
# params={'form data': craft})
#
# print(r.status_code, r.reason, r.headers, r.url)
# # print(r.text)
