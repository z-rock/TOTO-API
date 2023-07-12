# TOTO-API

To use this python script all you need to do is enter your API key into the provided variable, select a desired function, and enter the twitter handle of the user as a string for the input.

For example if you wanted to show the user id of @DegenSpartan you would write something like this:
print(get_user_id("DegenSpartan"))

You should get a response of:  
{'username': 'DegenSpartan', 'userid': '1978953986'}
