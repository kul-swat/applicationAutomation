import powerfactory
int Application.ActivateProject("GBTSSNDF 2020 WK18 V1.IntPrj")
pf_starting = powerfactory.GetApplicatio()
project_folder = pf_starting.GetProjectFolder("swati.bohidar\\GBTSSNDF 2020 WK18 V1\\Network Model\\Network Data\\
                                                Schemes\\Equ-LF[EW]-Shc[rst]@OC2_ALL_REC")


"""1. int Application.ActivateProject(str name)
DataObject Application.GetDataFolder(str classname, [int iCreate])
DataObject.IsNetworkDataFolder()"""

""""2. Create the new -> expension stage in the folder and name it as Delete Tap Controllers.
Give activation date 1 year ahead.
A dialogue box will appear select NO.
"""
rightClick =  IntScheme.NewStage("Delete Tap Controllers", int iUTCtime, 1 ) #1 new stage is added
setAheadOneYr = ElmRelay.SetTime(float time, int type, int zone, int unit ) #for changing the time 1 yr ahead
"""list DataObject.GetContents([str Name,] [int recursive]) #for new
list DataObject.GetContents([str Name,] [int recursive]) # for expansion stage
int ComPython.SetInputParameterString(str name, str value ) 
#Sets the string input parameter value deﬁned in the ComPython edit dialog."""

"""3 "Right click on reduction stage and select Split.
Then select Delete Tap Controllers.
Click OK"
"""
reduction_stage = rightClick.GetInputParameterString("reduction stage") #checking the reduction stage present
split_selection = reduction_stage.GetContents("Split", 0) #0 is for only split is collected
third_done = split_selection.GetInputParameterString("OK")

"""4. "Click on down arrow and select filters.
Select all the tap controllers except 1st one."
"""
int SetColscheme.SetFilter(int filter, [int page] )

"""5. "Right click on selected Tap controllers and select assign with children from -> move
select split."
"""
ComUcteexp.SetGridSelection(list gridsToExport) #select all
list DataObject.GetContents([str children from move] [int recursive])
select split

6. activate scheme, list DataObject.GetContents([str split] [int recursive])
str Application.GetActiveCalculationStr() #load flow calculation
list DataObject.GetContents([str split] [int recursive]) # EDIT OBJ CLICK ON SPEN
7. bus target voltage #
str Application.GetActiveCalculationStr()
execute
variable = DataObject Application.GetActiveStudyCase()
int IntCase.Consolidate()



*[int error list mainNodes, list connectionCubicles, list allElements ] ElmTrfstat.GetSplit(int index)

DataObject DataObject.GetParent()
int DataObject.ShowEditDialog()

int SetColscheme.SetFilter(int filter, [int page]) int SetColscheme.SetFilter(DataObject obj, [int page])
int IntCase.Consolidate()
int IntCase.Consolidate()
int IntCase.Deactivate()







import powerfactory
pro = powerfactory.getapplication()
int Application.ActivateProject(str name) #activate proj
DataObject.IsNetworkDataFolder()
how to reach basic data via reduction stage,  change name to Dalete Tap Controllers and change the date to 1 year ahead, and no
right click on reductio sateg, select split. Ok to close the window.
click on down arrow button, select filter. select everything except 1st and right click on selected ssign with children-> move
select split to close the window.
go to output terminal. right click, edit obj, 
Application.WriteChangesToDb()

 ElmDsl.ExportToFile(str filePath, [str colSeparator], [int useLocalHeader] )

