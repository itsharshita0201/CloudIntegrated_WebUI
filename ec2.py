#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import subprocess
import boto3
import cgitb

cgitb.enable()

form=cgi.FieldStorage()

ImageId = form.getvalue("img")
InstanceType=form.getvalue("instance")
MaxCount=form.getvalue("max")
MinCount=form.getvalue("min")
print(ImageId, InstanceType, MaxCount, MinCount)
myec2=boto3.client("ec2", aws_access_key_id="your acess key", aws_secret_access_key="your Secret key", region_name="ap-south-1")
print(myec2)
response=myec2.run_instances(
    ImageId=ImageId,
    InstanceType=InstanceType,
    MaxCount=int(MaxCount),
    MinCount=int(MinCount)
 )
print(myec2)
print(response)