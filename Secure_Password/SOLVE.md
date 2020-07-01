# Secure Password

## Challenge prompt
```
We are provided with a file
```

## **Solution**

I have downloaded the linux version,you may work with the windows one too.
So lets try to find out the type of the file.
We find that it is a 64 bit ELF.
Make it an executable.
Run the program. The program asks for a password, and as we can expect, a random password returns an error.
So lets try to find the strings present in the  program

Linux users can use the strings command. Windows users can try opening the file in some text editor like notepad.

![Secure_Password](https://github.com/ajaysram/hackoff/blob/master/Secure_Password/img/SecurePassword1.png)

'''
HoustonWeHaveAProblem
'''

This one text stands out from the rest

```
Lets run the program and put feed this as the password.
```

And we get the flag

![Secure_Password](https://github.com/ajaysram/hackoff/blob/master/Secure_Password/img/SecurePassword2.png)

## flag : hackoff{that's_n0t_s3cur3}
