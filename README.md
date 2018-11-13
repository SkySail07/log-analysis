# Log Analysis Project

Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database.
 This reporting tool is a Python program using the psycopg2 module to connect to the database.


### Prerequisites

You'll need to download the following softwares.


* [Python3](https://www.python.org/downloads/release/python-371/) 
* [Vagrant](https://www.vagrantup.com/)
* [VM](https://www.virtualbox.org/)
* [Git](https://git-scm.com/)
* [The data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


### Installing Packages 


You'll need to install the following libraries using pip

```
pip3 install psycopg2
```

```
pip3 install pycodestyle
```



## Requirements

Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!
 **1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.**

Example:
```
    "Princess Shellfish Marries Prince Handsome" — 1201 views
    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
    "Political Scandal Ends In Political Scandal" — 553 views
```

**2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.**
Example:
```
    Ursula La Multa — 2304 views
    Rudolf von Treppenwitz — 1985 views
    Markoff Chaney — 1723 views
    Anonymous Contributor — 1023 views
```

**3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.**
Example:
```
    July 29, 2016 — 2.5% errors
```



### Startign up The VM

Navigate to the configurations file. From there you can type the following commands

```
vagrant up
```

```
vagrant ssh
```

## Frequently asked questions

### Q: I modified my database. Can I undo it?
If you'd like to revert the news database to its original form, you can do that by dropping each of the tables, then re-importing the data from the newsdata.sql file.

```
drop table log;
drop table articles;
drop table authors;
```
### psql: FATAL: database "news" does not exist or psql: could not connect to server: Connection refused?
— this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added

## Output result of this script

```
Most Popular Articles of all time?
         Candidate is jerk, alleges rival-338647 views
         Bears love berries, alleges bear-253801 views
         Bad things gone, say good people-170098 views
```

```
Most Popular Authors?
         Ursula La Multa-507594 views
         Rudolf von Treppenwitz-423457 views
         Anonymous Contributor-170098 views
         Markoff Chaney-84557 views

```

```
days more than 1% of requests lead to errors?

         July 17,2016 - 2.26% errors

```



## Authors

* **Tarek H** - *Initial work* - [Udacity](https://github.com/SkySail07)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

