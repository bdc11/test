import requests, json

more = True 
i = 1 #counter and we initialize at 1 so we start at page 1
hd_true = 0
hd_false = 0

while more == True:
	#print i #use to check if script is working 
	new_url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=500&page=' + str(i) #define url and iterate it using type casting
	ebates = requests.get(new_url, headers={'User-Agent': 'Mozilla/5.0'}) #connect to ebates server
	result = json.loads(ebates.content) #decode json object into a readable python object
	more = result['more'] #first check to see if more = true then continue
	for keys in result['response']: #loop to iterate keys present in response dictionary
		flags = keys['flags'] #finds flag key values where hd is nested
		hd = flags['hd'] #finds hd key value 
		if hd == True: #loop checks if hd value is true 
			hd_true += 1 #if any hd = true, adds to hd_true
		else:
			hd_false += 1 #if any hd = true, adds to hd_false

	i += 1 # for every page where more = true, it will increment i and increases url page number until more = false


print hd_true
print hd_false