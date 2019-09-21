#!/usr/bin/env python
import os
import pathlib
import subprocess
import argparse 
import glob
import time
import shutil

currentPath = os.getcwd()
parser = argparse.ArgumentParser(description='Number of reports you want to store.')
parser.add_argument('-n', '--number', required=False, type=int, help='Number of report to store')
myparser = parser.parse_args()
numberOfReport = myparser.number
enviroment='aws'
userID='H@ck#r' 
#reportSorted(numberOfReport, enviroment, userID)

#def reportSorted(numberOfReport, enviroment, userID):
    
def listOfFolder(number, directory):
    listOfReports = []
    for i in range(number):
        listOfReports.append(sorted(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)[-i-1])
#    print(listOfReports)
    return listOfReports


def inverseList(directory, number):
    totalFolderList = sorted(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)
    selectedFolder = listOfFolder(number, directory)
    ListOfDeletingFolder = set(totalFolderList).difference(selectedFolder)
 #   print(ListOfDeletingFolder)
    return ListOfDeletingFolder

def deleteListOfFolder(directory, number):
    deletingList = inverseList(directory, number)
    for i in deletingList:
  #      print(i)
        shutil.rmtree(i)

account_name = userID
if(enviroment == 'aws'):
    #from module import awsaudit
    awsPath = os.path.join(currentPath, 'reports/AWS/aws_audit')
    os.chdir(awsPath)
    aws = pathlib.Path(account_name)
    if aws.exists():
        awsUser = os.path.join(awsPath, account_name)
        print(awsUser)
        os.chdir(awsUser)
        os.getcwd()
        #listOfFolder(awsUser, numberOfReport)
#        listOfDirectory = listOfFolder(numberOfReport, awsUser)
        deleteListOfFolder(awsUser, numberOfReport)


elif(enviroment == 'azure'):
     #from module import azureaudit
     azurePath = os.path.join(currentPath, 'reports/AZURE')
     os.chdir(azurePath)
     azure = pathlib.Path(azureaudit.account_name)
     if azure.exists():
        azureUser = os.path.join(azurePath, account_name)
        os.chdir(azureUser)
        listOfDirectory = listOfFolder(numberOfReport, awsUser)
        deleteListOfFolder(directory, number)

# elif(enviroment == 'gcp'):
#      #from module import gcpaudit
#     gcpPath = os.path.join(currentPath, 'reports/GCP')
#     os.chdir(currentPath'reports/GCP/')
#     gcp = pathlib.Path(project_name)
#     if gcp.exists():
#         gcpUser = os.path.join(gcp, project_name)
#         os.chdir(gcpUser)
#         listOfDirectory = listOfFolder(numberOfReport, awsUser)
#         deleteListOfFolder(directory, number)
