# Anche Tu Brutale (100pts)

## Challenge prompt
```
Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him. The evil that men do lives after them; The good is oft interred with their bones; And crack away...!!!
```
## Short into
```
From the prompt, we get the a part from the play Julius Ceaser.

For the beginners, Julius ceser created one of the oldest text encoding method that laid foundation to modern cryptography.
Ceaser cipher questions are set in almost every ctf challenges
```

## Ceaser Cipher
```
Ceaser cipher is nothing but shifting of letter with a predefiend shift value.We just move the alphabets position with a constant shift value, thats all.

Example:
Our message : abc

On applying ceaser cipher with a shift of +1

Our message now : bcd


before: abc
after : bcd
```


## **Solution**

```
1. Download the text

This one is a classic ceaser cipher problem.
We know that flag starts with 'h', so our shift value will be : position_of(u)-position(h)

Or just brute force , its that simple, only 26 iteration are required... :D
 
 At shift value of 13, we get the flag
```

## flag : hackoff{caesar_1oved_thirteen}