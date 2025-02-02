# post module

def send_post(client, username, post_text):
    post = client.send_post(post_text)
    
    print(post.uri)
    print(post.cid)
    print('\n')
    print(f'Post successful to {username} !')