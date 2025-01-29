# post example bsky

import client
import post
import os
import app_config as config

    
    
def splash():
    os.system('cls' if os.name=='nt' else 'clear')
    print(config.BANNER)
    
    
def main():
    option = splash()
    conn = client.setup()
    os.system('cls' if os.name=='nt' else 'clear')
    option = splash()
        
    post_text = input('What\'s up ?\n\n')
    post.send_post(
        conn, 
        user.username,
        post_text
    )
    
    
if __name__ == '__main__':
    main()