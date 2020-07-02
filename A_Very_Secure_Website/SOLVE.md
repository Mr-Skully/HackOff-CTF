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

We got a new domain name, `hack.ing`, from the SSL certificate.
But how do we use it? We only have the IP address of the website.

Just typing in 
### flag :
