from odoo.addons.g2p_registry_rest_api.schemas import registrant


class RegistrantAddlInfoRequest(registrant.RegistrantInfoRequest, extends=registrant.RegistrantInfoRequest):
    additional_g2p_info: list | dict | None = None


class RegistrantInfoResponse(registrant.RegistrantInfoResponse, extends=registrant.RegistrantInfoResponse):
    additional_g2p_info: str | None = ""
