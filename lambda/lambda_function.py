import base64
import json
import mysql.connector 

def lambda_handler(event, context):
    # MySQL database connection
    db_config = {
        'user': 'admin',
        'password': 'pwd',
        'host': '*****.*****.ap-northeast-2.rds.amazonaws.com',
        'database': 'pipelinedb',
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for record in event['Records']:
        record_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(record_data)

        if data['user_type'] == 'new_user':

        # Prepare an INSERT statement for the MySQL database
            insert_query = """
            INSERT INTO channel_marketing_tb
            (serviceType, gtmLongTime, base_dt, channel_name, conversion_name, platform, user_type)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s);
            """
            values = (
                data['serviceType'],
                data['gtmLongTime'],
                data['base_dt'],
                data['channel_name'],
                data['conversion_name'],
                data['platform'],
                data['user_type']
                # Add values for other columns as well
            )
            cursor.execute(insert_query, values)
            connection.commit()
        
    cursor.close()
    connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps(f'Processed and saved {len(event["Records"])} records to MySQL')
    }
