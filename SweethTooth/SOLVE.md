# SweetTooth (100pts)
#### Author: [Ajay](https://github.com/ajaysram)

## Challege
http://ec2-15-206-70-213.ap-south-1.compute.amazonaws.com/web-ctf/SweetTooth/cookie.php  
(At the page we get an image saying something about a cookie monster)

## Solution

This challenge wants us to look into cookies. You could either use an extension, but the browser would do the work.

Just go to Developer Console and go to Storage tab. 

Inside cookies you could see some thing like this:

![SweethTooth](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/SweethTooth/img/SweetTooth.png)

It says `broser_Generated_junk`.    

*But whats a broser? lol, it was meant to take you off-course*

If you decode the string using base64, you get the flag.

Since I'm using Linux, I would do:
```bash
echo "aGFja29mZntjMDBraTM1X0ByM181dzMzN30K" | base64 -d
```
But any online decoders would work fine.

### flag : hackoff{c00ki35_@r3_5w337}

