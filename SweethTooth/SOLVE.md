# SweetTooth (100pts)

## Challege
```
At the page we get an image saying something about a cookie monster
```

## **Solution**

```
This challenge wants us to look into cookies.You could either use an extension, but the browser would do the work,

Just go to developers' console and go to storage tab 

Inside cookies you could see some thing like this

```
![SweethTooth](https://github.com/ajaysram/hackoff/blob/master/SweethTooth/img/SweetTooth.png)

It says broser_Generated_junk
```
But whats a broser ? lol, it was meant to take you off-course 

If you decode the sting using base64 you get the flag

Since i'm using linux, i would do

echo "aGFja29mZntjMDBraTM1X0ByM181dzMzN30K" | base64 -d

But any online decoders would work fine
```

## flag : hackoff{c00ki35_@r3_5w337}

