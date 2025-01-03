from django.apps import apps
from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import (
    permission_acl_edit, permission_acl_view
)
from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.classes import ModelCopy
from mayan.apps.common.menus import (
    menu_list_facet, menu_object, menu_related, menu_return, menu_secondary,
    menu_setup
)
from mayan.apps.documents.links.document_type_links import (
    link_document_type_list
)
from mayan.apps.events.classes import EventModelRegistry, ModelEventType
from mayan.apps.forms import column_widgets
from mayan.apps.navigation.source_columns import SourceColumn
from mayan.apps.rest_api.fields import DynamicSerializerField

from .events import event_web_link_edited, event_web_link_navigated
from .links import (
    link_document_type_web_links, link_document_web_link_list,
    link_web_link_create, link_web_link_delete, link_web_link_document_types,
    link_web_link_edit, link_web_link_instance_view, link_web_link_list,
    link_web_link_setup
)
from .methods import (
    method_document_type_web_links_add, method_document_type_web_links_remove
)
from .permissions import (
    permission_web_link_delete, permission_web_link_edit,
    permission_web_link_instance_view, permission_web_link_view
)


class WebLinksApp(MayanAppConfig):
    app_namespace = 'web_links'
    app_url = 'web_links'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.web_links'
    verbose_name = _(message='Web links')

    def ready(self):
        super().ready()

        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )
        DocumentType = apps.get_model(
            app_label='documents', model_name='DocumentType'
        )

        ResolvedWebLink = self.get_model(model_name='ResolvedWebLink')
        WebLink = self.get_model(model_name='WebLink')

        DocumentType.add_to_class(
            name='web_links_add',
            value=method_document_type_web_links_add
        )
        DocumentType.add_to_class(
            name='web_links_remove',
            value=method_document_type_web_links_remove
        )

        DynamicSerializerField.add_serializer(
            klass=WebLink,
            serializer_class='mayan.apps.web_links.serializers.WebLinkSerializer'
        )

        EventModelRegistry.register(
            model=ResolvedWebLink, acl_bind_link=False
        )
        EventModelRegistry.register(model=WebLink)

        ModelCopy(
            model=WebLink, bind_link=True, register_permission=True
        ).add_fields(
            field_names=(
                'label', 'template', 'enabled', 'document_types',
            )
        )

        ModelEventType.register(
            event_types=(
                event_web_link_navigated,
            ), model=Document
        )
        ModelEventType.register(
            event_types=(
                event_web_link_edited, event_web_link_navigated
            ), model=WebLink
        )

        ModelPermission.register(
            model=Document, permissions=(
                permission_web_link_instance_view,
            )
        )
        ModelPermission.register(
            model=DocumentType, permissions=(
                permission_web_link_instance_view,
            )
        )
        ModelPermission.register(
            model=WebLink, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_web_link_delete, permission_web_link_edit,
                permission_web_link_instance_view, permission_web_link_view
            )
        )

        SourceColumn(
            attribute='label', is_identifier=True, is_sortable=True,
            source=ResolvedWebLink
        )
        SourceColumn(
            attribute='label', is_identifier=True, is_sortable=True,
            source=WebLink
        )
        source_column_enabled = SourceColumn(
            attribute='enabled', include_label=True, is_sortable=True,
            source=WebLink,
            widget=column_widgets.TwoStateWidget
        )
        source_column_enabled.add_exclude(source=ResolvedWebLink)

        menu_list_facet.bind_links(
            links=(link_document_web_link_list,),
            sources=(Document,)
        )
        menu_list_facet.bind_links(
            exclude=(ResolvedWebLink,),
            links=(
                link_web_link_document_types,
            ), sources=(WebLink,)
        )
        menu_list_facet.bind_links(
            links=(link_document_type_web_links,), sources=(DocumentType,)
        )
        menu_object.bind_links(
            exclude=(ResolvedWebLink,),
            links=(
                link_web_link_delete, link_web_link_edit
            ), sources=(WebLink,)
        )
        menu_object.bind_links(
            links=(link_web_link_instance_view,),
            sources=(ResolvedWebLink,)
        )
        menu_related.bind_links(
            links=(link_web_link_list,),
            sources=(
                DocumentType, 'documents:document_type_list',
                'documents:document_type_create'
            )
        )
        menu_related.bind_links(
            links=(link_document_type_list,),
            sources=(
                WebLink, 'web_links:web_link_list',
                'web_links:web_link_create'
            )
        )
        menu_return.bind_links(
            links=(link_web_link_list,),
            sources=(
                WebLink, 'web_links:web_link_list',
                'web_links:web_link_create'
            )
        )
        menu_secondary.bind_links(
            links=(link_web_link_create,),
            sources=(
                WebLink, 'web_links:web_link_list',
                'web_links:web_link_create'
            )
        )
        menu_setup.bind_links(
            links=(link_web_link_setup,)
        )
