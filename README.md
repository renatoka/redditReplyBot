# Foobar

redditReplyBot is a simple Python bot that replies when trigger word is found.

## Installation

You will need to install some libraries first.

```bash
pip install praw
pip install random
```

## Usage
Make sure to edit these parameters to your own reddit bot

```python
import praw
import time
import random

reddit = praw.Reddit(
    client_id = "",
    client_secret = "",
    user_agent = "",
    password = "",
    username = "")

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
