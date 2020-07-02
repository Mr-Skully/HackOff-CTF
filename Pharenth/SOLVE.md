# Pharenth (300pts)
#### Author: [Ajay](https://github.com/ajaysram)
## Challenge
http://ec2-15-206-70-213.ap-south-1.compute.amazonaws.com/web-ctf/Pharenth/check.php
`Hint: Get inside and get data ~ the_sis!`  

![pharenth](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Pharenth/img/pharenth.png)
## Solution
Well we need two passwords, for Mr. Blue and Mr. Green.  
Below login button it talks about MD5 encryption.
Interesting...

Lets start by giving some default values.
As expected we don't get any flag. Lets dig deep...

![pharenth](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Pharenth/img/pharenthInput.png)

Looking at the URL, it is a GET request.

How did i know it was a GET request? Because my input is appended to the URL.

Okay now the GET request must be there for a reason.

Lets see if there is any hint on source code ?

At first glance there is nothing to be found, but look at the scroll bar, there are content below our source code.

![pharenth](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Pharenth/img/pharenthHints.png)

Let's look at the comments (ignoring the typos):
```
- Passwords of Mr.Blue and Mr.Green are not same
- But their MD5 hashes are
- Systems checks only the hash
```
How can the hash of two different strings be same?

What could this mean?

Are we looking at some hash-collision attack?  
Or am I missing something?

**Think different!**

PHP is a loosely built language. In PHP, we do not explicitly define the data-type of the variable.

For example in C
```c
int num;  /*This is an integer data type variable*/

int charVariable; /*This is an character data type variable*/
```
But it is a feature in PHP that we do not need to specify the data-type of the variable.

Could this be it?

Since can control the url , lets modify the url and try again


|Our url| Modified url|
|-------|--------------|
|` http://url/check.php?str1=Blue&str2=Green`|` http://url/check.phpcheck.php?str1[]=Blue&str2[]=Green`|


![pharenth](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Pharenth/img/pharenthSolution.png)  

**See what we did there?**

Instead of sending the strings as such, we are passing array as input.

**How does that work?**

We are passing an array as input, right? So PHP checks the data type of the array element.

**To sum up:**
  * Both array elements are of string data type
  * Both array elements are different

***And kids, that's how I got flag***

### flag : hackoff{m0d3rN_pr0b13m5_r3Quir3_m0d3rN_s0lu7i0n5}
