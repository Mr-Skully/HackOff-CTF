# BuggerMe

## Challenge prompt
```
We are given a url. So a web challenge
```
## **Solution**

The url leads to a login page, which probably only lets admins to login.

![BuggerMe](https://github.com/ajaysram/hackoff/blob/master/BuggerMe/img/BuggerMe1.png)

```
Since the name suggest BuggerMe, maybe we have to debug the web app. So using developer tools and selecting debugger.We find that it is a react webapp.
Usually the code for main page will be in App.js .Lets look into that.
Scrolling down a bit we see this.
```
![BuggerMe](https://github.com/ajaysram/hackoff/blob/master/BuggerMe/img/BuggerMe2.png)

Well there you go ! This must be the username and password in plain-text
Entering the same in the login form, we get the flag.

## flag : hackoff{at_your_service_captain}
