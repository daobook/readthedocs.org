"""Managers for OAuth models."""

from django.db import models


class RelatedUserQuerySet(models.QuerySet):

    """For models with relations through :py:class:`User`."""

    def api(self, user=None):
        """Return objects for user."""
        return self.none() if not user.is_authenticated else self.filter(users=user)


class RemoteRepositoryQuerySet(RelatedUserQuerySet):
    pass


class RemoteOrganizationQuerySet(RelatedUserQuerySet):
    pass
