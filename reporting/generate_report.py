import json


def generate_report(errors_dict):
with open('report.json','w') as f:
json.dump(errors_dict,f,indent=2)
print("Report generated")