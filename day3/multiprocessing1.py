import multiprocessing
import requests
import time


def download(url, name):        #started time 
        response = requests.get(url)
        open(f"D:/Interglad/day3/img/{name}.jpeg","wb").write(response.content)


time1=time.perf_counter()
url = "https://picsum.photos/2000/3000"
for i in range(10,16):
    download(url, i)
    

time2=time.perf_counter()   #End time 
print("without multiprocessor ",time2-time1)          #formula to calculate time required to execute


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    time3=time.perf_counter()
    for i in range(15,21):
        p1=multiprocessing.Process(target=download,args=(url, i))
        p1.start()
        p1.join()
      
        
    time4=time.perf_counter()   #End time 
    print("time required to complete execution using processor ",time4-time3)          #formula to calculate time required to execute