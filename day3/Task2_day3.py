import requests
import pandas as pd
import time 

time1=time.perf_counter() 
url = "https://api.mediastack.com/v1/news?access_key=d8c93ab0f06f0834bf46a72956264ba5&limit=10"

res = requests.get(url)
data = res.json()



for i in data['data']:
    category=i.get("category","N/A")
    fetched_category=category
    
    category_vice_news=f"https://api.mediastack.com/v1/news?access_key=d8c93ab0f06f0834bf46a72956264ba5&limit=10&category={fetched_category}"
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
time2=time.perf_counter()
print("time required to complte the program execution is an",time2-time1)   #time required to execute = 1.887585799999215
    
    
    

    

 