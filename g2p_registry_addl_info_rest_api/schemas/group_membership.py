from odoo.addons.g2p_registry_rest_api.schemas import group_membership


class GroupMembersInfoRequest(
    group_membership.GroupMembersInfoRequest, extends=group_membership.GroupMembersInfoRequest
):
    additional_g2p_info: list[dict] | dict = None
