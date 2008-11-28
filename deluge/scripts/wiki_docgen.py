#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Martijn Voncken 2008 <mvoncken@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, write to:
#     The Free Software Foundation, Inc.,
#     51 Franklin Street, Fifth Floor
#     Boston, MA  02110-1301, USA.
#

#

#generate docs for deluge-wiki
#client doc's For core.
#

from deluge.core.core import Core
from deluge.ui.client import aclient
import pydoc
import inspect



if False: #aclient non-core
    methods = sorted([m for m  in dir(aclient) if not m.startswith('_')
        if not m in ['add_torrent_file', 'has_callback', 'get_method',
            'methodHelp','methodSignature','list_methods','add_torrent_file_binary']])

    for m in methods:
        func = getattr(aclient, m)
        method_name = m
        if method_name in dir(aclient):
            func = getattr(aclient, method_name)
        try:
            params = inspect.getargspec(func)[0][1:]
        except:
            continue

        print("\n'''%s(%s): '''\n" %(method_name, ", ".join(params)))
        print("%s" % pydoc.getdoc(func))

if True: #baseclient/core
    methods = sorted([m for m in dir(Core) if m.startswith("export")]
        + ['export_add_torrent_file_binary'] #HACK

        )

    for m in methods:

        method_name = m[7:]
        if method_name in dir(aclient):
            func = getattr(aclient, method_name)
        else:
            func = getattr(Core, m)

        params = inspect.getargspec(func)[0][1:]
        if (aclient.has_callback(method_name)
                and not method_name in ['add_torrent_file_binary']):
            params = ["[callback]"] + params

        print("\n'''%s(%s): '''\n" %(method_name, ", ".join(params)))
        print("%s" % pydoc.getdoc(func))

if False: #plugin-manager
    import WebUi
    from WebUi.pluginmanager import PluginManager

    for m in methods:
        func = getattr(PluginManager, m)
        method_name = m
        params = inspect.getargspec(func)[0][1:]
        print("\n'''%s(%s): '''\n" %(method_name, ", ".join(params)))
        print("%s" % pydoc.getdoc(func))
