import requests
fp = open('php.txt',"r")
url = "http://www.jjunet.cn"
fp_read=fp.readlines()
lens=len(fp_read)
for i in range(lens):
    get_par="/"+fp_read[i].strip()
    result=requests.get(url+get_par)
    if result.status_code==200:
        print(url+get_par)
    #print(result.text)