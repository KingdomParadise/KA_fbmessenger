
import requests,json,re,emoji
 

import requests,json
def SERVER_MESSAGE(sender,message):
    url="http://99.79.146.226:5006/webhooks/rest/webhook"
    data = json.dumps({
        "sender": str(sender),
        "message":str(message)
    })                                                                
    data_received = requests.post(url, data=data,headers={"Content-Type":"application/json"})
    received_messages = json.dumps("  ".join([x['text'] for x in data_received.json()]).replace('\n',' '))
    print(received_messages) 
    def remove_emojis(data):
            emoj = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002500-\U00002BEF"  # chinese char
                u"\U00002702-\U000027B0"
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642" 
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"  
                u"\u3030"
                            "]+", re.UNICODE)
            return re.sub(emoj, '', data)
    if received_messages is not None:
        text = remove_emojis(received_messages).split(' ')
        text = [x for x in text if not str(x).startswith('\\')] 
        text = " ".join(text)  
        text = str(text).strip()
        print(text)
        return  text
    else:
        print("/"*50)
        print("-->> CHAT API is returning NONE. So BOT will not Reply.")
        print("/"*50)
        return None


 


if __name__ == "__main__":
    x=(SERVER_MESSAGE("123",str("hello")))
    print(x)