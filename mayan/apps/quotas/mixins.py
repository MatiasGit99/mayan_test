from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from mayan.apps.documents.models.document_type_models import DocumentType
from mayan.apps.user_management.querysets import get_user_queryset

from .classes import QuotaBackend
from .permissions import permission_quota_edit


class DocumentTypesQuotaMixin:
    @classmethod
    def get_fields(cls):
        cls.fields.update(
            {
                'document_type_all': {
                    'label': _(message='All document types'),
                    'class': 'django.forms.BooleanField', 'default': False,
                    'help_text': _(
                        message='Apply to all document types. Enabling this, '
                        'the quota will ignore the individual document type'
                        ' selection.'
                    ), 'required': False,
                },
                'document_type_ids': {
                    'label': _(message='Document types'),
                    'class': 'mayan.apps.forms.form_fields.ModelFormFieldFilteredModelMultipleChoice',
                    'kwargs': {
                        'permission': permission_quota_edit,
                        'required': False,
                        'source_queryset': DocumentType.objects.all()
                    }, 'help_text': _(
                        message='Document types to which the quota will be applied.'
                    )
                }
            }
        )

        cls.field_order = list(cls.field_order)
        cls.field_order.insert(0, 'document_type_ids')
        cls.field_order.insert(0, 'document_type_all')

        return super().get_fields()

    @classmethod
    def get_widgets(cls):
        cls.widgets.update(
            {
                'document_type_ids': {
                    'class': 'django.forms.widgets.SelectMultiple',
                    'kwargs': {
                        'attrs': {'class': 'select2', 'size': 10}
                    }
                }
            }
        )

        return super().get_widgets()

    def _get_document_types(self):
        return DocumentType.objects.filter(pk__in=self.document_type_ids)

    def get_filter_text(self):
        result = super().get_filter_text()

        if self.document_type_all:
            document_type_filter_text = _(message='all document types')
        else:
            document_type_filter_text = _(
                message='document types: %(document_types)s'
            ) % {
                'document_types': QuotaBackend._queryset_to_text_list(
                    queryset=self._get_document_types()
                )
            }

        result['document_type_filter_text'] = document_type_filter_text
        return result


class GroupsUsersQuotaMixin:
    @staticmethod
    def _get_user_full_name(user):
        try:
            return user.get_full_name() or user
        except AttributeError:
            return user

    @classmethod
    def get_fields(cls):
        cls.fields.update(
            {
                'group_ids': {
                    'label': _(message='Groups'),
                    'class': 'mayan.apps.forms.form_fields.ModelFormFieldFilteredModelMultipleChoice',
                    'kwargs': {
                        'permission': permission_quota_edit,
                        'required': False,
                        'source_model': Group
                    }, 'help_text': _(
                        message='Groups to which the quota will be applied.'
                    )
                },
                'user_all': {
                    'label': _(message='All users'),
                    'class': 'django.forms.BooleanField', 'default': False,
                    'help_text': _(
                        message='Apply the quota to all users in the system, '
                        'excluding admins and staff. '
                        'Enabling this option, the quota will ignore the '
                        'individual user and group selection.'
                    ), 'required': False
                },
                'user_ids': {
                    'label': _(message='Users'),
                    'class': 'mayan.apps.forms.form_fields.ModelFormFieldFilteredModelMultipleChoice',
                    'kwargs': {
                        'permission': permission_quota_edit,
                        'required': False,
                        'source_queryset': get_user_queryset()
                    }, 'help_text': _(
                        message='Users to which the quota will be applied.'
                    )
                }
            }
        )

        cls.field_order = list(cls.field_order)
        cls.field_order.insert(0, 'user_ids')
        cls.field_order.insert(0, 'group_ids')
        cls.field_order.insert(0, 'user_all')

        return super().get_fields()

    @classmethod
    def get_widgets(cls):
        cls.widgets.update(
            {
                'group_ids': {
                    'class': 'django.forms.widgets.SelectMultiple',
                    'kwargs': {
                        'attrs': {'class': 'select2', 'size': 10}
                    }
                },
                'user_ids': {
                    'class': 'django.forms.widgets.SelectMultiple',
                    'kwargs': {
                        'attrs': {'class': 'select2', 'size': 10}
                    }
                }
            }
        )

        return super().get_widgets()

    def get_filter_text(self):
        result = super().get_filter_text()

        if self.user_all:
            user_filter_text = _(message='all users')
        else:
            user_filter_text = _(message='groups: %(groups)s, users: %(users)s') % {
                'groups': QuotaBackend._queryset_to_text_list(
                    queryset=self._get_groups()
                ),
                'users': QuotaBackend._queryset_to_text_list(
                    queryset=self._get_users()
                )
            }

        result['user_filter_text'] = user_filter_text
        return result

    def _get_groups(self):
        return Group.objects.filter(pk__in=self.group_ids)

    def _get_users(self):
        queryset = get_user_queryset()
        return queryset.filter(pk__in=self.user_ids)
