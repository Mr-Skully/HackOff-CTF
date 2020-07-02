# A Very Secure Website (250pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)

## Challenge
`We did most of the hard work for you, and have tracked down the website Dr. Evil used to hide the flag.`  

`But somehow the site seems suspiciously legit. Take a look, maybe you're better at this than us... `  

`HINT: The CA requires a domain name for signing it.`

[Challenge URL](https://15.206.70.213/)

## Solution
The site seems to be a regular PHP page.  
But why does a simple page, that doesn't accept any input or display any confidential data, use SSL?

Let's inspect the SSL certificate.

![ssl-cert](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/A_Very_Secure_Website/screenshots/cert.png)

We got a new domain name, `hack.ing`, from the SSL certificate.
But how do we use it?

Just typing in `hack.ing` in the address bar does not give any useful results, it just times out. The URL is not registered in any DNS server.

We have the IP address of the challenge website. How can ask for `https://hack.ing/`, but get served by the server with the challenge IP?

BurpSuite users can intercept the request, and modify the `Host` parameter so that it looks something like:
```
Host: hack.ing
```

There is also another method to achieve this, without using BurpSuite.

All computers use a kind of internal DNS, called a *hosts* file. A DNS query is only forwarded to a browser cache, or later on a DNS server, only after the computer checks the *hosts* file for any useful entries.

For Windows users, the *hosts* file is located at **C:\Windows\System32\Drivers\etc\hosts**.

In Linux, it is located at **/etc/hosts**.

**(Use EXTREME CAUTION while modifying system files)**

We can add the following line to the end of the *hosts* file:
```
15.206.70.213     hack.ing
```
Now type in `hack.ing` into the address bar of your browser, and ta-daa!  
You're redirected to a site with the flag.

### flag : hackoff{ssl_certificate5_d0_n0t_pr0ve_anything}
