import json

with open("../aws_config.json", "r") as f:
    bubu = json.loads(f.read())
    print(bubu["bucket_arn"])
    