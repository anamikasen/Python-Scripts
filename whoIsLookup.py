import whois, io, json
from os import path



def whoIsLookup(dest, name):
    '''
        The script will return the whois lookup of a
        particular website.
    '''
    # f_name = name.split(".")[0]
    lookUp = whois.whois(name)
    # print(type(lookUp))
    # if not(path.isfile(dest+f_name)):
    #     with open(dest+f_name, 'w') as f:
    #         json.dump(lookUp, f, ensure_ascii=False)
     

    print(whois.whois(name))
    #print(name.split(".")[0])




if __name__=='__main__':
    destination = destination = '//home//anamika//PycharmProjects//firstScript//'
    url = raw_input("Enter a domain:")
    whoIsLookup(destination, url)