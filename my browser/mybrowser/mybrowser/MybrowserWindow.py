# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('mybrowser')

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('mybrowser')

from mybrowser_lib import Window
from mybrowser.AboutMybrowserDialog import AboutMybrowserDialog
from mybrowser.PreferencesMybrowserDialog import PreferencesMybrowserDialog

# See mybrowser_lib.Window.py for more details about how this class works
class MybrowserWindow(Window):
    __gtype_name__ = "MybrowserWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(MybrowserWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutMybrowserDialog
        self.PreferencesDialog = PreferencesMybrowserDialog

        # Code for other initialization actions should be added here.
        
        self.refreshBtn = self.builder.get_object("refreshBtn")
        self.urlEntry = self.builder.get_object("urlEntry") 
        self.scrolledwindow = self.builder.get_object("scrolledwindow") 
        self.toolbar = self.builder.get_object("toolbar")
        
        context = self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)
      
        self.webView = WebKit.WebView()
        self.scrolledwindow.add(self.webView)
        self.webView.show()    

    def on_refreshBtn_clicked(self, widget):
        self.webView.reload()

    def on_urlEntry_activate(self, widget):
        url = widget.get_text()
        self.webView.open(url)
        print url
