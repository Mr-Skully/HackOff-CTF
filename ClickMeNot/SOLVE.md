# ClickMeNot (100pts)
#### Author: [Ajay](https://github.com/ajaysram)
## Challenge
http://ec2-15-206-70-213.ap-south-1.compute.amazonaws.com/web-ctf/clickMeNot/clickMeNot.html

![ClickMeNot](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/ClickMeNot/img/clickMeNot.png)
## Solution
  1. First we have to find either the **id** or **name** related to the button using Developer Console.  
  You could get developer console in Firefox using shortcut : Ctrl+Shift+I
![GetId](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/ClickMeNot/img/getID.png)

  2. Now use console tab to automate the click event:
```javascript
for(i=0;i<=2000;i++)
{
    document.getElementById('btn').click()
}

//Here the click button displays the value 0, so I've taken an extra iteration to click 2000 times
```
  3. Get the flag
![Flag](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/ClickMeNot/img/flag.png)


### flag : hackoff{cl1ck3r5_ar3_fUn_rig#7_?}
