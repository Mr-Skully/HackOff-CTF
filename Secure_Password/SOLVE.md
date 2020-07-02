# Secure Password (150pts)
#### Author: [Bichu](https://github.com/ben-jnr)
## Challenge
https://mega.nz/folder/7nIDCKZZ#YO_pr3XrCv0gWgRACbQjRQ  
`HINT: plain text`
## Solution

I have downloaded the Linux version. You may work with the Windows one too.
So let's try to find out the type of the file.
We find that it is a *64 bit ELF*.
Make it executable and run the program.  
The program asks for a password, and as we can expect, a random password returns an error.  
So let's try to find the strings present in the program.

Linux users can use the `strings` command. Windows users can try opening the file in some text editor like notepad.

![Secure_Password](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Secure_Password/img/SecurePassword1.png)  

This one text stands out from the rest
```
HoustonWeHaveAProblem
```
Lets run the program and feed this as the password.

And we get the flag!

![Secure_Password](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Secure_Password/img/SecurePassword2.png)

### flag : hackoff{that's_n0t_s3cur3}
