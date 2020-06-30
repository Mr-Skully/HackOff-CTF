# The Game Is On

## Challenge prompt

```
We are given a url lets go to that
```
## **Solution**

We have a game ! First one to reach 100 wins

### Looking at source
```
Okay its just a counter game
```
The Catch
```
What ever value we choose , the script counter-acts so that computer can only win !!!
```
Think out of the box
```
How does the computer know the current value ? Is it stored in cookie ? An array ?

Or is it just taking value from the screen ?
```
What to do ?
```
The heading tag has an id Count , what if we modify that ? 
```

## Beating the game 

Using developers console let's go to the console tab

- ``` Set the the current value to 99 ```
    - ``` document.getElementById('Count').innerText = 99 ```
- ``` Press the (+) button ```

And there you go, the flag !

## flag : hackoff{mission_passed!_respect+}