import csv
import logging
import os
from dotenv import load_dotenv

import aioredis
from aredis_om import Migrator, get_redis_connection

from employee import Employee

config = load_dotenv(".env")

with open("employee.csv") as csv_file:
    employees = csv.DictReader(csv_file)

    for employee in employees:
        emp = Employee(**employee)
        print(f"{employee['firstname']} has pk = {emp.pk}")
        emp.save()

async def startup():
    await Migrator().run()
    logger = logging.getLogger("employee.info")
    url = os.getenv('REDIS_OM_URL')
    if not url:
        url = 'redis://default:mypassword@localhost:6379'
        logger.info("Using local redis")
    else:
        logger.info("Using redis from REDIS_OM_URL")

    r = aioredis.from_url(url, encoding="utf8", decode_responses=True)
    # FastAPICache.init(RedisBackend(r), prefix="fastapi-cache")
Migrator().run()
