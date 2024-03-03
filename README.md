# pyigdiff

Python program to find the Following and Followers difference of an account.

The code assumes that you have downloaded your information as a zip file with all the files in json format.
The program looks for the json file `following.json` and `followers_1.json` in the archive. Parses them and finds the differences between them.

The script yields the usernames of those accounts that follows the user (but the user does not follow back) and those accounts that the user follows (but don't follow the user back).


```console
$ python3 main.py $zip_filename
```