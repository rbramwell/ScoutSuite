from ScoutSuite.providers.base.configs.resources import Resources

class Bindings(Resources):
    def __init__(self, gcp_facade, project_id, service_account_email):
        self.gcp_facade = gcp_facade
        self.project_id = project_id
        self.service_account_email = service_account_email 

    async def fetch_all(self):
        raw_bindings = await self.gcp_facade.iam.get_bindings(self.project_id, self.service_account_email)
        for raw_binding in raw_bindings:
            binding_id, binding = self._parse_binding(raw_binding)
            self[binding_id] = binding

    def _parse_binding(self, raw_binding):
        return len(self), raw_binding