import tkinter as tk
from tkinter import ttk



def openInfoFile():
    with open('info.txt', 'r') as x:
        for line in x:
            (key, val) = line.rstrip("\n").split("=")
            cInfo_d[key] = val



def savePlayerSheet():
    cName_inputValue = cName_input.get("1.0",tk.END)
    cInfo_d.update(Name=str(cName_inputValue))
    print(cName_inputValue)

    with open('info.txt', 'w') as s:
        for key,value in cInfo_d.items():
            s.write('%s=%s\n' % (key,value))
            s.close()






cInfo_d = {}

window = tk.Tk()
window.title("Character Sheet")
openInfoFile()
print(cInfo_d)

notebook = ttk.Notebook(window)


dndPlayerSheet = tk.Label(notebook, background="grey")
dndSpellSheet = tk.Label(notebook)
dndMonsterSheet = tk.Label(notebook)

notebook.add(dndPlayerSheet, text = "Playercard")
notebook.add(dndSpellSheet, text = "Spell Sheet")
notebook.add(dndMonsterSheet, text = "Monster Data")


notebook.pack(expand=True, fill="both")















########################################################################################################################

#character General information frame
generalInfo_frame = tk.Frame(dndPlayerSheet)
generalInfo_frame.grid(row=0, column=0, padx=5, pady=(5,0), columnspan=3, sticky="news")

#character General information
cName = tk.Label(generalInfo_frame, text = "Name", height=1)
cName.grid(row=0, column=0, rowspan=2)
cName_input = tk.Text(generalInfo_frame, width=20, height=1, font=('', 32))
cName_input.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
cName_input.insert(tk.END, cInfo_d.get('Name'))

cClass = tk.Label(generalInfo_frame, text="Class")
cClass.grid(row=0, column=2)
cClass_input = tk.Text(generalInfo_frame, width=20, height=1)
cClass_input.grid(row=0, column=3, padx=5, pady=5)
#cClass_input.insert(tk.END, cInfo_d.get('Class'))

cLevel = tk.Label(generalInfo_frame, text="Level")
cLevel.grid(row=0, column=4)
cLevel_input = tk.Text(generalInfo_frame, width=3, height=1)
cLevel_input.grid(row=0, column=5, padx=5, pady=5)
#cLevel_input.insert(tk.END, cInfo_d.get('Level'))

cRace = tk.Label(generalInfo_frame, text="Race")
cRace.grid(row=1, column=2)
cRace_input = tk.Text(generalInfo_frame, width=20, height=1)
cRace_input.grid(row=1, column=3, padx=5, pady=5)
#cRace_input.insert(tk.END, cInfo_d.get('Race'))

cExperience = tk.Label(generalInfo_frame, text="Experience Points")
cExperience.grid(row=1, column=4)
cExperience_input = tk.Text(generalInfo_frame, width=10, height=1)
cExperience_input.grid(row=1, column=5, padx=5, pady=5)
#cExperience_input.insert(tk.END, cInfo_d.get('Experience_Points'))


########################################################################################################################

#Character Stats frame
stats_Frame = tk.Frame(dndPlayerSheet)
stats_Frame.grid(row=1, column=0, padx=(5,0), pady=5, rowspan=100, sticky="news")

#Character Stats
pBonus = tk.Label(stats_Frame, text="Proficiency Bonus")
pBonus.grid(row=0, column=0, padx=5, pady=5)
pBonus_input = tk.Text(stats_Frame, width=2, height=1)
pBonus_input.grid(row=0, column=1, padx=5, pady=5)
pInpiration = tk.Checkbutton(stats_Frame, text="Inspiration")
pInpiration.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

#Character Strength Stats
pStrength_Frame = tk.LabelFrame(stats_Frame, text="Strength")
pStrength_Frame.grid(row=2, column=0, columnspan=2, padx=10, pady=2)

pRolls = tk.Button(pStrength_Frame, text = "Roll")
pRolls.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pStr_input = tk.Text(pStrength_Frame, height=1, font=("", 64), width=2)
pStr_input.grid(row=0, column=0, rowspan=4, padx=5, pady=(5,0))

pStr_ST = tk.Checkbutton(pStrength_Frame, text = "Saving Throw")
pStr_ST.grid(row=0, column=1, sticky="W")
pStr_ST_Num = tk.Text(pStrength_Frame, width=2, height=1)
pStr_ST_Num.insert(tk.END, "22") #How to save the data inputed by the user *************************************
pStr_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pAthletics = tk.Checkbutton(pStrength_Frame, text = "Athletics")
pAthletics.grid(row=1, column=1, sticky="W")
pAthletics_Num = tk.Text(pStrength_Frame, width=2, height=1)
pAthletics_Num.grid(row=1, column=2, sticky="E", padx=15)

