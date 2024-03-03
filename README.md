# pyigdiff

Python program to find the Following and Followers difference of an account.

The code assumes that you have downloaded your information as a zip file with all the files in json format.
The program looks for the json file `following.json` and `followers_1.json` in the archive. Parses them and finds the differences between the two lists.

The script yields:
- the usernames of those accounts that follows the user but the user does not follow back
- the usernames of those accounts that the user follows but they don't follow back.

## Retrieving personal information from Instagram

In order to retrieve the zipped archive with the information needed to run the Python script, one needs to request these information from Instagram.

After opening `instagram.com` from a web browser and getting access to your account follow these steps:

1. Open Settings and select the options `Accounts Center`
2. Click on `Your information and permissions` > `Download your information` and click the button `Download or transfer information`
3. `instagram.com` will prompt you whether to download All available information or only some. You can choose the option that you please.
4. Once one of the aforementioned choices has been selected, click the option `Download to device`.
5. Specify: Date Range (`All Time`) and Format (`JSON`)
6. Confirm by pressing the button `Create files`

Once the requested information are ready, Instagram will send a notification to your email inbox.

From that point on, you just need to download the zip file and execute the program by opening a terminal and typing
```console
$ python3 main.py $zip_filename
```

From what I have observed, it does not matter where you store the zip file or where you run the script as long as you provide the correct relative filepaths when invoking it.

## Brief note
I want to be very clear that I have written this script because I was bored and because I find very annoying to search for the difference in Followings and Followers. I am not that interested in social media to waste time doing that, hence I have automated this task.

You might think, "Oh, why do you care so much then?" and to that I say "Mind your business".

Use this script as you please, I doubt you'll find something interesting other than unneccessary, overengineered and overcomplicated code.