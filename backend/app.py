import os
import sys
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv
from models.database_models import create_all_table

logging.basicConfig(format="%(levelname)s : %(message)s : %(asctime)s",level=logging.DEBUG)
logging.info("Sürücü oluşturuluyor")
load_dotenv()
 
print("DB_USER " + os.getenv("DB_USER"))
engine = create_engine("postgresql+psycopg2://alperen:alperen@127.0.0.1:5432/warehouse")
create_all_table(engine)

