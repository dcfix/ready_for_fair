from django.conf import settings
from django.db import models


class Club(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="The name of the club.",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="club_created_by",
        blank=True,
        null=True,
    )
    modified_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="club_modified_by",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    # a club can have zero to many projects
    # for example, Flathead County Fair, 2025
    # or the Food Fair
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    club = models.ForeignKey("Club", on_delete=models.RESTRICT, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="project_created_by",
        blank=True,
        null=True,
    )
    modified_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="project_modified_by",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    # a group can have zero to many groups
    # for example, The Smith family, who has 3 kids raising 3 pigs and a backup
    # or entries for the food fair
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    club = models.ForeignKey("Club", on_delete=models.RESTRICT, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="group_created_by",
        blank=True,
        null=True,
    )
    modified_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="group_modified_by",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Member(models.Model):
    # a group can have one to many members
    # For a family, a parent would be a member with leader=True,
    # while kids would be group members
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="member",
        blank=True,
        null=True,
    )
    is_leader = models.BooleanField()
    group = models.ForeignKey("Group", on_delete=models.RESTRICT, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="member_created_by",
        blank=True,
        null=True,
    )
    modified_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="member_modified_by",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
