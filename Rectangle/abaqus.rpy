# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_15-23.27.30 176069
# Run by r-sur on Thu Dec  7 16:00:18 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=177.151031494141, 
    height=132.476852416992)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Project2-2020.cae')
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#* MdbError: incompatible release number, expected 2022, got 2020
upgradeMdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/Project2-2020-2020.cae", 
    "C:/Users/r-sur/OneDrive/Desktop/Suresh1/Project2-2020.cae", )
#: The model database "C:\Users\r-sur\OneDrive\Desktop\Suresh1\Project2-2020_TEMP.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database has been saved to "C:\Users\r-sur\OneDrive\Desktop\Suresh1\Project2-2020.cae".
#: The model database "C:\Users\r-sur\OneDrive\Desktop\Suresh1\Project2-2020-2020.cae" has been converted.
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/XX.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/XX.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/XX1701945084.421.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/XX1701945084.421.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/XX1701945084.421.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR)
session.viewports['Viewport: 1'].animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.9366, 
    farPlane=49.2341, width=31.1734, height=12.7643, viewOffsetX=-0.3723, 
    viewOffsetY=0.450592)
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=NONE)
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/r-sur/AppData/Local/Temp/XX1701945084.421.odb'])
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/XY.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/XY.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/XY1701945311.173.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/XY1701945311.173.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/XY1701945311.173.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/r-sur/AppData/Local/Temp/XY1701945311.173.odb'])
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/XZ.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/XZ.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/XZ1701945324.458.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/XZ1701945324.458.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/XZ1701945324.458.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/r-sur/AppData/Local/Temp/XZ1701945324.458.odb'])
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/YY.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/YY.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/YY1701945337.227.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/YY1701945337.227.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/YY1701945337.227.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          4
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/r-sur/AppData/Local/Temp/YY1701945337.227.odb'])
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/YZ.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/YZ.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/YZ1701945343.881.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/YZ1701945343.881.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/YZ1701945343.881.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          3
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
a = mdb.models['XX'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/r-sur/AppData/Local/Temp/YZ1701945343.881.odb'])
o3 = session.openOdb(name='C:/Users/r-sur/OneDrive/Desktop/Suresh1/ZZ.odb')
#* OdbError: The database is from a previous release of Abaqus. 
#* Run abaqus -upgrade -job <newFileName> -odb <oldOdbFileName> to upgrade it.
from  abaqus import session
session.upgradeOdb("C:/Users/r-sur/OneDrive/Desktop/Suresh1/ZZ.odb", 
    "C:/Users/r-sur/AppData/Local/Temp/ZZ1701945349.931.odb", )
from  abaqus import session
o7 = session.openOdb('C:/Users/r-sur/AppData/Local/Temp/ZZ1701945349.931.odb')
#: Model: C:/Users/r-sur/AppData/Local/Temp/ZZ1701945349.931.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       6
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
mdb.save()
#: The model database has been saved to "C:\Users\r-sur\OneDrive\Desktop\Suresh1\Project2-2020.cae".