#Character Dexterity Stats
pDexterity_Frame = tk.LabelFrame(stats_Frame, text="Dexterity")
pDexterity_Frame.grid(row=3, column=0, columnspan=2, padx=10, pady=2)

pRolld = tk.Button(pDexterity_Frame, text = "Roll")
pRolld.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pDex_input = tk.Text(pDexterity_Frame, height=1, font=("", 64), width=2)
pDex_input.grid(row=0, column=0, rowspan=4, padx=5)

pDex_ST = tk.Checkbutton(pDexterity_Frame, text = "Saving Throw")
pDex_ST.grid(row=0, column=1, sticky="W")
pDex_ST_Num = tk.Text(pDexterity_Frame, width=2, height=1)
pDex_ST_Num.grid(row=0, column=2, sticky="E", padx=9)
pAcrobatics = tk.Checkbutton(pDexterity_Frame, text = "Acrobatics")
pAcrobatics.grid(row=1, column=1, sticky="W")
pAcrobatics_Num = tk.Text(pDexterity_Frame, width=2, heigh=1)
pAcrobatics_Num.grid(row=1, column=2, sticky="E", padx=9)
pSlight_of_Hand = tk.Checkbutton(pDexterity_Frame, text = "Sleight of Hand")
pSlight_of_Hand.grid(row=2, column=1, sticky="W")
pSlight_of_Hand_Num = tk.Text(pDexterity_Frame, width=2, height=1)
pSlight_of_Hand_Num.grid(row=2, column=2, sticky="E", padx=9)
pStealth = tk.Checkbutton(pDexterity_Frame, text = "Stealth")
pStealth.grid(row=3, column=1, sticky="W")
pStealth_Num = tk.Text(pDexterity_Frame, width=2, height=1)
pStealth_Num.grid(row=3, column=2, sticky="E", padx=9)

#Players Constitution Stats
pConstitution_Frame = tk.LabelFrame(stats_Frame, text="Constitution")
pConstitution_Frame.grid(row=4, column=0, columnspan=2, padx=10, pady=2)

pRollcon = tk.Button(pConstitution_Frame, text = "Roll")
pRollcon.grid(row=1, column=0, pady=(5), padx=5, sticky="news")

pCon_input = tk.Text(pConstitution_Frame, height=1, font=("", 64), width=2)
pCon_input.grid(row=0, column=0, padx=5)

pCon_ST = tk.Checkbutton(pConstitution_Frame, text = "Saving Throw")
pCon_ST.grid(row=0, column=1, sticky="W")
pCon_ST_Num = tk.Text(pConstitution_Frame, width=2, height=1)
pCon_ST_Num.grid(row=0, column=2, sticky="E", padx=15)

#Players Intelligence Stats
pIntelligence_Frame = tk.LabelFrame(stats_Frame, text="Intelligence")
pIntelligence_Frame.grid(row=5, column=0, columnspan=2, padx=10, pady=2)

pRolli = tk.Button(pIntelligence_Frame, text = "Roll")
pRolli.grid(row=4, column=0, pady=5, padx=5, sticky="news")

pInt_input = tk.Text(pIntelligence_Frame, height=1, font=("", 64), width=2)
pInt_input.grid(row=0, column=0, rowspan=4, padx=5)

pInt_ST = tk.Checkbutton(pIntelligence_Frame, text = "Saving Throw")
pInt_ST.grid(row=0, column=1, sticky="W")
pInt_ST_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pInt_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pArcana = tk.Checkbutton(pIntelligence_Frame, text = "Arcana")
pArcana.grid(row=1, column=1, sticky="W")
pArcana_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pArcana_Num.grid(row=1, column=2, sticky="E", padx=15)
pHistory = tk.Checkbutton(pIntelligence_Frame, text = "History")
pHistory.grid(row=2, column=1, sticky="W")
pHistory_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pHistory_Num.grid(row=2, column=2, sticky="E", padx=15)
pInvestigation = tk.Checkbutton(pIntelligence_Frame, text = "Investigation")
pInvestigation.grid(row=3, column=1, sticky="W")
pInvestigation_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pInvestigation_Num.grid(row=3, column=2, sticky="E", padx=15)
pNature = tk.Checkbutton(pIntelligence_Frame, text = "Nature")
pNature.grid(row=4, column=1, sticky="W")
pNature_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pNature_Num.grid(row=4, column=2, sticky="E", padx=15)
pReligion = tk.Checkbutton(pIntelligence_Frame, text = "Religion")
pReligion.grid(row=5, column=1, sticky="W")
pReligion_Num = tk.Text(pIntelligence_Frame, width=2, height=1)
pReligion_Num.grid(row=5, column=2, sticky="E", padx=15)

