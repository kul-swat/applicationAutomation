import powerfactory

pf_starting = powerfactory.GetApplicatio()
project_folder = pf_starting.GetProjectFolder("swati.bohidar\\2020 20 2wa\\Equipment Types\DNO - 05 - UKPN - Eastern\Line Types\t-C622")
Application.CommitTransaction()
project_folder.Move("swati.bohidar/2020 20 2wa\Equipment Types\TO - National Grid\Line Types")

project_folder = pf_starting.GetProjectFolder("swati.bohidar/2020 20 2wa/ Equipment Types\NEC - Technical Data\Culham JET")
Application.CommitTransaction()
project_folder.Move("swati.bohidar/2020 20 2wa\Equipment Types\TO - National Grid\Transformer Types\-2-W Transformer Types")

project_folder = pf_starting.GetProjectFolder("swati.bohidar/2020 20 2wa/ Equipment Types\NEC - Technical Data\Culham JET")
Application.CommitTransaction()
project_folder.Move("swati.bohidar/2020 20 2wa\Equipment Types\TO - National Grid\Transformer Types\-2-W Transformer Types")



