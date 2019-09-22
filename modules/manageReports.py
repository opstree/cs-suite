#!/usr/bin/env python
import os
import pathlib
import argparse 
import glob
import time
import shutil

def listOfFolder(number, directory):
    
    listOfReports = []
    for i in range(number):
        listOfReports.append(sorted(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)[-i-1])
    return listOfReports


def inverseList(directory, number):
    totalFolderList = sorted(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)
    selectedFolder = listOfFolder(number, directory)
    ListOfDeletingFolder = set(totalFolderList).difference(selectedFolder)
    return ListOfDeletingFolder

def deleteListOfFolder(directory, number):
    deletingList = inverseList(directory, number)
    for i in deletingList:
        shutil.rmtree(i)

def numberOfReports(enviroment, number):
    currentPath = os.getcwd()

    if(enviroment == 'aws'):
        from modules import awsaudit
        awsPath = os.path.join(currentPath, 'reports/AWS/aws_audit')
        os.chdir(awsPath)
        aws = pathlib.Path(awsaudit.account_name)
        if aws.exists():
            awsUser = os.path.join(awsPath, awsaudit.account_name)
            os.chdir(awsUser)
            os.getcwd()
            deleteListOfFolder(awsUser, number)


    elif(enviroment == 'azure'):
        from modules import azureaudit
        azurePath = os.path.join(currentPath, 'reports/AZURE')
        os.chdir(azurePath)
        azure = pathlib.Path(azureaudit.account_name)
        if azure.exists():
            azureUser = os.path.join(azurePath, azureaudit.account_name)
            os.chdir(azureUser)
            deleteListOfFolder(azureUser, number)

    elif(enviroment == 'gcp'):
        from module import gcpaudit
        gcpPath = os.path.join(currentPath, 'reports/GCP')
        os.chdir(gcpPath)
        gcp = pathlib.Path(gcpaudit.project_name)
        if gcp.exists():
            gcpUser = os.path.join(gcp, gcpaudit.project_name)
            os.chdir(gcpUser)
            deleteListOfFolder(gcpUser, number)
