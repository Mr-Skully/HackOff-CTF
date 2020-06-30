# Rotten_User

## Challenge prompt
```
There are 13 admins, become one http://ec2-15-206-70-213.ap-south-1.compute.amazonaws.com/web-ctf/rotten_user/rotten.html

Note : Prompt was changed to give some more hints upon request from participants
```
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Rotten_User/img/rottenUser.png)

## **Solution**
```
The prompt says some thing about 13 admins , let move on
```

```
Hmm..., lets test with a random text

Just type admin and see what happens ?
```

![pharenth](https://github.com/ajaysram/hackoff/blob/master/Rotten_User/img/rottenUserInput.png)

```
As expected , it won't give the flag.Let's see if there is any cookie ?
```
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Rotten_User/img/rottenUserInput1.png)

```
Well there is one saying "nimda" (reverse of admin) and the cookie name is wierd !
Lets decode the cookie name to get some info 
```
```
Base64 decoded value : hey_why_are_you_decoding_me_?

Well thats a fact right ?
```

```
What if we type nimda ? Will it give the flag?

There is no flag but the cookies have changed to "avzqn"
```
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Rotten_User/img/rottenUserInput2.png)

```
Hmm intresting....Lets give another input abcde
```

### Woah.... Did you see what happened ?

| Input  | Cookie value|
| ------ | ---------------|
|admin   | nimda|
|nimda   | avzqn|
|abcde   | nopqr |

```
The letters have a shift of 13 !
```
## Now when we put up all together
- ```Challenge prompt : saying something about 13 admins```
- ``` Input is converted to a cookie with a shift of 13 alpbet ```

```
This can only lead to one solution:

Input is rot13 encoded and evaluated. 

So our input must be rot13 encoded form of "admin", which is "nvqza"

And this gives out flag :D
```
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Rotten_User/img/rottenUserFlag.png)

## flag : hackoff{rott3n_c00kies_for_my_@dmin}