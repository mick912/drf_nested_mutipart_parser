# drf-nested-multipart-parser
DRF Parser for nested params in multipart file upload. 

# Usage
```python
from drf_nested_multipart_parser import NestedMultipartParser
from rest_framework import viewsets

class YourViewSet(viewsets.ViewSet):
	parser_classes = (NestedMultipartParser,)
```
To enable JSON and multipart

```python
from drf_nested_multipart_parser import NestedMultipartParser
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

class YourViewSet(viewsets.ViewSet):
	parser_classes = (JSONParser, NestedMultipartParser)
```

# Example:
Input data
```
user[email] = 'test@test.test'
user[name] = 'John Doe'

user[profile][balance] = 100.00
user[profile][phone_number] = '+996325698201'
user[profile][avatar] = avatar_file

user[roles][] = 1 
user[roles][] = 2 
user[roles][] = 3 
...
```

View
```python
from drf_nested_multipart_parser import NestedMultipartParser
from rest_framework import viewsets

class YourViewSet(viewsets.ViewSet):
	parser_classes = (NestedMultipartParser,)

    def post(self, request):
       user_data = request.data.get('user')
       
       email = user_data['email']  # test@test.test
       balance = user_data['profile']['balance'] # 100.0
       roles = user_data['roles'] # [1, 2, 3]
       ...   
```

# Installation
`pip install drf-nested-multipart-parser`
