from twitter import TwitterHTTPError

def tweet(instance,content):
    post = "https://redd.it/{id} {title} #rkpop #kpop".format(id=content["id"],title=content["title"])
    try:
        instance.statuses.update(status=post)
    except TwitterHTTPError:
        pass
