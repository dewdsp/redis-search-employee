import redis
from redis_om import JsonModel, Field, get_redis_connection

redis = get_redis_connection(port=6379)

class Employee(JsonModel):
    firstname: str = Field(index=True)
    lastname: str = Field(index=True)
    salary: int = Field(index=True)
    department: str = Field(index=True)
    isAdmin: int = Field(index=True)

    class Meta:
        database = redis
    