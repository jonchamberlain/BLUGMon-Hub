import os

def parsejobs():
    """Gets jobs to be run from the Jobs Folder and adds them
    to the jobs list
    """
    #moduleList = os.listdir(os.getcwd() + "/modules/")
    for root, moduleNames, fileNames in os.walk('./modules/'):
        for moduleName in moduleNames:
            #import each module in the module directory
            exec("import " + "modules." + moduleName + "." + moduleName + " as runModule")
            #run the moduleMain function in each module.
             #moduleMain always returns a list object with the following keys
            # - status (boolean True or False)
            # - message (string a short message that describes the result)
            result = runModule.moduleMain()
            print result['message']

def startschedular():
    pass
parsejobs()

