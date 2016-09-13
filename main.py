import requests
import json
import time

def meteor(username = "John.Smith@example.com", password = "123456", yournumber = "0850000000", recipientsnumber = "0850000000", message = "Hello World"):
    try:
        with requests.Session() as s:
            payload1 = {'username':username, 'password':password, 'submit':'Log in to myMeteor', 'gotoUrl':''}
            r1 = s.post('https://my.meteor.ie/login', data=payload1)
            payload2 = {'msisdn':yournumber}
            r2 = s.post('https://my.meteor.ie/rest/secure/brand/3/portalUser/authenticateMyMeteor?ts='+str(int(time.time())), data=payload2, cookies=r1.cookies)
            j1 = json.loads(r2.text)
            if j1[u'status'] == "Successful authentication":
                headers = {'content-type': 'application/json'}
                payload3 = json.dumps({"content":message[0:479],"recipients":["+353"+recipientsnumber[1:]]})
                r3 = s.post('https://my.meteor.ie/webtext/mobileNumbers/'+"+353"+yournumber[1:]+'/messages?ts='+str(int(time.time())), data=payload3, cookies=r2.cookies, headers=headers)
                j2 = json.loads(r3.text)
                return True
    except:
        return False