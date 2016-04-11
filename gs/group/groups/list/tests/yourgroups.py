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
from gs.group.groups.list.yourgroups import YourGroups


class TestYourGroups(TestCase):
    'Test the list of "your" groups'

    @patch('gs.group.groups.list.yourgroups.user_member_of_group')
    @patch.object(YourGroups, 'get_all_groups')
    @patch.object(YourGroups, 'loggedInUser', new_callable=PropertyMock)
    def test_groups(self, mock_user, mock_get_all_groups, mock_umog):
        mock_get_all_groups.return_value = range(0, 6)
        mock_umog.side_effect = [True, False, False, True, True, True]

        y = YourGroups(MagicMock())
        r = y.groups

        self.assertEqual([0, 3, 4, 5], r)
