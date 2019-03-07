from ScoutSuite.providers.base.configs.resources import Resources

class Keys(Resources):
    def __init__(self, gcp_facade, project_id, service_account_email):
        self.gcp_facade = gcp_facade
        self.project_id = project_id
        self.service_account_email = service_account_email 

    async def fetch_all(self):
        raw_keys = await self.gcp_facade.iam.get_keys(self.project_id, self.service_account_email)
        for raw_key in raw_keys:
            key_id, key = self._parse_key(raw_key)
            self[key_id] = key

    def _parse_key(self, raw_key):
        key_dict = {}
        key_dict['id'] = raw_key['name'].split('/')[-1]
        key_dict['valid_after'] = raw_key['validAfterTime']
        key_dict['valid_before'] = raw_key['validBeforeTime']
        key_dict['key_algorithm'] = raw_key['keyAlgorithm']
        return key_dict['id'], key_dict