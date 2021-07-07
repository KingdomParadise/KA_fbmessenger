
import requests,json,re,emoji
def SERVER_MESSAGE(chatid,message):
  
        url = "http://localhost:8000/"
        received_messages =  requests.post(url,data={'chatid':chatid,'message':message}).json()['message']
        if type(received_messages) is list:received_messages = " ".join(received_messages)
        # print(received_messages)
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
                u"\ufe0f"  # dingbats
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
            return '_'

 
if __name__ == "__main__":
    chatid= '0001'
    SERVER_MESSAGE(chatid,str("mashood@gmail.com is my email 40100 hello")) 

 