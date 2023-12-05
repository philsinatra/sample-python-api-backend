# Investigating the Suitability of Vercel for Hosting Python Serverless Functions

- [Investigating the Suitability of Vercel for Hosting Python Serverless Functions](#investigating-the-suitability-of-vercel-for-hosting-python-serverless-functions)
  - [Introduction](#introduction)
  - [Exploring Vercel as a Host for Python Serverless Functions: Feasibility and Limitations](#exploring-vercel-as-a-host-for-python-serverless-functions-feasibility-and-limitations)
  - [Adapting Python Serverless Functions for Deployment on Vercel](#adapting-python-serverless-functions-for-deployment-on-vercel)
  - [Implementing CORS Policies in Python Serverless Functions on Vercel](#implementing-cors-policies-in-python-serverless-functions-on-vercel)
  - [Connecting to the Vercel Python Function Using a JavaScript Fetch Request](#connecting-to-the-vercel-python-function-using-a-javascript-fetch-request)
  - [References](#references)

## Introduction

This project embarked on an investigative voyage to ascertain the feasibility of executing a Python script through a serverless function hosted on Vercel and subsequently fetching the output via a JavaScript API within a React Native and React Web application. A significant endeavor sought to discern the interoperability between various contemporaneous technologies, showcasing the potential to facilitate complex operations without reliance on traditional hosting services. By exploring the ability to utilize high-level Python scripts in conjunction with React Native - an eminent cross-platform framework, this research marked an attempt to foster a more distinctive and efficient approach towards mobile application development, and its findings hold profound implications for diverse programming paradigms.

The driving force underpinning this research originated from a pressing need expressed by several students aiming to integrate Python scripts with AI APIs into their junior project deliverables. The robust capacity of Python for AI programming and the increasing prevalence of JavaScript for front-end development presented both an opportunity and a challenge. The goal was to give these students a feasible method for leveraging Python's advanced capabilities within their projects, predominantly developed using React Native or React.js. Through this pursuit, I expected to enrich students' learning experience, enabling them to transcend traditional boundaries and delve into a more integrated and innovative realm of application development hinged on AI technology.

## Exploring Vercel as a Host for Python Serverless Functions: Feasibility and Limitations

This research clarifies the feasibility of hosting a Python script for a serverless function in a platform conducive to serverless computing, such as Vercel. Being a propitious platform, Vercel enables the scribing of Python code to create serverless functions accessible via the `/api` route. In the context of deploying such scripts, it is plausible to leverage the Python runtime combined with Vercel's serverless functions. A Python file with a singular HTTP handler variable, derived from the `BaseHTTPRequestHandler` class handler inside the `api` directory, will be served as a serverless function by Vercel. Consequently, this facilitates the possibility of invoking the fetch method originating from a web application and obtaining a response from the Python file - independent of the application's hosting location `[1]` `[3]`

For those utilizing the Serverless Framework, an array of plugins is designated for packaging Python Lambda functions that necessitate solely their dependencies, furnishing a mechanism to effectively manage and deploy Python functions `[4]`.

The following simplistic Python code demonstrates the prototypical concept for a serverless function that could potentially be hosted on a platform such as Vercel:

```python
# hello.py

def handler(request, response):
    return {
        'status': 200,
        'body': 'Hello, world!'
    }
```

Theoretically, the `handler` function should accept a `request` object and reciprocate a `response` object containing a status code and a body. This script is intended to be deployed as a serverless function on Vercel, providing access via the /api route. The designed operation permits calling this function using the JavaScript fetch method originating from any web application, irrespective of the hosting location.

However, it is noteworthy to mention that, in its current form, when hosted with Vercel, the illustrated script may result in an `issubclass()` error. This apparent incongruity and its resolution will be comprehensively addressed in the subsequent section of this discussion.

## Adapting Python Serverless Functions for Deployment on Vercel

For serverless functions deployed on Vercel utilizing Python, the conventional construct necessitates the `handler` function to accept a singular `request` parameter and return a `Response` object. This departs from the initially proposed function signature, which prescribes two parameters—`request` and `response`.

```python
from http.server import BaseHTTPRequestHandler
from typing import Any

class handler(BaseHTTPRequestHandler):
    def do_GET(self: Any) -> None:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
```

The paradigm above defines the class handler as an extension of the `BaseHTTPRequestHandler` class. The `do_GET` function, invoked upon receipt of a `GET` request, outlines the server's response hierarchy to such an input.

## Implementing CORS Policies in Python Serverless Functions on Vercel

In a scenario where the API is invoked from frontend JavaScript operating within a browser, the browser's inherent policy is invoked to deter potential security vulnerabilities. Subsequently, backends can sanction such requests by dispatching the appropriate headers.

```python
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

In the code above, `Access-Control-Allow-Origin` is designated as `*`, granting access to any domain to interact with this serverless function. For secure applications, it is recommended that this parameter should be adjusted accordingly to allow specific domains. It is paramount to recognize that assigning the `Access-Control-Allow-Origin` to `*` is generally discouraged for production applications because of potential security ramifications. Commonly, one would explicitly delineate the origins to be granted access.

## Connecting to the Vercel Python Function Using a JavaScript Fetch Request

The following JavaScript code is an example of a front-end snippet that interfaces with the previously discussed Python serverless function.

```javascript
fetch('https://sample-python-api-backend.vercel.app/api/index')
  .then((response) => response.text())
  //               or response.json() if you are sending JSON
  .then((data) => {
    /** @type {string} */
    let message = data; // data is the response from server
    console.log(message);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
```

A fetch request is made to the URL where the Python serverless function resides -- `'https://sample-python-api-backend.vercel.app/api/index'`.

Using JavaScript's promise-based Fetch API, the response from the server is processed and returned as a text string via the invocation of `response.text()`. The equivalent option to process returned JSON data would be `response.json()`. Then, by leveraging promise chaining, the subsequent `.then()` block is used to consume and potentially perform operations on the received `data`.

Here, `data` is declared as a `string` type variable `message`, which encapsulates the response received from the server and is subsequently logged to the console with `console.log(message)`. Error handling is incorporated via a `.catch()` block, ensuring any errors during the fetch are logged to the console with `console.error('Error:', error);`.

## References

- `[1]` <https://vercel.com/docs/functions/serverless-functions/runtimes/python>
- `[2]` <https://hevodata.com/learn/serverless-python/>
- `[3]` <https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0>
- `[4]` <https://www.serverless.com/plugins/serverless-package-python-functions>
- `[5]` <https://stackoverflow.com/questions/74252398/import-python-functions-into-serversless>
-  `[6]` <https://www.geeksforgeeks.org/python-programming-examples/>
- `[7]` <https://www.programiz.com/python-programming/examples>
- `[8]` <https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/>
- `[9]` <https://skillcrush.com/blog/python-programming-examples/>
- `[10]` <https://www.w3schools.com/python/python_examples.asp>
