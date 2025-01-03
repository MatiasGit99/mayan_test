import logging

from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import (
    permission_acl_edit, permission_acl_view
)
from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.menus import (
    menu_multi_item, menu_object, menu_secondary, menu_topbar
)
from mayan.apps.events.classes import EventModelRegistry, ModelEventType
from mayan.apps.forms import column_widgets
from mayan.apps.navigation.source_columns import SourceColumn

from .events import event_message_edited
from .links import (
    link_message_all_mark_read, link_message_create, link_message_list,
    link_message_multiple_delete, link_message_multiple_mark_read,
    link_message_multiple_mark_unread, link_message_single_delete,
    link_message_single_mark_read, link_message_single_mark_unread
)
from .permissions import (
    permission_message_delete, permission_message_edit,
    permission_message_view
)

logger = logging.getLogger(name=__name__)


class MessagingApp(MayanAppConfig):
    app_namespace = 'messaging'
    app_url = 'messaging'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.messaging'
    verbose_name = _(message='Messaging')

    def ready(self):
        super().ready()

        Message = self.get_model(model_name='Message')

        EventModelRegistry.register(model=Message)

        ModelEventType.register(
            model=Message, event_types=(event_message_edited,)
        )

        ModelPermission.register(
            model=Message, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_message_delete, permission_message_edit,
                permission_message_view
            )
        )

        SourceColumn(
            attribute='date_time', empty_value=_(message='None'),
            include_label=True, is_identifier=True,
            is_object_absolute_url=True, is_sortable=True, source=Message
        )
        SourceColumn(
            attribute='sender_object', include_label=True,
            is_object_absolute_url=True, label=_(message='Sender'), source=Message
        )
        SourceColumn(
            attribute='subject', is_object_absolute_url=True,
            is_sortable=True, source=Message
        )
        SourceColumn(
            attribute='read', include_label=True, is_sortable=True,
            source=Message, widget=column_widgets.TwoStateWidget
        )

        menu_multi_item.bind_links(
            links=(
                link_message_multiple_delete,
                link_message_multiple_mark_read,
                link_message_multiple_mark_unread
            ), sources=(Message,)
        )
        menu_object.bind_links(
            links=(
                link_message_single_delete, link_message_single_mark_read,
                link_message_single_mark_unread
            ), sources=(Message,)
        )

        menu_secondary.bind_links(
            links=(link_message_create, link_message_all_mark_read),
            sources=(
                Message, 'messaging:message_list', 'messaging:message_create'
            )
        )

        menu_topbar.bind_links(
            links=(link_message_list,), position=40
        )
