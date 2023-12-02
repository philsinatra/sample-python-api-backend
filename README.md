# Python API Backend

- [Python API Backend](#python-api-backend)
  - [Research](#research)
    - [`issubclass()` error](#issubclass-error)
    - [CORS error](#cors-error)

## Research

You can host the Python file for your serverless function on a platform that supports serverless computing, such as Vercel. Vercel allows you to write Python code and create serverless functions that can be accessed via the /api route. You can use the Python runtime with Vercel serverless functions to deploy your Python script. When a Python file has a singular HTTP handler variable, inheriting from the BaseHTTPRequestHandler class handler within the api directory, Vercel will serve it as a serverless function. This allows you to call the fetch method from your web application and receive a response from the Python file, regardless of where your web app is hosted[1][3].

If you use the Serverless Framework, there are plugins available for packaging Python Lambda functions with only the dependencies they need. This can help you manage and deploy your Python functions effectively[4].

Citations:

- [1] <https://vercel.com/docs/functions/serverless-functions/runtimes/python>
- [2] <https://hevodata.com/learn/serverless-python/>
- [3] <https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0>
- [4] <https://www.serverless.com/plugins/serverless-package-python-functions>
- [5] <https://stackoverflow.com/questions/74252398/import-python-functions-into-serversless>

Here's a simple example of a Python code for a serverless function that can be hosted on a platform like Vercel:

```python
# hello.py

def handler(request, response):
    return {
        'status': 200,
        'body': 'Hello, world!'
    }
```

In this example, the `handler` function takes a `request` object and returns a `response` object with a status code and a body. This code can be deployed as a serverless function on Vercel, and the function will be accessible via the /api route. You can call this function using the JavaScript fetch method from your web application, regardless of where your web app is hosted.

Citations:

- [1] <https://www.geeksforgeeks.org/python-programming-examples/>
- [2] <https://www.programiz.com/python-programming/examples>
- [3] <https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/>
- [4] <https://skillcrush.com/blog/python-programming-examples/>
- [5] <https://www.w3schools.com/python/python_examples.asp>

### `issubclass()` error

For serverless functions on Vercel using Python, the standard format expects the `handler` function to accept a `request` parameter and return a `Response` object, which is different from the original function signature that takes two parameters (`request`, `response`).

```py
from http.server import BaseHTTPRequestHandler
from typing import Any

class handler(BaseHTTPRequestHandler):
    def do_GET(self: Any) -> None:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
```

This example defines a class `handler` that extends teh `BaseHTTPRequestHandler` class. The `do_GET` function is called when a `GET` request is received, and defines the server's response to that request.

### CORS error

When calling the API from frontend Javascript running in a browser, the browser enforces a policy to prevent potential security issues. Backends can allow such requests by sending the appropriate headers.

```py
from http.server import BaseHTTPRequestHandler
from typing import Any
import random

def generate_random_number():
    return random.randint(0, 100)

class handler(BaseHTTPRequestHandler):
    def do_GET(self: Any) -> None:
        self.send_response(200)
        # Set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()
        num = generate_random_number()
        self.wfile.write(str(num).encode())
```

This specifies `Access-Control-Allow-Origin` to `*`, which allows any domain to access this serverless function. Adjust accordingly for secure applications to allow only specific domains. Note, setting the `Access-Control-Allow-Origin` to `*` is generally not recommended for production applications due to security reasons. You would typically specify the exact origins that should be allowed access.
