from sh_prim import *
import random
import tweepy
from tweepy import OAuthHandler

consumer_key = 'Nbn76SiWgEct6xD4lYSqC8BQn'
consumer_secret = '0YtodsAx90PvYoPM7ENZa70iGmyUjDkvjR8zgiEJNO1kmzmVSG'
access_token = '886288995436687360-OSRZmyVU50nSELJdUQN5CkE513HisgD'
access_secret = 'nMyS2aAKZH4yb76Ji9N3Pfog79BS5FVAYJMXBaHkYHrHy'

sh=random.choice(shlist)
link='http://aidecider.com/geekzone/'+sh[0].replace(' ','').lower()+'-vs-'+sh[1].replace(' ','').lower()
shmsg = '#' + sh[0].replace(' ','').replace('-','').replace('.','') +' has '+ sh[2]+ ' against #'+sh[1].replace('-','').replace('.','').replace(' ','') +' with '+ sh[3] +' chance to win '+link+' #whowouldwin #Superhero'

if len(shmsg)>140:
    shmsg = '#' + sh[0].replace(' ','').replace('-','').replace('.','') +' has '+ sh[2]+ ' vs #'+sh[1].replace('-','').replace('.','').replace(' ','') +' with '+ sh[3] +' chance win '+link+' #whowouldwin'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
api.update_status(shmsg)



