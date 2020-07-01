# JustRunIt

## Challenge
```
Here we have two options a Windows executable or Linux one,download the one you need. I will be using the Linux one

```
## **Solution**

First let's find out the type of file provided to us.
Using file <file> command we find out that the file is a 64 bit ELF.
We convert it into an executable(linux) using chmod and run the program.
You will get the flag.

```
file JustRunIt
chmod +x JustRunIt
./JustRunIt
```

If windows, running the exe file may cause the shell to appear and disapper, giving us no time to read.
If so open the window in your cmd and run the exe using the command

```
.\JustRunIt.exe
```

![JustRunIt](https://github.com/ajaysram/hackoff/blob/master/JustRunIt/img/JustRunIt.png)

## flag : hackoff{3x3cutabl3s}

# Safety Tip :
 Please take care while running executables on your daily system. Please use a virtual environment to run an unknown executable.
