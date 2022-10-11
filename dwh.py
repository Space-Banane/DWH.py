
import requests
class Send():
 """
 Send Things with a Webhook
 """
 def content(url,username,content,avatarurl=None):
    """Send an message with a Discord-Webhook
 
    Args:
        url (_type_): _description_
        username (_type_): _description_
        content (_type_): _description_
        avatarurl (_type_, optional): _description_. Defaults to None.
 
    Returns:
        _type_: _description_
    """
    if avatarurl:
        json = {'content': content,"username" : username}
    else:
        json = {'content': content,"username" : username,"avatar_url":avatarurl}
    x = requests.post(url, json = json)
    return x
 def embed(url,title,description,username=None,avatarurl=None,footer=None):
    """Send an embed with a Discord-Webhook
 
    Args:
        url (_type_): _description_
        title (_type_): _description_
        description (_type_): _description_
        username (_type_): _description_
        avatarurl (_type_, optional): _description_. Defaults to None.
        footer (_type_, optional): _description_. Defaults to None.
    """
    if avatarurl:
        json = {"username" : username}
    else:
        json = {"username" : username,"avatar_url":avatarurl}
    json = {
  "username": username,
  "avatar_url": avatarurl,
  "content": "",
  "embeds": [
    {
      "author": {
        "name": username,
        "icon_url": avatarurl
      },
      "title": title,
      "description": description
      }]}
    #print(json)
    x = requests.post(url, json = json)
    #print(x)
    return x
