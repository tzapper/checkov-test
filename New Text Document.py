class S3EnvironmentCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure s3 has environment tag of developemnt/staging/production"
        id = "CUSTOM_AWS_1"
        supported_resources = ['aws_s3_bucket']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

 

    def scan_resource_conf(self, conf):
        if conf.get("tags",[]):
            env = conf["tags"][0].get("Environment",{})
            if env in ["Developemnt","Staging","Production"]:
                return CheckResult.PASSED
        return CheckResult.FAILED

 


scanner = S3EnvironmentCheck()