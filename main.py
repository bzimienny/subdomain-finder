import sys
import requests
import threading
def dns_scan(dns, dictionary, first, last):
    first = int(first)
    
    last = int(last)
    dictionary = dictionary[first:last]
    for subdomain in dictionary:
        subdomain = subdomain.rstrip('\n')
        address = f"{subdomain}.{dns}" 
        try: 
            r = requests.get(f'https://{address}')
            if r.status_code == 200:
                print(address)
        except:
            None
def dictionary_dns_scan(dictionary,dns):
    dictionary = open(dictionary,'r')
    dictionary = dictionary.readlines()
    length = len(dictionary)
    dictionary0 = length/4 - 1
    dictionary1 = dictionary0 + length
    dictionary2 = dictionary1 + length
    dictionary3 = dictionary2 + length
    t1 = threading.Thread(target=dns_scan,args=(dns, dictionary, 0, dictionary0))
    t2 = threading.Thread(target=dns_scan,args=(dns, dictionary, dictionary0, dictionary1))
    t3 = threading.Thread(target=dns_scan,args=(dns, dictionary, dictionary1, dictionary2))
    t4 = threading.Thread(target=dns_scan,args=(dns, dictionary, dictionary2, dictionary3))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

def main(arg0, arg1):
    if arg0 == '-d':
        dictionary_dns_scan(arg1, arg2)

if __name__ == '__main__':
    arg0 = str(sys.argv[1])
    arg1 = str(sys.argv[2])
    arg2 = str(sys.argv[3])
    main(arg0, arg1)