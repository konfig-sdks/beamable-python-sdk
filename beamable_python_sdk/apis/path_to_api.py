import typing_extensions

from beamable_python_sdk.paths import PathValues
from beamable_python_sdk.apis.paths.basic_trials_admin_data import BasicTrialsAdminData
from beamable_python_sdk.apis.paths.basic_trials_data import BasicTrialsData
from beamable_python_sdk.apis.paths.basic_trials_pause import BasicTrialsPause
from beamable_python_sdk.apis.paths.basic_trials_schedule import BasicTrialsSchedule
from beamable_python_sdk.apis.paths.basic_trials_admin import BasicTrialsAdmin
from beamable_python_sdk.apis.paths.basic_trials_start import BasicTrialsStart
from beamable_python_sdk.apis.paths.basic_accounts_me_device import BasicAccountsMeDevice
from beamable_python_sdk.apis.paths.basic_accounts_me import BasicAccountsMe
from beamable_python_sdk.apis.paths.basic_accounts_me_third_party import BasicAccountsMeThirdParty
from beamable_python_sdk.apis.paths.basic_accounts_get_personally_identifiable_information import BasicAccountsGetPersonallyIdentifiableInformation
from beamable_python_sdk.apis.paths.basic_accounts_search import BasicAccountsSearch
from beamable_python_sdk.apis.paths.basic_accounts_email_update_init import BasicAccountsEmailUpdateInit
from beamable_python_sdk.apis.paths.basic_accounts_email_update_confirm import BasicAccountsEmailUpdateConfirm
from beamable_python_sdk.apis.paths.basic_accounts_available_third_party import BasicAccountsAvailableThirdParty
from beamable_python_sdk.apis.paths.basic_accounts_admin_admin_user import BasicAccountsAdminAdminUser
from beamable_python_sdk.apis.paths.basic_accounts_register import BasicAccountsRegister
from beamable_python_sdk.apis.paths.basic_accounts_admin_me import BasicAccountsAdminMe
from beamable_python_sdk.apis.paths.basic_accounts_password_update_init import BasicAccountsPasswordUpdateInit
from beamable_python_sdk.apis.paths.basic_accounts_admin_admin_users import BasicAccountsAdminAdminUsers
from beamable_python_sdk.apis.paths.basic_accounts_find import BasicAccountsFind
from beamable_python_sdk.apis.paths.basic_accounts_available_device_id import BasicAccountsAvailableDeviceId
from beamable_python_sdk.apis.paths.basic_accounts_available import BasicAccountsAvailable
from beamable_python_sdk.apis.paths.basic_accounts_password_update_confirm import BasicAccountsPasswordUpdateConfirm
from beamable_python_sdk.apis.paths.object_accounts_object_id_admin_email import ObjectAccountsObjectIdAdminEmail
from beamable_python_sdk.apis.paths.object_accounts_object_id_available_roles import ObjectAccountsObjectIdAvailableRoles
from beamable_python_sdk.apis.paths.object_accounts_object_id_role import ObjectAccountsObjectIdRole
from beamable_python_sdk.apis.paths.object_accounts_object_id_admin_scope import ObjectAccountsObjectIdAdminScope
from beamable_python_sdk.apis.paths.object_accounts_object_id_admin_third_party import ObjectAccountsObjectIdAdminThirdParty
from beamable_python_sdk.apis.paths.object_accounts_object_id_admin_forget import ObjectAccountsObjectIdAdminForget
from beamable_python_sdk.apis.paths.basic_announcements_search import BasicAnnouncementsSearch
from beamable_python_sdk.apis.paths.basic_announcements_content import BasicAnnouncementsContent
from beamable_python_sdk.apis.paths.basic_announcements_list import BasicAnnouncementsList
from beamable_python_sdk.apis.paths.object_announcements_object_id_read import ObjectAnnouncementsObjectIdRead
from beamable_python_sdk.apis.paths.object_announcements_object_id_claim import ObjectAnnouncementsObjectIdClaim
from beamable_python_sdk.apis.paths.object_announcements_object_id_raw import ObjectAnnouncementsObjectIdRaw
from beamable_python_sdk.apis.paths.basic_auth_token import BasicAuthToken
from beamable_python_sdk.apis.paths.object_calendars_object_id_claim import ObjectCalendarsObjectIdClaim
from beamable_python_sdk.apis.paths.object_chat_v2_object_id_rooms import ObjectChatV2ObjectIdRooms
from beamable_python_sdk.apis.paths.object_chat_v2_object_id_messages import ObjectChatV2ObjectIdMessages
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_replace import BasicCloudsavingDataReplace
from beamable_python_sdk.apis.paths.basic_cloudsaving_data import BasicCloudsavingData
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_download_url import BasicCloudsavingDataDownloadURL
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_metadata import BasicCloudsavingDataMetadata
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_move import BasicCloudsavingDataMove
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_upload_url_from_portal import BasicCloudsavingDataUploadURLFromPortal
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_commit_manifest import BasicCloudsavingDataCommitManifest
from beamable_python_sdk.apis.paths.basic_cloudsaving_data_upload_url import BasicCloudsavingDataUploadURL
from beamable_python_sdk.apis.paths.basic_commerce_catalog import BasicCommerceCatalog
from beamable_python_sdk.apis.paths.basic_commerce_skus import BasicCommerceSkus
from beamable_python_sdk.apis.paths.object_commerce_object_id_coupons_count import ObjectCommerceObjectIdCouponsCount
from beamable_python_sdk.apis.paths.object_commerce_object_id_offers_admin import ObjectCommerceObjectIdOffersAdmin
from beamable_python_sdk.apis.paths.object_commerce_object_id_purchase import ObjectCommerceObjectIdPurchase
from beamable_python_sdk.apis.paths.object_commerce_object_id_listings import ObjectCommerceObjectIdListings
from beamable_python_sdk.apis.paths.object_commerce_object_id_status import ObjectCommerceObjectIdStatus
from beamable_python_sdk.apis.paths.object_commerce_object_id_coupons import ObjectCommerceObjectIdCoupons
from beamable_python_sdk.apis.paths.object_commerce_object_id_stats_update import ObjectCommerceObjectIdStatsUpdate
from beamable_python_sdk.apis.paths.object_commerce_object_id_offers import ObjectCommerceObjectIdOffers
from beamable_python_sdk.apis.paths.basic_content_manifest_pull import BasicContentManifestPull
from beamable_python_sdk.apis.paths.basic_content_content import BasicContentContent
from beamable_python_sdk.apis.paths.basic_content_text import BasicContentText
from beamable_python_sdk.apis.paths.basic_content_manifest import BasicContentManifest
from beamable_python_sdk.apis.paths.basic_content_manifest_public import BasicContentManifestPublic
from beamable_python_sdk.apis.paths.basic_content_manifest_private import BasicContentManifestPrivate
from beamable_python_sdk.apis.paths.basic_content_manifest_checksum import BasicContentManifestChecksum
from beamable_python_sdk.apis.paths.basic_events_content import BasicEventsContent
from beamable_python_sdk.apis.paths.basic_events_calendar import BasicEventsCalendar
from beamable_python_sdk.apis.paths.basic_events_apply_content import BasicEventsApplyContent
from beamable_python_sdk.apis.paths.basic_events_running import BasicEventsRunning
from beamable_python_sdk.apis.paths.object_events_object_id_end_phase import ObjectEventsObjectIdEndPhase
from beamable_python_sdk.apis.paths.object_events_object_id_ping import ObjectEventsObjectIdPing
from beamable_python_sdk.apis.paths.object_events_object_id_content import ObjectEventsObjectIdContent
from beamable_python_sdk.apis.paths.object_events_object_id_refresh import ObjectEventsObjectIdRefresh
from beamable_python_sdk.apis.paths.object_event_players_object_id_claim import ObjectEventPlayersObjectIdClaim
from beamable_python_sdk.apis.paths.object_event_players_object_id_score import ObjectEventPlayersObjectIdScore
from beamable_python_sdk.apis.paths.object_gamerelay_object_id_sync import ObjectGamerelayObjectIdSync
from beamable_python_sdk.apis.paths.object_gamerelay_object_id_results import ObjectGamerelayObjectIdResults
from beamable_python_sdk.apis.paths.object_inventory_object_id_preview import ObjectInventoryObjectIdPreview
from beamable_python_sdk.apis.paths.object_inventory_object_id_multipliers import ObjectInventoryObjectIdMultipliers
from beamable_python_sdk.apis.paths.object_inventory_object_id_transaction import ObjectInventoryObjectIdTransaction
from beamable_python_sdk.apis.paths.object_inventory_object_id_transfer import ObjectInventoryObjectIdTransfer
from beamable_python_sdk.apis.paths.basic_inventory_items import BasicInventoryItems
from beamable_python_sdk.apis.paths.basic_inventory_currency import BasicInventoryCurrency
from beamable_python_sdk.apis.paths.basic_leaderboards_list import BasicLeaderboardsList
from beamable_python_sdk.apis.paths.basic_leaderboards_player import BasicLeaderboardsPlayer
from beamable_python_sdk.apis.paths.basic_leaderboards_assignment import BasicLeaderboardsAssignment
from beamable_python_sdk.apis.paths.basic_leaderboards_uid import BasicLeaderboardsUid
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_entries import ObjectLeaderboardsObjectIdEntries
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_membership import ObjectLeaderboardsObjectIdMembership
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_ranks import ObjectLeaderboardsObjectIdRanks
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_partition import ObjectLeaderboardsObjectIdPartition
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_matches import ObjectLeaderboardsObjectIdMatches
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_assignment import ObjectLeaderboardsObjectIdAssignment
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_entry import ObjectLeaderboardsObjectIdEntry
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_freeze import ObjectLeaderboardsObjectIdFreeze
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_details import ObjectLeaderboardsObjectIdDetails
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_view import ObjectLeaderboardsObjectIdView
from beamable_python_sdk.apis.paths.object_leaderboards_object_id_swap import ObjectLeaderboardsObjectIdSwap
from beamable_python_sdk.apis.paths.basic_groups_search import BasicGroupsSearch
from beamable_python_sdk.apis.paths.object_groups_object_id_role import ObjectGroupsObjectIdRole
from beamable_python_sdk.apis.paths.object_groups_object_id_kick import ObjectGroupsObjectIdKick
from beamable_python_sdk.apis.paths.object_groups_object_id_apply import ObjectGroupsObjectIdApply
from beamable_python_sdk.apis.paths.object_groups_object_id_donations import ObjectGroupsObjectIdDonations
from beamable_python_sdk.apis.paths.object_groups_object_id_member import ObjectGroupsObjectIdMember
from beamable_python_sdk.apis.paths.object_groups_object_id_invite import ObjectGroupsObjectIdInvite
from beamable_python_sdk.apis.paths.object_groups_object_id_petition import ObjectGroupsObjectIdPetition
from beamable_python_sdk.apis.paths.object_group_users_object_id_availability import ObjectGroupUsersObjectIdAvailability
from beamable_python_sdk.apis.paths.object_group_users_object_id_recommended import ObjectGroupUsersObjectIdRecommended
from beamable_python_sdk.apis.paths.object_group_users_object_id_join import ObjectGroupUsersObjectIdJoin
from beamable_python_sdk.apis.paths.object_group_users_object_id_group import ObjectGroupUsersObjectIdGroup
from beamable_python_sdk.apis.paths.object_group_users_object_id_search import ObjectGroupUsersObjectIdSearch
from beamable_python_sdk.apis.paths.basic_mail_attachments import BasicMailAttachments
from beamable_python_sdk.apis.paths.basic_mail_template import BasicMailTemplate
from beamable_python_sdk.apis.paths.basic_mail_bulk import BasicMailBulk
from beamable_python_sdk.apis.paths.object_mail_object_id_detail import ObjectMailObjectIdDetail
from beamable_python_sdk.apis.paths.object_mail_object_id_categories import ObjectMailObjectIdCategories
from beamable_python_sdk.apis.paths.object_mail_object_id_search import ObjectMailObjectIdSearch
from beamable_python_sdk.apis.paths.object_mail_object_id_bulk import ObjectMailObjectIdBulk
from beamable_python_sdk.apis.paths.object_mail_object_id_accept_many import ObjectMailObjectIdAcceptMany
from beamable_python_sdk.apis.paths.object_matchmaking_object_id_tick import ObjectMatchmakingObjectIdTick
from beamable_python_sdk.apis.paths.object_matchmaking_object_id_match import ObjectMatchmakingObjectIdMatch
from beamable_python_sdk.apis.paths.basic_payments_windows_purchase_track import BasicPaymentsWindowsPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_audits import BasicPaymentsAudits
from beamable_python_sdk.apis.paths.basic_payments_windows_purchase_complete import BasicPaymentsWindowsPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_test_purchase_begin import BasicPaymentsTestPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_facebook_update import BasicPaymentsFacebookUpdate
from beamable_python_sdk.apis.paths.basic_payments_steam_purchase_fail import BasicPaymentsSteamPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_facebook_purchase_complete import BasicPaymentsFacebookPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_facebook_purchase_fail import BasicPaymentsFacebookPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_test_purchase_complete import BasicPaymentsTestPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_itunes_product import BasicPaymentsItunesProduct
from beamable_python_sdk.apis.paths.basic_payments_googleplay_purchase_complete import BasicPaymentsGoogleplayPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_test_purchase_track import BasicPaymentsTestPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_googleplay_purchase_begin import BasicPaymentsGoogleplayPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_itunes_purchase_begin import BasicPaymentsItunesPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_facebook_purchase_cancel import BasicPaymentsFacebookPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_coupon_purchase_track import BasicPaymentsCouponPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_steam_purchase_complete import BasicPaymentsSteamPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_facebook_purchase_track import BasicPaymentsFacebookPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_itunes_purchase_fail import BasicPaymentsItunesPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_test_purchase_cancel import BasicPaymentsTestPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_googleplay_purchase_track import BasicPaymentsGoogleplayPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_steam_prices import BasicPaymentsSteamPrices
from beamable_python_sdk.apis.paths.basic_payments_test_purchase_fail import BasicPaymentsTestPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_coupon_purchase_cancel import BasicPaymentsCouponPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_itunes_purchase_complete import BasicPaymentsItunesPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_coupon_purchase_begin import BasicPaymentsCouponPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_steam_purchase_track import BasicPaymentsSteamPurchaseTrack
from beamable_python_sdk.apis.paths.basic_payments_facebook_purchase_begin import BasicPaymentsFacebookPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_steam_order import BasicPaymentsSteamOrder
from beamable_python_sdk.apis.paths.basic_payments_windows_purchase_begin import BasicPaymentsWindowsPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_windows_product import BasicPaymentsWindowsProduct
from beamable_python_sdk.apis.paths.basic_payments_googleplay_purchase_fail import BasicPaymentsGoogleplayPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_facebook_product import BasicPaymentsFacebookProduct
from beamable_python_sdk.apis.paths.basic_payments_googleplay_purchase_cancel import BasicPaymentsGoogleplayPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_coupon_product import BasicPaymentsCouponProduct
from beamable_python_sdk.apis.paths.basic_payments_coupon_purchase_fail import BasicPaymentsCouponPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_steam_purchase_begin import BasicPaymentsSteamPurchaseBegin
from beamable_python_sdk.apis.paths.basic_payments_steam_purchase_cancel import BasicPaymentsSteamPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_steam_auth import BasicPaymentsSteamAuth
from beamable_python_sdk.apis.paths.basic_payments_steam_product import BasicPaymentsSteamProduct
from beamable_python_sdk.apis.paths.basic_payments_coupon_purchase_complete import BasicPaymentsCouponPurchaseComplete
from beamable_python_sdk.apis.paths.basic_payments_windows_purchase_cancel import BasicPaymentsWindowsPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_googleplay_product import BasicPaymentsGoogleplayProduct
from beamable_python_sdk.apis.paths.basic_payments_windows_purchase_fail import BasicPaymentsWindowsPurchaseFail
from beamable_python_sdk.apis.paths.basic_payments_itunes_purchase_cancel import BasicPaymentsItunesPurchaseCancel
from beamable_python_sdk.apis.paths.basic_payments_test_product import BasicPaymentsTestProduct
from beamable_python_sdk.apis.paths.basic_payments_itunes_purchase_track import BasicPaymentsItunesPurchaseTrack
from beamable_python_sdk.apis.paths.basic_push_register import BasicPushRegister
from beamable_python_sdk.apis.paths.basic_push_send import BasicPushSend
from beamable_python_sdk.apis.paths.basic_realms_project_beamable import BasicRealmsProjectBeamable
from beamable_python_sdk.apis.paths.basic_realms_customer_alias_available import BasicRealmsCustomerAliasAvailable
from beamable_python_sdk.apis.paths.basic_realms_project import BasicRealmsProject
from beamable_python_sdk.apis.paths.basic_realms_games import BasicRealmsGames
from beamable_python_sdk.apis.paths.basic_realms_config import BasicRealmsConfig
from beamable_python_sdk.apis.paths.basic_realms_project_rename import BasicRealmsProjectRename
from beamable_python_sdk.apis.paths.basic_realms_plans import BasicRealmsPlans
from beamable_python_sdk.apis.paths.basic_realms_customer import BasicRealmsCustomer
from beamable_python_sdk.apis.paths.basic_realms_launch_message import BasicRealmsLaunchMessage
from beamable_python_sdk.apis.paths.basic_realms_is_customer import BasicRealmsIsCustomer
from beamable_python_sdk.apis.paths.basic_realms_admin_customer import BasicRealmsAdminCustomer
from beamable_python_sdk.apis.paths.basic_realms_game import BasicRealmsGame
from beamable_python_sdk.apis.paths.basic_realms_project_promote import BasicRealmsProjectPromote
from beamable_python_sdk.apis.paths.basic_realms_customers import BasicRealmsCustomers
from beamable_python_sdk.apis.paths.basic_realms_promotion import BasicRealmsPromotion
from beamable_python_sdk.apis.paths.basic_notification_player import BasicNotificationPlayer
from beamable_python_sdk.apis.paths.basic_notification_global import BasicNotificationGlobal
from beamable_python_sdk.apis.paths.basic_notification_custom import BasicNotificationCustom
from beamable_python_sdk.apis.paths.basic_notification_server import BasicNotificationServer
from beamable_python_sdk.apis.paths.basic_notification_generic import BasicNotificationGeneric
from beamable_python_sdk.apis.paths.basic_notification_game import BasicNotificationGame
from beamable_python_sdk.apis.paths.basic_session_history import BasicSessionHistory
from beamable_python_sdk.apis.paths.basic_session_status import BasicSessionStatus
from beamable_python_sdk.apis.paths.basic_session_heartbeat import BasicSessionHeartbeat
from beamable_python_sdk.apis.paths.basic_stats_client_batch import BasicStatsClientBatch
from beamable_python_sdk.apis.paths.basic_stats_batch import BasicStatsBatch
from beamable_python_sdk.apis.paths.basic_stats_search import BasicStatsSearch
from beamable_python_sdk.apis.paths.basic_stats_subscribe import BasicStatsSubscribe
from beamable_python_sdk.apis.paths.object_stats_object_id_client_stringlist import ObjectStatsObjectIdClientStringlist
from beamable_python_sdk.apis.paths.object_stats_object_id_client import ObjectStatsObjectIdClient
from beamable_python_sdk.apis.paths.basic_tournaments_rewards import BasicTournamentsRewards
from beamable_python_sdk.apis.paths.basic_tournaments_global import BasicTournamentsGlobal
from beamable_python_sdk.apis.paths.basic_tournaments_standings import BasicTournamentsStandings
from beamable_python_sdk.apis.paths.basic_tournaments_admin_player import BasicTournamentsAdminPlayer
from beamable_python_sdk.apis.paths.basic_tournaments_me import BasicTournamentsMe
from beamable_python_sdk.apis.paths.basic_tournaments_champions import BasicTournamentsChampions
from beamable_python_sdk.apis.paths.basic_tournaments_score import BasicTournamentsScore
from beamable_python_sdk.apis.paths.basic_social_friends import BasicSocialFriends
from beamable_python_sdk.apis.paths.basic_social_my import BasicSocialMy
from beamable_python_sdk.apis.paths.basic_social_friends_import import BasicSocialFriendsImport
from beamable_python_sdk.apis.paths.basic_social_blocked import BasicSocialBlocked
from beamable_python_sdk.apis.paths.basic_legacy_timers_defs import BasicLegacyTimersDefs
from beamable_python_sdk.apis.paths.basic_legacy_promos_codes import BasicLegacyPromosCodes
from beamable_python_sdk.apis.paths.basic_legacy_promos_claim import BasicLegacyPromosClaim
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs_grant import BasicLegacyEntitlementDefsGrant
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs_revoke import BasicLegacyEntitlementDefsRevoke
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs_upload import BasicLegacyEntitlementDefsUpload
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs_player import BasicLegacyEntitlementDefsPlayer
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs_claim import BasicLegacyEntitlementDefsClaim
from beamable_python_sdk.apis.paths.basic_legacy_cloud_campaigns_schedule import BasicLegacyCloudCampaignsSchedule
from beamable_python_sdk.apis.paths.basic_legacy_cloud_templates import BasicLegacyCloudTemplates
from beamable_python_sdk.apis.paths.basic_legacy_cloud_campaigns import BasicLegacyCloudCampaigns
from beamable_python_sdk.apis.paths.basic_legacy_pvp_defs_file import BasicLegacyPvpDefsFile
from beamable_python_sdk.apis.paths.basic_legacy_shards_accepting import BasicLegacyShardsAccepting
from beamable_python_sdk.apis.paths.basic_legacy_shards_preferred import BasicLegacyShardsPreferred
from beamable_python_sdk.apis.paths.basic_history_apiaccess_url import BasicHistoryApiaccessUrl
from beamable_python_sdk.apis.paths.basic_history_query_url import BasicHistoryQueryUrl
from beamable_python_sdk.apis.paths.basic_history_query import BasicHistoryQuery
from beamable_python_sdk.apis.paths.basic_history_microservices import BasicHistoryMicroservices
from beamable_python_sdk.apis.paths.basic_history_account_roles import BasicHistoryAccountRoles
from beamable_python_sdk.apis.paths.basic_history_apiaccess import BasicHistoryApiaccess
from beamable_python_sdk.apis.paths.basic_history_events import BasicHistoryEvents
from beamable_python_sdk.apis.paths.basic_trials import BasicTrials
from beamable_python_sdk.apis.paths.basic_announcements import BasicAnnouncements
from beamable_python_sdk.apis.paths.object_announcements_object_id import ObjectAnnouncementsObjectId
from beamable_python_sdk.apis.paths.object_calendars_object_id import ObjectCalendarsObjectId
from beamable_python_sdk.apis.paths.object_chat_v2_object_id import ObjectChatV2ObjectId
from beamable_python_sdk.apis.paths.basic_cloudsaving import BasicCloudsaving
from beamable_python_sdk.apis.paths.object_commerce_object_id import ObjectCommerceObjectId
from beamable_python_sdk.apis.paths.basic_content import BasicContent
from beamable_python_sdk.apis.paths.object_events_object_id import ObjectEventsObjectId
from beamable_python_sdk.apis.paths.object_event_players_object_id import ObjectEventPlayersObjectId
from beamable_python_sdk.apis.paths.object_gamerelay_object_id import ObjectGamerelayObjectId
from beamable_python_sdk.apis.paths.object_inventory_object_id import ObjectInventoryObjectId
from beamable_python_sdk.apis.paths.object_leaderboards_object_id import ObjectLeaderboardsObjectId
from beamable_python_sdk.apis.paths.object_groups_object_id import ObjectGroupsObjectId
from beamable_python_sdk.apis.paths.object_group_users_object_id import ObjectGroupUsersObjectId
from beamable_python_sdk.apis.paths.basic_mail import BasicMail
from beamable_python_sdk.apis.paths.object_mail_object_id import ObjectMailObjectId
from beamable_python_sdk.apis.paths.object_payments_object_id import ObjectPaymentsObjectId
from beamable_python_sdk.apis.paths.basic_notification import BasicNotification
from beamable_python_sdk.apis.paths.basic_session import BasicSession
from beamable_python_sdk.apis.paths.object_stats_object_id import ObjectStatsObjectId
from beamable_python_sdk.apis.paths.basic_tournaments import BasicTournaments
from beamable_python_sdk.apis.paths.object_tournaments_object_id import ObjectTournamentsObjectId
from beamable_python_sdk.apis.paths.basic_legacy_timers import BasicLegacyTimers
from beamable_python_sdk.apis.paths.basic_legacy_promos import BasicLegacyPromos
from beamable_python_sdk.apis.paths.basic_legacy_entitlement_defs import BasicLegacyEntitlementDefs
from beamable_python_sdk.apis.paths.basic_legacy_pvp_defs import BasicLegacyPvpDefs
from beamable_python_sdk.apis.paths.basic_legacy_shards import BasicLegacyShards

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BASIC_TRIALS_ADMIN_DATA: BasicTrialsAdminData,
        PathValues.BASIC_TRIALS_DATA: BasicTrialsData,
        PathValues.BASIC_TRIALS_PAUSE: BasicTrialsPause,
        PathValues.BASIC_TRIALS_SCHEDULE: BasicTrialsSchedule,
        PathValues.BASIC_TRIALS_ADMIN: BasicTrialsAdmin,
        PathValues.BASIC_TRIALS_START: BasicTrialsStart,
        PathValues.BASIC_ACCOUNTS_ME_DEVICE: BasicAccountsMeDevice,
        PathValues.BASIC_ACCOUNTS_ME: BasicAccountsMe,
        PathValues.BASIC_ACCOUNTS_ME_THIRDPARTY: BasicAccountsMeThirdParty,
        PathValues.BASIC_ACCOUNTS_GETPERSONALLYIDENTIFIABLEINFORMATION: BasicAccountsGetPersonallyIdentifiableInformation,
        PathValues.BASIC_ACCOUNTS_SEARCH: BasicAccountsSearch,
        PathValues.BASIC_ACCOUNTS_EMAILUPDATE_INIT: BasicAccountsEmailUpdateInit,
        PathValues.BASIC_ACCOUNTS_EMAILUPDATE_CONFIRM: BasicAccountsEmailUpdateConfirm,
        PathValues.BASIC_ACCOUNTS_AVAILABLE_THIRDPARTY: BasicAccountsAvailableThirdParty,
        PathValues.BASIC_ACCOUNTS_ADMIN_ADMINUSER: BasicAccountsAdminAdminUser,
        PathValues.BASIC_ACCOUNTS_REGISTER: BasicAccountsRegister,
        PathValues.BASIC_ACCOUNTS_ADMIN_ME: BasicAccountsAdminMe,
        PathValues.BASIC_ACCOUNTS_PASSWORDUPDATE_INIT: BasicAccountsPasswordUpdateInit,
        PathValues.BASIC_ACCOUNTS_ADMIN_ADMINUSERS: BasicAccountsAdminAdminUsers,
        PathValues.BASIC_ACCOUNTS_FIND: BasicAccountsFind,
        PathValues.BASIC_ACCOUNTS_AVAILABLE_DEVICEID: BasicAccountsAvailableDeviceId,
        PathValues.BASIC_ACCOUNTS_AVAILABLE: BasicAccountsAvailable,
        PathValues.BASIC_ACCOUNTS_PASSWORDUPDATE_CONFIRM: BasicAccountsPasswordUpdateConfirm,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_EMAIL: ObjectAccountsObjectIdAdminEmail,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_AVAILABLEROLES: ObjectAccountsObjectIdAvailableRoles,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ROLE: ObjectAccountsObjectIdRole,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_SCOPE: ObjectAccountsObjectIdAdminScope,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_THIRDPARTY: ObjectAccountsObjectIdAdminThirdParty,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_FORGET: ObjectAccountsObjectIdAdminForget,
        PathValues.BASIC_ANNOUNCEMENTS_SEARCH: BasicAnnouncementsSearch,
        PathValues.BASIC_ANNOUNCEMENTS_CONTENT: BasicAnnouncementsContent,
        PathValues.BASIC_ANNOUNCEMENTS_LIST: BasicAnnouncementsList,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_READ: ObjectAnnouncementsObjectIdRead,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_CLAIM: ObjectAnnouncementsObjectIdClaim,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_RAW: ObjectAnnouncementsObjectIdRaw,
        PathValues.BASIC_AUTH_TOKEN: BasicAuthToken,
        PathValues.OBJECT_CALENDARS_OBJECT_ID_CLAIM: ObjectCalendarsObjectIdClaim,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID_ROOMS: ObjectChatV2ObjectIdRooms,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID_MESSAGES: ObjectChatV2ObjectIdMessages,
        PathValues.BASIC_CLOUDSAVING_DATA_REPLACE: BasicCloudsavingDataReplace,
        PathValues.BASIC_CLOUDSAVING_DATA: BasicCloudsavingData,
        PathValues.BASIC_CLOUDSAVING_DATA_DOWNLOAD_URL: BasicCloudsavingDataDownloadURL,
        PathValues.BASIC_CLOUDSAVING_DATA_METADATA: BasicCloudsavingDataMetadata,
        PathValues.BASIC_CLOUDSAVING_DATA_MOVE: BasicCloudsavingDataMove,
        PathValues.BASIC_CLOUDSAVING_DATA_UPLOAD_URLFROM_PORTAL: BasicCloudsavingDataUploadURLFromPortal,
        PathValues.BASIC_CLOUDSAVING_DATA_COMMIT_MANIFEST: BasicCloudsavingDataCommitManifest,
        PathValues.BASIC_CLOUDSAVING_DATA_UPLOAD_URL: BasicCloudsavingDataUploadURL,
        PathValues.BASIC_COMMERCE_CATALOG: BasicCommerceCatalog,
        PathValues.BASIC_COMMERCE_SKUS: BasicCommerceSkus,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_COUPONS_COUNT: ObjectCommerceObjectIdCouponsCount,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_OFFERS_ADMIN: ObjectCommerceObjectIdOffersAdmin,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_PURCHASE: ObjectCommerceObjectIdPurchase,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_LISTINGS: ObjectCommerceObjectIdListings,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_STATUS: ObjectCommerceObjectIdStatus,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_COUPONS: ObjectCommerceObjectIdCoupons,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_STATS_UPDATE: ObjectCommerceObjectIdStatsUpdate,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_OFFERS: ObjectCommerceObjectIdOffers,
        PathValues.BASIC_CONTENT_MANIFEST_PULL: BasicContentManifestPull,
        PathValues.BASIC_CONTENT_CONTENT: BasicContentContent,
        PathValues.BASIC_CONTENT_TEXT: BasicContentText,
        PathValues.BASIC_CONTENT_MANIFEST: BasicContentManifest,
        PathValues.BASIC_CONTENT_MANIFEST_PUBLIC: BasicContentManifestPublic,
        PathValues.BASIC_CONTENT_MANIFEST_PRIVATE: BasicContentManifestPrivate,
        PathValues.BASIC_CONTENT_MANIFEST_CHECKSUM: BasicContentManifestChecksum,
        PathValues.BASIC_EVENTS_CONTENT: BasicEventsContent,
        PathValues.BASIC_EVENTS_CALENDAR: BasicEventsCalendar,
        PathValues.BASIC_EVENTS_APPLY_CONTENT: BasicEventsApplyContent,
        PathValues.BASIC_EVENTS_RUNNING: BasicEventsRunning,
        PathValues.OBJECT_EVENTS_OBJECT_ID_END_PHASE: ObjectEventsObjectIdEndPhase,
        PathValues.OBJECT_EVENTS_OBJECT_ID_PING: ObjectEventsObjectIdPing,
        PathValues.OBJECT_EVENTS_OBJECT_ID_CONTENT: ObjectEventsObjectIdContent,
        PathValues.OBJECT_EVENTS_OBJECT_ID_REFRESH: ObjectEventsObjectIdRefresh,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID_CLAIM: ObjectEventPlayersObjectIdClaim,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID_SCORE: ObjectEventPlayersObjectIdScore,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID_SYNC: ObjectGamerelayObjectIdSync,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID_RESULTS: ObjectGamerelayObjectIdResults,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_PREVIEW: ObjectInventoryObjectIdPreview,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_MULTIPLIERS: ObjectInventoryObjectIdMultipliers,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_TRANSACTION: ObjectInventoryObjectIdTransaction,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_TRANSFER: ObjectInventoryObjectIdTransfer,
        PathValues.BASIC_INVENTORY_ITEMS: BasicInventoryItems,
        PathValues.BASIC_INVENTORY_CURRENCY: BasicInventoryCurrency,
        PathValues.BASIC_LEADERBOARDS_LIST: BasicLeaderboardsList,
        PathValues.BASIC_LEADERBOARDS_PLAYER: BasicLeaderboardsPlayer,
        PathValues.BASIC_LEADERBOARDS_ASSIGNMENT: BasicLeaderboardsAssignment,
        PathValues.BASIC_LEADERBOARDS_UID: BasicLeaderboardsUid,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ENTRIES: ObjectLeaderboardsObjectIdEntries,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_MEMBERSHIP: ObjectLeaderboardsObjectIdMembership,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_RANKS: ObjectLeaderboardsObjectIdRanks,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_PARTITION: ObjectLeaderboardsObjectIdPartition,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_MATCHES: ObjectLeaderboardsObjectIdMatches,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ASSIGNMENT: ObjectLeaderboardsObjectIdAssignment,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ENTRY: ObjectLeaderboardsObjectIdEntry,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_FREEZE: ObjectLeaderboardsObjectIdFreeze,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_DETAILS: ObjectLeaderboardsObjectIdDetails,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_VIEW: ObjectLeaderboardsObjectIdView,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_SWAP: ObjectLeaderboardsObjectIdSwap,
        PathValues.BASIC_GROUPS_SEARCH: BasicGroupsSearch,
        PathValues.OBJECT_GROUPS_OBJECT_ID_ROLE: ObjectGroupsObjectIdRole,
        PathValues.OBJECT_GROUPS_OBJECT_ID_KICK: ObjectGroupsObjectIdKick,
        PathValues.OBJECT_GROUPS_OBJECT_ID_APPLY: ObjectGroupsObjectIdApply,
        PathValues.OBJECT_GROUPS_OBJECT_ID_DONATIONS: ObjectGroupsObjectIdDonations,
        PathValues.OBJECT_GROUPS_OBJECT_ID_MEMBER: ObjectGroupsObjectIdMember,
        PathValues.OBJECT_GROUPS_OBJECT_ID_INVITE: ObjectGroupsObjectIdInvite,
        PathValues.OBJECT_GROUPS_OBJECT_ID_PETITION: ObjectGroupsObjectIdPetition,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_AVAILABILITY: ObjectGroupUsersObjectIdAvailability,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_RECOMMENDED: ObjectGroupUsersObjectIdRecommended,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_JOIN: ObjectGroupUsersObjectIdJoin,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_GROUP: ObjectGroupUsersObjectIdGroup,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_SEARCH: ObjectGroupUsersObjectIdSearch,
        PathValues.BASIC_MAIL_ATTACHMENTS: BasicMailAttachments,
        PathValues.BASIC_MAIL_TEMPLATE: BasicMailTemplate,
        PathValues.BASIC_MAIL_BULK: BasicMailBulk,
        PathValues.OBJECT_MAIL_OBJECT_ID_DETAIL: ObjectMailObjectIdDetail,
        PathValues.OBJECT_MAIL_OBJECT_ID_CATEGORIES: ObjectMailObjectIdCategories,
        PathValues.OBJECT_MAIL_OBJECT_ID_SEARCH: ObjectMailObjectIdSearch,
        PathValues.OBJECT_MAIL_OBJECT_ID_BULK: ObjectMailObjectIdBulk,
        PathValues.OBJECT_MAIL_OBJECT_ID_ACCEPT_MANY: ObjectMailObjectIdAcceptMany,
        PathValues.OBJECT_MATCHMAKING_OBJECT_ID_TICK: ObjectMatchmakingObjectIdTick,
        PathValues.OBJECT_MATCHMAKING_OBJECT_ID_MATCH: ObjectMatchmakingObjectIdMatch,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_TRACK: BasicPaymentsWindowsPurchaseTrack,
        PathValues.BASIC_PAYMENTS_AUDITS: BasicPaymentsAudits,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_COMPLETE: BasicPaymentsWindowsPurchaseComplete,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_BEGIN: BasicPaymentsTestPurchaseBegin,
        PathValues.BASIC_PAYMENTS_FACEBOOK_UPDATE: BasicPaymentsFacebookUpdate,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_FAIL: BasicPaymentsSteamPurchaseFail,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_COMPLETE: BasicPaymentsFacebookPurchaseComplete,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_FAIL: BasicPaymentsFacebookPurchaseFail,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_COMPLETE: BasicPaymentsTestPurchaseComplete,
        PathValues.BASIC_PAYMENTS_ITUNES_PRODUCT: BasicPaymentsItunesProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_COMPLETE: BasicPaymentsGoogleplayPurchaseComplete,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_TRACK: BasicPaymentsTestPurchaseTrack,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_BEGIN: BasicPaymentsGoogleplayPurchaseBegin,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_BEGIN: BasicPaymentsItunesPurchaseBegin,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_CANCEL: BasicPaymentsFacebookPurchaseCancel,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_TRACK: BasicPaymentsCouponPurchaseTrack,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_COMPLETE: BasicPaymentsSteamPurchaseComplete,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_TRACK: BasicPaymentsFacebookPurchaseTrack,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_FAIL: BasicPaymentsItunesPurchaseFail,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_CANCEL: BasicPaymentsTestPurchaseCancel,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_TRACK: BasicPaymentsGoogleplayPurchaseTrack,
        PathValues.BASIC_PAYMENTS_STEAM_PRICES: BasicPaymentsSteamPrices,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_FAIL: BasicPaymentsTestPurchaseFail,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_CANCEL: BasicPaymentsCouponPurchaseCancel,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_COMPLETE: BasicPaymentsItunesPurchaseComplete,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_BEGIN: BasicPaymentsCouponPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_TRACK: BasicPaymentsSteamPurchaseTrack,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_BEGIN: BasicPaymentsFacebookPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_ORDER: BasicPaymentsSteamOrder,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_BEGIN: BasicPaymentsWindowsPurchaseBegin,
        PathValues.BASIC_PAYMENTS_WINDOWS_PRODUCT: BasicPaymentsWindowsProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_FAIL: BasicPaymentsGoogleplayPurchaseFail,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PRODUCT: BasicPaymentsFacebookProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_CANCEL: BasicPaymentsGoogleplayPurchaseCancel,
        PathValues.BASIC_PAYMENTS_COUPON_PRODUCT: BasicPaymentsCouponProduct,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_FAIL: BasicPaymentsCouponPurchaseFail,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_BEGIN: BasicPaymentsSteamPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_CANCEL: BasicPaymentsSteamPurchaseCancel,
        PathValues.BASIC_PAYMENTS_STEAM_AUTH: BasicPaymentsSteamAuth,
        PathValues.BASIC_PAYMENTS_STEAM_PRODUCT: BasicPaymentsSteamProduct,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_COMPLETE: BasicPaymentsCouponPurchaseComplete,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_CANCEL: BasicPaymentsWindowsPurchaseCancel,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PRODUCT: BasicPaymentsGoogleplayProduct,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_FAIL: BasicPaymentsWindowsPurchaseFail,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_CANCEL: BasicPaymentsItunesPurchaseCancel,
        PathValues.BASIC_PAYMENTS_TEST_PRODUCT: BasicPaymentsTestProduct,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_TRACK: BasicPaymentsItunesPurchaseTrack,
        PathValues.BASIC_PUSH_REGISTER: BasicPushRegister,
        PathValues.BASIC_PUSH_SEND: BasicPushSend,
        PathValues.BASIC_REALMS_PROJECT_BEAMABLE: BasicRealmsProjectBeamable,
        PathValues.BASIC_REALMS_CUSTOMER_ALIAS_AVAILABLE: BasicRealmsCustomerAliasAvailable,
        PathValues.BASIC_REALMS_PROJECT: BasicRealmsProject,
        PathValues.BASIC_REALMS_GAMES: BasicRealmsGames,
        PathValues.BASIC_REALMS_CONFIG: BasicRealmsConfig,
        PathValues.BASIC_REALMS_PROJECT_RENAME: BasicRealmsProjectRename,
        PathValues.BASIC_REALMS_PLANS: BasicRealmsPlans,
        PathValues.BASIC_REALMS_CUSTOMER: BasicRealmsCustomer,
        PathValues.BASIC_REALMS_LAUNCHMESSAGE: BasicRealmsLaunchMessage,
        PathValues.BASIC_REALMS_ISCUSTOMER: BasicRealmsIsCustomer,
        PathValues.BASIC_REALMS_ADMIN_CUSTOMER: BasicRealmsAdminCustomer,
        PathValues.BASIC_REALMS_GAME: BasicRealmsGame,
        PathValues.BASIC_REALMS_PROJECT_PROMOTE: BasicRealmsProjectPromote,
        PathValues.BASIC_REALMS_CUSTOMERS: BasicRealmsCustomers,
        PathValues.BASIC_REALMS_PROMOTION: BasicRealmsPromotion,
        PathValues.BASIC_NOTIFICATION_PLAYER: BasicNotificationPlayer,
        PathValues.BASIC_NOTIFICATION_GLOBAL: BasicNotificationGlobal,
        PathValues.BASIC_NOTIFICATION_CUSTOM: BasicNotificationCustom,
        PathValues.BASIC_NOTIFICATION_SERVER: BasicNotificationServer,
        PathValues.BASIC_NOTIFICATION_GENERIC: BasicNotificationGeneric,
        PathValues.BASIC_NOTIFICATION_GAME: BasicNotificationGame,
        PathValues.BASIC_SESSION_HISTORY: BasicSessionHistory,
        PathValues.BASIC_SESSION_STATUS: BasicSessionStatus,
        PathValues.BASIC_SESSION_HEARTBEAT: BasicSessionHeartbeat,
        PathValues.BASIC_STATS_CLIENT_BATCH: BasicStatsClientBatch,
        PathValues.BASIC_STATS_BATCH: BasicStatsBatch,
        PathValues.BASIC_STATS_SEARCH: BasicStatsSearch,
        PathValues.BASIC_STATS_SUBSCRIBE: BasicStatsSubscribe,
        PathValues.OBJECT_STATS_OBJECT_ID_CLIENT_STRINGLIST: ObjectStatsObjectIdClientStringlist,
        PathValues.OBJECT_STATS_OBJECT_ID_CLIENT: ObjectStatsObjectIdClient,
        PathValues.BASIC_TOURNAMENTS_REWARDS: BasicTournamentsRewards,
        PathValues.BASIC_TOURNAMENTS_GLOBAL: BasicTournamentsGlobal,
        PathValues.BASIC_TOURNAMENTS_STANDINGS: BasicTournamentsStandings,
        PathValues.BASIC_TOURNAMENTS_ADMIN_PLAYER: BasicTournamentsAdminPlayer,
        PathValues.BASIC_TOURNAMENTS_ME: BasicTournamentsMe,
        PathValues.BASIC_TOURNAMENTS_CHAMPIONS: BasicTournamentsChampions,
        PathValues.BASIC_TOURNAMENTS_SCORE: BasicTournamentsScore,
        PathValues.BASIC_SOCIAL_FRIENDS: BasicSocialFriends,
        PathValues.BASIC_SOCIAL_MY: BasicSocialMy,
        PathValues.BASIC_SOCIAL_FRIENDS_IMPORT: BasicSocialFriendsImport,
        PathValues.BASIC_SOCIAL_BLOCKED: BasicSocialBlocked,
        PathValues.BASIC_LEGACYTIMERS_DEFS: BasicLegacyTimersDefs,
        PathValues.BASIC_LEGACYPROMOS_CODES: BasicLegacyPromosCodes,
        PathValues.BASIC_LEGACYPROMOS_CLAIM: BasicLegacyPromosClaim,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_GRANT: BasicLegacyEntitlementDefsGrant,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_REVOKE: BasicLegacyEntitlementDefsRevoke,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_UPLOAD: BasicLegacyEntitlementDefsUpload,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_PLAYER: BasicLegacyEntitlementDefsPlayer,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_CLAIM: BasicLegacyEntitlementDefsClaim,
        PathValues.BASIC_LEGACYCLOUD_CAMPAIGNS_SCHEDULE: BasicLegacyCloudCampaignsSchedule,
        PathValues.BASIC_LEGACYCLOUD_TEMPLATES: BasicLegacyCloudTemplates,
        PathValues.BASIC_LEGACYCLOUD_CAMPAIGNS: BasicLegacyCloudCampaigns,
        PathValues.BASIC_LEGACYPVPDEFS_FILE: BasicLegacyPvpDefsFile,
        PathValues.BASIC_LEGACYSHARDS_ACCEPTING: BasicLegacyShardsAccepting,
        PathValues.BASIC_LEGACYSHARDS_PREFERRED: BasicLegacyShardsPreferred,
        PathValues.BASIC_HISTORY_APIACCESS_URL: BasicHistoryApiaccessUrl,
        PathValues.BASIC_HISTORY_QUERY_URL: BasicHistoryQueryUrl,
        PathValues.BASIC_HISTORY_QUERY: BasicHistoryQuery,
        PathValues.BASIC_HISTORY_MICROSERVICES: BasicHistoryMicroservices,
        PathValues.BASIC_HISTORY_ACCOUNT_ROLES: BasicHistoryAccountRoles,
        PathValues.BASIC_HISTORY_APIACCESS: BasicHistoryApiaccess,
        PathValues.BASIC_HISTORY_EVENTS: BasicHistoryEvents,
        PathValues.BASIC_TRIALS: BasicTrials,
        PathValues.BASIC_ANNOUNCEMENTS: BasicAnnouncements,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID: ObjectAnnouncementsObjectId,
        PathValues.OBJECT_CALENDARS_OBJECT_ID: ObjectCalendarsObjectId,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID: ObjectChatV2ObjectId,
        PathValues.BASIC_CLOUDSAVING: BasicCloudsaving,
        PathValues.OBJECT_COMMERCE_OBJECT_ID: ObjectCommerceObjectId,
        PathValues.BASIC_CONTENT: BasicContent,
        PathValues.OBJECT_EVENTS_OBJECT_ID: ObjectEventsObjectId,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID: ObjectEventPlayersObjectId,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID: ObjectGamerelayObjectId,
        PathValues.OBJECT_INVENTORY_OBJECT_ID: ObjectInventoryObjectId,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID: ObjectLeaderboardsObjectId,
        PathValues.OBJECT_GROUPS_OBJECT_ID: ObjectGroupsObjectId,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID: ObjectGroupUsersObjectId,
        PathValues.BASIC_MAIL: BasicMail,
        PathValues.OBJECT_MAIL_OBJECT_ID: ObjectMailObjectId,
        PathValues.OBJECT_PAYMENTS_OBJECT_ID: ObjectPaymentsObjectId,
        PathValues.BASIC_NOTIFICATION: BasicNotification,
        PathValues.BASIC_SESSION: BasicSession,
        PathValues.OBJECT_STATS_OBJECT_ID: ObjectStatsObjectId,
        PathValues.BASIC_TOURNAMENTS: BasicTournaments,
        PathValues.OBJECT_TOURNAMENTS_OBJECT_ID: ObjectTournamentsObjectId,
        PathValues.BASIC_LEGACYTIMERS: BasicLegacyTimers,
        PathValues.BASIC_LEGACYPROMOS: BasicLegacyPromos,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS: BasicLegacyEntitlementDefs,
        PathValues.BASIC_LEGACYPVPDEFS: BasicLegacyPvpDefs,
        PathValues.BASIC_LEGACYSHARDS: BasicLegacyShards,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BASIC_TRIALS_ADMIN_DATA: BasicTrialsAdminData,
        PathValues.BASIC_TRIALS_DATA: BasicTrialsData,
        PathValues.BASIC_TRIALS_PAUSE: BasicTrialsPause,
        PathValues.BASIC_TRIALS_SCHEDULE: BasicTrialsSchedule,
        PathValues.BASIC_TRIALS_ADMIN: BasicTrialsAdmin,
        PathValues.BASIC_TRIALS_START: BasicTrialsStart,
        PathValues.BASIC_ACCOUNTS_ME_DEVICE: BasicAccountsMeDevice,
        PathValues.BASIC_ACCOUNTS_ME: BasicAccountsMe,
        PathValues.BASIC_ACCOUNTS_ME_THIRDPARTY: BasicAccountsMeThirdParty,
        PathValues.BASIC_ACCOUNTS_GETPERSONALLYIDENTIFIABLEINFORMATION: BasicAccountsGetPersonallyIdentifiableInformation,
        PathValues.BASIC_ACCOUNTS_SEARCH: BasicAccountsSearch,
        PathValues.BASIC_ACCOUNTS_EMAILUPDATE_INIT: BasicAccountsEmailUpdateInit,
        PathValues.BASIC_ACCOUNTS_EMAILUPDATE_CONFIRM: BasicAccountsEmailUpdateConfirm,
        PathValues.BASIC_ACCOUNTS_AVAILABLE_THIRDPARTY: BasicAccountsAvailableThirdParty,
        PathValues.BASIC_ACCOUNTS_ADMIN_ADMINUSER: BasicAccountsAdminAdminUser,
        PathValues.BASIC_ACCOUNTS_REGISTER: BasicAccountsRegister,
        PathValues.BASIC_ACCOUNTS_ADMIN_ME: BasicAccountsAdminMe,
        PathValues.BASIC_ACCOUNTS_PASSWORDUPDATE_INIT: BasicAccountsPasswordUpdateInit,
        PathValues.BASIC_ACCOUNTS_ADMIN_ADMINUSERS: BasicAccountsAdminAdminUsers,
        PathValues.BASIC_ACCOUNTS_FIND: BasicAccountsFind,
        PathValues.BASIC_ACCOUNTS_AVAILABLE_DEVICEID: BasicAccountsAvailableDeviceId,
        PathValues.BASIC_ACCOUNTS_AVAILABLE: BasicAccountsAvailable,
        PathValues.BASIC_ACCOUNTS_PASSWORDUPDATE_CONFIRM: BasicAccountsPasswordUpdateConfirm,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_EMAIL: ObjectAccountsObjectIdAdminEmail,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_AVAILABLEROLES: ObjectAccountsObjectIdAvailableRoles,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ROLE: ObjectAccountsObjectIdRole,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_SCOPE: ObjectAccountsObjectIdAdminScope,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_THIRDPARTY: ObjectAccountsObjectIdAdminThirdParty,
        PathValues.OBJECT_ACCOUNTS_OBJECT_ID_ADMIN_FORGET: ObjectAccountsObjectIdAdminForget,
        PathValues.BASIC_ANNOUNCEMENTS_SEARCH: BasicAnnouncementsSearch,
        PathValues.BASIC_ANNOUNCEMENTS_CONTENT: BasicAnnouncementsContent,
        PathValues.BASIC_ANNOUNCEMENTS_LIST: BasicAnnouncementsList,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_READ: ObjectAnnouncementsObjectIdRead,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_CLAIM: ObjectAnnouncementsObjectIdClaim,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID_RAW: ObjectAnnouncementsObjectIdRaw,
        PathValues.BASIC_AUTH_TOKEN: BasicAuthToken,
        PathValues.OBJECT_CALENDARS_OBJECT_ID_CLAIM: ObjectCalendarsObjectIdClaim,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID_ROOMS: ObjectChatV2ObjectIdRooms,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID_MESSAGES: ObjectChatV2ObjectIdMessages,
        PathValues.BASIC_CLOUDSAVING_DATA_REPLACE: BasicCloudsavingDataReplace,
        PathValues.BASIC_CLOUDSAVING_DATA: BasicCloudsavingData,
        PathValues.BASIC_CLOUDSAVING_DATA_DOWNLOAD_URL: BasicCloudsavingDataDownloadURL,
        PathValues.BASIC_CLOUDSAVING_DATA_METADATA: BasicCloudsavingDataMetadata,
        PathValues.BASIC_CLOUDSAVING_DATA_MOVE: BasicCloudsavingDataMove,
        PathValues.BASIC_CLOUDSAVING_DATA_UPLOAD_URLFROM_PORTAL: BasicCloudsavingDataUploadURLFromPortal,
        PathValues.BASIC_CLOUDSAVING_DATA_COMMIT_MANIFEST: BasicCloudsavingDataCommitManifest,
        PathValues.BASIC_CLOUDSAVING_DATA_UPLOAD_URL: BasicCloudsavingDataUploadURL,
        PathValues.BASIC_COMMERCE_CATALOG: BasicCommerceCatalog,
        PathValues.BASIC_COMMERCE_SKUS: BasicCommerceSkus,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_COUPONS_COUNT: ObjectCommerceObjectIdCouponsCount,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_OFFERS_ADMIN: ObjectCommerceObjectIdOffersAdmin,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_PURCHASE: ObjectCommerceObjectIdPurchase,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_LISTINGS: ObjectCommerceObjectIdListings,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_STATUS: ObjectCommerceObjectIdStatus,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_COUPONS: ObjectCommerceObjectIdCoupons,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_STATS_UPDATE: ObjectCommerceObjectIdStatsUpdate,
        PathValues.OBJECT_COMMERCE_OBJECT_ID_OFFERS: ObjectCommerceObjectIdOffers,
        PathValues.BASIC_CONTENT_MANIFEST_PULL: BasicContentManifestPull,
        PathValues.BASIC_CONTENT_CONTENT: BasicContentContent,
        PathValues.BASIC_CONTENT_TEXT: BasicContentText,
        PathValues.BASIC_CONTENT_MANIFEST: BasicContentManifest,
        PathValues.BASIC_CONTENT_MANIFEST_PUBLIC: BasicContentManifestPublic,
        PathValues.BASIC_CONTENT_MANIFEST_PRIVATE: BasicContentManifestPrivate,
        PathValues.BASIC_CONTENT_MANIFEST_CHECKSUM: BasicContentManifestChecksum,
        PathValues.BASIC_EVENTS_CONTENT: BasicEventsContent,
        PathValues.BASIC_EVENTS_CALENDAR: BasicEventsCalendar,
        PathValues.BASIC_EVENTS_APPLY_CONTENT: BasicEventsApplyContent,
        PathValues.BASIC_EVENTS_RUNNING: BasicEventsRunning,
        PathValues.OBJECT_EVENTS_OBJECT_ID_END_PHASE: ObjectEventsObjectIdEndPhase,
        PathValues.OBJECT_EVENTS_OBJECT_ID_PING: ObjectEventsObjectIdPing,
        PathValues.OBJECT_EVENTS_OBJECT_ID_CONTENT: ObjectEventsObjectIdContent,
        PathValues.OBJECT_EVENTS_OBJECT_ID_REFRESH: ObjectEventsObjectIdRefresh,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID_CLAIM: ObjectEventPlayersObjectIdClaim,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID_SCORE: ObjectEventPlayersObjectIdScore,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID_SYNC: ObjectGamerelayObjectIdSync,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID_RESULTS: ObjectGamerelayObjectIdResults,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_PREVIEW: ObjectInventoryObjectIdPreview,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_MULTIPLIERS: ObjectInventoryObjectIdMultipliers,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_TRANSACTION: ObjectInventoryObjectIdTransaction,
        PathValues.OBJECT_INVENTORY_OBJECT_ID_TRANSFER: ObjectInventoryObjectIdTransfer,
        PathValues.BASIC_INVENTORY_ITEMS: BasicInventoryItems,
        PathValues.BASIC_INVENTORY_CURRENCY: BasicInventoryCurrency,
        PathValues.BASIC_LEADERBOARDS_LIST: BasicLeaderboardsList,
        PathValues.BASIC_LEADERBOARDS_PLAYER: BasicLeaderboardsPlayer,
        PathValues.BASIC_LEADERBOARDS_ASSIGNMENT: BasicLeaderboardsAssignment,
        PathValues.BASIC_LEADERBOARDS_UID: BasicLeaderboardsUid,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ENTRIES: ObjectLeaderboardsObjectIdEntries,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_MEMBERSHIP: ObjectLeaderboardsObjectIdMembership,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_RANKS: ObjectLeaderboardsObjectIdRanks,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_PARTITION: ObjectLeaderboardsObjectIdPartition,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_MATCHES: ObjectLeaderboardsObjectIdMatches,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ASSIGNMENT: ObjectLeaderboardsObjectIdAssignment,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_ENTRY: ObjectLeaderboardsObjectIdEntry,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_FREEZE: ObjectLeaderboardsObjectIdFreeze,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_DETAILS: ObjectLeaderboardsObjectIdDetails,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_VIEW: ObjectLeaderboardsObjectIdView,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID_SWAP: ObjectLeaderboardsObjectIdSwap,
        PathValues.BASIC_GROUPS_SEARCH: BasicGroupsSearch,
        PathValues.OBJECT_GROUPS_OBJECT_ID_ROLE: ObjectGroupsObjectIdRole,
        PathValues.OBJECT_GROUPS_OBJECT_ID_KICK: ObjectGroupsObjectIdKick,
        PathValues.OBJECT_GROUPS_OBJECT_ID_APPLY: ObjectGroupsObjectIdApply,
        PathValues.OBJECT_GROUPS_OBJECT_ID_DONATIONS: ObjectGroupsObjectIdDonations,
        PathValues.OBJECT_GROUPS_OBJECT_ID_MEMBER: ObjectGroupsObjectIdMember,
        PathValues.OBJECT_GROUPS_OBJECT_ID_INVITE: ObjectGroupsObjectIdInvite,
        PathValues.OBJECT_GROUPS_OBJECT_ID_PETITION: ObjectGroupsObjectIdPetition,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_AVAILABILITY: ObjectGroupUsersObjectIdAvailability,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_RECOMMENDED: ObjectGroupUsersObjectIdRecommended,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_JOIN: ObjectGroupUsersObjectIdJoin,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_GROUP: ObjectGroupUsersObjectIdGroup,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID_SEARCH: ObjectGroupUsersObjectIdSearch,
        PathValues.BASIC_MAIL_ATTACHMENTS: BasicMailAttachments,
        PathValues.BASIC_MAIL_TEMPLATE: BasicMailTemplate,
        PathValues.BASIC_MAIL_BULK: BasicMailBulk,
        PathValues.OBJECT_MAIL_OBJECT_ID_DETAIL: ObjectMailObjectIdDetail,
        PathValues.OBJECT_MAIL_OBJECT_ID_CATEGORIES: ObjectMailObjectIdCategories,
        PathValues.OBJECT_MAIL_OBJECT_ID_SEARCH: ObjectMailObjectIdSearch,
        PathValues.OBJECT_MAIL_OBJECT_ID_BULK: ObjectMailObjectIdBulk,
        PathValues.OBJECT_MAIL_OBJECT_ID_ACCEPT_MANY: ObjectMailObjectIdAcceptMany,
        PathValues.OBJECT_MATCHMAKING_OBJECT_ID_TICK: ObjectMatchmakingObjectIdTick,
        PathValues.OBJECT_MATCHMAKING_OBJECT_ID_MATCH: ObjectMatchmakingObjectIdMatch,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_TRACK: BasicPaymentsWindowsPurchaseTrack,
        PathValues.BASIC_PAYMENTS_AUDITS: BasicPaymentsAudits,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_COMPLETE: BasicPaymentsWindowsPurchaseComplete,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_BEGIN: BasicPaymentsTestPurchaseBegin,
        PathValues.BASIC_PAYMENTS_FACEBOOK_UPDATE: BasicPaymentsFacebookUpdate,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_FAIL: BasicPaymentsSteamPurchaseFail,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_COMPLETE: BasicPaymentsFacebookPurchaseComplete,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_FAIL: BasicPaymentsFacebookPurchaseFail,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_COMPLETE: BasicPaymentsTestPurchaseComplete,
        PathValues.BASIC_PAYMENTS_ITUNES_PRODUCT: BasicPaymentsItunesProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_COMPLETE: BasicPaymentsGoogleplayPurchaseComplete,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_TRACK: BasicPaymentsTestPurchaseTrack,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_BEGIN: BasicPaymentsGoogleplayPurchaseBegin,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_BEGIN: BasicPaymentsItunesPurchaseBegin,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_CANCEL: BasicPaymentsFacebookPurchaseCancel,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_TRACK: BasicPaymentsCouponPurchaseTrack,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_COMPLETE: BasicPaymentsSteamPurchaseComplete,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_TRACK: BasicPaymentsFacebookPurchaseTrack,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_FAIL: BasicPaymentsItunesPurchaseFail,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_CANCEL: BasicPaymentsTestPurchaseCancel,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_TRACK: BasicPaymentsGoogleplayPurchaseTrack,
        PathValues.BASIC_PAYMENTS_STEAM_PRICES: BasicPaymentsSteamPrices,
        PathValues.BASIC_PAYMENTS_TEST_PURCHASE_FAIL: BasicPaymentsTestPurchaseFail,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_CANCEL: BasicPaymentsCouponPurchaseCancel,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_COMPLETE: BasicPaymentsItunesPurchaseComplete,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_BEGIN: BasicPaymentsCouponPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_TRACK: BasicPaymentsSteamPurchaseTrack,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PURCHASE_BEGIN: BasicPaymentsFacebookPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_ORDER: BasicPaymentsSteamOrder,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_BEGIN: BasicPaymentsWindowsPurchaseBegin,
        PathValues.BASIC_PAYMENTS_WINDOWS_PRODUCT: BasicPaymentsWindowsProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_FAIL: BasicPaymentsGoogleplayPurchaseFail,
        PathValues.BASIC_PAYMENTS_FACEBOOK_PRODUCT: BasicPaymentsFacebookProduct,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PURCHASE_CANCEL: BasicPaymentsGoogleplayPurchaseCancel,
        PathValues.BASIC_PAYMENTS_COUPON_PRODUCT: BasicPaymentsCouponProduct,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_FAIL: BasicPaymentsCouponPurchaseFail,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_BEGIN: BasicPaymentsSteamPurchaseBegin,
        PathValues.BASIC_PAYMENTS_STEAM_PURCHASE_CANCEL: BasicPaymentsSteamPurchaseCancel,
        PathValues.BASIC_PAYMENTS_STEAM_AUTH: BasicPaymentsSteamAuth,
        PathValues.BASIC_PAYMENTS_STEAM_PRODUCT: BasicPaymentsSteamProduct,
        PathValues.BASIC_PAYMENTS_COUPON_PURCHASE_COMPLETE: BasicPaymentsCouponPurchaseComplete,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_CANCEL: BasicPaymentsWindowsPurchaseCancel,
        PathValues.BASIC_PAYMENTS_GOOGLEPLAY_PRODUCT: BasicPaymentsGoogleplayProduct,
        PathValues.BASIC_PAYMENTS_WINDOWS_PURCHASE_FAIL: BasicPaymentsWindowsPurchaseFail,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_CANCEL: BasicPaymentsItunesPurchaseCancel,
        PathValues.BASIC_PAYMENTS_TEST_PRODUCT: BasicPaymentsTestProduct,
        PathValues.BASIC_PAYMENTS_ITUNES_PURCHASE_TRACK: BasicPaymentsItunesPurchaseTrack,
        PathValues.BASIC_PUSH_REGISTER: BasicPushRegister,
        PathValues.BASIC_PUSH_SEND: BasicPushSend,
        PathValues.BASIC_REALMS_PROJECT_BEAMABLE: BasicRealmsProjectBeamable,
        PathValues.BASIC_REALMS_CUSTOMER_ALIAS_AVAILABLE: BasicRealmsCustomerAliasAvailable,
        PathValues.BASIC_REALMS_PROJECT: BasicRealmsProject,
        PathValues.BASIC_REALMS_GAMES: BasicRealmsGames,
        PathValues.BASIC_REALMS_CONFIG: BasicRealmsConfig,
        PathValues.BASIC_REALMS_PROJECT_RENAME: BasicRealmsProjectRename,
        PathValues.BASIC_REALMS_PLANS: BasicRealmsPlans,
        PathValues.BASIC_REALMS_CUSTOMER: BasicRealmsCustomer,
        PathValues.BASIC_REALMS_LAUNCHMESSAGE: BasicRealmsLaunchMessage,
        PathValues.BASIC_REALMS_ISCUSTOMER: BasicRealmsIsCustomer,
        PathValues.BASIC_REALMS_ADMIN_CUSTOMER: BasicRealmsAdminCustomer,
        PathValues.BASIC_REALMS_GAME: BasicRealmsGame,
        PathValues.BASIC_REALMS_PROJECT_PROMOTE: BasicRealmsProjectPromote,
        PathValues.BASIC_REALMS_CUSTOMERS: BasicRealmsCustomers,
        PathValues.BASIC_REALMS_PROMOTION: BasicRealmsPromotion,
        PathValues.BASIC_NOTIFICATION_PLAYER: BasicNotificationPlayer,
        PathValues.BASIC_NOTIFICATION_GLOBAL: BasicNotificationGlobal,
        PathValues.BASIC_NOTIFICATION_CUSTOM: BasicNotificationCustom,
        PathValues.BASIC_NOTIFICATION_SERVER: BasicNotificationServer,
        PathValues.BASIC_NOTIFICATION_GENERIC: BasicNotificationGeneric,
        PathValues.BASIC_NOTIFICATION_GAME: BasicNotificationGame,
        PathValues.BASIC_SESSION_HISTORY: BasicSessionHistory,
        PathValues.BASIC_SESSION_STATUS: BasicSessionStatus,
        PathValues.BASIC_SESSION_HEARTBEAT: BasicSessionHeartbeat,
        PathValues.BASIC_STATS_CLIENT_BATCH: BasicStatsClientBatch,
        PathValues.BASIC_STATS_BATCH: BasicStatsBatch,
        PathValues.BASIC_STATS_SEARCH: BasicStatsSearch,
        PathValues.BASIC_STATS_SUBSCRIBE: BasicStatsSubscribe,
        PathValues.OBJECT_STATS_OBJECT_ID_CLIENT_STRINGLIST: ObjectStatsObjectIdClientStringlist,
        PathValues.OBJECT_STATS_OBJECT_ID_CLIENT: ObjectStatsObjectIdClient,
        PathValues.BASIC_TOURNAMENTS_REWARDS: BasicTournamentsRewards,
        PathValues.BASIC_TOURNAMENTS_GLOBAL: BasicTournamentsGlobal,
        PathValues.BASIC_TOURNAMENTS_STANDINGS: BasicTournamentsStandings,
        PathValues.BASIC_TOURNAMENTS_ADMIN_PLAYER: BasicTournamentsAdminPlayer,
        PathValues.BASIC_TOURNAMENTS_ME: BasicTournamentsMe,
        PathValues.BASIC_TOURNAMENTS_CHAMPIONS: BasicTournamentsChampions,
        PathValues.BASIC_TOURNAMENTS_SCORE: BasicTournamentsScore,
        PathValues.BASIC_SOCIAL_FRIENDS: BasicSocialFriends,
        PathValues.BASIC_SOCIAL_MY: BasicSocialMy,
        PathValues.BASIC_SOCIAL_FRIENDS_IMPORT: BasicSocialFriendsImport,
        PathValues.BASIC_SOCIAL_BLOCKED: BasicSocialBlocked,
        PathValues.BASIC_LEGACYTIMERS_DEFS: BasicLegacyTimersDefs,
        PathValues.BASIC_LEGACYPROMOS_CODES: BasicLegacyPromosCodes,
        PathValues.BASIC_LEGACYPROMOS_CLAIM: BasicLegacyPromosClaim,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_GRANT: BasicLegacyEntitlementDefsGrant,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_REVOKE: BasicLegacyEntitlementDefsRevoke,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_UPLOAD: BasicLegacyEntitlementDefsUpload,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_PLAYER: BasicLegacyEntitlementDefsPlayer,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS_CLAIM: BasicLegacyEntitlementDefsClaim,
        PathValues.BASIC_LEGACYCLOUD_CAMPAIGNS_SCHEDULE: BasicLegacyCloudCampaignsSchedule,
        PathValues.BASIC_LEGACYCLOUD_TEMPLATES: BasicLegacyCloudTemplates,
        PathValues.BASIC_LEGACYCLOUD_CAMPAIGNS: BasicLegacyCloudCampaigns,
        PathValues.BASIC_LEGACYPVPDEFS_FILE: BasicLegacyPvpDefsFile,
        PathValues.BASIC_LEGACYSHARDS_ACCEPTING: BasicLegacyShardsAccepting,
        PathValues.BASIC_LEGACYSHARDS_PREFERRED: BasicLegacyShardsPreferred,
        PathValues.BASIC_HISTORY_APIACCESS_URL: BasicHistoryApiaccessUrl,
        PathValues.BASIC_HISTORY_QUERY_URL: BasicHistoryQueryUrl,
        PathValues.BASIC_HISTORY_QUERY: BasicHistoryQuery,
        PathValues.BASIC_HISTORY_MICROSERVICES: BasicHistoryMicroservices,
        PathValues.BASIC_HISTORY_ACCOUNT_ROLES: BasicHistoryAccountRoles,
        PathValues.BASIC_HISTORY_APIACCESS: BasicHistoryApiaccess,
        PathValues.BASIC_HISTORY_EVENTS: BasicHistoryEvents,
        PathValues.BASIC_TRIALS: BasicTrials,
        PathValues.BASIC_ANNOUNCEMENTS: BasicAnnouncements,
        PathValues.OBJECT_ANNOUNCEMENTS_OBJECT_ID: ObjectAnnouncementsObjectId,
        PathValues.OBJECT_CALENDARS_OBJECT_ID: ObjectCalendarsObjectId,
        PathValues.OBJECT_CHAT_V2_OBJECT_ID: ObjectChatV2ObjectId,
        PathValues.BASIC_CLOUDSAVING: BasicCloudsaving,
        PathValues.OBJECT_COMMERCE_OBJECT_ID: ObjectCommerceObjectId,
        PathValues.BASIC_CONTENT: BasicContent,
        PathValues.OBJECT_EVENTS_OBJECT_ID: ObjectEventsObjectId,
        PathValues.OBJECT_EVENTPLAYERS_OBJECT_ID: ObjectEventPlayersObjectId,
        PathValues.OBJECT_GAMERELAY_OBJECT_ID: ObjectGamerelayObjectId,
        PathValues.OBJECT_INVENTORY_OBJECT_ID: ObjectInventoryObjectId,
        PathValues.OBJECT_LEADERBOARDS_OBJECT_ID: ObjectLeaderboardsObjectId,
        PathValues.OBJECT_GROUPS_OBJECT_ID: ObjectGroupsObjectId,
        PathValues.OBJECT_GROUPUSERS_OBJECT_ID: ObjectGroupUsersObjectId,
        PathValues.BASIC_MAIL: BasicMail,
        PathValues.OBJECT_MAIL_OBJECT_ID: ObjectMailObjectId,
        PathValues.OBJECT_PAYMENTS_OBJECT_ID: ObjectPaymentsObjectId,
        PathValues.BASIC_NOTIFICATION: BasicNotification,
        PathValues.BASIC_SESSION: BasicSession,
        PathValues.OBJECT_STATS_OBJECT_ID: ObjectStatsObjectId,
        PathValues.BASIC_TOURNAMENTS: BasicTournaments,
        PathValues.OBJECT_TOURNAMENTS_OBJECT_ID: ObjectTournamentsObjectId,
        PathValues.BASIC_LEGACYTIMERS: BasicLegacyTimers,
        PathValues.BASIC_LEGACYPROMOS: BasicLegacyPromos,
        PathValues.BASIC_LEGACYENTITLEMENTDEFS: BasicLegacyEntitlementDefs,
        PathValues.BASIC_LEGACYPVPDEFS: BasicLegacyPvpDefs,
        PathValues.BASIC_LEGACYSHARDS: BasicLegacyShards,
    }
)
