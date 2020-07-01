# The Game Is On

## Challenge prompt

```
We are given a url lets go to that
```
## **Solution**

We have a game ! First one to reach 100 wins.
Input the number of your choice, which is increemented to the total count. After a couple of tries it is quite evident that it is impossible to win the game. So we need to find a way out.

![The_Game_Is_On](https://github.com/ajaysram/hackoff/blob/master/The_Game_Is_On/img/TheGameIsOn1.png)


Lets inspect the count. Open developer tools and select the 'Inspect Using Mouse' icon. On hovering over the count, we see that the count is used in an h1 html tag with an id='Count'.


Lets try modifying the html manually and set the content to some number, say 95.
![The_Game_Is_On](https://github.com/ajaysram/hackoff/blob/master/The_Game_Is_On/img/TheGameIsOn2.png)


We see the count modified to 95 in the game also. Add 5.
We get the flag.


![The_Game_Is_On](https://github.com/ajaysram/hackoff/blob/master/The_Game_Is_On/img/TheGameIsOn3.png)
 
 
## flag : hackoff{mission_passed!_respect+}
