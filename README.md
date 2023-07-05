# LoginAPI-getUsersFunctions
This repository contains an API to handle login and 3 functions to get user details through 'companyId'.

The Login API is built using a switch case format.
Initially it was built using if-elif-else loops and if-else nested loops. But, to avoid confusion in reading the code and making it easier to execute the same, I decided to use the switch case format.
The previous versions of the login function are still there as comments. Feel free to check them out and I am eager to get your feedback on them as well as on the whole project.

The getUsers function was demanded to be a function that takes a companyId (a column name that is also a foreign key between the "company" and "user" tables), and returns a list with
the details of all the users added with that companyId.
I have created 3 variations of that function.

The first one returns a list that itself contains separate lists with the details of the users added with different companyIds.

The second one shows the companyId and companyName of available companies and take a valid companyId as input to return a list with the details of all the users added with that companyId.

The third one shows the companyId and companyName of available companies and take a valid companyId as input to return a list with the details including the companyName of all the users added with that companyId.


I hope you will like the project. I am extremely enthusiastic to get constructive feedback of you all.
