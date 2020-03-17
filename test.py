import pytest
import pyodbc
server='SHANTANU\SHANTANU'
db='Python'

@pytest.fixture
def SetUp():
    print('Setup is called')
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+db+';Trusted_Connection=yes')
    curr=conn.cursor()
    yield curr
    curr.close()
    conn.close()
    
def test_MethodA(SetUp):
    count=SetUp.execute("SELECT COUNT(1) FROM T_BusinessEntityAddress_1")
    count= SetUp.fetchone()
    assert count[0]==1914
    
    
def test_MethodB(SetUp):
    count=SetUp.execute("SELECT COUNT(1) FROM T_BusinessEntityAddress_1")
    count= SetUp.fetchone()
    assert count[0]==19614