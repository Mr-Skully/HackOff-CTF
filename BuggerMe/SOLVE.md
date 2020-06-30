# BuggerMe

## Challenge prompt
```
We are given an url. So a web challenge
```
## **Solution**
```
Since the name suggest BuggerMe, i think we have to debug the web app. So using developers tools and selecting debugger.We find that it is a react webapp.

Usually the code for main page will be in App.js .Lets look into that
```

Well there you go ! Just we have username and password in plain-text
```
username: admin
password: hopeyoudebuggedme 
```

## flag : hackoff{at_your_service_captain}