#Characters Wisdom Stats
pWisdom_Frame = tk.LabelFrame(stats_Frame, text="Wisdom")
pWisdom_Frame.grid(row=6, column=0, columnspan=2, padx=10, pady=2)

pRollw = tk.Button(pWisdom_Frame, text = "Roll")
pRollw.grid(row=4, column=0, padx=5, pady=5, sticky="news")

pWis_input = tk.Text(pWisdom_Frame, height=1, font=("", 64), width=2)
pWis_input.grid(row=0, column=0, rowspan=4, padx=5)

pWis_ST = tk.Checkbutton(pWisdom_Frame, text = "Saving Throw")
pWis_ST.grid(row=0, column=1, sticky="W")
pWis_ST_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pWis_ST_Num.grid(row=0, column=2, sticky="W", padx=(0,10))
pAnimal_Handling = tk.Checkbutton(pWisdom_Frame, text = "Animal Handling")
pAnimal_Handling.grid(row=1, column=1, sticky="W")
pAnimal_Handling_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pAnimal_Handling_Num.grid(row=1, column=2, sticky="W")
pInsight = tk.Checkbutton(pWisdom_Frame, text = "Insight")
pInsight.grid(row=2, column=1, sticky="W")
pInsight_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pInsight_Num.grid(row=2, column=2, sticky="W")
pMedicine = tk.Checkbutton(pWisdom_Frame, text = "Medicine")
pMedicine.grid(row=3, column=1, sticky="W")
pMedicine_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pMedicine_Num.grid(row=3, column=2, sticky="W")
pPerception = tk.Checkbutton(pWisdom_Frame, text = "Perception")
pPerception.grid(row=4, column=1, sticky="W")
pPerception_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pPerception_Num.grid(row=4, column=2, sticky="W")
pSurvival = tk.Checkbutton(pWisdom_Frame, text = "Survival")
pSurvival.grid(row=5, column=1, sticky="W")
pSurvival_Num = tk.Text(pWisdom_Frame, width=2, height=1)
pSurvival_Num.grid(row=5, column=2, sticky="W")


#Characters Charisma Stats
pCharisma_Frame = tk.LabelFrame(stats_Frame, text="Charisma")
pCharisma_Frame.grid(row=7, column=0, columnspan=2, padx=10, pady=2)

pRollc = tk.Button(pCharisma_Frame, text = "Roll")
pRollc.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pChr_input = tk.Text(pCharisma_Frame, height=1, font=("", 64), width=2)
pChr_input.grid(row=0, column=0, rowspan=4, padx=5)

pWis_ST = tk.Checkbutton(pCharisma_Frame, text = "Saving Throw")
pWis_ST.grid(row=0, column=1, sticky="W")
pWis_ST_Num = tk.Text(pCharisma_Frame, width=2, height=1)
pWis_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pDeception = tk.Checkbutton(pCharisma_Frame, text = "Deception")
pDeception.grid(row=1, column=1, sticky="W")
pDeception_Num = tk.Text(pCharisma_Frame, width=2, height=1)
pDeception_Num.grid(row=1, column=2, sticky="E", padx=15)
pIntimidation = tk.Checkbutton(pCharisma_Frame, text = "Intimidation")
pIntimidation.grid(row=2, column=1, sticky="W")
pIntimidation_Num = tk.Text(pCharisma_Frame, width=2, height=1)
pIntimidation_Num.grid(row=2, column=2, sticky="E", padx=15)
pPerformance = tk.Checkbutton(pCharisma_Frame, text = "Performance")
pPerformance.grid(row=3, column=1, sticky="W")
pPerformance_Num = tk.Text(pCharisma_Frame, width=2, height=1)
pPerformance_Num.grid(row=3, column=2, sticky="E", padx=15)
pPersuasion = tk.Checkbutton(pCharisma_Frame, text = "Persuasion")
pPersuasion.grid(row=4, column=1, sticky="W")
pPersuasion_Num = tk.Text(pCharisma_Frame, width=2, height=1)
pPersuasion_Num.grid(row=4, column=2, sticky="E", padx=15)

