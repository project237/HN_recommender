"""
TASKS:
1 - Open a text file, save all of the page-1 titles for the previous day to that file
*2 - push the code after previous step into the git
*3 - Open a csv with a single field "title", do the same
*4 - List all the relevant metadata, create column on the csv
"""
import requests
from bs4 import BeautifulSoup
import string
from datetime import datetime
import os

def title_2_file_name(input_title):
    """
    :param input_title: scraped title string in raw form
    :return: a string with all punctuations removed and spaced turned into "_"
    """
    input_title = input_title.translate(str.maketrans('', '', string.punctuation))
    return input_title.translate(str.maketrans(" ", "_")) + ".txt"


if __name__ == '__main__':
    url = "https://news.ycombinator.com/"

    r = requests.get(url)

    out = None
    title_list = []

    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        titles = soup.find_all('a', {"class": "titlelink"})
        out = "Sucess!"


        # saving title into file
        # ->constructing file string
        now = datetime.now()
        today_string = date_time = now.strftime("%d%b%Y")
        title_string = "HN_titles-" + today_string + ".txt"

        # file ops
        file = open(title_string, "w")

        for i in range(len(titles)):
            file.write(titles[i].text + "\n")

        file.close()

    else:
        out = "Invalid quote response!"

    print(out)

"""
PATTERN - titles
    1 - <td align="right" valign="top" class="title"><span class="rank">2.</span></td>      <td valign="top" class="votelinks"><center><a id='up_29333217'href='vote?id=29333217&amp;how=up&amp;goto=news'><div class='votearrow' title='upvote'></div></a></center></td><td class="title"><a href="https://www.stevenbuccini.com/zillow-offers" class="titlelink">Zillow lost money because they weren't willing to lose money</a><span class="sitebit comhead"> (<a href="from?site=stevenbuccini.com"><span class="sitestr">stevenbuccini.com</span></a>)</span></td></tr><tr><td colspan="2"></td><td class="subtext">
        <span class="score" id="score_29333217">135 points</span> by <a href="user?id=mjmayank" class="hnuser">mjmayank</a> <span class="age" title="2021-11-24T18:19:08"><a href="item?id=29333217">3 hours ago</a></span> <span id="unv_29333217"></span> | <a href="hide?id=29333217&amp;goto=news">hide</a> | <a href="item?id=29333217">111&nbsp;comments</a>              </td></tr>
canditates:
    1 - <td align="right" valign="top" class="title">    
    2 - 
"""

