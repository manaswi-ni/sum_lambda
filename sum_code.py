# import boto3
# import json

# def lambda_handler(event=None, context=None):
#     # Perform sum
#     a = 5
#     b = 7
#     total = a + b
#     result_text = f"Sum of {a} and {b} is {total}"

#     # --- Upload to S3 ---
#     s3 = boto3.client('s3')
#     bucket_name = 'hosting32'  # 🔁 Replace this
#     file_key = 'sum_result.txt'

#     s3_upload_message = ''
#     try:
#         s3.put_object(Bucket=bucket_name, Key=file_key, Body=result_text)
#         s3_upload_message = f"Uploaded to S3: {bucket_name}/{file_key}"
#     except Exception as e:
#         s3_upload_message = f"Failed to upload to S3: {str(e)}"

#     # --- Publish to MQTT ---
#     iot = boto3.client('iot-data', region_name='ca-central-1')  # Change region if needed
#     topic = 'lambda/sum'
#     mqtt_payload = {
#         'sum': total,
#         'message': 'Lambda calculated the sum and uploaded to S3'
#     }

#     mqtt_publish_message = ''
#     try:
#         iot.publish(
#             topic=topic,
#             qos=1,
#             payload=json.dumps(mqtt_payload)
#         )
#         mqtt_publish_message = f"Published to MQTT topic: {topic}"
#     except Exception as e:
#         mqtt_publish_message = f"Failed to publish to MQTT: {str(e)}"

#     # --- Final Lambda Response ---
#     return {
#         'statusCode': 200,
#         'body': {
#             'result': result_text,
#             's3_status': s3_upload_message,
#             'mqtt_status': mqtt_publish_message
#         }
#     }




import boto3
import json

def lambda_handler(event=None, context=None):
    a = 10
    b = 7
    total = a + b
    result_text = f"Sum of {a} and {b} is {total}"

    # --- Upload to S3 ---
    s3 = boto3.client('s3')
    bucket_name = 'hosting32'  # 🔁 Replace with your actual bucket
    file_key = 'sum_result.txt'

    try:
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=result_text)
        s3_status = f"✅ Uploaded to S3: {bucket_name}/{file_key}"
    except Exception as e:
        s3_status = f"❌ Failed to upload to S3: {str(e)}"

    # --- Publish to MQTT (IoT Core) ---
    iot = boto3.client('iot-data', region_name='ca-central-1')  # 🔁 Update region if needed
    topic = 'lambda/sum'
    payload = {
        'sum': total,
        'source': 'Local VS Code'
    }

    try:
        iot.publish(
            topic=topic,
            qos=1,
            payload=json.dumps(payload)
        )
        mqtt_status = f"✅ Published to MQTT topic: {topic}"
    except Exception as e:
        mqtt_status = f"❌ Failed to publish to MQTT: {str(e)}"

    return {
        'statusCode': 200,
        'body': {
            'result': result_text,
            's3_status': s3_status,
            'mqtt_status': mqtt_status
        }
    }

# ✅ Run locally
if __name__ == '__main__':
    response = lambda_handler()
    print(json.dumps(response, indent=2))