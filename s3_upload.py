#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:Project:   EC_Flood
:Created:   Fri Aug  7 11:16:12 2020

Uploads annoted snapshots to AWS for hosting to OneRain
"""
__version__ = "0.0.1"
__author__ = "Perry Oddo <perry.oddo@nasa.gov>"


import logging
import boto3
from botocore.exceptions import ClientError

ACCESS_KEY = 'AKIA6Q4BKMF7MZQVHOVQ'
SECRET_KEY = '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'


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    
    upload_file(file_name="snapshot_text1.png", bucket="ec-snapshots-s3")
    upload_file(file_name="snapshot_text2.png", bucket="ec-snapshots-s3")