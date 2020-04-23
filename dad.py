from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd
import urllib.request

class Dad(BotPlugin):
    """Tell Dad Jokes"""

    @botcmd
    def dad(self,msg,args):
        url='https://icanhazdadjoke.com/'
        page = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0','Accept': 'text/plain'})
        response = urllib.request.urlopen(page).read().decode('utf-8')
        return response
