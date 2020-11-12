## Quickstart
### Routing
Use the `route()` decorator to bind a function to a URL.
``` python
@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello, World"
```
You can do more! You can make parts of the URL **dynamic** and **attach multiple rules** to a function.

### Variable Rules
可以通过`<converter:variable_name>`标记可变的URL部分
``` python
from markupsafe import escape


@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % escape(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d" % post_id


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath %s" % escape(subpath)
```

converter types:
|        |                                            |
| --     | --                                         |
| string | (default) accepts any text without a slash |
| int    | accepts positive integers                  |
| float  | accepts positive floating point values     |
| path   | like string but also accepts slashes       |
| uuid   | accepts UUID strings                       |

