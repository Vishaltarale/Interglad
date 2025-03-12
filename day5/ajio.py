import requests
import os
import csv
import logging

logging.basicConfig(
    filename="logger.log",
    filemode="a+",
    format='%(asctime)s %(message)s',
)


headers = {
    "Host": "www.ajio.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Alt-Used": "www.ajio.com",
    "Connection": "keep-alive",
    "Cookie": "bm_ss=ab8e18ef4e; bm_s=YAAQ3ZfmZ68AvFmVAQAA/Jf3fgOGq1NL288lfLqYF7VDSf7lHynGLwNHBx48G5UsxP/zAnqHuwtikqj6I0cCsLT+WbG8PWLddM9785QeyaTdnvjtGK5ufgRUCfDLUV8g/HjUNP1zOquVMhoYjoeo1P892/EQRGerrbSny9j89YwETCo3lWrvotGt28r1YXHkXgzI/34oZYAlDqUGgvZwVgNOuszLIWSpMU4yAZ3Hvue90K5XXM9RH1zjrnnC3htWRegcJm5rRg1xKpM5fIez54E9PVXdgKhYIGuC0goPAi23VVvknTwAh9GX7xdtEfwOZYEMtP5ENMzZ5tJs4Bo/M1BoJxwiUu3Vmxy3fI9WkGK8xBHFW4oqn8bHbuQ0BujoLOjzC6+BfQ8x6EIxlGVZtjFhua3cCjtLH9k2tGl67COe3Vhoq8YCrFCa77MTZbISe/OufF+t9yNts=; V=201; TS01de1f4a=01ef61aed01f41cf51aca91fc80066339f8defe4b958785bbadd010cf69a795032aa4decfe213b2a91af76a8ab4307ff0d3d388de23bf02a917c9881e2e74acc3eb3d85dcb1da9379ac296eb49c0654abb833df2f970cbbf24aa59c90e31496ef8b11b9c86; TS01ac9890=01ef61aed0594ad3fe99a91e99cece069c1f5cb2ae58785bbadd010cf69a795032aa4decfee31980630ffff4d66e68c26d1183e871",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "TE": "trailers"
}

try:

     product_urls=[]
     with open("url.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # if not empty
                    product_urls.append(row[0].strip())  # searches for the blank characater in the url
                    
                    get_code = lambda x : x.split("/")[-1]

                    product_code_list = [get_code(x) for x in product_urls] 
                    
                    logging.debug("url load successfully:")
                    

     for product_code in product_code_list:
        API_URL = f"https://www.ajio.com/api/p/{product_code}"

        res = requests.get(API_URL, headers=headers)
        product_details = res.json()
            
    

        output=(f"""
        Product Name: {product_details['baseOptions'][0]['options'][0]['modelImage']['altText']}
        Product Stock: {'Available' if product_details['baseOptions'][0]['options'][0]['stock']['stockLevelStatus'] == 'inStock' else 'Out of Stock'}
        Quantity in stock: {product_details['baseOptions'][0]['options'][0]['stock']['stockLevel']}
        Current Price: {product_details['baseOptions'][0]['options'][0]['priceData']['value']}
        Best Promos: {[{x['code']:x['maxSavingPrice']} for x in product_details['potentialPromotions']][:3]}
        """
        )

        fp=open("final.txt","a+")
        fp.write(f"{output}")
        
        logging.warning(f"Data added succesfully :{output}")
        
except requests.exceptions.ConnectionError:
    print("coonection error please connect to internet")
except KeyError:
    print("please give proper Keyword")
except ValueError:
    print("something went wrong in while fwtching value ")

finally:
    fp.close()
    
    