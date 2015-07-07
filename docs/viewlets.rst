Viewlets
========

.. currentmodule:: gs.group.groups.list.

This :mod:`gs.group.groups.list` product provides

* A viewlet for the `site homepage`_, which contains a viewlet
  *manager* for the group lists
* The `privacy viewlets`_ for the different privacy levels 
* A `content provider`_ for displaying a list of groups.

Site homepage
-------------

The viewlet ``gs-groups-list`` provides the viewlet for the main
area of the site homepage (see :mod:`gs.site.home`). It contains
nothing other than the viewletc *manager*, which provides the
interface :class:`.interfaces.IGroupList`.

.. class:: gs.group.groups.list.interfaces.IGroupList

   The interface for the Groups viewlet manager. The `privacy
   viewlets`_ that actually list the groups use this manager,

Privacy viewlets
----------------

The viewlets provide the actual lists of groups for the `site
homepage`_. There are four lists, for each of the four privacy
levels (see :mod:`gs.group.privacy`):

* Public ``gs-groups-list-public``
* Private ``gs-groups-list-private``
* Restricted ``gs-groups-list-restricted``
* Secret ``gs-groups-list-secret``

Each viewlet is registered using some ZCML:

.. code-block:: xml

  <browser:viewlet
    name="gs-groups-list-public"
    manager=".interfaces.IGroupList"
    class=".sitehomeviewlet.ListPublic"
    template="browser/templates/list-public.pt"
    permission="zope2.View"
    weight="10"
    title="Public Groups" />

Content provider
----------------

The content provider ``groupserver.GroupListContent`` lists the
groups, taking in a list of group-info objects as its argument,
as shown in the following TAL:

.. code-block:: xml

  <tal:block
    define="groups view/memberGroups"
    replace="structure provider:groupserver.GroupListContent">
    A list of the secret groups that the viewer is a member of.
  </tal:block>

..  LocalWords:  Viewlets viewlets
