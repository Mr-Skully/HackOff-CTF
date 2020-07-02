# JustRunIt (100pts)
#### Author: [Bichu](https://github.com/ben-jnr)
## Challenge
https://mega.nz/folder/nmJUwCBJ#1MHLGcs85JouX4egn5HxbQ## 
## Solution

First let's find out the type of file provided to us.
Using `file <file>` command we find out that the file is a *64 bit ELF*.
We convert it into an executable(linux) using `chmod` and run the program.
You will get the flag.

```bash
file JustRunIt
chmod +x JustRunIt
./JustRunIt
```

If you are using Windows, running the **exe** file may cause the shell to appear and disapper, giving us no time to read.
If so, open the Command Prompt and run the **exe** using the command:

```powershell
.\JustRunIt.exe
```

![JustRunIt](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/JustRunIt/img/JustRunIt.png)

### flag : hackoff{3x3cutabl3s}

## Safety Tip :
 Please take care while running executables on your daily-use system. Please use a virtual environment to run an unknown executable file.
