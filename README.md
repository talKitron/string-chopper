# string-chopper


Author: Tal Kitron

![testing-python](https://github.com/talKitron/string-chopper/workflows/testing-python/badge.svg)

Endpoint: <https://string-chopper.herokuapp.com/api/docs>

-----

## Prompt

Write a small web application in Python/Ruby/Node. The application only needs to do the following:

* Receives a POST request to the route “/test”, which accepts one argument “raw_string”
* Returns a JSON object with the key “chopped_string” and a string value containing every third letter from the original string.

-----

## Example

If you POST
```json
{"raw_string": "hello world!"}
```
it will return:
```json
{"chopped_string": "l r!"}
```
<br>
Note: To see expected behavior you can test against a current working example with the command:

```bash
curl -X POST https://stringchopper.herokuapp.com/test --data '{"raw_string": "hello world!"}' -H 'Content-Type: application/json'
```

-----

## Approach

### Approach using Enumerate

The first approach is to use enumerate to access the index of the input string and build a new string.

```python
str = "hello world!"
seq = ""

for i, letter in enumerate(str, start=1):
    if i % 3 == 0:
        seq += letter
return seq
```

Complexity Analysis

* Time Complexity: ```O(n)```. We need to iterate every character from the string where ```n``` is the length of the input string.
* Space Complexity: ```O(n)```. The new string will store  ```1/3 * n``` where ```n``` is the length of input string.

### Approach using Join

Since strings in Python are immutable, a new string needs to be created to solve the problem. This continual copying from the initial approach can lead to significant inefficiencies in Python programs.

We can optimize the above approach using ```s = "".join(list)```

```python
str = "hello world!"

chars = str[2::3]
seq = "".join(chars)
return seq
```

Complexity Analysis

* Time Complexity: ```O(k)```. Where ```k``` is either the value of a parameter or the number of elements in the parameter.
* Space Complexity: ```O(n)```. The new string will take ```1/3 * n``` space where ```n``` is the length of input string.

----

## Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/talKitron/string-chopper.git
```

Install the dependencies:

```bash
pip3 install -r requirements.txt
```

### Development Mode

Start the application in development mode with the following command in terminal:

```bash
FLASK_ENV=development flask run
```

Test the functionality of the endpoint running at ```localhost:5000``` with the following command:

```bash
curl -X POST http://127.0.0.1:5000/chopper --data '{"raw_string": "hello world!"}' -H 'Content-Type: application/json'
```

The expected output of the above command is:

```json
{
    "return_string": "l r!"
}
```

Alternatively, test the functionality of the endpoint running at <http://127.0.0.1:5000/api/docs/> by clicking the ```Try it out``` button.

![open_api_desc](https://user-images.githubusercontent.com/9827474/94448647-6aeec380-01ab-11eb-8e67-66ea3d6d7e43.png)

Run the automated test with the following command while the server is running:

```bash
pytest
```

The expected output of the above command is:

```bash
test/test_endpoints.py ..............                                    [100%]

============================== 13 passed in 0.76s ==============================
```

### Production

Run the application in production with the following command:

```bash
uwsgi --ini app.ini --need-app
```

The application is currently deployed on Heroku with the following endpoint: <https://string-chopper.herokuapp.com/test>

Run the automated test on the deployed Heroku with the following command:

```bash
pytest --host https://string-chopper.herokuapp.com
```

----

## Credits

* [Data Science Blog - REST API Development with Flask](https://www.datascienceblog.net/post/programming/flask-api-development/)
* [Python - PerformanceTips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
* [Python - TimeComplexity](https://wiki.python.org/moin/TimeComplexity#list)
* [pythonise.com - Working with JSON data | Learning Flask Ep. 9](https://pythonise.com/series/learning-flask/working-with-json-in-flask)
* [pytest - Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/parametrize.html)
* [uWSGI - Running python webapps on Heroku with uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/heroku_python.html)
* [Heroku Dev Center - Deploying Python Applications with Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn)

----
