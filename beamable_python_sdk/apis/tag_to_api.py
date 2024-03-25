import typing_extensions

from beamable_python_sdk.apis.tags import TagValues
from beamable_python_sdk.apis.tags.payment_api import PaymentApi
from beamable_python_sdk.apis.tags.object_api import ObjectApi
from beamable_python_sdk.apis.tags.account_api import AccountApi
from beamable_python_sdk.apis.tags.group_api import GroupApi
from beamable_python_sdk.apis.tags.realm_api import RealmApi
from beamable_python_sdk.apis.tags.leaderboard_api import LeaderboardApi
from beamable_python_sdk.apis.tags.mail_api import MailApi
from beamable_python_sdk.apis.tags.content_api import ContentApi
from beamable_python_sdk.apis.tags.tournament_api import TournamentApi
from beamable_python_sdk.apis.tags.trial_api import TrialApi
from beamable_python_sdk.apis.tags.cloudsaving_api import CloudsavingApi
from beamable_python_sdk.apis.tags.announcement_api import AnnouncementApi
from beamable_python_sdk.apis.tags.game_api import GameApi
from beamable_python_sdk.apis.tags.event_api import EventApi
from beamable_python_sdk.apis.tags.product_api import ProductApi
from beamable_python_sdk.apis.tags.message_api import MessageApi
from beamable_python_sdk.apis.tags.notification_api import NotificationApi
from beamable_python_sdk.apis.tags.history_api import HistoryApi
from beamable_python_sdk.apis.tags.shard_api import ShardApi
from beamable_python_sdk.apis.tags.legacy_pvp_def_api import LegacyPvpDefApi
from beamable_python_sdk.apis.tags.entitlement_api import EntitlementApi
from beamable_python_sdk.apis.tags.promo_api import PromoApi
from beamable_python_sdk.apis.tags.session_api import SessionApi
from beamable_python_sdk.apis.tags.timer_api import TimerApi
from beamable_python_sdk.apis.tags.campaign_api import CampaignApi
from beamable_python_sdk.apis.tags.authentication_api import AuthenticationApi
from beamable_python_sdk.apis.tags.statistic_api import StatisticApi
from beamable_python_sdk.apis.tags.template_api import TemplateApi
from beamable_python_sdk.apis.tags.plan_api import PlanApi
from beamable_python_sdk.apis.tags.sku_api import SKUApi
from beamable_python_sdk.apis.tags.friend_api import FriendApi
from beamable_python_sdk.apis.tags.block_api import BlockApi
from beamable_python_sdk.apis.tags.update_api import UpdateApi
from beamable_python_sdk.apis.tags.registration_api import RegistrationApi
from beamable_python_sdk.apis.tags.activity_api import ActivityApi
from beamable_python_sdk.apis.tags.item_api import ItemApi
from beamable_python_sdk.apis.tags.audit_api import AuditApi
from beamable_python_sdk.apis.tags.subscription_api import SubscriptionApi
from beamable_python_sdk.apis.tags.currency_api import CurrencyApi
from beamable_python_sdk.apis.tags.order_api import OrderApi
from beamable_python_sdk.apis.tags.price_api import PriceApi
from beamable_python_sdk.apis.tags.legacy_entitlement_def_api import LegacyEntitlementDefApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PAYMENT: PaymentApi,
        TagValues.OBJECT: ObjectApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.GROUP: GroupApi,
        TagValues.REALM: RealmApi,
        TagValues.LEADERBOARD: LeaderboardApi,
        TagValues.MAIL: MailApi,
        TagValues.CONTENT: ContentApi,
        TagValues.TOURNAMENT: TournamentApi,
        TagValues.TRIAL: TrialApi,
        TagValues.CLOUDSAVING: CloudsavingApi,
        TagValues.ANNOUNCEMENT: AnnouncementApi,
        TagValues.GAME: GameApi,
        TagValues.EVENT: EventApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.SHARD: ShardApi,
        TagValues.LEGACY_PVP_DEF: LegacyPvpDefApi,
        TagValues.ENTITLEMENT: EntitlementApi,
        TagValues.PROMO: PromoApi,
        TagValues.SESSION: SessionApi,
        TagValues.TIMER: TimerApi,
        TagValues.CAMPAIGN: CampaignApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.STATISTIC: StatisticApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.PLAN: PlanApi,
        TagValues.SKU: SKUApi,
        TagValues.FRIEND: FriendApi,
        TagValues.BLOCK: BlockApi,
        TagValues.UPDATE: UpdateApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.ITEM: ItemApi,
        TagValues.AUDIT: AuditApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.ORDER: OrderApi,
        TagValues.PRICE: PriceApi,
        TagValues.LEGACY_ENTITLEMENT_DEF: LegacyEntitlementDefApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PAYMENT: PaymentApi,
        TagValues.OBJECT: ObjectApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.GROUP: GroupApi,
        TagValues.REALM: RealmApi,
        TagValues.LEADERBOARD: LeaderboardApi,
        TagValues.MAIL: MailApi,
        TagValues.CONTENT: ContentApi,
        TagValues.TOURNAMENT: TournamentApi,
        TagValues.TRIAL: TrialApi,
        TagValues.CLOUDSAVING: CloudsavingApi,
        TagValues.ANNOUNCEMENT: AnnouncementApi,
        TagValues.GAME: GameApi,
        TagValues.EVENT: EventApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.MESSAGE: MessageApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.SHARD: ShardApi,
        TagValues.LEGACY_PVP_DEF: LegacyPvpDefApi,
        TagValues.ENTITLEMENT: EntitlementApi,
        TagValues.PROMO: PromoApi,
        TagValues.SESSION: SessionApi,
        TagValues.TIMER: TimerApi,
        TagValues.CAMPAIGN: CampaignApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.STATISTIC: StatisticApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.PLAN: PlanApi,
        TagValues.SKU: SKUApi,
        TagValues.FRIEND: FriendApi,
        TagValues.BLOCK: BlockApi,
        TagValues.UPDATE: UpdateApi,
        TagValues.REGISTRATION: RegistrationApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.ITEM: ItemApi,
        TagValues.AUDIT: AuditApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.ORDER: OrderApi,
        TagValues.PRICE: PriceApi,
        TagValues.LEGACY_ENTITLEMENT_DEF: LegacyEntitlementDefApi,
    }
)
