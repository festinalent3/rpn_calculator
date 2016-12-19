
## Python3/Django calculator

My first python project! A calculator using [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) to parse an infix expression and return the result of the calculation. 


## Installation

####Clone the project from github:

```
$ git clone git@github.com:festinalent3/rpn_calculator.git
```

####Create virtual environment

You need to have [virtuelenv](https://virtualenv.pypa.io/en/stable/) installed

```
$ cd rpn_calculator
$ virtualenv . -p python3
```

####Install project requirements 

```
$ pip install -r requirements.txt
```

####Add a development key

You can fetch a key [here](http://www.miniwebtool.com/django-secret-key-generator/)

```
$ echo "SECRET_KEY_DEV='your_key_here'" > calculator/keys.py
```

## Usage


The service offers two endpoints - __calculus__ and __convert__. 

They both take a base64 encoded string containing a mathematical expression. Example: 

- Original query: `2 * (23/(3*3))- 23 * (2*3)`
- With encoding: `MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=`

Allowed operations are: `+  -  *  /  (  )`

__convert__ endpoint will return the expression converted into reverse polish notation (postfix notation)

__calculus__ will return the result of the calculated expression (no need to convert it first)


The response will be in JSON form:
- On success (__convert__): `{ error: false, result: string}`
- On success (__calculus__): `{ error: false, result: number}` 
- On error: `{ error: true, message: string }`

####Start server
```
$ python manage.py runserver
```

####Convert to RPN
```
$ curl http://127.0.0.1:8000/convert?q=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=
```

####Calculate
```
$ curl http://127.0.0.1:8000/calculus?q=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=
```


## Try it immediately

The service is also available on heroku at https://rpn-calculus.herokuapp.com/endpoint?q=[your-query]


