from __future__ import absolute_import, print_function

from sentry.db.models import (
    FlexibleForeignKey,
    DateTimeField,
    BoundedPositiveIntegerField,
    Model,
    sane_repr)
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from enum import Enum


class DeletedReason(Enum):
    ACCOUNT_CLOSURE = 0
    USER_REQUESTED = 1


class OrganizationDeleted(Model):
    deleted_user = FlexibleForeignKey('sentry.User')
    reason = BoundedPositiveIntegerField(  # Am I doing this right? Choices?
        choices=(
            (DeletedReason.ACCOUNT_CLOSURE, _('ACCOUNT_CLOSURE')),
            (DeletedReason.USER_REQUESTED, _('USER_REQUESTED'))
        )
    )
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(default=timezone.now)
    timestamp = DateTimeField(default=timezone.now)
    __repr__ = sane_repr('deleted_user_id', 'name', 'slug')
