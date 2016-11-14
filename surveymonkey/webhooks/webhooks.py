# -*- coding: utf-8 -*-
from __future__ import absolute_import

import six

from surveymonkey.manager import BaseManager
from surveymonkey.webhooks.constants import SURVEY, COLLECTOR
from surveymonkey.constants import URL_WEBHOOKS


class Webhook(BaseManager):

    def _create(self, object_type, event_type, object_ids, subscription_url):
        object_ids = [object_ids] if isinstance(object_ids, six.string_types) else object_ids

        return self.post(
            base_url=URL_WEBHOOKS,
            data={
                "event_type": event_type,
                "object_type": object_type,
                "object_ids": object_ids,
                "subscription_url": subscription_url
            }
        )

    def create_for_survey(self, event_type, object_ids, subscription_url):
        return self._create(SURVEY, event_type, object_ids, subscription_url)

    def create_for_collector(self, event_type, object_ids, subscription_url):
        return self._create(COLLECTOR, event_type, object_ids, subscription_url)
