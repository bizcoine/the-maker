# This file was automatically generated by pywxrc, do not edit by hand.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res


class xrcnewFile(wx.Dialog):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "newFile")
        self.PostCreate(pre)

        # create attributes for the named items in this container
        self.textField = xrc.XRCCTRL(self, "textField")
        self.langChoice = xrc.XRCCTRL(self, "langChoice")
        self.static = xrc.XRCCTRL(self, "static")
        self.Add = xrc.XRCCTRL(self, "Add")
        self.Cancel = xrc.XRCCTRL(self, "Cancel")



# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    newFile_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxDialog" name="newFile">
    <title>add new file</title>
    <centered>1</centered>
    <pos>10,0</pos>
    <size>450, 140</size>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxPanel">
              <object class="wxTextCtrl" name="textField">
                <value>newFilename</value>
                <pos>20,40</pos>
                <size>300, 25</size>
              </object>
              <object class="wxChoice" name="langChoice">
                <content>
                  <item/></content>
                <selection></selection>
                <pos>340, 40</pos>
                <size>78,20</size>
              </object>
              <object class="wxStaticText" name="static">
                <label>Language:</label>
                <pos>346, 15</pos>
              </object>
            </object>
          </object>
        </object>
        <option>1</option>
        <flag>wxGROW</flag>
      </object>
      <object class="sizeritem">
        <object class="wxPanel">
          <object class="wxButton" name="Add">
            <label>Add</label>
            <default>1</default>
            <pos>335, 4</pos>
            <size>80, 25</size>
          </object>
          <object class="wxButton" name="Cancel">
            <label>Cancel</label>
            <default>0</default>
            <pos>236, 4</pos>
            <size>80, 25</size>
          </object>
        </object>
        <option>0</option>
        <flag>wxEXPAND</flag>
        <minsize>440, 40</minsize>
      </object>
    </object>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/newFile/newFile_xrc', newFile_xrc)
    __res.Load('memory:XRC/newFile/newFile_xrc')


# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("add new file")
    _("newFilename")
    _("Language:")
    _("Add")
    _("Cancel")

