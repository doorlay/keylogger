Write a keylogger that runs on the background of a linux machine, exfiltrates the data via API calls.

Figure out how to have it hidden on the computer. Also figure out how to have it hide the network data that's being sent out.

Also, design the phishing page that gets the keylogger installed and running. Also, discussh how you would go about preventing this.


Use the requests package to exfiltrate the data out to some server.

Also, figure out how I would prevent this kind of thing from happening.



Run `python3 main.py`, type a bunch of stuff, and then hit enter. When enter is pressed, key data is sent to the S3 bucket.