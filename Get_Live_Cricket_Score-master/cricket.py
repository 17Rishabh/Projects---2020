#rishabh cse 65120902717 minor project for industrial training
import requests
from datetime import datetime
class ScoreGet:
    def __init__(self):
        self.url_get_all_matches = "http://cricapi.com/api/matches"
        self.url_get_score="http://cricapi.com/api/cricketScore"
        self.api_key = "jO5hpZWBE1OcuODQyLidgM8eVah1"
        self.unique_id = ""  # unique to every match
    def get_unique_id(self):
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0
        for i in resp_dict['matches']:
            if (i['team-1'] == "Victoria" or i['team-2'] == "New South Wales") and i['matchStarted']:
                todays_date = datetime.today().strftime('%Y-%m-%d')
                if todays_date == i['date'].split("T")[0]:
                    uid_found=1
                    self.unique_id=i['unique_id']
                    break
        if not uid_found:
            self.unique_id=-1

        send_data1=self.get_score(self.unique_id)
        return send_data1
    def get_score(self,unique_id):
        data1="" #stores the cricket match data
        if unique_id == -1:
            data1="No matches today"
        else:
            uri_params = {"apikey": self.api_key, "unique_id": self.unique_id}
            resp=requests.get(self.url_get_score,params=uri_params)
            data1_json=resp.json()
            try:
                data1="Here's the score : "+ "\n" + data1_json['stat'] +'\n' + data1_json['score']
            except KeyError as e:
               print(e)
        return data1



if __name__ == "__main__":
    obj_score=ScoreGet()
    whatsapp_msg =obj_score.get_unique_id()
    from twilio.rest import Client
    account_sid = 'ACaa5e0baf1b87a4f8925d02eba532458d'
    auth_token = '7f94fff22384f81a291669f2b3333022'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=whatsapp_msg, from_='whatsapp:+14155238886', to='whatsapp:+918700433343' )
