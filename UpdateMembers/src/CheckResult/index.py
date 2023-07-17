#!/bin/python


def lambda_handler(event, context):
    result = {}
    failed = False
    for execution in event["processedItems"]:
        if execution["statusCode"] == 500:
            failed = True
            result[execution["account"]] = execution["error"] + " in the region: " + execution["region"]

    if failed:
        return {"statusCode": 500, "failed_accounts": result}

    return {"statusCode": 200}
