import boto3
import random
from datetime import datetime, timedelta
from faker import Faker


fake = Faker()


session = boto3.Session(
    #here are keys and passwords
)

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('test_data')

def generate_random_data(x: int):

    start_date = datetime.strptime('2020-05-24', '%Y-%m-%d')
    end_date = datetime.strptime('2030-05-24', '%Y-%m-%d')
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    return {
        'id': x,
        'createDate': random_date.strftime('%Y-%m-%d'),
        'catalog': random.choice([1, 2, 3]),
        'userName': 'Guoxiang Zhao'
    }

def insert_data_to_dynamodb(data):
    table.put_item(Item=data)

def main():
    for i in range(10000,13000):
        data = generate_random_data(i)
        insert_data_to_dynamodb(data)
        print(f"Inserted: {data}")
        

if __name__ == "__main__":
    main()




