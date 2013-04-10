#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os
import shutil
import makerProjectManager
import makerWxGUI
import wx
import sys
import makerVersion
from random import randint

class TestApp(wx.App):
    
    def OnInit(self):

        self.mainView = self.create(None)
        return True
       

    def create(self, parent):
        return TestView(parent) 


class ProjectManagerTestController(makerProjectManager.ProjectManagerController):


   def showProgress(self, limit, Message, title):
       print Message
       
   def updateProgressPulse(self, foo):

       print "updating progress pulse"
       
   def errorMessage(self, message):
       
       print "Error Message:", message 
       

class TestProjectManager(makerProjectManager.ProjectManager):

    def __init__(self, view):
        
        self.controller = ProjectManagerTestController(self, view)
        self.setProjectDir()
        
        self.linkedProjectPaths = []
        self.loadLinkedProjects()
        self.linkedProjects = {}
        self.controller.listProjectsInTree(self.getProjects())
        self.openProjects = []
        self.openFiles = []
        self.projectConvertRepoName = "Test-MakerProjects"
        
        # call converter manually for testing
        #self.checkForSandboxedProjects()
        
    def getSystemPath(self):
        """ get system path """
        return os.path.join(os.getcwd(), "system/")
    
    def getApplicationSupportDir(self):
    
        try:
            theDir = os.environ['HOME']
        except:
            theDir = os.environ['HOMEPATH']
        
        return os.path.join(theDir, "Library/Application Support/TheMaker-TESTING/")
   


class TestView(makerWxGUI.wxPythonGUI):
    
    def Ask_YesOrNo(self, question):
        return self.choiceReturnString
    
    
    def Input(self, Question="?", title = None):
    
        print "Input string was:", self.inputReturnString
        return self.inputReturnString
    
    def partArt(self, il, image_size):
        """ don't need no custom art in this mock class """
        pass

    def Error(self, Message):
        
        self._lastErrorMessage = Message

    
    def setInputReturnString(self, string):

        self.inputReturnString = string


    def setChoiceReturnString(self, string):

        self.choiceReturnString = string



class MakerTest(unittest.TestCase):
    
    def tearDown(self):
        
        shutil.rmtree(self.convertedProjectsPath, True)
        self.app.Destroy()
    
    def setUp(self):
       
        self.user_home = "/Users/maker"
         
        self.app = TestApp()
        self.pm = TestProjectManager(self.app.mainView)
        self.pm.controller.testing = True
        
        self.projectPath = os.path.join(self.pm.getApplicationSupportDir(), "makerProjects")
        self.sandBox = self.projectPath
       
        
        self.convertedProjectsPath = os.path.join(self.user_home, self.pm.projectConvertRepoName)


    def test_todo(self):
        pass
    
    # controller should not create central project dir !!!

    def test_ifNoProjectsInSandboxDoNothing(self):
        pass
    

    def test_ifProjectExistsInNewRepoAppendNumber(self):
        pass
    

    def test_ifProjectsInSandboxMoveToHomeAndConvert(self):
        
        # create Test Sandbox
        if not os.path.isdir(self.sandBox):
            os.mkdir(self.sandBox)
        
        
        print "creating dummy projects"
        dummy = ["Test_One","Test_Two","Test Three"," Test Four"]
        for item in dummy:
            if not os.path.isdir(os.path.join(self.sandBox, item)):
                os.mkdir(os.path.join(self.sandBox, item))
        
        projectsInSandbox = [] 
        projectsInNewRepo = []
        
        def getProjectsInSandbox():
            projects = []
            for item in os.listdir(self.sandBox):
                if not item.startswith("."):
                    projects.append(item)
            
            return projects
        
        def getProjectsInCreatedRepo():
            projects = []
            for item in os.listdir(self.convertedProjectsPath):
                if not item.startswith("."):
                    projects.append(item)
            
            return projects
        
        projectsInSandbox = getProjectsInSandbox()
        
        self.pm.checkForSandboxedProjects()
        
        self.assertTrue(os.path.isdir(self.convertedProjectsPath), "new Repo should have been created...")
        
        self.assertEqual(len(projectsInSandbox), len(getProjectsInCreatedRepo()), "All projects should have been moved...")
        
        self.assertEqual(len(projectsInSandbox), 
                         len(getProjectsInCreatedRepo()), 
                         "Projects from Sandbox should be all linked")
        
        
        for item in getProjectsInCreatedRepo():
            self.assertTrue(item.endswith(".makerProject"), "projects in new repo should be bundles")

        self.assertFalse(os.path.isdir(self.sandBox), "Sandbox project repo deleted...")
        
              
if __name__=="__main__":
    unittest.main()