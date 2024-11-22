import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import urllib.parse








def upload_to_azure_sql(df, table_name, server, database, username, password):
    """
    Upload a pandas DataFrame to Azure SQL Database through a virtual network connection.
    """

    # Configure the connection string - This One Works
    params = urllib.parse.quote_plus(
        'Driver={ODBC Driver 17 for SQL Server};'
        f'Server=tcp:{server},1433;'
        f'Database={database};'
        f'Uid={username};'
        f'Pwd={password};'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=60;'
        'Command Timeout=60;'
    )

    try:
        # Create SQLAlchemy engine
        engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
        
        # Upload the DataFrame
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',  # Options: 'fail', 'replace', 'append'
            index=False,
            schema='LANDING'  # Default schema
        )
        
        print(f"Successfully uploaded {len(df)} rows to {table_name}")
        
    except Exception as e:
        print(f"Error uploading data: {str(e)}")
    
    finally:
        if 'engine' in locals():
            engine.dispose()









