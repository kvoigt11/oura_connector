import snowflake.connector

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine, text
from settings import SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT
from settings import SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA

# Create SQLAlchemy engine
engine = create_engine(URL(account = SNOWFLAKE_ACCOUNT,
                            user = SNOWFLAKE_USER,
                            password = SNOWFLAKE_PASSWORD,
                            database = SNOWFLAKE_DATABASE,
                            schema = SNOWFLAKE_SCHEMA,
                            warehouse = SNOWFLAKE_WAREHOUSE,
                            ))

# Test connection
try:
    connection = engine.connect()
    results = connection.execute(text("SELECT CURRENT_VERSION()"))
    version = results.scalar() 
    print(version)
finally:
    connection.close()
    engine.dispose()

