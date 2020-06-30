# Pharenth

## CHallenge prompt

```
We are given a url to visit
```
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Pharenth/img/pharenth.png)
## **Solution**

```
Well we need two password for Mr.Blue and Mr.Greeen. Below login button it says about MD5 encryption.
Intresting.....
```
Lets start by giving some default values.
As expected we don't get any flag.Lets dig deep ...

![pharenth](https://github.com/ajaysram/hackoff/blob/master/Pharenth/img/pharenthInput.png)
Looking at url it is a GET request.
```
How did i know it was a GET request ? Because my input is appended to the url ...

Okay now the GET request must be there for a reason ?

```
Lets see if there is any hint on source code ?
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Pharenth/img/pharenthHints.png)
```
At first glance there is nothing to be found, but look at the scroll bar , there are content below our source code
```

### Hidden Comments
![pharenth](https://github.com/ajaysram/hackoff/blob/master/Pharenth/img/pharenthSource.png)
```
There are some typo lets fix the type and look at the comments
```
- Passwords of Mr.Blue and Mr.Green are not same
- But their MD5 hashes are
- Systems checks only the hash

```
How can the hash of two different strings be same ?
```
What could this mean ?
```
Are we looking at some hash-collision attack ?
Or am I missing something ?
```
### Think different !

PHP is loosely built language. In php we do not explicitly define the data-type of the variable,

For example in c
```c
int num;  /*This is an integer data type variable*/

int charVariable; /*This is an character data type variable*/
```
But it is a feature in php that we do not need to specify the data-type of the variable.

Could this be it ?
```
Since can control the url , lets modify the url and try again
```
|Our url| Modified url|
|-------|--------------|
|``` http://url/check.php?str1=Blue&str2=Green```|``` http://url/check.phpcheck.php?str1[]=Blue&str2[]=Green ```


![pharenth](https://github.com/ajaysram/hackoff/blob/master/Pharenth/img/pharenthSolution.png)
## See what we did there ?
Insted of sending the strings as such, we are passing array as input !

## **How does that work ?**
```
We are passing an array as input right ; so php checks the data type of the array element.
```
### To sum up
- Both array elements are of string data type
- Both array elements are different

## ***and kids thats how I got flag***

## flag : hackoff{m0d3rN_pr0b13m5_r3Quir3_m0d3rN_s0lu7i0n5}