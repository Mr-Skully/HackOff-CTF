# Fast And  Furious (200pts)
#### Author: [Bichu](https://github.com/ben-jnr)
## Challenge
`
Everthing went by so fast... How can I slow things down?
`

## Solution

First let's find out the type of file provided to us.
Using `file <file>` command we find out that the file is a 64 bit ELF.
We convert it into an executable(linux) using chmod and run the program.

![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious1.png)

On running the executable, we find that first, we have to press **enter** and then before we can enter the password, we get an out of time message.
Lets now try the `strings` command:

After an initial recon with `strings` command, we come across the string `IBelieveICanFly`, which might be our password.

```
Press Enter and then type in your password as fast as you can..

Enter password:
Sorry, but you ran out of time...
```

Now how can we make the program accept the input?  
Lets look at the code using some disassembler. I'll be using IDA Pro for the same.

Opening the executable using ida pro we get the following window:

![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious2.png)

Notice how the each block of the program is split into different boxes, to help us understand the control flow.
Now, look at the last line of the first box 

```
jg	short loc_96D
```

From here, we see 2 paths. Either to the left box, which accepts the password and compares it to 'IBelieveICanFly' or the right block which shows the 'out of time' message. Currently execution moves to the right, and we must change it to the left.
We can set a breakpoint to the last line of the first box, which now turns red as shown above.

Now run the debugger and select the option which continues execution of the program till the next wait. The terminal now shows us the following:  

![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious3.png)

Press **enter** and return to the IDA window. Now again run the program till the next wait. We can see that the execution has now stopped at the last line of the first box. The very same point we had set the breakpoint.

![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious4.png)

Here we can see the 2 arrows pointing to the next boxes. But the right arrow seems to be blinking, which tells us that, the control will now move to the right to execute the next instruction. This has to be changed. We need to go left.

Look at the rightmost column in the window. We can see some alphabets assigned some values. 

```
ID	0
VIP	0
.
.
.
ZF	0
AF	0
PF	1
CF	0
```

These are the registers and one of these decides the control flow in our case. In our case it is the ZF(Zero Flag). Double click on the '0' and you will get an input field with the value:

```
0x0
```

Change it as follows:

![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious5.png)

This changes `XF` to 1.

Now we can see the left arrow blinking. We have successfully changed the control flow.
Run the program till the next wait and your terminal window will show the following.


![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious6.png)


Enter the password, press **enter**, return to IDA and again run the program till the next wait.


![Fast_And_Furious](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Fast_And_Furious/img/FastAndFurious7.png)

We got our flag.

## Alternate Solution
###### Submitted by [Emil](https://github.com/TheSkullCrushr)
Inspecting the executable file in a text-editor, we come across some pieces of code and the string `IBelieveICanFly`. This might be our password.  
The program seems to time out pretty fast. So typing in the password is not a viable option.

Let's try something else - input redirection.

Create a text file, `pass.txt`, with the following contents:
```
   
IBelieveICanFly  
   
```   
Notice that there are blank lines above and below the password. This is actually there to represent a *newline* character, as the program asks us to *hit enter* at the beginning.  
(The *newline* at the end is optional, just in case the program needs a final push to accept the password. It doesn't mess up the logic, anyway.)

Now let us use this file to supply the password to the program.

On the Linux terminal:
```bash
./FastAndFurious < pass.txt
```
On the Windows Powershell:
```powershell
Get-Content .\pass.txt | .\FastAndFurious.exe
```

If it doesn't work at the first try, run the command again. And presto - you get the flag.  
(Sometimes you'll need to run it twice due to discrepencies with writing to the input buffer).  
### flag : hackoff{fast3r_than_f3dx}
