# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from mock import MagicMock, patch, PropertyMock
from unittest import TestCase
from gs.group.groups.list.membergroups import (
    MemberGroups, PublicGroups, RestrictedGroups, PrivateGroups, SecretGroups, )


class TestMemberGroups(TestCase):
    def test_lower_name(self):
        m = MemberGroups(MagicMock(), MagicMock())
        g = MagicMock(spec=['name'])
        g.name = 'Ethel the Frog'
        r = m.lower_name(g)

        self.assertEqual('ethel the frog', r)

    @patch('gs.group.groups.list.membergroups.user_member_of_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_member_group_true(self, mock_user, mock_umog):
        '''Ensure that the member property of the group is ``True``'''
        mock_umog.return_value = True
        m = MemberGroups(MagicMock(), MagicMock())
        r = m.member_group(MagicMock())

        self.assertTrue(r.member)

    @patch('gs.group.groups.list.membergroups.user_member_of_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_member_group_false(self, mock_user, mock_umog):
        '''Ensure that the member property of the group is ``False``'''
        mock_umog.return_value = False
        m = MemberGroups(MagicMock(), MagicMock())
        r = m.member_group(MagicMock())

        self.assertFalse(r.member)


def create_group(gId, name):
    retval = MagicMock(spec=['id', 'name', ])
    retval.id = gId
    retval.name = name
    return retval


class TestPublicGroups(TestCase):
    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_true(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPublic = True
        m = PublicGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(5, len(r))
        self.assertEqual('abcde', ''.join([g.id for g in r]))

    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_false(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPublic = False
        m = PublicGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(0, len(r))


class TestRestrictedGroups(TestCase):
    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_true(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPublicToSite = True
        m = RestrictedGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(5, len(r))
        self.assertEqual('abcde', ''.join([g.id for g in r]))

    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_false(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPublicToSite = False
        m = RestrictedGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(0, len(r))


class TestPrivateGroups(TestCase):
    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_true(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPrivate = True
        m = PrivateGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(5, len(r))
        self.assertEqual('abcde', ''.join([g.id for g in r]))

    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_false(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isPrivate = False
        m = PrivateGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(0, len(r))


class TestSecretGroups(TestCase):
    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_true(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isSecret = True
        m = SecretGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(5, len(r))
        self.assertEqual('abcde', ''.join([g.id for g in r]))

    @patch('gs.group.groups.list.membergroups.GroupVisibility')
    @patch.object(MemberGroups, 'member_group')
    @patch.object(MemberGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_false(self, mock_user, mock_mg, mock_GV):
        mock_mg.side_effect = lambda g: g
        mock_GV().isSecret = False
        m = SecretGroups(MagicMock(), [create_group(g, g.upper()) for g in 'cabed'])
        r = m.groups

        self.assertEqual(0, len(r))