pPassiveWisdom = tk.Label(stats_Frame, text="Passive Wisdom/Perception")
pPassiveWisdom.grid(row=8, column=0, padx=5, pady=5)
pPassiveWisdom_Num = tk.Text(stats_Frame, width=2, height=1)
pPassiveWisdom_Num.grid(row=8, column=1, padx=5, pady=15, sticky="W")

########################################################################################################################

#Save Button
save_Button = tk.Button(stats_Frame, text= "Save", height=4, command=lambda:savePlayerSheet())
save_Button.grid(row=9, column=0, rowspan=4, columnspan=2, padx=5, pady=5, sticky="swe")

########################################################################################################################

#Character AC Initiative and speed
ac_i_s_Frame = tk.Frame(dndPlayerSheet)
ac_i_s_Frame.grid(row=1, column=1, padx=5, pady=(5,0), columnspan=2, sticky="news")

pAC = tk.Label(ac_i_s_Frame, text="Armor Class")
pAC.grid(row=0, column=0, padx=5, pady=5)
pAC_input = tk.Text(ac_i_s_Frame, height=1, font=("", 40), width=2)
pAC_input.grid(row=1, column=0, padx=5, pady=5)
ACequalSign = tk.Label(ac_i_s_Frame, text=" = ")
ACequalSign.grid(row=1, column=1)
ACdexModifier = tk.Label(ac_i_s_Frame, text="Dexterity Modifier")
ACdexModifier.grid(row=0, column=2)
ACdexModifier_input = tk.Text(ac_i_s_Frame, height=1, width=2)
ACdexModifier_input.grid(row=1, column=2)
ACplus1 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus1.grid(row=1, column=3)
ACarmor = tk.Label(ac_i_s_Frame, text="Armor")
ACarmor.grid(row=0, column=4)
ACarmor_input = tk.Text(ac_i_s_Frame, height=1, width=2)
ACarmor_input.grid(row=1, column=4)
ACplus2 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus2.grid(row=1, column=5)
ACshield = tk.Label(ac_i_s_Frame, text="Shield")
ACshield.grid(row=0, column=6)
ACshield_input = tk.Text(ac_i_s_Frame, height=1, width=2)
ACshield_input.grid(row=1, column=6)
ACplus3 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus3.grid(row=1, column=7)
ACshield = tk.Label(ac_i_s_Frame, text="Shield")
ACshield.grid(row=0, column=6)
ACshield_input = tk.Text(ac_i_s_Frame, height=1, width=2)
ACshield_input.grid(row=1, column=6)
ACplus3 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus3.grid(row=1, column=7)
ACMisc = tk.Label(ac_i_s_Frame, text="Misc.")
ACMisc.grid(row=0, column=8)
ACMisc_input = tk.Text(ac_i_s_Frame, height=1, width=2)
ACMisc_input.grid(row=1, column=8)

pInitiative = tk.Label(ac_i_s_Frame, text="Initiatve")
pInitiative.grid(row=0, column=9, padx=(160, 0))
pInitiative_input = tk.Text(ac_i_s_Frame, height=1, font=("", 40), width=2)
pInitiative_input.grid(row=1, column=9, padx=(160, 0))

pSpeed = tk.Label(ac_i_s_Frame, text="Speed")
pSpeed.grid(row=0, column=10, padx=20)
pSpeed_input = tk.Text(ac_i_s_Frame, height=1, font=("", 40), width=2)
pSpeed_input.grid(row=1, column=10, padx=20)

########################################################################################################################


#Hit points and death saves
health_Frame = tk.Frame(dndPlayerSheet)
health_Frame.grid(row=2, column=1, padx=5, pady=(5,0), sticky="news")

#hitpoints frame
hitPoint_Frame = tk.Frame(health_Frame)
hitPoint_Frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

hpm_label = tk.Label(hitPoint_Frame, text="Hit Points Maximum")
hpm_label.grid(row=0, column=0, sticky="E")
hpm_label_input = tk.Text(hitPoint_Frame, height=1, width=4)
hpm_label_input.grid(row=0, column=1, sticky="W")
chp_input = tk.Text(hitPoint_Frame, height=1, width=4, font=("", 64))
chp_input.grid(row=1, column=0, columnspan=2, padx=86)
chp_label = tk.Label(hitPoint_Frame, text="Current Hit Points")
chp_label.grid(row=2, column=0, columnspan=2)

#Hit dice frame
hd_Frame = tk.Frame(health_Frame)
hd_Frame.grid(row=1, column=0, padx=5, pady=5)

