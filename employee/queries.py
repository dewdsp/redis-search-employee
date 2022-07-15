from redis import ResponseError
from redisearch import Client, TextField, NumericField, IndexDefinition
from redisearch.aggregation import AggregateRequest
from redisearch import reducers

from employee import Employee

def show_results(results):
  for employee in results:
    print(employee)
    print("")

def initializeClient():
  SCHEMA = (
    TextField("firstname"),
    TextField("lastname"),
    NumericField("salary"),
    TextField("department"),
    NumericField("isAdmin")
  )
  client = Client("myIndex",host='localhost', port=6379, password='mypassword')
  definition = IndexDefinition(prefix=[':employee.Employee:'])
  try:
    client.info()
  except ResponseError:
    client.create_index(SCHEMA, definition=definition)
  return client

client = initializeClient()

## Find entries by first name
def findByFirstName():
  return Employee.find(Employee.firstname == "ahmad").all()
# show_results(findByFirstName())

def findByFirstNameRS(client):
  res = client.search("@firstname:ahmad")
  for r in res.docs:
    print(r)
# findByFirstNameRS(client)

def findByFirstAndLastname():
  return Employee.find((Employee.firstname == 'สิทธการย์') & (Employee.lastname == 'ประสมทรัพย์'))

# show_results(findByFirstAndLastname())

def sort_by_salary():  
  return Employee.find(Employee.salary>0).sort_by("salary")

# show_results(sort_by_salary())

def sort_by_salary_RS():
  request = AggregateRequest('*').group_by(['@salary'], reducers.count()).sort_by('@salary')
  result = client.aggregate(request)
  for r in result.rows:
    print(r)
sort_by_salary_RS()