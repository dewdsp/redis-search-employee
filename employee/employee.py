from redis_om import JsonModel, Field

class Employee(JsonModel):
    firstname: str = Field(index=True)
    lastname: str = Field(index=True)
    salary: int = Field(index=True)
    department: str = Field(index=True)
    isAdmin: int = Field(index=True)

    