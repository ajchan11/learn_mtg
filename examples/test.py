import sys
sys.path.append("/Users/Alex/Desktop/learn/tweepy/build/lib/tweepy")
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
ckey="zHGMjGH6yYLQeoYjBlaEQymJ6"
csecret="hgwb5tCDoUnQ4ymbXKXZvjObJRCxS3Qc0Q0TwlKxJQnlxITKL6"

# After the step above, you will be redirected to your app"s page.
# Create an access token under the the "Your access token" section
atoken="3468205034-uniumGpwoPlXmT6q8ItSjxgPZVBVXLTvNyQf1xp"
asecret="886WPbZOfiV253d7UEGqRIeAr3ln1hoi0RAX06mXz0khB"


class listener(StreamListener):
  def on_data(self, data):
    try:
      print(data)
      saveFile = open("twitDB.csv", "a")
      saveFile.write(data)
    #   saveFile.write("n\")
      saveFile.close()
      return True
    except BaseException as e:
      print("failed ondata, ",str(e))
      time.sleep(5)

  def on_error(self, status):
    print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["mtgfinance", "magicthegathering", "ptahk", "tcgplayer", "edh", "mtgbuysell", "#ptakh", "#wotcstaff", "#mtg", "#mtgfinance", "#magicthegathering", "#magic", "#pack1pick1", "#CMDR", "#puzzlequest", "#genesis", "#lingeringsouls", "#cfb", "#channelfireball", "#cfbice", "#scg", "#pptq", "#ptq", "#jund", "#mtgmintcard", "#mtgo", "#modo", "#PTAmonkhet", "#mtgbentcard", "#mtgakh", "#dexarmy", "#ligamagic", "#dexthird", "#commander"])