total_Label = tk.Label(hd_Frame, text="Total")
total_Label.grid(row=0, column=0)
total_input = tk.Text(hd_Frame, height=1, width=4)
total_input.grid(row=0, column=1)
hd_input = tk.Text(hd_Frame, height=1, width=3, font=("", 40))
hd_input.grid(row=1, column=0, columnspan=2)
hd_Label = tk.Label(hd_Frame, text="Hit Dice")
hd_Label.grid(row=2, column=0, columnspan=2)

#Death saves frame
ds_Frame = tk.Frame(health_Frame)
ds_Frame.grid(row=1, column=1, padx=5, pady=(0,5))

success_Label = tk.Label(ds_Frame, text="Successes")
success_Label.grid(row=0, column=0)
success_1 = tk.Checkbutton(ds_Frame)
success_1.grid(row=0, column=1, padx=5)
success_2 = tk.Checkbutton(ds_Frame)
success_2.grid(row=0, column=2, padx=5)
success_3 = tk.Checkbutton(ds_Frame)
success_3.grid(row=0, column=3, padx=5)

failure_Label = tk.Label(ds_Frame, text="Failures")
failure_Label.grid(row=1, column=0)
failure_1 = tk.Checkbutton(ds_Frame)
failure_1.grid(row=1, column=1, padx=5)
failure_2 = tk.Checkbutton(ds_Frame)
failure_2.grid(row=1, column=2, padx=5)
failure_3 = tk.Checkbutton(ds_Frame)
failure_3.grid(row=1, column=3, padx=5)

death_save_Label = tk.Label(ds_Frame, text="Death Saves")
death_save_Label.grid(row=2, column=0, columnspan=4, pady=5)

########################################################################################################################

#Weapon / Spell Frame
weapon_Frame = tk.Frame(dndPlayerSheet)
weapon_Frame.grid(row=3, column=1, padx=5, pady=5, sticky="news")

playerWeapon1 = tk.LabelFrame(weapon_Frame, text="Weapon 1")
playerWeapon1.grid(row=0, column=0, padx=5, pady=5)

pWeapon1 = tk.LabelFrame(playerWeapon1, text="Weapon/Spell")
pWeapon1.grid(row=0, column=0, padx=(5,0))
pWeapon1_Num = tk.Text(pWeapon1, width=20, height=1)
pWeapon1_Num.pack(padx=5, pady=5)
pWeapon1Range = tk.LabelFrame(playerWeapon1, text="Range")
pWeapon1Range.grid(row=0, column=1, columnspan=2, padx=5)
pWeapon1Range_Num = tk.Text(pWeapon1Range, width=20, height=1)
pWeapon1Range_Num.pack(padx=5, pady=5)
pWeapon1Type = tk.LabelFrame(playerWeapon1, text="Type")
pWeapon1Type.grid(row=1, column=0, padx=(5,0), pady=5)
pWeapon1Type_Num = tk.Text(pWeapon1Type, width=20, height=1)
pWeapon1Type_Num.pack(padx=5, pady=5)
pWeapon1AB = tk.LabelFrame(playerWeapon1, text="Attack Bonus")
pWeapon1AB.grid(row=1, column=1)
pWeapon1AB_Num = tk.Text(pWeapon1AB, width=10, height=1)
pWeapon1AB_Num.pack(padx=5, pady=5)
pWeapon1Damage = tk.LabelFrame(playerWeapon1, text="Damage")
pWeapon1Damage.grid(row=1, column=2)
pWeapon1Damage_Num = tk.Text(pWeapon1Damage, width=7, height=1)
pWeapon1Damage_Num.pack(padx=5, pady=5)

pWeapon1AttackButton = tk.Button(playerWeapon1, text="Attack")
pWeapon1AttackButton.grid(row=2, column=0, columnspan=5, padx=5, pady=(0,5), sticky="news")


playerWeapon2 = tk.LabelFrame(weapon_Frame, text="Weapon 2")
playerWeapon2.grid(row=1, column=0, padx=5, pady=5)

