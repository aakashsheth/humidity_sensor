import urllib
ip = urllib.urlopen('http://arlenburroughs.com/ip.php').read()
print ("------ Publishing Pi's IP to DB ------")
print ("Public IP: '"+ip+"'")

key = "this is such a secret password..."

url = 'http://arlenburroughs.com/extras/486/save_addr.php?key=';
url += key+'&addr='+ip
#print ("Update URL: "+url)
resp = urllib.urlopen(url).read()

print ("Response: "+resp)
