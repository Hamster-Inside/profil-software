Arkadiusz Budkowski

arkadiusz.budkowski.1990@gmail.com

796-070-128

How to use the script:

1) Type in console:
   * python script.py METHOD --login USERNAME_LOGIN --password USERNAME_PASSWORD

      where METHOD is one of those:
    
          a) print-all-accounts (can be used only by users with role = 'admin')
        
          b) print-oldest-account (can be used only by users with role = 'admin')
        
          c) group-by-age (can be used only by users with role = 'admin')
        
          d) print-children
        
          e) find-similar-children-by-age
        
          f) create_database (it just create database based on cleaned data from folder "data")

Example:

    python script.py create_database --login kcabrera@example.net --password 'gk2VM$qk@S'
    python script.py find-similar-children-by-age --login kcabrera@example.net --password 'gk2VM$qk@S'

Warning:

    windows shell sometimes don't accept special signs in password like "$" so to be safe close it in ''
    instead of: --password gk2VM$qk@S
    type: --password 'gk2VM$qk@S'
    like in the example

