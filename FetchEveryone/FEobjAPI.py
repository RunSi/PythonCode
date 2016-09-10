# Simple Fetcheveryone API for Pythonistas
import requests
import base64


class objAPI:
    def __init__(self):
        self.user = "065f23c5acc4bc0b6a11ae7b733f7195"
        self.secret = "dc2ce4f8174acc7a54c901acd7bef40c"
        self.token = None
        self.tokenheaders ={'Accept': "application/json",
        'Authorization':"Basic "+base64.urlsafe_b64encode(self.user+":"+self.secret)}
 
    def loadToken(self):
        self.token = None
        
        # follows location redirects by default so that part of the php version is ignored
        r = requests.get("https://api.fetcheveryone.com/token.php",headers=self.tokenheaders)
        if r.status_code != requests.codes.ok:
            print 'Problem with request to',r.url,'status',r.status_code
            r.raise_for_status()
        try:
            self.token = r.json()
        except:
            pass
            
    def getResource(self, resourcedict):
        if self.token is None:
            print 'Call loadToken() before calling getResource()'
            return None
        headers={'Authorization':'Bearer '+self.token['access_token'],
                 'Content-type':'application/json'}
        r = requests.get("https://api.fetcheveryone.com/api.php",params=resourcedict,headers=headers)
        if r.status_code != requests.codes.ok:
            print 'Problem with request to',r.url,'status',r.status_code
            r.raise_for_status()
        try:
            json_results = r.json()
        except:
            json_results = None 

        return json_results
        
    def putResource(self, resourcedict, datadict ):
        headers={'Authorization':'Bearer '+self.token['access_token'],
                'Accept':'application/json'}

        r = requests.post('https://api.fetcheveryone.com/api.php',
            params=resourcedict,
            data=datadict,
            headers=headers)

        if r.status_code != requests.codes.ok:
            print 'Problem with request to',r.url,'status',r.status_code
            r.raise_for_status()
        try:
            json_results = r.json()
        except:
            json_results = None 

        return json_results                