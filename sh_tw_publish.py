from sh_prim import *
import random
import tweepy
from tweepy import OAuthHandler

consumer_key = '7KxQJO6XRfzS3yb0CM7JrV4lq'
consumer_secret = 'hufTlsIhQQVwxgtRXFNZqsjYlLFpeaSpCuNkxGRzalUy3tb4D8'
access_token = '346047803-XaHyBKp3NaNOfvThdn0TXYNpLO2JcwZod9RuqZtd'
access_secret = 'vemR6w9mjkuw0cUoiGNcanpxvjBIyKcD9ynIgt223EW8Z'

sh=random.choice(shlist)
link='http://aidecider.com/geekzone/'+sh[0].replace(' ','').lower()+'-vs-'+sh[1].replace(' ','').lower()
shmsg = '#' + sh[0].replace(' ','').replace('-','').replace('.','') +' has '+ sh[2]+ ' against #'+sh[1].replace('-','').replace('.','').replace(' ','') +' with '+ sh[3] +' chance to win '+link+' #whowouldwin #Superhero'

if len(shmsg)>140:
    shmsg = '#' + sh[0].replace(' ','').replace('-','').replace('.','') +' has '+ sh[2]+ ' vs #'+sh[1].replace('-','').replace('.','').replace(' ','') +' with '+ sh[3] +' chance win '+link+' #whowouldwin'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
api.update_status(shmsg)
