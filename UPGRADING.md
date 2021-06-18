# UPGRADING

This file documents the process of upgrading the application to a newer release. These instructions are important in order to help ensure a smooth upgrade and prevent data loss.

## General Upgrade Process

__IMPORTANT:__ Always take a backup of your current application directory before using `git pull` to donwload a new release.

These are the general instructions to upgrade your application to a new version, and should be followed _unless_ instructions for a specific version upgrade appear below:
1. Take a backup of your existing application directory.
2. Stop the running application with Ctrl+C.
3. Use `git pull` to download the latest release.
4. Run the following commands to perform any database changes included in the new release:

  `python3 manage.py makemigrations`  
  `python3 manage.py migrate`  

5. Start the application.
6. Enjoy!

## Upgrading to v1.1.0
__Note:__ This upgrade will delete all your existing fauna unless you follow the instructions below to migrate your data. If you have no fauna data or do not wish to save it then you can follow the general upgrade instructions above.
1. __DO NOT__ run `git pull` yet!
2. Stop the running application with Ctrl+C.
3. Run the following command to export your existing fauna data:

  `python3 manage.py dumpdata worlds.fauna -o fauna.json`  

4. Use a text editor to edit the `fauna.json` file and replace all occurrences of `worlds.fauna` with `fauna.fauna` and save the file.
5. Use `git pull` to download the latest release.
6. Run the following commands to perform any database changes included in the new release:

  `python3 manage.py makemigrations`  
  `python3 manage.py migrate`  

7. Run the following command to load your saved fauna data:

  `python3 manage.py loaddata fauna.json`  

8. Start the application.
9. Enjoy!
