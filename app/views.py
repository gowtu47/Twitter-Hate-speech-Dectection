from django.shortcuts import render,redirect
from . models import*
import csv
from Predicting import run2
from django.contrib.auth.models import User,auth


def home_page(request):
    if request.method == "POST":
        t=request.POST.get("t")
        # Findtweet(t)
        answer=run2(t)
        print(answer)
        return render(request,'home.html',{'answer': answer})

        
    return render(request,'home.html')

def login_page(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        password1=request.POST["p_password"]
        u=auth.authenticate(username=uname,password=password1)
        if u is not None:
            auth.login(request,u)
            return redirect(home_page)
        else:
            return render(request,'login.html')
    return render(request,'login.html')




def output(request):
    a=[]
    with open("words.csv", 'r',encoding="utf-8") as csvFile1:
            reader1 = csv.reader(csvFile1)
            for x in reader1:
                for i in x:
                    a.append(i)
    
    print(a)
    if request.method == "POST":
        a.clear()
        with open("words.csv", 'r',encoding="utf-8") as csvFile1:
            reader1 = csv.reader(csvFile1)
            for x in reader1:
                for c in x:
                    answer=run2(c)
                    a.append([c,answer])
        return render(request,'output.html',{'a': a})
                    

    
    return render(request,'output.html',{'a': a})


def register_page(request):
    if request.method=="POST":
        uname=request.POST['uname']
        mail=request.POST['mail']
        p_password=request.POST['p_password']
        pp_password=request.POST['pp_password']
        if p_password==pp_password:
            if User.objects.filter(username=uname):
                print("USERNAME ALREADY TAKEN")
                return render(request,'register.html')
            elif User.objects.filter(email=mail):
                print("EMAIL ALREADY TAKEN")
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=uname,email=mail,password=p_password,)
                user.save()
                return redirect(login_page)
        else:
            
                

                print("password does not matching")

                return render(request,'register.html')
    else:
                
                return render(request,'register.html')

# Create your views here.


def Findtweet(t):
        import twitter
        import re
        import string
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        from nltk.tokenize import sent_tokenize

        stop_word = set(stopwords.words('English'))

        


        api = twitter.Api(consumer_key="EvQ4PSZ7hReiEefNRh7urwCAZ",
            consumer_secret="pHqO7c4CKrtRskdzxkI8QymAMMNTF8iu11ViIES0EzNJRhY8aO",
            access_token_key="1235812024371691521-VgJotURj8nMWKHMLCImcB7xNxvZ88X",
            access_token_secret="FGFjahEdNYOZkC4damdj2ZKrSE8gfbryMjQRnHLB8teAX")
        


        
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  
            u"\U0001F300-\U0001F5FF"  
            u"\U0001F680-\U0001F6FF"  
            u"\U0001F1E0-\U0001F1FF"
                            "]+", flags=re.UNICODE)

        search = api.GetSearch(t, count=2)

        f=[]
        for t in search:
            global word,clean_words

            # print(t)

            tweets=t.text

            tweets = re.sub(r"http\S+", "", tweets)

            tweets = tweets.replace("…","")

            tweets = tweets.strip()

            sentences = sent_tokenize(tweets.replace('\n',' '))

            clean_words = [word for word in sentences if word not in set(string.punctuation)]



            characters_to_remove = ["''",'``','...']


            clean_words = [word for word in clean_words if word not in set(characters_to_remove)]

            characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
            clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
            f.append(clean_words)
        with open("words.csv", 'w+',encoding="utf-8",newline="") as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(f)
            csvFile1.close()
