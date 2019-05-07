# DS_CFD

## the project has different modules
 1. Distributed Database
 2. Distributed File System
 
 
## Distributed Database
### we use the structure master slave which we have a main master and other slaves
### in the master the users create users and there is a backup database to insert all the users that should be inserted in the slaves
### we have implemented backupdatabase program to check periodically all the slaves and insert the user in it
### we have to ensure that all databases are consistent as the user try to enter can log in from any slave 
### if a user tries to log in to database then he selects from slaves and if all slaves are dead then we select from master
### a lot of other things
