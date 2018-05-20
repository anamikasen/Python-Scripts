import time as t
from os import path


def createFile(dest):

    '''
    The script creates an html file at the passed in location,
    names file based on time of the day.
    '''
    date = t.localtime(t.time())
    #File name should be Month_Day_Year.txt
    name = '%d_%d_%d.html'%(date[1], date[2], (date[0]%100))

    #if not(path.isfile(dest+name)):
    f = open(dest+name, 'w')
    f.write('<h1>Welcome to a script generated HTML     file</h1>')
    f.close()

if __name__=='__main__':
    # insert the location where you want the file to be
    destination = '//home//anamika//PycharmProjects//firstScript//'
    createFile(destination)
    raw_input("Done!")