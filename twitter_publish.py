from prim_publish import *
import random
import tweepy
from tweepy import OAuthHandler

consumer_key = '7KxQJO6XRfzS3yb0CM7JrV4lq'
consumer_secret = 'hufTlsIhQQVwxgtRXFNZqsjYlLFpeaSpCuNkxGRzalUy3tb4D8'
access_token = '346047803-XaHyBKp3NaNOfvThdn0TXYNpLO2JcwZod9RuqZtd'
access_secret = 'vemR6w9mjkuw0cUoiGNcanpxvjBIyKcD9ynIgt223EW8Z'

r=random.choice(r_list)
if '/relocation/it-' in r:
    rmsg='Check #decision map for #relocation from '+r.replace('http://aidecider.com/relocation/it-from-','#').replace('.html','').replace('-to-',' to #').title()+' for #IT #softwaredeveloper specialist #decisionmaker '+r.replace('.html', '')
else:
    rmsg='Check #decision map for #relocation from '+r.replace('http://aidecider.com/relocation/from-','#').replace('.html','').replace('-to-',' to #').title()+' #decisionmaker #decider '+r.replace('.html', '')

n=random.choice(n_list)
nmsg = 'Pick #baby #name between ' + n.replace('http://aidecider.com/name/', '#').replace(
    '.html', '').replace('-vs-', ' vs #').title() + ' #decider #decision ' + n.replace('.html', '')

j=random.choice(j_list)
jmsg = 'Check result for #newjob #decision between ' + j.replace('http://aidecider.com/job/', '#').replace(
    '.html', '').replace('-vs-', ' and #').title() + ' #decider ' + j.replace('.html', '')

u=random.choice(u_list)
umsg = 'Check who would win #UFC ' + u.replace('http://aidecider.com/sport/ufc/ufc-', '#').replace(
    '.html', '').replace('-vs-', ' vs #').title() + ' #whowouldwin #decision ' + u.replace('.html', '')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
api.update_status(rmsg)
api.update_status(nmsg)
api.update_status(jmsg)
api.update_status(umsg)
