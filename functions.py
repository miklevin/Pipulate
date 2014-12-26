def Func1():
  return "Out from Function One"

def Func2(param1, param2='', status='Okay'):
  return "%s %s" % (param1, param2)

def tweets(url):
  import requests
  acount = 0
  api = "http://urls.api.twitter.com/1/urls/count.json?url="
  try:
    respobj = requests.get(api + url)
    # responses other than 200 are not considered exceptions, so:
    respobj.raise_for_status()
    adict = respobj.json()
    acount = adict["count"]
  except requests.exceptions.RequestException as e:
    acount = "error!"
    print("requests.exceptions.RequestException Error=%s"%e)
  except Exception as e:
    acount = "error!"
    # need a logger instead of: print("Error:\n%s"%e)
    print("Error=%s"%e)
  return acount

def plusses(url):
  import requests
  acount = 0
  api = "https://clients6.google.com/rpc"
  jobj = '''{
    "method":"pos.plusones.get",
    "id":"p",
    "params":{
        "nolog":true,
        "id":"%s",
        "source":"widget",
        "userId":"@viewer",
        "groupId":"@self"
        },
    "jsonrpc":"2.0",
    "key":"p",
    "apiVersion":"v1"
  }''' % (url)
  try:
    respobj = requests.post(api, jobj)
    respobj.raise_for_status()
    adict = respobj.json()
    acount = adict['result']['metadata']['globalCounts']['count']
  except requests.exceptions.RequestException as e:
    acount = "error!"
    print("requests.exceptions.RequestException Error=%s"%e)
  except Exception as e:
    acount = "error!"
    # need a logger instead of: print("Error:\n%s"%e)
    print("Error=%s"%e)
  return acount
