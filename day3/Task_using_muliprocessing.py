import multiprocessing
import time
import threading
import pandas as pd
import requests

def NewsData(mainurl):
    url = mainurl

    res = requests.get(url)
    data = res.json()

    for i in data['data']:
        category=i.get("category","N/A")
        fetched_category=category
        
        category_vice_news=f"https://api.mediastack.com/v1/news?access_key=7bdb00756023273b97357db0606dc362&limit=10&category={fetched_category}"   #2nd API
        res2=requests.get(category_vice_news).json()
        

        result=[
                {
                'category':i.get("category","N/A"),
                'author':i.get("author","N/A"),
                'country':i.get("country","N/A"),
                'description':i.get("description","N/A"),
                'published_at':i.get("published_at","N/A")
            }
                for i in res2['data']
            ]
        
        df = pd.DataFrame(result)
        print(df)
        break
    
    

url="https://api.mediastack.com/v1/news?access_key=7bdb00756023273b97357db0606dc362&limit=10"       #1st API


#without using Multithreding
start=time.perf_counter() 

NewsData(url)

end=time.perf_counter()
print("time required to complte the program execution is an",end - start)


#by using Multithreading
pstart=time.perf_counter() 

p1 = threading.Thread(target=NewsData, args=[url])
p1.start()
p1.join()

pend=time.perf_counter()
print("time required to complte the program execution with threading ",pend - pstart)