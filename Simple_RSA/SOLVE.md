# Simple RSA (300pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge

`Okay, here's the deal. We caught the bad guy as he was tring to hide the flag, but he encrypted it, more or less.`  
`During our interrogation, we found out that he used RSA encryption to encryt the flag.`  
`Our forensic experts have uncovered some of the data he used to do it. Can you work out the rest?`  
```
n = 49143162609134800648101058228802135733371930439144541653038722439355672137401
e = 7
```
## Solution

Refer [RSA on Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example) for a simpler example, then come back here for a better understanding of the solution.

We are given `n`, which is the product of 2 prime numbers `p` and `q`. The core strength of the RSA encryption algorithm lies in the difficulty in factorizing very large numbers into large primes, but as this is for a beginner-level CTF, `p` and `q` are sufficiently small.

Use any tool to factorize `n`. In this write-up, I’ve used [FactorDB](https://factordb.com).  

![FactorDB](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Simple_RSA/screenshots/factordb.png)  

```
p = 192957463140203145916602490416933130981
q = 254683917426025207486315812040438442821
e = 7 (given)
```
Now, we have to calculate the values for phi, and then d.
```
Totient function, phi = (p-1)(q-1)
                      = 49143162609134800648101058228802135732924289058578313299635804136898300563600
```  

![d-formula](http://www.sciweavers.org/tex2img.php?eq=d%20%3D%20e%5E%7B-1%7D%5Cpmod%20%7Bphi%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)  

```
d = 21061355403914914563471882098058058171253266739390705699843916058670700241543
```

The encrypted text is base64 encoded. To perform operations on it, we need it in a numeric form. So we’ll decode it, and then convert it into an integer form. I used the `b64decode()` and `bytes_to_long()` functions in Python to do this.

After converting to long int,
```
ciphertext c = 22929265407137463694489600316472394032252578974348041493919741207353444122671
```
Now we have everything we need to decode the message.

Plaintext message, ![formula](http://www.sciweavers.org/tex2img.php?eq=m%20%3D%20c%5Ed%5Cpmod%20n&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Simply convert `m` back into text, and ta-da!

### flag : hackoff{crackab13}
