##################################################################################################################
# Description : Automation script for Searching your desired Jobs                                                #
# Author :      Ritwek Khosla                                                                                    #
# Dependencies : bs4, requests                                                                                   #                          
# Theme : Web Scrappoing                                                                                         #                    
##################################################################################################################


import requests
from bs4 import BeautifulSoup
import re
# A function to parse url from different
# job Portals
def SearchJobsForMe(location, position):
    portals = ['naukri', 'linkedin', 'monster', 'shine', 'timesJobs']
    searchReport = ""

    for portal in portals:
        link = UrlPassesr(location, position, portal)
        #print (link)
        source = requests.get(link).text
        try:
            searchReport = searchReport + (DataExtracted(portal, source))
        except:
            continue

    return searchReport




def DataExtracted(portal, source):
    ans  = "\n"

    if portal == 'timesJobs':
        ans = ans + 'Here are Jobs that fits the criteria from timesJobs:\n'
        soup = BeautifulSoup(source, 'lxml')
        jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
        for mem in jobs :
            title = mem.h2.a.text
            company = mem.h3.text
            experience = str (mem.ul.text)
            experience = re.sub('(card_travel)','', experience)
            experience = re.sub('(location_on)','Location:', experience)
            
            Description = mem.find_all('ul', class_ = 'list-job-dtl clearfix')
            Des = ""
            for member in Description:
                Des = Des + str(member.text)
            
            ans = ans + '\n+-----------------------------------------------------------------------------------------+\n'
            ans = ans + 'Company : ' + str(company) + '\n'
            ans = ans +  'Title : ' + str(title) 
            ans = ans +  'Experience required :' + experience + '\n'
            ans = ans + Des 
            


    return ans
                

    
def UrlPassesr(location, position, portal):
    if portal == 'naukri':
        return "https://www.naukri.com/" + position + "-jobs-in-" + location + "?k=" + position + "&l=" + location
    elif portal == 'linkedin':
        return "https://www.linkedin.com/jobs/search?keywords=" + position + "&location=" + location + "&trk=homepage-jobseeker_jobs-search-bar_search-submit&currentJobId=2011219488&position=2&pageNum=0"
    elif portal ==  'monster':
        return "https://www.monsterindia.com/srp/results?query=" + position + "&locations=" + location + "&searchId=e5c446eb-45c4-4cd1-a876-70e4253be7de"
    elif portal == 'shine':
        return "https://www.shine.com/job-search/" + position + "-jobs-in-" + location
    elif portal == 'timesJobs':
        return "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=" + position + "+&txtLocation=" + location
     


def main():
    print ("Hi User this your Personal job  Assisant \nAnswer the following questions and we are good to go")
    location = input('Your Preffered job location:')
    position = input('What position are you searching for:')
    Report  = SearchJobsForMe(location, position)
    print (Report)

    

main()
