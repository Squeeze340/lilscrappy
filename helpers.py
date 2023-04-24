import urllib

def inline(doc):
    return "data:text/html;charset=utf-8,{}".format(urllib.quote(doc))