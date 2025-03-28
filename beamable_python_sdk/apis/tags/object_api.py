# coding: utf-8

"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

from beamable_python_sdk.paths.object_calendars_object_id_claim.post import ClaimCalendar
from beamable_python_sdk.paths.object_chat_v2_object_id_rooms.post import CreateChatRoom
from beamable_python_sdk.paths.object_commerce_object_id_coupons.post import CreateCommerceCoupons
from beamable_python_sdk.paths.object_inventory_object_id.post import CreateInventoryObject
from beamable_python_sdk.paths.object_stats_object_id.post import CreateObjectStats
from beamable_python_sdk.paths.object_chat_v2_object_id_rooms.delete import DeleteRoom
from beamable_python_sdk.paths.object_stats_object_id.delete import DeleteStatsObject
from beamable_python_sdk.paths.object_commerce_object_id_status.delete import DeleteStatusById
from beamable_python_sdk.paths.object_commerce_object_id.get import GetById
from beamable_python_sdk.paths.object_calendars_object_id.get import GetCalendars
from beamable_python_sdk.paths.object_chat_v2_object_id_rooms.get import GetChatRooms
from beamable_python_sdk.paths.object_chat_v2_object_id.get import GetChatV2
from beamable_python_sdk.paths.object_stats_object_id_client.get import GetClientStats
from beamable_python_sdk.paths.object_commerce_object_id_coupons_count.get import GetCommerceCouponCount
from beamable_python_sdk.paths.object_commerce_object_id_listings.get import GetCommerceListings
from beamable_python_sdk.paths.object_commerce_object_id_offers.get import GetCommerceOffers
from beamable_python_sdk.paths.object_inventory_object_id.get import GetInventoryObjectById
from beamable_python_sdk.paths.object_matchmaking_object_id_match.get import GetMatchmakingData
from beamable_python_sdk.paths.object_inventory_object_id_multipliers.get import GetMultipliers
from beamable_python_sdk.paths.object_stats_object_id.get import GetObjectStats
from beamable_python_sdk.paths.object_commerce_object_id_offers_admin.get import GetOffersAdmin
from beamable_python_sdk.paths.object_payments_object_id.get import GetPaymentDetails
from beamable_python_sdk.paths.object_matchmaking_object_id_match.delete import MatchmakingDelete
from beamable_python_sdk.paths.object_stats_object_id_client.post import PostClientStats
from beamable_python_sdk.paths.object_stats_object_id_client_stringlist.post import PostClientStringlist
from beamable_python_sdk.paths.object_commerce_object_id_purchase.put import PurchaseById
from beamable_python_sdk.paths.object_commerce_object_id_purchase.post import PurchaseItem
from beamable_python_sdk.paths.object_inventory_object_id_transaction.delete import RemoveTransactionById
from beamable_python_sdk.paths.object_matchmaking_object_id_match.post import StartMatchmakingProcess
from beamable_python_sdk.paths.object_inventory_object_id_transfer.put import TransferItemInventory
from beamable_python_sdk.paths.object_inventory_object_id.put import UpdateInventoryObject
from beamable_python_sdk.paths.object_inventory_object_id_preview.put import UpdateInventoryPreview
from beamable_python_sdk.paths.object_matchmaking_object_id_tick.put import UpdateMatchmakingTick
from beamable_python_sdk.paths.object_commerce_object_id_stats_update.post import UpdateStatObject
from beamable_python_sdk.apis.tags.object_api_raw import ObjectApiRaw


class ObjectApi(
    ClaimCalendar,
    CreateChatRoom,
    CreateCommerceCoupons,
    CreateInventoryObject,
    CreateObjectStats,
    DeleteRoom,
    DeleteStatsObject,
    DeleteStatusById,
    GetById,
    GetCalendars,
    GetChatRooms,
    GetChatV2,
    GetClientStats,
    GetCommerceCouponCount,
    GetCommerceListings,
    GetCommerceOffers,
    GetInventoryObjectById,
    GetMatchmakingData,
    GetMultipliers,
    GetObjectStats,
    GetOffersAdmin,
    GetPaymentDetails,
    MatchmakingDelete,
    PostClientStats,
    PostClientStringlist,
    PurchaseById,
    PurchaseItem,
    RemoveTransactionById,
    StartMatchmakingProcess,
    TransferItemInventory,
    UpdateInventoryObject,
    UpdateInventoryPreview,
    UpdateMatchmakingTick,
    UpdateStatObject,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ObjectApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ObjectApiRaw(api_client)
