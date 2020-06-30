# ClickMeNot (100pts)

## Challenge
```
The challenge requires us to click the blue button 2000 times.
You could do that manually or just use the browser
```
![ClickMeNot](https://github.com/ajaysram/hackoff-writeup/ClickMeNot/img/clickMeNot.png)
## **Solution**
```
1 .First we have to find either id or name related to the button using developer console 

You could get developer console in Firefox using shortcut : Cntrl+Shift+i

```
![GetId](https;//github.com/ajaysram/hackoff-writeup/ClickMeNot/img/getId.png)
```javascript
2. Now use console tab to automate the click event

for(i=0;i<=2000;i++)
{
    document.getElementById('btn').click()
}

//Here the click button displays the value 0 ,so i've taken an extra iteration to click 2000 times
```
```
3.Get the flag
```
![GetId](https;//github.com/ajaysram/hackoff-writeup/ClickMeNot/img/flag.png)


## flag : hackoff{cl1ck3r5_ar3_fUn_rig#7_?}