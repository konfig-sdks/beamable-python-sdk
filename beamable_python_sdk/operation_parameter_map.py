operation_parameter_map = {
    '/basic/accounts/available/device-id-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/basic/accounts/available-GET': {
        'parameters': [
            {
                'name': 'email'
            },
        ]
    },
    '/basic/accounts/available/third-party-GET': {
        'parameters': [
            {
                'name': 'thirdParty'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/basic/accounts/admin/admin-user-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/scope-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/accounts/me/third-party-DELETE': {
        'parameters': [
            {
                'name': 'thirdParty'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/third-party-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'thirdParty'
            },
            {
                'name': 'userAppId'
            },
        ]
    },
    '/basic/accounts/find-GET': {
        'parameters': [
            {
                'name': 'query'
            },
        ]
    },
    '/basic/accounts/admin/admin-users-GET': {
        'parameters': [
        ]
    },
    '/basic/accounts/admin/me-GET': {
        'parameters': [
        ]
    },
    '/object/accounts/{objectId}/available-roles-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/accounts/get-personally-identifiable-information-GET': {
        'parameters': [
            {
                'name': 'query'
            },
        ]
    },
    '/basic/accounts/me-GET': {
        'parameters': [
        ]
    },
    '/basic/history/account/roles-GET': {
        'parameters': [
        ]
    },
    '/basic/accounts/register-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/forget-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/accounts/me/device-DELETE': {
        'parameters': [
            {
                'name': 'deviceIds'
            },
        ]
    },
    '/object/accounts/{objectId}/role-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/accounts/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pagesize'
            },
        ]
    },
    '/basic/accounts/me-PUT': {
        'parameters': [
            {
                'name': 'hasThirdPartyToken'
            },
            {
                'name': 'thirdParty'
            },
            {
                'name': 'country'
            },
            {
                'name': 'language'
            },
            {
                'name': 'gamerTagAssoc'
            },
            {
                'name': 'token'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'userName'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/scope-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'realm'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/basic/accounts/password-update/confirm-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'newPassword'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/basic/accounts/password-update/init-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'codeType'
            },
        ]
    },
    '/object/accounts/{objectId}/role-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'cid'
            },
            {
                'name': 'realm'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/third-party-PUT': {
        'parameters': [
            {
                'name': 'fromAccountId'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'thirdParty'
            },
        ]
    },
    '/basic/events/running-GET': {
        'parameters': [
        ]
    },
    '/object/announcements/{objectId}/claim-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'announcement'
            },
            {
                'name': 'announcements'
            },
        ]
    },
    '/basic/announcements-POST': {
        'parameters': [
            {
                'name': 'summary'
            },
            {
                'name': 'title'
            },
            {
                'name': 'body'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'gift'
            },
            {
                'name': 'mongo_start_date'
            },
            {
                'name': 'stat_requirements'
            },
            {
                'name': 'mongo_end_date'
            },
            {
                'name': 'symbol'
            },
            {
                'name': 'clientData'
            },
            {
                'name': 'validationErrors'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/basic/announcements-DELETE': {
        'parameters': [
            {
                'name': 'symbol'
            },
        ]
    },
    '/basic/announcements/list-GET': {
        'parameters': [
        ]
    },
    '/object/announcements/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'include_deleted'
            },
        ]
    },
    '/object/announcements/{objectId}/raw-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/announcements/{objectId}/read-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'announcement'
            },
            {
                'name': 'announcements'
            },
        ]
    },
    '/object/announcements/{objectId}-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'announcement'
            },
            {
                'name': 'announcements'
            },
        ]
    },
    '/basic/announcements/search-GET': {
        'parameters': [
            {
                'name': 'date'
            },
        ]
    },
    '/basic/payments/audits-GET': {
        'parameters': [
            {
                'name': 'providerid'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'state'
            },
            {
                'name': 'txid'
            },
            {
                'name': 'player'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/basic/auth/token-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/basic/auth/token-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'refresh_token'
            },
            {
                'name': 'third_party'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'code'
            },
            {
                'name': 'token'
            },
            {
                'name': 'customerScoped'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/basic/payments/steam/auth-POST': {
        'parameters': [
            {
                'name': 'ticket'
            },
        ]
    },
    '/basic/social/blocked-POST': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/social/blocked-DELETE': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/legacy-cloud/campaigns-POST': {
        'parameters': [
            {
                'name': 'resend_to_past_recipients'
            },
            {
                'name': 'sent'
            },
            {
                'name': 'mtype'
            },
            {
                'name': 'mb_store'
            },
            {
                'name': 'mb_expiration'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'mb_ent_spec'
            },
            {
                'name': 'mb_ent_quant'
            },
            {
                'name': 'datepoint'
            },
            {
                'name': 'mb_attachments'
            },
            {
                'name': 'recur'
            },
            {
                'name': 'msg'
            },
            {
                'name': 'rules'
            },
            {
                'name': 'mb_ent'
            },
            {
                'name': 'start'
            },
            {
                'name': 'days'
            },
        ]
    },
    '/basic/legacy-cloud/campaigns-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-cloud/campaigns-DELETE': {
        'parameters': [
            {
                'name': 'sid'
            },
        ]
    },
    '/basic/legacy-cloud/campaigns/schedule-PUT': {
        'parameters': [
            {
                'name': 'sid'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/basic/cloudsaving/data/commitManifest-PUT': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data-DELETE': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving-GET': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data/downloadURL-POST': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data/metadata-GET': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data/move-PUT': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data/replace-POST': {
        'parameters': [
            {
                'name': 'sourcePlayerId'
            },
            {
                'name': 'targetPlayerId'
            },
        ]
    },
    '/basic/cloudsaving/data/uploadURL-POST': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/cloudsaving/data/uploadURLFromPortal-POST': {
        'parameters': [
            {
                'name': 'request'
            },
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/events/applyContent-POST': {
        'parameters': [
            {
                'name': 'items'
            },
        ]
    },
    '/basic/content/manifest/checksum-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/content/manifest-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'references'
            },
        ]
    },
    '/basic/content-POST': {
        'parameters': [
            {
                'name': 'content'
            },
        ]
    },
    '/object/events/{objectId}/content-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/announcements/content-GET': {
        'parameters': [
        ]
    },
    '/basic/events/content-GET': {
        'parameters': [
        ]
    },
    '/basic/content/content-GET': {
        'parameters': [
            {
                'name': 'contentId'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/basic/content/manifest-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/content/manifest/private-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/content/manifest/public-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/content/manifest/pull-POST': {
        'parameters': [
            {
                'name': 'sourceRealmPid'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/basic/content/text-POST': {
        'parameters': [
            {
                'name': 'text'
            },
        ]
    },
    '/object/events/{objectId}/content-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'event'
            },
            {
                'name': 'origin'
            },
        ]
    },
    '/basic/inventory/currency-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-entitlement-defs/grant-POST': {
        'parameters': [
            {
                'name': 'gamerTags'
            },
            {
                'name': 'generators'
            },
        ]
    },
    '/basic/legacy-entitlement-defs-PUT': {
        'parameters': [
            {
                'name': 'symbol'
            },
            {
                'name': 'request'
            },
        ]
    },
    '/basic/legacy-entitlement-defs/claim-PUT': {
        'parameters': [
            {
                'name': 'gt'
            },
            {
                'name': 'symbol'
            },
            {
                'name': 'spec'
            },
            {
                'name': 'uuid'
            },
        ]
    },
    '/basic/legacy-entitlement-defs/player-GET': {
        'parameters': [
            {
                'name': 'gt'
            },
            {
                'name': 'state'
            },
            {
                'name': 'skip'
            },
            {
                'name': 'symbol'
            },
            {
                'name': 'icw'
            },
            {
                'name': 'spec'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/basic/legacy-entitlement-defs/revoke-DELETE': {
        'parameters': [
            {
                'name': 'uuid'
            },
        ]
    },
    '/basic/legacy-entitlement-defs/upload-POST': {
        'parameters': [
            {
                'name': 'entitlements'
            },
        ]
    },
    '/object/event-players/{objectId}/claim-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'eventId'
            },
        ]
    },
    '/basic/events/calendar-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/object/events/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/event-players/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/events/{objectId}/ping-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/events/{objectId}/refresh-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/events/{objectId}/endPhase-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/object/event-players/{objectId}/score-PUT': {
        'parameters': [
            {
                'name': 'score'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'eventId'
            },
            {
                'name': 'increment'
            },
            {
                'name': 'stats'
            },
        ]
    },
    '/basic/social/friends/import-POST': {
        'parameters': [
            {
                'name': 'source'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/basic/social/friends-DELETE': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/basic/realms/game-POST': {
        'parameters': [
            {
                'name': 'gameName'
            },
        ]
    },
    '/basic/realms/game-GET': {
        'parameters': [
            {
                'name': 'rootPID'
            },
        ]
    },
    '/basic/realms/games-GET': {
        'parameters': [
        ]
    },
    '/basic/notification/game-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'dbid'
            },
            {
                'name': 'customChannelSuffix'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/object/gamerelay/{objectId}-POST': {
        'parameters': [
            {
                'name': 'keepSubscribed'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'roomName'
            },
            {
                'name': 'players'
            },
            {
                'name': 'gameType'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/object/gamerelay/{objectId}/results-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'results'
            },
        ]
    },
    '/object/gamerelay/{objectId}/sync-POST': {
        'parameters': [
            {
                'name': 't'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'events'
            },
        ]
    },
    '/basic/realms/game-PUT': {
        'parameters': [
            {
                'name': 'rootPID'
            },
            {
                'name': 'projects'
            },
        ]
    },
    '/object/groups/{objectId}/apply-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/group-users/{objectId}/group-POST': {
        'parameters': [
            {
                'name': 'requirement'
            },
            {
                'name': 'maxSize'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enrollmentType'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'clientData'
            },
            {
                'name': 'scores'
            },
            {
                'name': 'time'
            },
            {
                'name': 'type'
            },
            {
                'name': 'group'
            },
        ]
    },
    '/object/groups/{objectId}/donations-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'currencyId'
            },
            {
                'name': 'config'
            },
        ]
    },
    '/object/groups/{objectId}/petition-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/groups/{objectId}-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/group-users/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/groups/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/group-users/{objectId}/recommended-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/group-users/{objectId}/availability-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'type'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/groups/{objectId}/invite-POST': {
        'parameters': [
            {
                'name': 'gamerTag'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/group-users/{objectId}/join-DELETE': {
        'parameters': [
            {
                'name': 'group'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'successor'
            },
            {
                'name': 'score'
            },
            {
                'name': 'subGroup'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/object/group-users/{objectId}/join-POST': {
        'parameters': [
            {
                'name': 'group'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'successor'
            },
            {
                'name': 'score'
            },
            {
                'name': 'subGroup'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/object/groups/{objectId}/kick-POST': {
        'parameters': [
            {
                'name': 'gamerTag'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/groups/{objectId}/member-DELETE': {
        'parameters': [
            {
                'name': 'gamerTag'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/basic/groups/search-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'scoreMin'
            },
            {
                'name': 'sortField'
            },
            {
                'name': 'userScore'
            },
            {
                'name': 'hasSlots'
            },
            {
                'name': 'enrollmentTypes'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'scoreMax'
            },
            {
                'name': 'subGroup'
            },
            {
                'name': 'sortValue'
            },
            {
                'name': 'type'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/object/group-users/{objectId}/search-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'scoreMin'
            },
            {
                'name': 'sortField'
            },
            {
                'name': 'userScore'
            },
            {
                'name': 'hasSlots'
            },
            {
                'name': 'enrollmentTypes'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'scoreMax'
            },
            {
                'name': 'subGroup'
            },
            {
                'name': 'sortValue'
            },
            {
                'name': 'type'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/object/groups/{objectId}/donations-PUT': {
        'parameters': [
            {
                'name': 'recipientId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/groups/{objectId}-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enrollmentType'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'slogan'
            },
            {
                'name': 'requirement'
            },
            {
                'name': 'motd'
            },
            {
                'name': 'clientData'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/object/groups/{objectId}/role-PUT': {
        'parameters': [
            {
                'name': 'gamerTag'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'role'
            },
            {
                'name': 'subGroup'
            },
        ]
    },
    '/basic/history/apiaccess-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/basic/history/apiaccess/url-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'customerScoped'
            },
        ]
    },
    '/basic/history/events-GET': {
        'parameters': [
        ]
    },
    '/basic/history/microservices-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/basic/history/query/url-POST': {
        'parameters': [
            {
                'name': 'query'
            },
        ]
    },
    '/basic/history/query-POST': {
        'parameters': [
            {
                'name': 'query'
            },
        ]
    },
    '/basic/inventory/items-GET': {
        'parameters': [
        ]
    },
    '/object/leaderboards/{objectId}/freeze-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/entries-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/leaderboards/assignment-GET': {
        'parameters': [
            {
                'name': 'boardId'
            },
            {
                'name': 'joinBoard'
            },
        ]
    },
    '/object/leaderboards/{objectId}/details-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'max'
            },
        ]
    },
    '/object/leaderboards/{objectId}/matches-GET': {
        'parameters': [
            {
                'name': 'poolSize'
            },
            {
                'name': 'windows'
            },
            {
                'name': 'windowSize'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/membership-GET': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/partition-GET': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/view-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'max'
            },
            {
                'name': 'focus'
            },
            {
                'name': 'friends'
            },
            {
                'name': 'from'
            },
            {
                'name': 'outlier'
            },
            {
                'name': 'guild'
            },
        ]
    },
    '/basic/leaderboards/player-GET': {
        'parameters': [
            {
                'name': 'dbid'
            },
        ]
    },
    '/basic/leaderboards/uid-GET': {
        'parameters': [
        ]
    },
    '/object/leaderboards/{objectId}/ranks-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'ids'
            },
        ]
    },
    '/basic/leaderboards/list-GET': {
        'parameters': [
            {
                'name': 'skip'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/object/leaderboards/{objectId}/assignment-DELETE': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/entry-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/leaderboards/{objectId}-POST': {
        'parameters': [
            {
                'name': 'sharded'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'freezeTime'
            },
            {
                'name': 'derivatives'
            },
            {
                'name': 'scoreName'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'maxEntries'
            },
            {
                'name': 'partitioned'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/object/leaderboards/{objectId}/swap-PUT': {
        'parameters': [
            {
                'name': 'swapBase'
            },
            {
                'name': 'delta'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'winnerId'
            },
            {
                'name': 'loserId'
            },
        ]
    },
    '/object/leaderboards/{objectId}/entry-PUT': {
        'parameters': [
            {
                'name': 'score'
            },
            {
                'name': 'id'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'maxScore'
            },
            {
                'name': 'stats'
            },
            {
                'name': 'minScore'
            },
            {
                'name': 'increment'
            },
        ]
    },
    '/basic/legacy-entitlement-defs-POST': {
        'parameters': [
            {
                'name': 'symbol'
            },
            {
                'name': 'request'
            },
        ]
    },
    '/basic/legacy-pvp-defs-PUT': {
        'parameters': [
            {
                'name': 'lbid'
            },
        ]
    },
    '/basic/legacy-pvp-defs-DELETE': {
        'parameters': [
            {
                'name': 'lbid'
            },
        ]
    },
    '/basic/legacy-entitlement-defs-DELETE': {
        'parameters': [
            {
                'name': 'symbol'
            },
        ]
    },
    '/basic/legacy-pvp-defs-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-entitlement-defs-GET': {
        'parameters': [
            {
                'name': 'symbol'
            },
        ]
    },
    '/basic/legacy-pvp-defs/file-POST': {
        'parameters': [
            {
                'name': 'lbid'
            },
        ]
    },
    '/object/mail/{objectId}/accept/many-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'mailIds'
            },
        ]
    },
    '/object/mail/{objectId}-POST': {
        'parameters': [
            {
                'name': 'senderGamerTag'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'expires'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'rewards'
            },
            {
                'name': 'id'
            },
            {
                'name': 'category'
            },
            {
                'name': 'bodyRef'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/basic/mail/template-GET': {
        'parameters': [
            {
                'name': 'gamerTag'
            },
            {
                'name': 'templateName'
            },
        ]
    },
    '/basic/mail-GET': {
        'parameters': [
            {
                'name': 'mid'
            },
        ]
    },
    '/object/mail/{objectId}/categories-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/mail/{objectId}/detail-GET': {
        'parameters': [
            {
                'name': 'mid'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/mail/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/mail/{objectId}/search-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'clauses'
            },
        ]
    },
    '/basic/mail/bulk-POST': {
        'parameters': [
            {
                'name': 'sendMailRequests'
            },
        ]
    },
    '/object/mail/{objectId}/bulk-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'sendMailRequests'
            },
        ]
    },
    '/object/accounts/{objectId}/admin/email-PUT': {
        'parameters': [
            {
                'name': 'newEmail'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'codeType'
            },
        ]
    },
    '/basic/accounts/email-update/confirm-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/basic/accounts/email-update/init-POST': {
        'parameters': [
            {
                'name': 'newEmail'
            },
            {
                'name': 'codeType'
            },
        ]
    },
    '/basic/mail-PUT': {
        'parameters': [
            {
                'name': 'mailId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'expires'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'state'
            },
            {
                'name': 'category'
            },
            {
                'name': 'acceptAttachments'
            },
        ]
    },
    '/object/mail/{objectId}/bulk-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'updateMailRequests'
            },
        ]
    },
    '/object/mail/{objectId}-PUT': {
        'parameters': [
            {
                'name': 'mailId'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'expires'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'state'
            },
            {
                'name': 'category'
            },
            {
                'name': 'acceptAttachments'
            },
        ]
    },
    '/basic/mail/attachments-PUT': {
        'parameters': [
            {
                'name': 'mailIds'
            },
        ]
    },
    '/basic/realms/launch-message-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'body'
            },
        ]
    },
    '/basic/realms/launch-message-DELETE': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/basic/realms/launch-message-GET': {
        'parameters': [
        ]
    },
    '/basic/social/my-GET': {
        'parameters': [
        ]
    },
    '/object/chatV2/{objectId}/messages-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'roomId'
            },
            {
                'name': 'content'
            },
        ]
    },
    '/basic/push/send-POST': {
        'parameters': [
            {
                'name': 'msgs'
            },
        ]
    },
    '/basic/notification/custom-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'dbid'
            },
            {
                'name': 'customChannelSuffix'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/basic/notification-GET': {
        'parameters': [
        ]
    },
    '/basic/notification/global-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'dbid'
            },
            {
                'name': 'customChannelSuffix'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/basic/notification/generic-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'dbid'
            },
            {
                'name': 'customChannelSuffix'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/basic/notification/player-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'dbid'
            },
            {
                'name': 'customChannelSuffix'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/basic/notification/server-POST': {
        'parameters': [
            {
                'name': 'toAll'
            },
            {
                'name': 'event'
            },
            {
                'name': 'payload'
            },
        ]
    },
    '/object/calendars/{objectId}/claim-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/object/chatV2/{objectId}/rooms-POST': {
        'parameters': [
            {
                'name': 'keepSubscribed'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'roomName'
            },
            {
                'name': 'players'
            },
            {
                'name': 'gameType'
            },
            {
                'name': 'dbids'
            },
        ]
    },
    '/object/commerce/{objectId}/coupons-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'listing'
            },
        ]
    },
    '/object/inventory/{objectId}-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/object/stats/{objectId}-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'set'
            },
            {
                'name': 'add'
            },
            {
                'name': 'emitAnalytics'
            },
        ]
    },
    '/object/chatV2/{objectId}/rooms-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'roomId'
            },
        ]
    },
    '/object/stats/{objectId}-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'stats'
            },
        ]
    },
    '/object/commerce/{objectId}/status-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'store'
            },
        ]
    },
    '/object/commerce/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/object/calendars/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/chatV2/{objectId}/rooms-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/chatV2/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/object/stats/{objectId}/client-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'stats'
            },
        ]
    },
    '/object/commerce/{objectId}/coupons/count-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/commerce/{objectId}/listings-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'listing'
            },
            {
                'name': 'store'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/object/commerce/{objectId}/offers-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
            {
                'name': 'stores'
            },
        ]
    },
    '/object/inventory/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/object/matchmaking/{objectId}/match-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/inventory/{objectId}/multipliers-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/stats/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'stats'
            },
        ]
    },
    '/object/commerce/{objectId}/offersAdmin-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
            {
                'name': 'stores'
            },
        ]
    },
    '/object/payments/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/matchmaking/{objectId}/match-DELETE': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/stats/{objectId}/client-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'set'
            },
            {
                'name': 'add'
            },
            {
                'name': 'emitAnalytics'
            },
        ]
    },
    '/object/stats/{objectId}/client/stringlist-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'set'
            },
        ]
    },
    '/object/commerce/{objectId}/purchase-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'listingId'
            },
            {
                'name': 'free'
            },
        ]
    },
    '/object/commerce/{objectId}/purchase-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'purchaseId'
            },
        ]
    },
    '/object/inventory/{objectId}/transaction-DELETE': {
        'parameters': [
            {
                'name': 'transaction'
            },
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/matchmaking/{objectId}/match-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/inventory/{objectId}/transfer-PUT': {
        'parameters': [
            {
                'name': 'recipientPlayer'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'transaction'
            },
            {
                'name': 'currencies'
            },
        ]
    },
    '/object/inventory/{objectId}-PUT': {
        'parameters': [
            {
                'name': 'empty'
            },
            {
                'name': 'currencyContentIds'
            },
            {
                'name': 'itemContentIds'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'currencyProperties'
            },
            {
                'name': 'applyVipBonus'
            },
            {
                'name': 'updateItems'
            },
            {
                'name': 'newItems'
            },
            {
                'name': 'transaction'
            },
            {
                'name': 'deleteItems'
            },
        ]
    },
    '/object/inventory/{objectId}/preview-PUT': {
        'parameters': [
            {
                'name': 'empty'
            },
            {
                'name': 'currencyContentIds'
            },
            {
                'name': 'itemContentIds'
            },
            {
                'name': 'objectId'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'currencyProperties'
            },
            {
                'name': 'applyVipBonus'
            },
            {
                'name': 'updateItems'
            },
            {
                'name': 'newItems'
            },
            {
                'name': 'transaction'
            },
            {
                'name': 'deleteItems'
            },
        ]
    },
    '/object/matchmaking/{objectId}/tick-PUT': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/object/commerce/{objectId}/stats/update-POST': {
        'parameters': [
            {
                'name': 'objectId'
            },
            {
                'name': 'statsBefore'
            },
            {
                'name': 'statsAfter'
            },
        ]
    },
    '/basic/payments/steam/order-GET': {
        'parameters': [
            {
                'name': 'orderId'
            },
        ]
    },
    '/basic/payments/test/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/itunes/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/itunes/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/test/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/coupon/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/googleplay/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/coupon/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/coupon/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/facebook/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/facebook/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/facebook/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/facebook/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/coupon/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/googleplay/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/googleplay/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/windows/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/itunes/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/itunes/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/test/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/windows/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/itunes/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/test/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/googleplay/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/windows/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/steam/purchase/begin-POST': {
        'parameters': [
            {
                'name': 'purchaseId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/basic/payments/steam/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/steam/purchase/complete-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/steam/purchase/fail-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/basic/payments/test/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/coupon/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/facebook/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/googleplay/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/steam/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/payments/windows/purchase/cancel-POST': {
        'parameters': [
            {
                'name': 'txid'
            },
        ]
    },
    '/basic/payments/windows/purchase/track-POST': {
        'parameters': [
            {
                'name': 'priceInLocalCurrency'
            },
            {
                'name': 'skuName'
            },
            {
                'name': 'skuProductId'
            },
            {
                'name': 'store'
            },
            {
                'name': 'obtainItems'
            },
            {
                'name': 'obtainCurrency'
            },
            {
                'name': 'purchaseId'
            },
            {
                'name': 'isoCurrencySymbol'
            },
        ]
    },
    '/basic/realms/plans-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'memcachedHosts'
            },
            {
                'name': 'mongoSSL'
            },
            {
                'name': 'platformJBDC'
            },
            {
                'name': 'sharded'
            },
            {
                'name': 'mongoHosts'
            },
            {
                'name': 'redisShards'
            },
            {
                'name': 'messageBusAnalytics'
            },
            {
                'name': 'messageBusCommon'
            },
        ]
    },
    '/basic/realms/plans-GET': {
        'parameters': [
        ]
    },
    '/basic/payments/steam/prices-GET': {
        'parameters': [
            {
                'name': 'steamId'
            },
        ]
    },
    '/basic/commerce/catalog-GET': {
        'parameters': [
            {
                'name': 'version'
            },
        ]
    },
    '/basic/payments/coupon/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/facebook/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/googleplay/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/itunes/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/steam/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/windows/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/payments/test/product-GET': {
        'parameters': [
            {
                'name': 'sku'
            },
        ]
    },
    '/basic/legacy-promos/claim-POST': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/basic/legacy-promos-POST': {
        'parameters': [
            {
                'name': 'codes'
            },
            {
                'name': 'claimsPerCode'
            },
            {
                'name': 'definition'
            },
        ]
    },
    '/basic/legacy-promos/codes-POST': {
        'parameters': [
            {
                'name': 'definitionId'
            },
            {
                'name': 'claimsPerCode'
            },
            {
                'name': 'codes'
            },
        ]
    },
    '/basic/legacy-promos-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-promos/codes-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/realms/customer/alias/available-GET': {
        'parameters': [
            {
                'name': 'alias'
            },
        ]
    },
    '/basic/realms/is-customer-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/project/beamable-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'plan'
            },
            {
                'name': 'sharded'
            },
            {
                'name': 'parent'
            },
        ]
    },
    '/basic/realms/customer-POST': {
        'parameters': [
            {
                'name': 'projectName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'customerName'
            },
            {
                'name': 'hierarchy'
            },
            {
                'name': 'alias'
            },
        ]
    },
    '/basic/realms/project-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'plan'
            },
            {
                'name': 'sharded'
            },
            {
                'name': 'parent'
            },
        ]
    },
    '/basic/realms/promotion-POST': {
        'parameters': [
            {
                'name': 'sourcePid'
            },
            {
                'name': 'promotions'
            },
            {
                'name': 'contentManifestIds'
            },
        ]
    },
    '/basic/realms/project-DELETE': {
        'parameters': [
            {
                'name': 'pid'
            },
        ]
    },
    '/basic/realms/config-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/customer-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/admin/customer-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/project-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/promotion-GET': {
        'parameters': [
            {
                'name': 'sourcePid'
            },
            {
                'name': 'promotions'
            },
            {
                'name': 'contentManifestIds'
            },
        ]
    },
    '/basic/realms/customers-GET': {
        'parameters': [
        ]
    },
    '/basic/realms/project/promote-POST': {
        'parameters': [
            {
                'name': 'sourcePid'
            },
            {
                'name': 'promotions'
            },
            {
                'name': 'contentManifestIds'
            },
        ]
    },
    '/basic/realms/project/promote-GET': {
        'parameters': [
            {
                'name': 'sourcePid'
            },
            {
                'name': 'promotions'
            },
            {
                'name': 'contentManifestIds'
            },
        ]
    },
    '/basic/realms/project/rename-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'newName'
            },
        ]
    },
    '/basic/realms/config-PUT': {
        'parameters': [
            {
                'name': 'config'
            },
        ]
    },
    '/basic/realms/project-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/basic/push/register-POST': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/basic/commerce/skus-POST': {
        'parameters': [
            {
                'name': 'definitions'
            },
        ]
    },
    '/basic/commerce/skus-GET': {
        'parameters': [
            {
                'name': 'version'
            },
        ]
    },
    '/basic/session-POST': {
        'parameters': [
            {
                'name': 'source'
            },
            {
                'name': 'customParams'
            },
            {
                'name': 'shard'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'deviceParams'
            },
            {
                'name': 'language'
            },
            {
                'name': 'time'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'gamer'
            },
            {
                'name': 'device'
            },
        ]
    },
    '/basic/session/history-GET': {
        'parameters': [
            {
                'name': 'dbid'
            },
            {
                'name': 'month'
            },
            {
                'name': 'year'
            },
        ]
    },
    '/basic/session/status-GET': {
        'parameters': [
            {
                'name': 'intervalSecs'
            },
            {
                'name': 'playerIds'
            },
            {
                'name': 'playerIdsSeq'
            },
        ]
    },
    '/basic/session/heartbeat-POST': {
        'parameters': [
        ]
    },
    '/basic/legacy-shards-DELETE': {
        'parameters': [
            {
                'name': 'shardId'
            },
        ]
    },
    '/basic/legacy-shards/accepting-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-shards-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-shards/preferred-GET': {
        'parameters': [
            {
                'name': 'preference'
            },
        ]
    },
    '/basic/legacy-shards-POST': {
        'parameters': [
            {
                'name': 'shardId'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/basic/legacy-shards-PUT': {
        'parameters': [
            {
                'name': 'shardId'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/basic/stats/batch-POST': {
        'parameters': [
            {
                'name': 'updates'
            },
        ]
    },
    '/basic/stats/client/batch-GET': {
        'parameters': [
            {
                'name': 'objectIds'
            },
            {
                'name': 'stats'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/basic/stats/search-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
            {
                'name': 'access'
            },
            {
                'name': 'objectType'
            },
            {
                'name': 'criteria'
            },
        ]
    },
    '/basic/stats/subscribe-PUT': {
        'parameters': [
            {
                'name': 'service'
            },
            {
                'name': 'subscriptions'
            },
        ]
    },
    '/basic/legacy-cloud/templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'msg'
            },
        ]
    },
    '/basic/legacy-cloud/templates-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/legacy-cloud/templates-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-timers-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'cronish'
            },
        ]
    },
    '/basic/legacy-timers-DELETE': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/basic/legacy-timers/defs-GET': {
        'parameters': [
        ]
    },
    '/basic/legacy-timers-GET': {
        'parameters': [
        ]
    },
    '/basic/tournaments/admin/player-GET': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments-POST': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments/rewards-POST': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments/champions-GET': {
        'parameters': [
            {
                'name': 'cycles'
            },
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments/global-GET': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
            {
                'name': 'max'
            },
            {
                'name': 'focus'
            },
            {
                'name': 'cycle'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/basic/tournaments/me-GET': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments/rewards-GET': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
        ]
    },
    '/basic/tournaments/standings-GET': {
        'parameters': [
            {
                'name': 'tournamentId'
            },
            {
                'name': 'max'
            },
            {
                'name': 'focus'
            },
            {
                'name': 'cycle'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/object/tournaments/{objectId}-GET': {
        'parameters': [
            {
                'name': 'objectId'
            },
        ]
    },
    '/basic/tournaments-GET': {
        'parameters': [
            {
                'name': 'isRunning'
            },
        ]
    },
    '/basic/tournaments/score-POST': {
        'parameters': [
            {
                'name': 'score'
            },
            {
                'name': 'playerId'
            },
            {
                'name': 'tournamentId'
            },
            {
                'name': 'stats'
            },
            {
                'name': 'increment'
            },
        ]
    },
    '/basic/tournaments/admin/player-PUT': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'tournamentId'
            },
            {
                'name': 'update'
            },
        ]
    },
    '/basic/trials/admin/data-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/trials-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'strat'
            },
            {
                'name': 'cohortType'
            },
            {
                'name': 'cohorts'
            },
        ]
    },
    '/basic/trials/data-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/basic/trials/admin-GET': {
        'parameters': [
            {
                'name': 'dbid'
            },
        ]
    },
    '/basic/trials-GET': {
        'parameters': [
        ]
    },
    '/basic/trials/pause-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/basic/trials/data-POST': {
        'parameters': [
            {
                'name': 'trialName'
            },
            {
                'name': 'cohortName'
            },
            {
                'name': 'dataName'
            },
            {
                'name': 'filePayloadBase64'
            },
        ]
    },
    '/basic/trials-DELETE': {
        'parameters': [
            {
                'name': 'trialType'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/basic/trials/schedule-PUT': {
        'parameters': [
            {
                'name': 'time'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/basic/trials/start-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/basic/payments/facebook/update-GET': {
        'parameters': [
            {
                'name': 'hubMode'
            },
            {
                'name': 'hubChallenge'
            },
            {
                'name': 'hubVerifyToken'
            },
        ]
    },
    '/basic/payments/facebook/update-POST': {
        'parameters': [
            {
                'name': 'object'
            },
            {
                'name': 'entry'
            },
        ]
    },
};