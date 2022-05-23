import boto3
client = boto3.client('config')

list_of_rules=[]

paginator = client.get_paginator('describe_config_rules')

response_iterator = paginator.paginate()

for rules in response_iterator:
    for rule_name in rules['ConfigRules']:
        compliance_paginator = client.get_paginator('get_compliance_details_by_config_rule')
        compliance_iterator = compliance_paginator.paginate(ConfigRuleName=rule_name['ConfigRuleName'], ComplianceTypes=['NON_COMPLIANT'])
        print("***",rule_name['ConfigRuleName'],"****")
        for item in compliance_iterator:
            for x in item['EvaluationResults']:
                print(x['EvaluationResultIdentifier']['EvaluationResultQualifier'])
        print("-----------")
       




