from selenium import webdriver
import time,os,uuid,json,re,sched, timeit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random,time,getpass,csv
  
from api import SERVER_MESSAGE





chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
uindex=0


def BOT_THREAD_STARTER(driver,EMAILID,PASSWORD,your_id,minimum_contacts,max_wait_for_reply):
    global uindex
     
    try:
        print("Loading facebook.com ...")

        driver.get('https://web.facebook.com/')
        time.sleep(5)
        print("Starting Logging in Procees ...")

        driver.find_element_by_id('email').send_keys(EMAILID)
        driver.find_element_by_id('pass').send_keys(PASSWORD)
        time.sleep(3)
        driver.find_element_by_name('login').click()
        print("Logging in ...")
        time.sleep(15)

        from marketplace_contact_fetch import ContactFetcher

        # if os.path.exists(os.path.join(os.getcwd(),'fresh_fetched_contacts.txt')):pass
        # else: ContactFetcher(driver,int(your_id),int(minimum_contacts))
        ContactFetcher(driver,int(your_id),int(minimum_contacts))



        IDLIST = [] 
        with open('fresh_fetched_contacts.txt', 'r') as file:
            for line in file.readlines():
                IDLIST.append(str(line).strip())
                    
        MESSAGES_LOG=[ {"id":x,"sessional_len":0,"init_messgae_handler":0} for x in IDLIST]



        BOTINITTIME = int(time.time())
        total_received_messages = 0
        loop_counter=0





        while True:

            for index,TARGETCHATID in enumerate(IDLIST[:int(minimum_contacts)]):
                SESSIONAL_LEN = 0
                print("Opening Messenger ...")
                driver.get('https://web.facebook.com/messages/t/{}'.format(TARGETCHATID))
                print("Messenger Loaded ... ")
                time.sleep(20)
                HELLO_MESSAGE = "Hello. Is it still avaliable."

                def CHAT_CONTEXT_HANDLER(): 
                    try:
                        time_locker = time.time()

                        while True:   
                            print("** Refreshing Chat Inbox")
                            time.sleep(3)  
                            cclass="oo9gr5id"
                            mclass="ljqsnud1" 
                            body_soup = driver.find_element_by_tag_name("body")
                            soup = BeautifulSoup(str(body_soup.get_attribute("innerHTML")), 'lxml')
                            allmsgs = soup.select("div.ljqsnud1.g6srhlxm.odn2s2vf")
                            allmsgs = [[msg.select('div')[0].text,msg.select('div')[0].attrs['class']] for msg in allmsgs]
                            mymsgs = [x for x in allmsgs if mclass in x[-1]]
                            clientmsgs = [x for x in allmsgs if cclass in x[-1]]
                            hasclientreplied = True if mclass not in  allmsgs[-1][-1] else False
                            whosentlastmsg = ''
                            lastmsg_class = allmsgs[-1][-1]
                            if mclass in lastmsg_class :whosentlastmsg = "me"
                            elif mclass not in lastmsg_class:whosentlastmsg='client' 
                            

                            print("#"*20)
                            print(len(mymsgs))
                            print(len(clientmsgs))
                            print(whosentlastmsg)
                            print(hasclientreplied) 
                            print("-"*20)
                            print('//'*30)
                            print(mymsgs)
                            print(allmsgs)
                            print('//'*30)

                            
                            if 'bye' in mymsgs[-1][0].lower() or 'thanks' in mymsgs[-1][0].lower() or 'thank you' in mymsgs[-1][0].lower() or 'thank' in mymsgs[-1][0].lower():
                                print("Thanks / Bye is in message")
                                print(f"-->> Thanks / Bye is in message -- moving to next user")
                                break
                            else:
                                print("No Thanks / Bye")






                            if len(clientmsgs)==0 and  len(mymsgs)==1:
                                time.sleep(2)
                                print("Sending hello message")
                                textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                                try: 
                                    for char in str(HELLO_MESSAGE):
                                        textAreaElem.send_keys(str(char))
                                        time.sleep(0.05)
                                    time.sleep(2)
                                    time.sleep(2)
                                    sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
                                    sender.click() 
                                except:
                                    print("stale element reference")
                                    continue


                                


                            elif whosentlastmsg=='me' and len(clientmsgs)==0:
                                print("** No Wait")
                                break

                            elif whosentlastmsg=='me':
                                if time.time()-time_locker>int(max_wait_for_reply):
                                    print("timer completed")
                                    break
                                else:
                                    print("__waiting")
                                     

                            elif whosentlastmsg=='client':
                                lastmsgtext = allmsgs[-1][0]
                                
                                
                                mymsgs =  mymsgs[-1]
                                last_occurance = [index for index,msg in enumerate(allmsgs)  if msg[-1][0]==mclass]
                                if len(last_occurance)>1:last_occurance=last_occurance[-1]
                                elif len(last_occurance)==1:last_occurance=last_occurance[0]
                                elif len(last_occurance)==0:last_occurance=0
                                client_last_messages = allmsgs[last_occurance+1:]
                                required_client_message = client_last_messages[0][0]





                                if len(required_client_message)!=0:
                                    print(f"-->> API CALL for ( {required_client_message} )")
                                    msg = SERVER_MESSAGE(TARGETCHATID,str(required_client_message))
                                    if msg is not None:
                                        print(f"-->> API Response ( {msg} )")
                                        if str(msg).startswith('"') and str(msg).endswith('"'):
                                            msg = msg[1:-1] 
                                        textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                                        try:
                                            for x in msg:
                                                textAreaElem.send_keys(str(x))
                                                time.sleep(0.05)  
                                            textAreaElem.send_keys(Keys.RETURN) 
                                            time_locker = time.time() 
                                        except:
                                            print("stale element reference")
                                    else:
                                        print("-->> GOT NONE from API. So ignoring this BOT Reply")
                                else:
                                    print("-->> Typing ... ")


                            else:print("no condition meet")
                                    



                            
                            print("#"*20)  
                    except Exception as e:
                        print(e)
                        print(e.__traceback__.tb_lineno)

                CHAT_CONTEXT_HANDLER()
 
        
        return True
    except Exception as e:
        print("*"*50)
        print(e.__traceback__.tb_lineno)
        print(e)
        print("*"*50)
        return False            


