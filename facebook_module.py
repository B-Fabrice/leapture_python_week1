# facebook module contains many fucntionalities as is shown below
import facebook

#print facebook graph url
graph = facebook.GraphAPI(access_token='access_token')

post = graph.get_object(id='post_id', fields='message')
print(post['message'])