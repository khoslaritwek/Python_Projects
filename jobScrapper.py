##################################################################################################################
# Description : Automation script for Searching your desired Jobs                                                #
# Author :      Ritwek Khosla                                                                                    #
# Dependencies : bs4, requests                                                                                   #                          
#                                                                                                                #
##################################################################################################################


import requests
from bs4 import BeautifulSoup
# A function to parse url from different
# job Portals
def SearchJobsForMe(location, position):
    portals = ['naukri', 'linkedin']
    searchReport = ""

    for portal in portals:
        print ( UrlPassesr(location, position, portal) )





    
def UrlPassesr(location, position, portal):
    if portal == 'naukri':
        return "https://www.naukri.com/" + position + "-jobs-in-" + location + "?k=" + position + "&l=" + location
    elif portal == 'linkedin':
        return "https://www.linkedin.com/jobs/search?keywords=" + position + "&location=" + location + "&trk=homepage-jobseeker_jobs-search-bar_search-submit&currentJobId=2011219488&position=2&pageNum=0"



def main():
    print ("Hi User this your Personal job  Assisant \nAnswer the following questions and we are good to go")
    location = input('Your Preffered job location:')
    position = input('What position are you searching for:')
    Report  = SearchJobsForMe(location, position)

    

main()
