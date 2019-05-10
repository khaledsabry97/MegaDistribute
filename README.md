# MegaDistribute

## the project has two modules
 1. Distributed Database
 2. Distributed File System
 
 
## Distributed Database
* we use the structure master slave which we have a main master and other slaves
* in the master the users create users and there is a backup database to insert all the users that should be inserted in the slaves
* we have implemented backupdatabase program to check periodically all the slaves and insert the user in it
* we have to ensure that all databases are consistent as the user try to enter can log in from any slave 
* if a user tries to log in to database then he selects from slaves and if all slaves are dead then we select from master
* a lot of other things




## Distributed File System
* we make a master tracker and data node keeper
* master tracker handle the connections between the client and data nodes to upload and download
* master tracker has database so can store where client files in which data nodes
* we make replications to three data nodes for each file and we make sure they are alive
* all and more than in the document requirement we have handle it
