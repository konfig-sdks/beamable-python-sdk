# coding: utf-8
"""
    history basic

    var Beamable = BeamContext.Default; - That one line of code is a gateway to everything you need to build custom server logic via microservices along with a world of LiveOps tools and live services to build games that players love.

    The version of the OpenAPI document: 1.0
    Contact: support@beamable.com
    Created by: https://api.beamable.com
"""

import typing
import inspect
from datetime import date, datetime
from beamable_python_sdk.client_custom import ClientCustom
from beamable_python_sdk.configuration import Configuration
from beamable_python_sdk.api_client import ApiClient
from beamable_python_sdk.type_util import copy_signature
from beamable_python_sdk.apis.tags.account_api import AccountApi
from beamable_python_sdk.apis.tags.activity_api import ActivityApi
from beamable_python_sdk.apis.tags.announcement_api import AnnouncementApi
from beamable_python_sdk.apis.tags.audit_api import AuditApi
from beamable_python_sdk.apis.tags.authentication_api import AuthenticationApi
from beamable_python_sdk.apis.tags.block_api import BlockApi
from beamable_python_sdk.apis.tags.campaign_api import CampaignApi
from beamable_python_sdk.apis.tags.cloudsaving_api import CloudsavingApi
from beamable_python_sdk.apis.tags.content_api import ContentApi
from beamable_python_sdk.apis.tags.currency_api import CurrencyApi
from beamable_python_sdk.apis.tags.entitlement_api import EntitlementApi
from beamable_python_sdk.apis.tags.event_api import EventApi
from beamable_python_sdk.apis.tags.friend_api import FriendApi
from beamable_python_sdk.apis.tags.game_api import GameApi
from beamable_python_sdk.apis.tags.group_api import GroupApi
from beamable_python_sdk.apis.tags.history_api import HistoryApi
from beamable_python_sdk.apis.tags.item_api import ItemApi
from beamable_python_sdk.apis.tags.leaderboard_api import LeaderboardApi
from beamable_python_sdk.apis.tags.legacy_entitlement_def_api import LegacyEntitlementDefApi
from beamable_python_sdk.apis.tags.legacy_pvp_def_api import LegacyPvpDefApi
from beamable_python_sdk.apis.tags.mail_api import MailApi
from beamable_python_sdk.apis.tags.message_api import MessageApi
from beamable_python_sdk.apis.tags.notification_api import NotificationApi
from beamable_python_sdk.apis.tags.object_api import ObjectApi
from beamable_python_sdk.apis.tags.order_api import OrderApi
from beamable_python_sdk.apis.tags.payment_api import PaymentApi
from beamable_python_sdk.apis.tags.plan_api import PlanApi
from beamable_python_sdk.apis.tags.price_api import PriceApi
from beamable_python_sdk.apis.tags.product_api import ProductApi
from beamable_python_sdk.apis.tags.promo_api import PromoApi
from beamable_python_sdk.apis.tags.realm_api import RealmApi
from beamable_python_sdk.apis.tags.registration_api import RegistrationApi
from beamable_python_sdk.apis.tags.sku_api import SKUApi
from beamable_python_sdk.apis.tags.session_api import SessionApi
from beamable_python_sdk.apis.tags.shard_api import ShardApi
from beamable_python_sdk.apis.tags.statistic_api import StatisticApi
from beamable_python_sdk.apis.tags.subscription_api import SubscriptionApi
from beamable_python_sdk.apis.tags.template_api import TemplateApi
from beamable_python_sdk.apis.tags.timer_api import TimerApi
from beamable_python_sdk.apis.tags.tournament_api import TournamentApi
from beamable_python_sdk.apis.tags.trial_api import TrialApi
from beamable_python_sdk.apis.tags.update_api import UpdateApi



class Beamable(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.account: AccountApi = AccountApi(api_client)
        self.activity: ActivityApi = ActivityApi(api_client)
        self.announcement: AnnouncementApi = AnnouncementApi(api_client)
        self.audit: AuditApi = AuditApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.block: BlockApi = BlockApi(api_client)
        self.campaign: CampaignApi = CampaignApi(api_client)
        self.cloudsaving: CloudsavingApi = CloudsavingApi(api_client)
        self.content: ContentApi = ContentApi(api_client)
        self.currency: CurrencyApi = CurrencyApi(api_client)
        self.entitlement: EntitlementApi = EntitlementApi(api_client)
        self.event: EventApi = EventApi(api_client)
        self.friend: FriendApi = FriendApi(api_client)
        self.game: GameApi = GameApi(api_client)
        self.group: GroupApi = GroupApi(api_client)
        self.history: HistoryApi = HistoryApi(api_client)
        self.item: ItemApi = ItemApi(api_client)
        self.leaderboard: LeaderboardApi = LeaderboardApi(api_client)
        self.legacy_entitlement_def: LegacyEntitlementDefApi = LegacyEntitlementDefApi(api_client)
        self.legacy_pvp_def: LegacyPvpDefApi = LegacyPvpDefApi(api_client)
        self.mail: MailApi = MailApi(api_client)
        self.message: MessageApi = MessageApi(api_client)
        self.notification: NotificationApi = NotificationApi(api_client)
        self.object: ObjectApi = ObjectApi(api_client)
        self.order: OrderApi = OrderApi(api_client)
        self.payment: PaymentApi = PaymentApi(api_client)
        self.plan: PlanApi = PlanApi(api_client)
        self.price: PriceApi = PriceApi(api_client)
        self.product: ProductApi = ProductApi(api_client)
        self.promo: PromoApi = PromoApi(api_client)
        self.realm: RealmApi = RealmApi(api_client)
        self.registration: RegistrationApi = RegistrationApi(api_client)
        self.sku: SKUApi = SKUApi(api_client)
        self.session: SessionApi = SessionApi(api_client)
        self.shard: ShardApi = ShardApi(api_client)
        self.statistic: StatisticApi = StatisticApi(api_client)
        self.subscription: SubscriptionApi = SubscriptionApi(api_client)
        self.template: TemplateApi = TemplateApi(api_client)
        self.timer: TimerApi = TimerApi(api_client)
        self.tournament: TournamentApi = TournamentApi(api_client)
        self.trial: TrialApi = TrialApi(api_client)
        self.update: UpdateApi = UpdateApi(api_client)
