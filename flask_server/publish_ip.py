import urllib

#get's public ip address
#ip = urllib.urlopen('http://arlenburroughs.com/ip.php').read()

#get local IP address
import netifaces as ni
ni.ifaddresses("eth0")
ip = ni.ifaddresses("eth0")[2][0]["addr"]

print ("------ Publishing Pi's IP to DB ------")
print ("Public IP: '"+ip+"'")

key = "this is such a secret password..."

url = 'http://arlenburroughs.com/extras/486/save_addr.php?key=';
url += key+'&addr='+ip
#print ("Update URL: "+url)
resp = urllib.urlopen(url).read()

print ("Response: "+resp)
