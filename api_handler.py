import urllib2

class ApiHandler:
    KEY = "4e4bfc034a0852b27922205222070521"
    URL = "http://apps.titsa.com/apps/apps_sae_llegadas_parada.asp?idParada="
    URL2 = "&idApp=" + KEY

    @staticmethod
    def new_request(id):
        url_final = ApiHandler.URL + str(id) + ApiHandler.URL2

        req = urllib2.Request(url_final)
        response = urllib2.urlopen(req).read()
        print response