# schedule-delete-whatsapp-group
A script that deletes a specific group on a specific date

To run it you have to install the requirements

Prereably install it in a virtual enviroment 
which can be created via
### `python3 -m venv yourvenvname`
and activated via 
### `source path-to-yourvenvname/bin/activate`

Than you can install the requirements

### `pip install -r requirements.txt`

Than you have to add the path to your chrome profile to the script 
(in the line with the comment change to profile path)

Depending on your OS the chrome path slightly depends. You can find it if you 
navigate to chrome://version in your chrome browser.
The path can be found under "Profile Path"
(Go to https://chromium.googlesource.com/chromium/src/+/HEAD/docs/user_data_dir.md for details)

Than you have to open https://web.whatsapp.com/  with your chrome profile and scan the qr code with your smartphone.

After that you can run the script and enter the groupname, 
the number of members and the date on which the group should be deleted.


