import requests

class ZomatoClient:
    "make zomato request easy"
    def GetRestaurantMenu(self, restaurantName):
        searchUrl = 'https://developers.zomato.com/api/v2.1/search'
        payload = {'entity_id':70 , 'entity_type':'city','q': restaurantName,'count':1}
        headers = {"User-agent": "curl/7.43.0",'accept':'application/json','user-key':'01e3829fc7efac8578c78ffb8398ecd6' }
        r = requests.get(searchUrl,params=payload, headers=headers)
        jsonResult = r.json()
        return jsonResult['restaurants'][0]['restaurant']['menu_url']

c = ZomatoClient()
print(c.GetRestaurantMenu('smart kitchen'))
