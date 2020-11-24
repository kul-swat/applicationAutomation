import pandas as pd
import powerfactory
import logging
logging.basicConfig(filename="log_test.log",level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s')

read_file = pd.read_excel("C:/Users/swat/Documents/NationalGrid/oc2/2018_OC2 Boundary_copy.xlsx", sheet_name = "OC2-Template")
withReplaced_value = read_file.replace(to_replace ="\\Charles.V.Omondi.IntUser\\2018 46 2WA.IntPrj", 
                                            value ="\\Nutan.Verma.IntUser\\OC2\\OC2 Submission\\2020 21 2WA.IntPrj")
logging.debug(withReplaced_value.head(2))
number_of_rows = len(index) + 1

pf_starting = powerfactory.GetApplication()
project_folder = pf_starting.GetProjectFolder("swati.bohidar/2020 20 2wa/ network model/ network data/boundaries/ 
                                                    current oc2 boundaries/ basic data")
Application.CommitTransaction()
project_folder.Clear()
IntVec.Set(int index, float value = number_of_rows) #ht