pWeapon2 = tk.LabelFrame(playerWeapon2, text="Weapon/Spell")
pWeapon2.grid(row=2, column=0, padx=(5,0))
pWeapon2_Num = tk.Text(pWeapon2, width=20, height=1)
pWeapon2_Num.pack(padx=5, pady=5)
pWeapon2Range = tk.LabelFrame(playerWeapon2, text="Range")
pWeapon2Range.grid(row=2, column=1, columnspan=2, padx=5)
pWeapon2Range_Num = tk.Text(pWeapon2Range, width=20, height=1)
pWeapon2Range_Num.pack(padx=5, pady=5)
pWeapon2Type = tk.LabelFrame(playerWeapon2, text="Type")
pWeapon2Type.grid(row=3, column=0, padx=(5,0), pady=5)
pWeapon2Type_Num = tk.Text(pWeapon2Type, width=20, height=1)
pWeapon2Type_Num.pack(padx=5, pady=5)
pWeapon2AB = tk.LabelFrame(playerWeapon2, text="Attack Bonus")
pWeapon2AB.grid(row=3, column=1)
pWeapon2AB_Num = tk.Text(pWeapon2AB, width=10, height=1)
pWeapon2AB_Num.pack(padx=5, pady=5)
pWeapon2Damage = tk.LabelFrame(playerWeapon2, text="Damage")
pWeapon2Damage.grid(row=3, column=2)
pWeapon2Damage_Num = tk.Text(pWeapon2Damage, width=7, height=1)
pWeapon2Damage_Num.pack(padx=5, pady=5)

pWeapon2AttackButton = tk.Button(playerWeapon2, text="Attack")
pWeapon2AttackButton.grid(row=4, column=0, columnspan=5, padx=5, pady=(0,5), sticky="news")


playerWeapon3 = tk.LabelFrame(weapon_Frame, text="Weapon 3")
playerWeapon3.grid(row=2, column=0, padx=5, pady=5)

pWeapon3 = tk.LabelFrame(playerWeapon3, text="Weapon/Spell")
pWeapon3.grid(row=0, column=0, padx=(5,0))
pWeapon3_Num = tk.Text(pWeapon3, width=20, height=1)
pWeapon3_Num.pack(padx=5, pady=5)
pWeapon3Range = tk.LabelFrame(playerWeapon3, text="Range")
pWeapon3Range.grid(row=0, column=1, columnspan=2, padx=5)
pWeapon3Range_Num = tk.Text(pWeapon3Range, width=20, height=1)
pWeapon3Range_Num.pack(padx=5, pady=5)
pWeapon3Type = tk.LabelFrame(playerWeapon3, text="Type")
pWeapon3Type.grid(row=1, column=0, padx=(5,0), pady=5)
pWeapon3Type_Num = tk.Text(pWeapon3Type, width=20, height=1)
pWeapon3Type_Num.pack(padx=5, pady=5)
pWeapon3AB = tk.LabelFrame(playerWeapon3, text="Attack Bonus")
pWeapon3AB.grid(row=1, column=1)
pWeapon3AB_Num = tk.Text(pWeapon3AB, width=10, height=1)
pWeapon3AB_Num.pack(padx=5, pady=5)
pWeapon3Damage = tk.LabelFrame(playerWeapon3, text="Damage")
pWeapon3Damage.grid(row=1, column=2)
pWeapon3Damage_Num = tk.Text(pWeapon3Damage, width=7, height=1)
pWeapon3Damage_Num.pack(padx=5, pady=5)

pWeapon3AttackButton = tk.Button(playerWeapon3, text="Attack")
pWeapon3AttackButton.grid(row=2, column=0, columnspan=5, padx=5, pady=(0,5), sticky="news")

########################################################################################################################

#Equipped/Carried Items
items_Frame = tk.LabelFrame(dndPlayerSheet, text="Items")
items_Frame.grid(row=4, column=1, padx=5, pady=(0,5), sticky="news")

items_text1 = tk.Text(items_Frame, width=22, height=18)
items_text1.grid(row=0, column=0, padx=5, sticky="N")
items_text2 = tk.Text(items_Frame, width=22, height=18)
items_text2.grid(row=0, column=1, padx=5, sticky="N")

########################################################################################################################

#Features and Traits
features_Traits = tk.LabelFrame(dndPlayerSheet, text="Features / Traits")
features_Traits.grid(row=2, column=2, rowspan=2, pady=5, padx=(0,5), sticky="news")
features_Traits_text = tk.Text(features_Traits, width=40, height=47)
features_Traits_text.pack()

#Other proficiencies and languages
opl_Traits = tk.LabelFrame(dndPlayerSheet, text="Other Proficiencies / Languages")
opl_Traits.grid(row=4, column=2, padx=(0,5), pady=(0,5), sticky="news")
opl_Traits_text = tk.Text(opl_Traits, width=40, height=18)
opl_Traits_text.pack()




window.mainloop()
