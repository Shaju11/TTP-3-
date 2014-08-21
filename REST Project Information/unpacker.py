import test_main
import ast


def splitObjectsNew(aString):
    aString = aString[2:(len(aString)-2)]
    listOfString = aString.split('}, {')
    listOfDicts = []
    for rowString in listOfString:
        rowDict = ast.literal_eval('{' + rowString + '}')
        listOfDicts.append(rowDict)
    return listOfDicts


def splitObjects(string):
    string = string[2:(len(string)-2)]  # deletes first and last brackets
    stringList = string.split('), (')  # splits on ')'
    return stringList


def makePersonsStringIntoObjects(personString):
    """takes a sting with the person info then turns it into a list of objects"""
    listOfDictOfPerson = splitObjectsNew(personString)
    personObjList = []
    #[{"EmployeeID":"33", "Name":"James", "Availability":"0", "AvailabilityDate":"2011-05-05", "Position":"7", "EmploymentType":"0"}]
    for dictOfPerson in listOfDictOfPerson:
        personObj = test_main.Person()
        personObj.id = dictOfPerson['EmployeeID']
        personObj.name = dictOfPerson['Name']
        personObj.availability = dictOfPerson['Availability']
        personObj.availabilitydate = dictOfPerson['AvailabilityDate']
        personObj.position = dictOfPerson['Position']  # as in, rank, I think?
        personObj.employeetype = dictOfPerson['EmploymentType'] # not relevant (yet??)
        personObjList.append(personObj)
    return personObjList


#def makePersonsStringIntoObjects(personsString):
#    """takes a sting with the person info then turns it into a list of objects"""
#    personList = splitObjects(personsString)
#    personObjList = []
#    for item in personList:
#        personAttribList = item.split(', ')
#        personObj = test_main.Person()
#        personObj.id = personAttribList[0]
#        personObj.name = personAttribList[1]
#        personObj.availability = personAttribList[2]
#        personObj.position = personAttribList[3]  # as in, rank, I think?
#        personObj.availabilitydate = personAttribList[4]
#        personObj.employeetype = personAttribList[5]  # not relevant (yet??)
#        personObjList.append(personObj)
#    return personObjList


def makePersonSkillsStringIntoObjects(personSkillString):
    """takes a sting with the person skill info then turns it into a list of objects"""
    listOfDictOfPersonSkill = splitObjectsNew(personSkillString)
    personSkillObjList = []
    #[{"EmployeeSkillID":"35", "EmployeeID":"33", "SkillID":"30", "SkillLevel":"3", "CategoryID":"31"}]
    for dictOfPersonSkill in listOfDictOfPersonSkill:
         personSkillObj = test_main.PersonSkill()
         personSkillObj.id = dictOfPersonSkill['EmployeeSkillID']
         personSkillObj.EmployeeID = dictOfPersonSkill['EmployeeID']
         personSkillObj.SkillID = dictOfPersonSkill['SkillID']
         personSkillObj.SkillLevel = dictOfPersonSkill['SkillLevel']
         personSkillObj.CategoryID = dictOfPersonSkill['CategoryID']  # as in, rank, I think?
         personSkillObjList.append(personSkillObj)
    return personSkillObjList


#def makePersonSkillsStringIntoObjects(personSkillsString):
#    """takes a sting with the person skill info then turns it into a list of objects"""
#    skillList = splitObjects(personSkillsString)
#    skillObjList = []
#    for item in skillList:
#        skillAttribList = item.split(', ')
#        skillObj = test_main.PersonSkill()
#        skillObj.id = skillAttribList[0]
#        skillObj.personId = skillAttribList[1]
#        skillObj.skillId = skillAttribList[2]
#        skillObj.level = skillAttribList[3]
#        skillObj.categoryId = skillAttribList[4]
#        skillObjList.append(skillObj)
#    return skillObjList


def makeProjectsStringIntoObjects(projectsString):
    listOfDictOfProject = splitObjectsNew(projectsString)
    projectObjList = []
    for dictOfProject in listOfDictOfProject:
        #and example of a dictOfProject
        #{"Status": "Active", "StartDate": "2013/10/03", "NumberOfPeople": 5, "EndDate": "2014/09/20", "Name": "Ninja Swords", "ProjectID": 1, "Client": "Hattori Hanzo"}
        project = test_main.Project()
        project.id = dictOfProject['ProjectID']
        project.name = dictOfProject['Name']
        project.client = dictOfProject['Client']
        project.status = dictOfProject['Status']
        project.numberOfPeople = dictOfProject['NumberOfPeople']
        project.startdate = dictOfProject['StartDate']
        project.enddate = dictOfProject['EndDate']
        projectObjList.append(project)
    return projectObjList

#def makeProjectsStringIntoObjects(projectsString):
#    """takes a string with the project info then turns it into a list of objects"""
#    projectList = splitObjects(projectsString)
#    projectObjList = []
#    for item in projectList:
#        projectAttribList = item.split(', ')
#        projectObj = test_main.Project()
#        projectObj.id = projectAttribList[0]
#        projectObj.name = projectAttribList[1]
#        projectObj.client = projectAttribList[2]
#        projectObj.status = projectAttribList[3]
#        projectObj.numberOfPeople = projectAttribList[4]
#        projectObj.startDate = projectAttribList[5]
#        projectObj.endDate = projectAttribList[6]
#        projectObjList.append(projectObj)
#    return projectObjList


def makeProjectSkillsStringIntoObjects(projectSkillsString):
    listOfDictOfProjectSkills = splitObjectsNew(projectSkillsString)
    projectSkillObjList = []
    for dictOfProjectSkills in listOfDictOfProjectSkills:
        #eg of dictOfProjectSkills
        #[{"ProjectSkillID":"40", "ProjectID":"39", "SkillID":"30", "LevelMin":"3", "LevelMax":"5", "CategoryID":31"}]
        projectSkillsObj = test_main.ProjectSkill()
        projectSkillsObj.id = dictOfProjectSkills['ProjectSkillID']
        projectSkillsObj.projectId = dictOfProjectSkills['ProjectID']
        projectSkillsObj.skillId = dictOfProjectSkills['SkillID']
        projectSkillsObj.levelMin = dictOfProjectSkills['LevelMin']
        projectSkillsObj.levelMax = dictOfProjectSkills['LevelMax']
        projectSkillsObj.categoryId = dictOfProjectSkills['CategoryID']
        projectSkillObjList.append(projectSkillsObj)
    return projectSkillObjList

#def makeProjectSkillsStringIntoObjects(projectSkillsString):
#    projectSkillsList = splitObjects(projectSkillsString)
#    projectSkillsObjList = []
#    for item in projectSkillsList:
#        projectSkillsAttribList = item.split(', ')
#        projectSkillsObj = test_main.ProjectSkill()
#        projectSkillsObj.id = projectSkillsAttribList[0]
#        projectSkillsObj.projectId = projectSkillsAttribList[1]
#        projectSkillsObj.skillId = projectSkillsAttribList[2]
#        projectSkillsObj.levelMin = projectSkillsAttribList[3]
#        projectSkillsObj.levelMax = projectSkillsAttribList[4]
#        projectSkillsObj.categoryId = projectSkillsAttribList[5]
#        projectSkillsObjList.append(projectSkillsObj)
#    return projectSkillsObjList