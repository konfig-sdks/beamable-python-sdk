# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beamable_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PAYMENT = "Payment"
    OBJECT = "Object"
    ACCOUNT = "Account"
    GROUP = "Group"
    REALM = "Realm"
    LEADERBOARD = "Leaderboard"
    MAIL = "Mail"
    CONTENT = "Content"
    TOURNAMENT = "Tournament"
    TRIAL = "Trial"
    CLOUDSAVING = "Cloudsaving"
    ANNOUNCEMENT = "Announcement"
    GAME = "Game"
    EVENT = "Event"
    PRODUCT = "Product"
    MESSAGE = "Message"
    NOTIFICATION = "Notification"
    HISTORY = "History"
    SHARD = "Shard"
    LEGACY_PVP_DEF = "LegacyPvpDef"
    ENTITLEMENT = "Entitlement"
    PROMO = "Promo"
    SESSION = "Session"
    TIMER = "Timer"
    CAMPAIGN = "Campaign"
    AUTHENTICATION = "Authentication"
    STATISTIC = "Statistic"
    TEMPLATE = "Template"
    PLAN = "Plan"
    SKU = "SKU"
    FRIEND = "Friend"
    BLOCK = "Block"
    UPDATE = "Update"
    REGISTRATION = "Registration"
    ACTIVITY = "Activity"
    ITEM = "Item"
    AUDIT = "Audit"
    SUBSCRIPTION = "Subscription"
    CURRENCY = "Currency"
    ORDER = "Order"
    PRICE = "Price"
    LEGACY_ENTITLEMENT_DEF = "LegacyEntitlementDef"
