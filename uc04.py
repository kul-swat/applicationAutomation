import powerfactory
pf_starting = powerfactory.GetApplication()
activating_project = Application.ActivateProject("2020 27 2WA.IntPrj")
DataObject Application.GetDataFolder("CIM Model.IntPrjfolder")
Clear("CIM Model.IntPrjfolder")
DataObject Application.GetDataFolder("Demand Groups.IntPrjfolder")
Clear("Demand Groups.IntPrjfolder")
DataObject Application.GetDataFolder("Equipment Types.IntPrjfolder\DNO - 01 - UKPN-L.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 02 - UKPN-SE.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 03 - SSE Southern.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 04 - WPD-SW.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 05 - UKPN - Eastern.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 06 - WPD-Mids-E.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 07 - WPD-Mids-W.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 08 - WPD-Wales.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 09 - SP MANWEB.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 10 - NPG-Y.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 11 - NPG-NE.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 12 - ENWL.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 90 - Scottish Power.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\DNO - 91 - SSE-Scot.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\Generic SO Types.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\IFA detailed model types.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\NEC - Technical Data.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\TO - Scottish Hydro Transmission.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\TO - Scittish Power Transmission.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\Western Link HVDC Types.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\Blacklaw items.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\BritNed Harmonic Filter.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\Caithness Moray HVDC Types.IntPrjfolder,
                                      Equipment Types.IntPrjfolder\HVDC Transformers.IntPrjfolder")

Clear("Equipment Types.IntPrjfolder\DNO - 01 - UKPN-L.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 02 - UKPN-SE.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 03 - SSE Southern.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 04 - WPD-SW.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 05 - UKPN - Eastern.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 06 - WPD-Mids-E.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 07 - WPD-Mids-W.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 08 - WPD-Wales.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 09 - SP MANWEB.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 10 - NPG-Y.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 11 - NPG-NE.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 12 - ENWL.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 90 - Scottish Power.IntPrjfolder,
       Equipment Types.IntPrjfolder\DNO - 91 - SSE-Scot.IntPrjfolder
       Equipment Types.IntPrjfolder\Generic SO Types.IntPrjfolder,
       Equipment Types.IntPrjfolder\IFA detailed model types.IntPrjfolder,
       Equipment Types.IntPrjfolder\NEC - Technical Data.IntPrjfolder,
       Equipment Types.IntPrjfolder\TO - Scottish Hydro Transmission.IntPrjfolder,
       Equipment Types.IntPrjfolder\TO - Scittish Power Transmission.IntPrjfolder,
       Equipment Types.IntPrjfolder\Western Link HVDC Types.IntPrjfolder,
       Equipment Types.IntPrjfolder\Blacklaw items.IntPrjfolder,
       Equipment Types.IntPrjfolder\BritNed Harmonic Filter.IntPrjfolder,
       Equipment Types.IntPrjfolder\Caithness Moray HVDC Types.IntPrjfolder,
       Equipment Types.IntPrjfolder\HVDC Transformers.IntPrjfolder")

DataObject Application.GetDataFolder("Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Cross Compound Model for Longannet,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Excitation Control Systems,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Frames,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Governor Control Systems,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\SVC Controllers,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\SWP 2.3IG CS Model,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Switchgear,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\UG Plant Data,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Vestas Library,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Cables,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Generators,
                                      Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Transformer")

Clear("Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Cross Compound Model for Longannet,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Excitation Control Systems,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Frames,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Governor Control Systems,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\SVC Controllers,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\SWP 2.3IG CS Model,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Switchgear,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\UG Plant Data,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Vestas Library,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Cables,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Generators,
       Equipment Types.IntPrjfolder\GEN - Technical Plant Data.IntPrjfolder\Wind Turbine Transformer")
DataObject Application.GetDataFolder("Library.IntPrjfolder")
Clear("Library.IntPrjfolder")
DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Caithness Moray HVDC.ElmNet")
Int ElmNet.Deactivate("Caithness Moray HVDC.ElmNet")
Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Caithness Moray HVDC.ElmNet")
DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 01 - UKPN-London,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 02 - UKPN-SE,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 03 - SSE Southern,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 04 - WPD South West,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 05 - UK Power Networks Eastern,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 06 - WPD East Midlands,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 07 - WPD West Midlands,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 08 - WPD South Wales,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 09 - SP MANWEB (Scottish Power),
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 10 - NPG-Y (Northen Power Grid),
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 11 - NPG-NE  (Northen Power Grid),
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 12 - ENW (Elecrtic North-West),
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\NEC,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\analysis Fixes,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\Distributed Slack-England")

Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 01 - UKPN-London,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 02 - UKPN-SE,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 03 - SSE Southern,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 04 - WPD South West,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 05 - UK Power Networks Eastern,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 06 - WPD East Midlands,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 07 - WPD West Midlands,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 08 - WPD South Wales,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 09 - SP MANWEB (Scottish Power),
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 10 - NPG-Y (Northen Power Grid),
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 11 - NPG-NE  (Northen Power Grid),
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\DNO - 12 - ENW (Elecrtic North-West),
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\NEC,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\analysis Fixes,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - England & Wales.ElmNet\Distributed Slack-England")

DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - Scotland.ElmNet")
Int ElmNet.Deactivate("Grid - Scotland.ElmNet")
Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Grid - Scotland.ElmNet")

DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\IFA 1 HVDC.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\NEMO_HVDCp.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Western Link HVDC.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Areas.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\BMUs.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Boundaries.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Feeders.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Operators.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Owners.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Paths.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Routes.ElmNet,
                                      Network Model.IntPrjfolder\Network Data.IntPrjfolder\Zones.ElmNet")
Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\IFA 1 HVDC.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\NEMO_HVDCp.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Western Link HVDC.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Areas.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\BMUs.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Boundaries.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Feeders.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Operators.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Owners.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Paths.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Routes.ElmNet,
       Network Model.IntPrjfolder\Network Data.IntPrjfolder\Zones.ElmNet")

DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\OFTO.ElmNet\Scotland")
Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\OFTO.ElmNet\Scotland")

int IntCase.Deactivate("Study Cases.IntPrjfolder\01 Monday\Equ-LF[EW]-Shc[rst]@OC2_ALL_REC.IntCase")
DataObject Application.GetDataFolder("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Schemes.IntPrjfolder")
Clear("Network Model.IntPrjfolder\Network Data.IntPrjfolder\Schemes.IntPrjfolder")  
int IntPrj.Activate("Study Cases.IntPrjfolder\01 Monday\Equ-LF[EW]-Shc[rst]@OC2_ALL_REC.IntCase")                                 


int IntScheme.Consolidate("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\CY Variations.IntScheme,
                           Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Defaults.IntScheme,
                           Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation CY.IntScheme")

int IntScheme.Deactivate("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\CY Variations.IntScheme,
                          Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Defaults.IntScheme,
                          Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation CY.IntScheme")

DataObject Application.GetDataFolder("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\SPTL,
                                      Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\CY Variations.IntScheme,
                                      Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Defaults.IntScheme,
                                      Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Life-Time Derogations.IntScheme,
                                      Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Specials for 1B.IntScheme,
                                      Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\SPTL,
                                      Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation CY.IntScheme,
                                      Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation YA.IntScheme")

Clear("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\SPTL,
       Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder\CY Variations.IntScheme,
       Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Defaults.IntScheme,
       Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Life-Time Derogations.IntScheme,
       Operational Library.IntPrjfolder\Mvar Limit Curves.IntPrjfolder\Specials for 1B.IntScheme,
       Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\SPTL,
       Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation CY.IntScheme,
       Operational Library.IntPrjfolder\Thermal Ratings.IntPrjfolder\Variation YA.IntScheme")

DataObject Application.GetDataFolder("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder,
                                      Operational Library.IntPrjfolder\Characteristics.IntPrjfolder,
                                      Operational Library.IntPrjfolder\Demand Transfer.IntPrjfolder,
                                      Operational Library.IntPrjfolder\Outages.IntPrjfolder,
                                      Operational Library.IntPrjfolder\QP-Curves.IntPrjfolder,
                                      Operational Library.IntPrjfolder\Short Circuit Events.IntPrjfolder,
                                      Operational Library.IntPrjfolder\Toga Previous Extract.IntPrjfolder")

Clear("Operational Library.IntPrjfolder\CB Ratings.IntPrjfolder,
       Operational Library.IntPrjfolder\Characteristics.IntPrjfolder,
       Operational Library.IntPrjfolder\Demand Transfer.IntPrjfolder,
       Operational Library.IntPrjfolder\Outages.IntPrjfolder,
       Operational Library.IntPrjfolder\QP-Curves.IntPrjfolder,
       Operational Library.IntPrjfolder\Short Circuit Events.IntPrjfolder,
       Operational Library.IntPrjfolder\Toga Previous Extract.IntPrjfolder")

int IntPrj.Deactivate("2020 27 2WA.IntPrj")
int IntPrj.Activate("2020 27 2WA.IntPrj")
DataObject Application.GetDataFolder("Scenarios.IntPrjfolder")
Clear("Scenarios.IntPrjfolder")


DataObject Application.GetDataFolder("Scripts.IntPrjfolder,
                                      Templates.IntPrjfolder,
                                      Constraint Analysis.IntPrjfolder,
                                      E&W Boundaries.IntPrjfolder,
                                      Favoured Scripts.IntPrjfolder,
                                      Scotland Boundaries.IntPrjfolder,
                                      Scotland Voltages.IntPrjfolder,
                                      Step Response Test.IntPrjfolder,
                                      Test Scripts.IntPrjfolder")
Clear("Scripts.IntPrjfolder,
       Templates.IntPrjfolder,
       Constraint Analysis.IntPrjfolder,
       E&W Boundaries.IntPrjfolder,
       Favoured Scripts.IntPrjfolder,
       Scotland Boundaries.IntPrjfolder,
       Scotland Voltages.IntPrjfolder,
       Step Response Test.IntPrjfolder,
       Test Scripts.IntPrjfolder")

DataObject Application.GetDataFolder("Study Cases.IntPrjfolder")
DataObject DataObject.AddCopy("Study Cases.IntPrjfolder\01 Monday\Equ-LF[EW]-Shc[rst]@OC2_ALL_REC.IntCase")
           DataObject.CopyData("Study Cases.IntPrjfolder")

DataObject Application.GetDataFolder("Study Cases.IntPrjfolder\Base Case.IntCase,
                                      Study Cases.IntPrjfolder\Base Case No Scheme.IntCase,
                                      Study Cases.IntPrjfolder\IFA HVDC Control.IntCase,
                                      Study Cases.IntPrjfolder\01 Monday,
                                      Study Cases.IntPrjfolder\02 Tuesday,
                                      Study Cases.IntPrjfolder\03 Wednesday,
                                      Study Cases.IntPrjfolder\04 Thursday,
                                      Study Cases.IntPrjfolder\05 Friday,
                                      Study Cases.IntPrjfolder\06 Saturday,
                                      Study Cases.IntPrjfolder\07 Sunday,
                                      Study Cases.IntPrjfolder\TAE Released Study Cases")
Clear("Study Cases.IntPrjfolder\Base Case.IntCase,
       Study Cases.IntPrjfolder\Base Case No Scheme.IntCase,       
       Study Cases.IntPrjfolder\IFA HVDC Control.IntCase,
       Study Cases.IntPrjfolder\01 Monday,
       Study Cases.IntPrjfolder\02 Tuesday,
       Study Cases.IntPrjfolder\03 Wednesday,
       Study Cases.IntPrjfolder\04 Thursday,
       Study Cases.IntPrjfolder\05 Friday,
       Study Cases.IntPrjfolder\06 Saturday,
       Study Cases.IntPrjfolder\07 Sunday,
       Study Cases.IntPrjfolder\TAE Released Study Cases")

Application.CommitTransaction()





