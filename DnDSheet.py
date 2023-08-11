import tkinter as tk
from tkinter import ttk
import json
import random as ran
from ast import literal_eval



def openInfoFile():
    global cInfo_d
    f = open("info.json")
    cInfo_d = json.load(f)
    try:
        cName_input.insert(tk.END, cInfo_d['Name'])
        cClass_input.insert(tk.END, cInfo_d['Class'])
        cLevel_input.insert(tk.END, cInfo_d['Level'])
        cRace_input.insert(tk.END, cInfo_d['Race'])
        cExperience_input.insert(tk.END, cInfo_d['Experience_Points'])
        pBonus_input.insert(tk.END, cInfo_d['Proficiency_Bonus'])
        pStr_input.insert(tk.END, cInfo_d['Strength'])
        pStr_ST_Num.insert(tk.END, cInfo_d['StrST'])
        pAthletics_Num.insert(tk.END, cInfo_d['Athletics'])
        pDex_input.insert(tk.END, cInfo_d['Dexterity'])
        pDex_ST_Num.insert(tk.END, cInfo_d['Dex_Saving_Throw'])
        pAcrobatics_Num.insert(tk.END, cInfo_d['Acrobatics'])
        pSlight_of_Hand_Num.insert(tk.END, cInfo_d['Slight_of_Hand'])
        pStealth_Num.insert(tk.END, cInfo_d['Stealth'])
        pCon_input.insert(tk.END, cInfo_d['Constitution'])
        pCon_ST_Num.insert(tk.END, cInfo_d['Con_Saving_Throw'])
        pInt_input.insert(tk.END, cInfo_d['Intelligence'])
        pInt_ST_Num.insert(tk.END, cInfo_d['Int_Saving_Throw'])
        pArcana_Num.insert(tk.END, cInfo_d['Arcana'])
        pHistory_Num.insert(tk.END, cInfo_d['History'])
        pInvestigation_Num.insert(tk.END, cInfo_d['Investigation'])
        pNature_Num.insert(tk.END, cInfo_d['Nature'])
        pReligion_Num.insert(tk.END, cInfo_d['Religion'])
        pWis_input.insert(tk.END, cInfo_d['Wisdom'])
        pWis_ST_Num.insert(tk.END, cInfo_d['Wis_Saving_Throw'])
        pAnimal_Handling_Num.insert(tk.END, cInfo_d['Animal_Handling'])
        pInsight_Num.insert(tk.END, cInfo_d['Insight'])
        pMedicine_Num.insert(tk.END, cInfo_d['Medicine'])
        pPerception_Num.insert(tk.END, cInfo_d['Perception'])
        pSurvival_Num.insert(tk.END, cInfo_d['Survival'])
        pChr_input.insert(tk.END, cInfo_d['Charisma'])
        pChr_ST_Num.insert(tk.END, cInfo_d['Chr_Saving_Throw'])
        pDeception_Num.insert(tk.END, cInfo_d['Deception'])
        pIntimidation_Num.insert(tk.END, cInfo_d['Intimidation'])
        pPerformance_Num.insert(tk.END, cInfo_d['Performance'])
        pPersuasion_Num.insert(tk.END, cInfo_d['Persuasion'])
        pPassiveWisdom_Num.insert(tk.END, cInfo_d['PassiveWisdom'])
        pAC_input.insert(tk.END, cInfo_d['ArmorClass'])
        ACdexModifier_input.insert(tk.END, cInfo_d['AC_Dexterity_Modifier'])
        ACarmor_input.insert(tk.END, cInfo_d['AC_Armor'])
        ACshield_input.insert(tk.END, cInfo_d['AC_Shield'])
        ACMisc_input.insert(tk.END, cInfo_d['AC_Misc'])
        pInitiative_input.insert(tk.END, cInfo_d['Initiative'])
        pSpeed_input.insert(tk.END, cInfo_d['Speed'])
        hpm_label_input.insert(tk.END, cInfo_d['Health_Maximum'])
        chp_input.insert(tk.END, cInfo_d['Current_Health'])
        totalHD_input.insert(tk.END, cInfo_d['Total_Hit_Dice'])
        hd_input.insert(tk.END, cInfo_d['Hit_Dice'])
        pWeapon1_Num.insert(tk.END, cInfo_d['Weapon1'])
        pWeapon1Range_Num.insert(tk.END, cInfo_d['Weapon1Range'])
        pWeapon1Type_Num.insert(tk.END, cInfo_d['Weapon1Type'])
        pWeapon1AB_Num.insert(tk.END, cInfo_d['Weapon1AttackBonus'])
        pWeapon1Damage_Num.insert(tk.END, cInfo_d['Weapon1Damage'])
        pWeapon2_Num.insert(tk.END, cInfo_d['Weapon2'])
        pWeapon2Range_Num.insert(tk.END, cInfo_d['Weapon2Range'])
        pWeapon2Type_Num.insert(tk.END, cInfo_d['Weapon2Type'])
        pWeapon2AB_Num.insert(tk.END, cInfo_d['Weapon2AttackBonus'])
        pWeapon2Damage_Num.insert(tk.END, cInfo_d['Weapon2Damage'])
        pWeapon3_Num.insert(tk.END, cInfo_d['Weapon3'])
        pWeapon3Range_Num.insert(tk.END, cInfo_d['Weapon3Range'])
        pWeapon3Type_Num.insert(tk.END, cInfo_d['Weapon3Type'])
        pWeapon3AB_Num.insert(tk.END, cInfo_d['Weapon3AttackBonus'])
        pWeapon3Damage_Num.insert(tk.END, cInfo_d['Weapon3Damage'])
        items_text1.insert(tk.END, cInfo_d['Items_Text_Box'])
        items_text2.insert(tk.END, cInfo_d['Items_Text_Box2'])
        features_Traits_text.insert(tk.END, cInfo_d['Featires_Traits_Box'])
        opl_Traits_text.insert(tk.END, cInfo_d['OtherProficienciesLanguages_Box'])
        if(cInfo_d['StrengthProficiencyButton']==1):
            pStr_ST.select()
        if(cInfo_d['AthleticsProficiencyButton']==1):
            pAthletics.select()
        if(cInfo_d['DexterityProcifiencyButton']==1):
            pDex_ST.select()
        if(cInfo_d['AcrobaticsProficiencyButton']==1):
            pAcrobatics.select()
        if(cInfo_d['SoHProficiencyButton']==1):
            pSlight_of_Hand.select()
        if(cInfo_d['StealthProficiencyButton']==1):
            pStealth.select()
        if(cInfo_d['ConstitutionProficiencyButton']==1):
            pCon_ST.select()
        if(cInfo_d['IntelligenceProficiencyButton']==1):
            pInt_ST.select()
        if(cInfo_d['ArcanaProficiencyButton']==1):
            pArcana.select()
        if(cInfo_d['HistoryProficiencyButton']==1):
            pHistory.select()
        if(cInfo_d['InvestigationProficiencyButton']==1):
            pInvestigation.select()
        if(cInfo_d['NatureProficiencyButton']==1):
            pNature.select()
        if(cInfo_d['ReligionProficiencyButton']==1):
            pReligion.select()
        if(cInfo_d['WisdomProficiencyButton']==1):
            pWis_ST.select()
        if(cInfo_d['AnimalHandlingProficiencyButton']==1):
            pAnimal_Handling.select()
        if(cInfo_d['InsightProficiencyButton']==1):
            pInsight.select()
        if(cInfo_d['MedicineProficiencyButton']==1):
            pMedicine.select()
        if(cInfo_d['PerceptionProficiencyButton']==1):
            pPerception.select()
        if(cInfo_d['SurvivalProficiencyButton']==1):
            pSurvival.select()
        if(cInfo_d['CharismaProficiencyButton']==1):
            pChr_ST.select()
        if(cInfo_d['DeceptionProficiencyButton']==1):
            pDeception.select()
        if(cInfo_d['IntimidationProficiencyButton']==1):
            pIntimidation.select()
        if(cInfo_d['PerformanceProficiencyButton']==1):
            pPerformance.select()
        if(cInfo_d['PersuasionProficiencyButton']==1):
            pPersuasion.select()
        if(cInfo_d['DeathSave1']==1):
            success_1.select()
        if(cInfo_d['DeathSave2']==1):
            success_2.select()
        if(cInfo_d['DeathSave3']==1):
            success_3.select()
        if(cInfo_d['DeathFail1']==1):
            failure_1.select()
        if(cInfo_d['DeathFail2']==1):
            failure_2.select()
        if(cInfo_d['DeathFail3']==1):
            failure_3.select()
        spellcasting_ability.insert(tk.END, cInfo_d['SpellcastingAbility'])
        spell_save_dc.insert(tk.END, cInfo_d['SpellSaveDC'])
        spell_attack_bonus.insert(tk.END, cInfo_d['SpellAttackBonus'])
        first_slots = cInfo_d['FirstLevelSpellSlotsCount']
        second_slots = cInfo_d['SecondLevelSpellSlotsCount']
        third_slots = cInfo_d['ThirdLevelSpellSlotsCount']
        fourth_slots = cInfo_d['FourthLevelSpellSlotsCount']
        fifth_slots = cInfo_d['FifthLevelSpellSlotsCount']
        sixth_slots = cInfo_d['SixthLevelSpellSlotsCount']
        seventh_slots = cInfo_d['SeventhLevelSpellSlotsCount']
        eigth_slots = cInfo_d['EigthLevelSpellSlotsCount']
        ninth_slots = cInfo_d['NinthLevelSpellSlotsCount']

        for _ in range(first_slots):
            add_slots_1()
        for _ in range(second_slots):
            add_slots_2()
        for _ in range(third_slots):
            add_slots_3()
        for _ in range(fourth_slots):
            add_slots_4()
        for _ in range(fifth_slots):
            add_slots_5()
        for _ in range(sixth_slots):
            add_slots_6()
        for _ in range(seventh_slots):
            add_slots_7()
        for _ in range(eigth_slots):
            add_slots_8()
        for _ in range(ninth_slots):
            add_slots_9()


    except json.JSONDecodeError:
        savePlayerSheet()
    
    except KeyError:
        savePlayerSheet()


def savePlayerSheet():

    cInfo_d.update(Name=str(cName_input.get()),
                   Class=str(cClass_input.get()),
                   Level=str(cLevel_input.get()),
                   Race=str(cRace_input.get()),
                   Experience_Points=str(cExperience_input.get()),
                   Proficiency_Bonus=str(pBonus_input.get()),
                   Strength=str(pStr_input.get()),
                   StrST=str(pStr_ST_Num.get()),
                   Athletics=str(pAthletics_Num.get()),
                   Dexterity=str(pDex_input.get()),
                   Dex_Saving_Throw=str(pDex_ST_Num.get()),
                   Acrobatics=str(pAcrobatics_Num.get()),
                   Slight_of_Hand=str(pSlight_of_Hand_Num.get()),
                   Stealth=str(pStealth_Num.get()),
                   Constitution=str(pCon_input.get()),
                   Con_Saving_Throw=str(pCon_ST_Num.get()),
                   Intelligence=str(pInt_input.get()),
                   Int_Saving_Throw=str(pInt_ST_Num.get()),
                   Arcana=str(pArcana_Num.get()),
                   History=str(pHistory_Num.get()),
                   Investigation=str(pInvestigation_Num.get()),
                   Nature=str(pNature_Num.get()),
                   Religion=str(pReligion_Num.get()),
                   Wisdom=str(pWis_input.get()),
                   Wis_Saving_Throw=str(pWis_ST_Num.get()),
                   Animal_Handling=str(pAnimal_Handling_Num.get()),
                   Insight=str(pInsight_Num.get()),
                   Medicine=str(pMedicine_Num.get()),
                   Perception=str(pPerception_Num.get()),
                   Survival=str(pSurvival_Num.get()),
                   Charisma=str(pChr_input.get()),
                   Chr_Saving_Throw=str(pChr_ST_Num.get()),
                   Deception=str(pDeception_Num.get()),
                   Intimidation=str(pIntimidation_Num.get()),
                   Performance=str(pPerformance_Num.get()),
                   Persuasion=str(pPersuasion_Num.get()),
                   PassiveWisdom=str(pPassiveWisdom_Num.get()),
                   ArmorClass=str(pAC_input.get()),
                   AC_Dexterity_Modifier=str(ACdexModifier_input.get()),
                   AC_Armor=str(ACarmor_input.get()),
                   AC_Shield=str(ACshield_input.get()),
                   AC_Misc=str(ACMisc_input.get()),
                   Initiative=str(pInitiative_input.get()),
                   Speed=str(pSpeed_input.get()),
                   Health_Maximum=str(hpm_label_input.get()),
                   Current_Health=str(chp_input.get()),
                   Total_Hit_Dice=str(totalHD_input.get()),
                   Hit_Dice=str(hd_input.get()),
                   Weapon1=str(pWeapon1_Num.get()),
                   Weapon1Range=str(pWeapon1Range_Num.get()),
                   Weapon1Type=str(pWeapon1Type_Num.get()),
                   Weapon1AttackBonus=str(pWeapon1AB_Num.get()),
                   Weapon1Damage=str(pWeapon1Damage_Num.get()),
                   Weapon2=str(pWeapon2_Num.get()),
                   Weapon2Range=str(pWeapon2Range_Num.get()),
                   Weapon2Type=str(pWeapon2Type_Num.get()),
                   Weapon2AttackBonus=str(pWeapon2AB_Num.get()),
                   Weapon2Damage=str(pWeapon2Damage_Num.get()),
                   Weapon3=str(pWeapon3_Num.get()),
                   Weapon3Range=str(pWeapon3Range_Num.get()),
                   Weapon3Type=str(pWeapon3Type_Num.get()),
                   Weapon3AttackBonus=str(pWeapon3AB_Num.get()),
                   Weapon3Damage=str(pWeapon3Damage_Num.get()),
                   Items_Text_Box=str(items_text1.get(1.0, "end-1c")),
                   Items_Text_Box2=str(items_text2.get(1.0, "end-1c")),
                   Featires_Traits_Box=str(features_Traits_text.get(1.0, "end-1c")),
                   OtherProficienciesLanguages_Box=str(opl_Traits_text.get(1.0, "end-1c")),
                   StrengthProficiencyButton=strSavingThrowCB.get(),
                   AthleticsProficiencyButton=AthleticsCB.get(),
                   DexterityProcifiencyButton=dexSavingThrowCB.get(),
                   AcrobaticsProficiencyButton=AcrobaticsCB.get(),
                   SoHProficiencyButton=SlightofHandCB.get(),
                   StealthProficiencyButton=StealthCB.get(),
                   ConstitutionProficiencyButton=ConSavingThrowCB.get(),
                   IntelligenceProficiencyButton=IntSavingThrowCB.get(),
                   ArcanaProficiencyButton=ArcanaCB.get(),
                   HistoryProficiencyButton=HistoryCB.get(),
                   InvestigationProficiencyButton=InvestigationCB.get(),
                   NatureProficiencyButton=NatureCB.get(),
                   ReligionProficiencyButton=ReligionCB.get(),
                   WisdomProficiencyButton=WisSavingThrowCB.get(),
                   AnimalHandlingProficiencyButton=AnimalHandlingCB.get(),
                   InsightProficiencyButton=InsightCB.get(),
                   MedicineProficiencyButton=MedicineCB.get(),
                   PerceptionProficiencyButton=PerceptionCB.get(),
                   SurvivalProficiencyButton=SurvivalCB.get(),
                   CharismaProficiencyButton=ChrSavingThrowCB.get(),
                   DeceptionProficiencyButton=DeceptionCB.get(),
                   IntimidationProficiencyButton=IntimidationCB.get(),
                   PerformanceProficiencyButton=PerformanceCB.get(),
                   PersuasionProficiencyButton=PersuasionCB.get(),
                   DeathSave1=dSave1.get(),
                   DeathSave2=dSave2.get(),
                   DeathSave3=dSave3.get(),
                   DeathFail1=dFail1.get(),
                   DeathFail2=dFail2.get(),
                   DeathFail3=dFail3.get(),
                   SpellcastingAbility=spellcasting_ability.get(),
                   SpellSaveDC=spell_save_dc.get(),
                   SpellAttackBonus=spell_attack_bonus.get(),
                   FirstLevelSpellSlotsCount=first_slots,
                   SecondLevelSpellSlotsCount=second_slots,
                   ThirdLevelSpellSlotsCount=third_slots,
                   FourthLevelSpellSlotsCount=fourth_slots,
                   FifthLevelSpellSlotsCount=fifth_slots,
                   SixthLevelSpellSlotsCount=sixth_slots,
                   SeventhLevelSpellSlotsCount=seventh_slots,
                   EigthLevelSpellSlotsCount=eigth_slots,
                   NinthLevelSpellSlotsCount=ninth_slots,
    )   
    
    json.dump(cInfo_d, open('info.json', 'w'), indent=2)


def add_proficiency_bonus(checkbox:tk.IntVar, entry:tk.Entry):
    if(checkbox.get()==1):
        isProficient = (int(entry.get()) + int(pBonus_input.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(entry.get()) - int(pBonus_input.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, isNotProficient)


def strProfButton():
    add_proficiency_bonus(strSavingThrowCB, pStr_ST_Num)

def athleticsProfButton():
    add_proficiency_bonus(AthleticsCB, pAthletics_Num)

def dexProfButton():
    add_proficiency_bonus(dexSavingThrowCB, pDex_ST_Num)

def acrobaticsProfButton():
    add_proficiency_bonus(AcrobaticsCB, pAcrobatics_Num)

def slightofHandProfButton():  
    add_proficiency_bonus(SlightofHandCB, pSlight_of_Hand_Num)

def stealthProfButton():
    add_proficiency_bonus(StealthCB, pStealth_Num)

def conProfButton():
    add_proficiency_bonus(ConSavingThrowCB, pCon_ST_Num)

def intProfButton():
    add_proficiency_bonus(IntSavingThrowCB, pInt_ST_Num)

def arcanaProfButton():
    add_proficiency_bonus(ArcanaCB, pArcana)

def historyProfButton():
    add_proficiency_bonus(HistoryCB, pHistory_Num)

def investigationProfButton():
    add_proficiency_bonus(InvestigationCB, pInvestigation_Num)

def natureProfButton():
    add_proficiency_bonus(NatureCB, pNature_Num)

def religionProfButton():
    add_proficiency_bonus(ReligionCB, pReligion_Num)

def wisProfButton():
    add_proficiency_bonus(WisSavingThrowCB, pWis_ST_Num)

def ahProfButton():
    add_proficiency_bonus(AnimalHandlingCB, pAnimal_Handling_Num)

def insightProfButton():
    add_proficiency_bonus(InsightCB, pInsight_Num)

def medicineProfButton():
    add_proficiency_bonus(MedicineCB, pMedicine_Num)

def perceptionProfButton():
    add_proficiency_bonus(PerceptionCB, pPerception_Num)

def survivalProfButton():
    add_proficiency_bonus(SurvivalCB, pSurvival_Num)

def chrProfButton():
    add_proficiency_bonus(ChrSavingThrowCB, pChr_ST_Num)

def deceptionProfButton():
    add_proficiency_bonus(DeceptionCB, pDeception_Num)

def intimidationProfButton():
    add_proficiency_bonus(IntimidationCB, pIntimidation_Num)

def performanceProfButton():
    add_proficiency_bonus(PerformanceCB, pPerformance_Num)

def persuasionProfButton():
    add_proficiency_bonus(PersuasionCB, pPersuasion_Num)

        
def acFormula():
    pAC_input.delete(0, tk.END)
    newAC_Number = (int(ACdexModifier_input.get())+(int(ACarmor_input.get())+(int(ACshield_input.get()))+(int(ACMisc_input.get()))))
    pAC_input.insert(tk.END, newAC_Number)

def addHealth():
    newCurrentHealth = int(chp_input.get())
    newCurrentHealth += 1
    chp_input.delete(0, tk.END)
    chp_input.insert(tk.END, newCurrentHealth)

def subHealth():
    newCurrentHealth = int(chp_input.get())
    newCurrentHealth -= 1
    chp_input.delete(0, tk.END)
    chp_input.insert(tk.END, newCurrentHealth)


def twentyone_check(roll_output, roll_output_wa):
        if(roll_output == 20):
            nat20_window = tk.Toplevel()
            nat20_text = tk.Label(nat20_window, text="You Rolled a Natural 20!", font=("", 100))
            nat20_text.pack()
        elif(roll_output == 1):
            nat1_window = tk.Toplevel()
            nat1_text = tk.Label(nat1_window, text="You Rolled a Natural 1!", font=("", 100))
            nat1_text.pack()
        if(roll_output_wa == 20):
            nat20_window = tk.Toplevel()
            nat20_text = tk.Label(nat20_window, text="You Rolled a Natural 20!", font=("", 100))
            nat20_text.pack()
        elif(roll_output_wa == 1):
            nat1_window = tk.Toplevel()
            nat1_text = tk.Label(nat1_window, text="You Rolled a Natural 1!", font=("", 100))
            nat1_text.pack()    

def twentyone_check_init(roll_output):
    if(roll_output == 20):
        nat20_window = tk.Toplevel()
        nat20_text = tk.Label(nat20_window, text="You Rolled a Natural 20!", font=("", 100))
        nat20_text.pack()
    elif(roll_output == 1):
        nat1_window = tk.Toplevel()
        nat1_text = tk.Label(nat1_window, text="You Rolled a Natural 1!", font=("", 100))
        nat1_text.pack()

def strRoll_window():

    def sst_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pStr_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pStr_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pStr_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def athletics_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pAthletics_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pAthletics_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pAthletics_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)


    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Strength Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=4)
    str_saving_throw_button = tk.Button(roll_frame,command=sst_roll_calculations , text="Strength Saving Throw", font=("", 16), padx=10, pady=5)
    str_saving_throw_button.grid(row=2, column=0, sticky="ew")
    athletics_button = tk.Button(roll_frame, command=athletics_roll_calculations, text="Athletics", font=("", 16), padx=10, pady=5)
    athletics_button.grid(row=3, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)

def dexRoll_window():

    def dst_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pDex_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pDex_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:        
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pDex_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def acrobatics_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pAcrobatics_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pAcrobatics_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:      
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pAcrobatics_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def SoH_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pSlight_of_Hand_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pSlight_of_Hand_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:      
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pSlight_of_Hand_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def stealth_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pStealth_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pStealth_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:   
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pStealth_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)        

    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Dexterity Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=4)
    dex_saving_throw_button = tk.Button(roll_frame,command=dst_roll_calculations , text="Dexterity Saving Throw", font=("", 16), padx=10, pady=5)
    dex_saving_throw_button.grid(row=2, column=0, sticky="ew")
    acrobatics_button = tk.Button(roll_frame, command=acrobatics_roll_calculations, text="Acrobatics", font=("", 16), padx=10, pady=5)
    acrobatics_button.grid(row=3, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    SoH_button = tk.Button(roll_frame, command=SoH_roll_calculations, text="Slight of Hand", font=("", 16), padx=10, pady=5)
    SoH_button.grid(row=4, column=0, sticky="ew")
    stealth_button = tk.Button(roll_frame, command=stealth_roll_calculations, text="Stealth", font=("", 16), padx=10, pady=5)
    stealth_button.grid(row=5, column=0, sticky="ew")
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2) 

def conRoll_window():
    
    def cst_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pCon_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pCon_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pCon_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)    


    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Constitution Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=3)
    con_saving_throw_button = tk.Button(roll_frame,command=cst_roll_calculations , text="Constitution Saving Throw", font=("", 16), padx=10, pady=5)
    con_saving_throw_button.grid(row=2, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)

def intRoll_window():
    def ist_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pInt_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pInt_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pInt_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def arcana_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pArcana_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pArcana_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pArcana_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def history_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pHistory_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pHistory_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pHistory_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def investigation_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pInvestigation_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pInvestigation_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pInvestigation_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     

    def nature_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pNature_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pNature_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pNature_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)  

    def religion_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pReligion_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pReligion_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)
            
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pReligion_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     


    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Intelligence Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=3)
    int_saving_throw_button = tk.Button(roll_frame,command=ist_roll_calculations , text="Intelligence Saving Throw", font=("", 16), padx=10, pady=5)
    int_saving_throw_button.grid(row=2, column=0, sticky="ew")
    arcana_button = tk.Button(roll_frame, command=arcana_roll_calculations, text="Arcana", font=("", 16), padx=10, pady=5)
    arcana_button.grid(row=3, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    history_button = tk.Button(roll_frame, command=history_roll_calculations, text="History", font=("", 16), padx=10, pady=5)
    history_button.grid(row=4, column=0, sticky="ew")
    investigation_button = tk.Button(roll_frame, command=investigation_roll_calculations, text="Investigation", font=("", 16), padx=10, pady=5)
    investigation_button.grid(row=5, column=0, sticky="ew")  
    nature_button = tk.Button(roll_frame, command=nature_roll_calculations, text="Nature", font=("", 16), padx=10, pady=5)
    nature_button.grid(row=6, column=0, sticky="ew")  
    religion_button = tk.Button(roll_frame, command=religion_roll_calculations, text="Religion", font=("", 16), padx=10, pady=5)
    religion_button.grid(row=7, column=0, sticky="ew")  
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)

def wisRoll_window():
    def wis_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pWis_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pWis_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pWis_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def animalhandling_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pAnimal_Handling_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pAnimal_Handling_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pAnimal_Handling_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def insight_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pInsight_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pInsight_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pInsight_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def medicine_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pMedicine_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pMedicine_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pMedicine_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     

    def perception_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pPerception_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pPerception_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pPerception_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)  

    def survival_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pSurvival_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pSurvival_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pSurvival_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     

    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Wisdom Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=3)
    wis_saving_throw_button = tk.Button(roll_frame,command=wis_roll_calculations , text="Wisdom Saving Throw", font=("", 16), padx=10, pady=5)
    wis_saving_throw_button.grid(row=2, column=0, sticky="ew")
    animalhandling_button = tk.Button(roll_frame, command=animalhandling_roll_calculations, text="Animal Handling", font=("", 16), padx=10, pady=5)
    animalhandling_button.grid(row=3, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    insight_button = tk.Button(roll_frame, command=insight_roll_calculations, text="Insight", font=("", 16), padx=10, pady=5)
    insight_button.grid(row=4, column=0, sticky="ew")
    medicine_button = tk.Button(roll_frame, command=medicine_roll_calculations, text="Medicine", font=("", 16), padx=10, pady=5)
    medicine_button.grid(row=5, column=0, sticky="ew")  
    perception_button = tk.Button(roll_frame, command=perception_roll_calculations, text="Perception", font=("", 16), padx=10, pady=5)
    perception_button.grid(row=6, column=0, sticky="ew")  
    survival_button = tk.Button(roll_frame, command=survival_roll_calculations, text="Survival", font=("", 16), padx=10, pady=5)
    survival_button.grid(row=7, column=0, sticky="ew") 
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)

def chrRoll_window():
    def chr_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pChr_ST_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pChr_ST_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pChr_ST_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def deception_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pDeception_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pDeception_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pDeception_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def intimidation_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pIntimidation_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pIntimidation_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pIntimidation_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)

    def performance_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pPerformance_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pPerformance_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pPerformance_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     

    def persuasion_roll_calculations():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pPersuasion_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pPersuasion_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pPersuasion_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)     

    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Wisdom Roll")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Choose a Attribute to Roll", font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=3)
    chr_saving_throw_button = tk.Button(roll_frame,command=chr_roll_calculations , text="Charisma Saving Throw", font=("", 16), padx=10, pady=5)
    chr_saving_throw_button.grid(row=2, column=0, sticky="ew")
    deception_button = tk.Button(roll_frame, command=deception_roll_calculations, text="Deception", font=("", 16), padx=10, pady=5)
    deception_button.grid(row=3, column=0, sticky="ew")
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    intimidation_button = tk.Button(roll_frame, command=intimidation_roll_calculations, text="Intimidation", font=("", 16), padx=10, pady=5)
    intimidation_button.grid(row=4, column=0, sticky="ew")
    performance_button = tk.Button(roll_frame, command=performance_roll_calculations, text="Performance", font=("", 16), padx=10, pady=5)
    performance_button.grid(row=5, column=0, sticky="ew")  
    persuasion_button = tk.Button(roll_frame, command=persuasion_roll_calculations, text="Persuasion", font=("", 16), padx=10, pady=5)
    persuasion_button.grid(row=6, column=0, sticky="ew")
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)

def attack_1():
    def attack_1_calc():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon1AB_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pWeapon1AB_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon1AB_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)
    
    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Attack")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text=pWeapon1_Num.get(), font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=4)
    roll_to_hit_button = tk.Button(roll_frame,command=attack_1_calc , text="Roll to Hit", font=("", 16), padx=10, pady=5)
    roll_to_hit_button.grid(row=2, column=0, sticky="ew", padx=20)
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)    

def attack_2():
    def attack_2_calc():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon2AB_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pWeapon2AB_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon2AB_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)
    
    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Attack")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text=pWeapon2_Num.get(), font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=4)
    roll_to_hit_button = tk.Button(roll_frame,command=attack_2_calc , text="Roll to Hit", font=("", 16), padx=10, pady=5)
    roll_to_hit_button.grid(row=2, column=0, sticky="ew", padx=20)
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)    

def attack_3():
    def attack_3_calc():
        if(advantageCD.get() == 1):
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_wa = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon3AB_Num.get()) + roll_output)
            roll_output_insert_wa = (int(pWeapon3AB_Num.get()) + roll_output_wa)
            results.insert(tk.END, roll_output_insert), results_wa.insert(tk.END, roll_output_insert_wa)
            twentyone_check(roll_output, roll_output_wa)        
        else:
            results.delete(0, tk.END), results_wa.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pWeapon3AB_Num.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check(roll_output)
    
    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Attack")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text=pWeapon3_Num.get(), font=("", 32), padx=10, pady=30)
    roll_question.grid(row=0, column=0, columnspan=4)
    roll_to_hit_button = tk.Button(roll_frame,command=attack_3_calc , text="Roll to Hit", font=("", 16), padx=10, pady=5)
    roll_to_hit_button.grid(row=2, column=0, sticky="ew", padx=20)
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.grid(row=2, column=2, rowspan=2)
    prof_question = tk.Checkbutton(roll_frame, text="Advantage", variable=advantageCD)
    prof_question.grid(row=1, column=3)
    results_wa = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results_wa.grid(row=2, column=3, rowspan=2)    

def initiative_button():

    def initiative_calc():
            results.delete(0, tk.END)
            roll_output = int(ran.randint(1,20))
            roll_output_insert = (int(pInitiative_input.get()) + roll_output)
            results.insert(tk.END, roll_output_insert)
            twentyone_check_init(roll_output)
    
    advantageCD = tk.IntVar()

    roll_window = tk.Toplevel()
    roll_window.title("Attack")
    
    roll_frame = tk.Frame(roll_window, padx=20, pady=20)
    roll_frame.pack()

    roll_question = tk.Label(roll_frame,text="Initiative Roll", font=("", 32), padx=10, pady=30)
    roll_question.pack()
    results = tk.Entry(roll_frame, font=("", 64), width=2, border=10)
    results.pack()

    initiative_calc()



root = tk.Tk()
root.title("Character Sheet")
root.geometry('1040x1320')
root.resizable(0,3000)

notebook = ttk.Notebook(root)


dndPlayerSheet_tab = tk.Label(notebook, background="grey")
dndSpellSheet_tab = tk.Label(notebook)
dndMonsterSheet_tab = tk.Label(notebook)

notebook.add(dndPlayerSheet_tab, text = "Playercard")
notebook.add(dndSpellSheet_tab, text = "Spell Sheet")
notebook.add(dndMonsterSheet_tab, text = "Monster Data")

notebook.pack(expand=True, fill="both")

########################################################################################################################
#Creation of the scroll bar for the dndPlayerSheet_tab
main_frame = tk.Frame(dndPlayerSheet_tab)
main_frame.pack(fill=tk.BOTH, expand=1)
#Create a canvas
dndPlayerSheet_Canvas = tk.Canvas(main_frame)
dndPlayerSheet_Canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
#Add the scroll bar to the canvas
playersheet_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=dndPlayerSheet_Canvas.yview)
playersheet_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#Configure the canvas so the scrollbar can be used
dndPlayerSheet_Canvas.configure(yscrollcommand=playersheet_scrollbar.set)
#Creates a binding box around the player sheet where an event is passed in "lambda e"
dndPlayerSheet_Canvas.bind('<Configure>', lambda e:dndPlayerSheet_Canvas.configure(scrollregion=dndPlayerSheet_Canvas.bbox('all')))
dndPlayerSheet = tk.Frame(dndPlayerSheet_Canvas)
dndPlayerSheet_Canvas.create_window((0,0), window=dndPlayerSheet, anchor="nw")
########################################################################################################################

#Checkbox variables
characterInspirationCB = tk.IntVar()
strSavingThrowCB = tk.IntVar()
AthleticsCB = tk.IntVar()
dexSavingThrowCB = tk.IntVar()
AcrobaticsCB = tk.IntVar()
SlightofHandCB = tk.IntVar()
StealthCB = tk.IntVar()
ConSavingThrowCB = tk.IntVar()
IntSavingThrowCB = tk.IntVar()
ArcanaCB = tk.IntVar()
HistoryCB = tk.IntVar()
InvestigationCB = tk.IntVar()
NatureCB = tk.IntVar()
ReligionCB = tk.IntVar()
WisSavingThrowCB = tk.IntVar()
AnimalHandlingCB = tk.IntVar()
InsightCB = tk.IntVar()
MedicineCB = tk.IntVar()
PerceptionCB = tk.IntVar()
SurvivalCB = tk.IntVar()
ChrSavingThrowCB = tk.IntVar()
DeceptionCB = tk.IntVar()
IntimidationCB = tk.IntVar()
PerformanceCB = tk.IntVar()
PersuasionCB = tk.IntVar()
dSave1 = tk.IntVar()
dSave2 = tk.IntVar()
dSave3 = tk.IntVar()
dFail1 = tk.IntVar()
dFail2 = tk.IntVar()
dFail3 = tk.IntVar()
########################################################################################################################
#character General information frame
generalInfo_frame = tk.Frame(dndPlayerSheet)
generalInfo_frame.grid(row=0, column=0, padx=5, pady=(5,0), columnspan=3, sticky="news")

#character General information
cName = tk.Label(generalInfo_frame, text = "Name")
cName.grid(row=0, column=0, rowspan=2)
cName_input = tk.Entry(generalInfo_frame, width=20, font=('', 32))
cName_input.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

cClass = tk.Label(generalInfo_frame, text="Class")
cClass.grid(row=0, column=2)
cClass_input = tk.Entry(generalInfo_frame, width=20)
cClass_input.grid(row=0, column=3, padx=5, pady=5)

cLevel = tk.Label(generalInfo_frame, text="Level")
cLevel.grid(row=0, column=4)
cLevel_input = tk.Entry(generalInfo_frame, width=3)
cLevel_input.grid(row=0, column=5, padx=5, pady=5)

cRace = tk.Label(generalInfo_frame, text="Race")
cRace.grid(row=1, column=2)
cRace_input = tk.Entry(generalInfo_frame, width=20)
cRace_input.grid(row=1, column=3, padx=5, pady=5)

cExperience = tk.Label(generalInfo_frame, text="Experience Points")
cExperience.grid(row=1, column=4)
cExperience_input = tk.Entry(generalInfo_frame, width=10)
cExperience_input.grid(row=1, column=5, padx=5, pady=5)

########################################################################################################################

#Character Stats frame
stats_Frame = tk.Frame(dndPlayerSheet)
stats_Frame.grid(row=1, column=0, padx=(5,0), pady=5, rowspan=4, sticky="news")

#Character Stats
pBonus = tk.Label(stats_Frame, text="Proficiency Bonus")
pBonus.grid(row=0, column=0, padx=5, pady=5)
pBonus_input = tk.Entry(stats_Frame, width=2)
pBonus_input.grid(row=0, column=1, padx=5, pady=5)
pInpiration = tk.Checkbutton(stats_Frame, text="Inspiration", variable=characterInspirationCB)
pInpiration.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

#Character Strength Stats
pStrength_Frame = tk.LabelFrame(stats_Frame, text="Strength")
pStrength_Frame.grid(row=2, column=0, columnspan=2, padx=10, pady=2)

pRolls = tk.Button(pStrength_Frame, text = "Roll", command=strRoll_window)
pRolls.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pStr_input = tk.Entry(pStrength_Frame, font=("", 64), width=2)
pStr_input.grid(row=0, column=0, rowspan=4, padx=5, pady=(5,0))

pStr_ST = tk.Checkbutton(pStrength_Frame, text = "Saving Throw", variable=strSavingThrowCB, command=strProfButton)
pStr_ST.grid(row=0, column=1, sticky="W")
pStr_ST_Num = tk.Entry(pStrength_Frame, width=2)
pStr_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pAthletics = tk.Checkbutton(pStrength_Frame, text = "Athletics", variable=AthleticsCB, command=athleticsProfButton)
pAthletics.grid(row=1, column=1, sticky="W")
pAthletics_Num = tk.Entry(pStrength_Frame, width=2)
pAthletics_Num.grid(row=1, column=2, sticky="E", padx=15)

#Character Dexterity Stats
pDexterity_Frame = tk.LabelFrame(stats_Frame, text="Dexterity")
pDexterity_Frame.grid(row=3, column=0, columnspan=2, padx=10, pady=2)

pRolld = tk.Button(pDexterity_Frame, text = "Roll", command=dexRoll_window)
pRolld.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pDex_input = tk.Entry(pDexterity_Frame, font=("", 64), width=2)
pDex_input.grid(row=0, column=0, rowspan=4, padx=5)

pDex_ST = tk.Checkbutton(pDexterity_Frame, text = "Saving Throw", variable=dexSavingThrowCB, command=dexProfButton)
pDex_ST.grid(row=0, column=1, sticky="W")
pDex_ST_Num = tk.Entry(pDexterity_Frame, width=2)
pDex_ST_Num.grid(row=0, column=2, sticky="E", padx=9)
pAcrobatics = tk.Checkbutton(pDexterity_Frame, text = "Acrobatics", variable=AcrobaticsCB, command=acrobaticsProfButton)
pAcrobatics.grid(row=1, column=1, sticky="W")
pAcrobatics_Num = tk.Entry(pDexterity_Frame, width=2)
pAcrobatics_Num.grid(row=1, column=2, sticky="E", padx=9)
pSlight_of_Hand = tk.Checkbutton(pDexterity_Frame, text = "Sleight of Hand", variable=SlightofHandCB, command=slightofHandProfButton)
pSlight_of_Hand.grid(row=2, column=1, sticky="W")
pSlight_of_Hand_Num = tk.Entry(pDexterity_Frame, width=2)
pSlight_of_Hand_Num.grid(row=2, column=2, sticky="E", padx=9)
pStealth = tk.Checkbutton(pDexterity_Frame, text = "Stealth", variable=StealthCB, command=stealthProfButton)
pStealth.grid(row=3, column=1, sticky="W")
pStealth_Num = tk.Entry(pDexterity_Frame, width=2)
pStealth_Num.grid(row=3, column=2, sticky="E", padx=9)

#Players Constitution Stats
pConstitution_Frame = tk.LabelFrame(stats_Frame, text="Constitution")
pConstitution_Frame.grid(row=4, column=0, columnspan=2, padx=10, pady=2)

pRollcon = tk.Button(pConstitution_Frame, text = "Roll", command=conRoll_window)
pRollcon.grid(row=1, column=0, pady=(5), padx=5, sticky="news")

pCon_input = tk.Entry(pConstitution_Frame, font=("", 64), width=2)
pCon_input.grid(row=0, column=0, padx=5)

pCon_ST = tk.Checkbutton(pConstitution_Frame, text = "Saving Throw", variable=ConSavingThrowCB, command=conProfButton)
pCon_ST.grid(row=0, column=1, sticky="W")
pCon_ST_Num = tk.Entry(pConstitution_Frame, width=2)
pCon_ST_Num.grid(row=0, column=2, sticky="E", padx=15)

#Players Intelligence Stats
pIntelligence_Frame = tk.LabelFrame(stats_Frame, text="Intelligence")
pIntelligence_Frame.grid(row=5, column=0, columnspan=2, padx=10, pady=2)

pRolli = tk.Button(pIntelligence_Frame, text = "Roll", command=intRoll_window)
pRolli.grid(row=4, column=0, pady=5, padx=5, sticky="news")

pInt_input = tk.Entry(pIntelligence_Frame, font=("", 64), width=2)
pInt_input.grid(row=0, column=0, rowspan=4, padx=5)

pInt_ST = tk.Checkbutton(pIntelligence_Frame, text = "Saving Throw", variable=IntSavingThrowCB, command=intProfButton)
pInt_ST.grid(row=0, column=1, sticky="W")
pInt_ST_Num = tk.Entry(pIntelligence_Frame, width=2)
pInt_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pArcana = tk.Checkbutton(pIntelligence_Frame, text = "Arcana", variable=ArcanaCB, command=arcanaProfButton)
pArcana.grid(row=1, column=1, sticky="W")
pArcana_Num = tk.Entry(pIntelligence_Frame, width=2)
pArcana_Num.grid(row=1, column=2, sticky="E", padx=15)
pHistory = tk.Checkbutton(pIntelligence_Frame, text = "History", variable=HistoryCB, command=historyProfButton)
pHistory.grid(row=2, column=1, sticky="W")
pHistory_Num = tk.Entry(pIntelligence_Frame, width=2)
pHistory_Num.grid(row=2, column=2, sticky="E", padx=15)
pInvestigation = tk.Checkbutton(pIntelligence_Frame, text = "Investigation", variable=InvestigationCB, command=investigationProfButton)
pInvestigation.grid(row=3, column=1, sticky="W")
pInvestigation_Num = tk.Entry(pIntelligence_Frame, width=2)
pInvestigation_Num.grid(row=3, column=2, sticky="E", padx=15)
pNature = tk.Checkbutton(pIntelligence_Frame, text = "Nature", variable=NatureCB, command=natureProfButton)
pNature.grid(row=4, column=1, sticky="W")
pNature_Num = tk.Entry(pIntelligence_Frame, width=2)
pNature_Num.grid(row=4, column=2, sticky="E", padx=15)
pReligion = tk.Checkbutton(pIntelligence_Frame, text = "Religion", variable=ReligionCB, command=religionProfButton)
pReligion.grid(row=5, column=1, sticky="W")
pReligion_Num = tk.Entry(pIntelligence_Frame, width=2)
pReligion_Num.grid(row=5, column=2, sticky="E", padx=15)

#Characters Wisdom Stats
pWisdom_Frame = tk.LabelFrame(stats_Frame, text="Wisdom")
pWisdom_Frame.grid(row=6, column=0, columnspan=2, padx=10, pady=2)

pRollw = tk.Button(pWisdom_Frame, text = "Roll", command=wisRoll_window)
pRollw.grid(row=4, column=0, padx=5, pady=5, sticky="news")

pWis_input = tk.Entry(pWisdom_Frame, font=("", 64), width=2)
pWis_input.grid(row=0, column=0, rowspan=4, padx=5)

pWis_ST = tk.Checkbutton(pWisdom_Frame, text = "Saving Throw", variable=WisSavingThrowCB, command=wisProfButton)
pWis_ST.grid(row=0, column=1, sticky="W")
pWis_ST_Num = tk.Entry(pWisdom_Frame, width=2)
pWis_ST_Num.grid(row=0, column=2, sticky="W", padx=(0,10))
pAnimal_Handling = tk.Checkbutton(pWisdom_Frame, text = "Animal Handling", variable=AnimalHandlingCB, command=ahProfButton)
pAnimal_Handling.grid(row=1, column=1, sticky="W")
pAnimal_Handling_Num = tk.Entry(pWisdom_Frame, width=2)
pAnimal_Handling_Num.grid(row=1, column=2, sticky="W")
pInsight = tk.Checkbutton(pWisdom_Frame, text = "Insight", variable=InsightCB, command=insightProfButton)
pInsight.grid(row=2, column=1, sticky="W")
pInsight_Num = tk.Entry(pWisdom_Frame, width=2)
pInsight_Num.grid(row=2, column=2, sticky="W")
pMedicine = tk.Checkbutton(pWisdom_Frame, text = "Medicine", variable=MedicineCB, command=medicineProfButton)
pMedicine.grid(row=3, column=1, sticky="W")
pMedicine_Num = tk.Entry(pWisdom_Frame, width=2)
pMedicine_Num.grid(row=3, column=2, sticky="W")
pPerception = tk.Checkbutton(pWisdom_Frame, text = "Perception", variable=PerceptionCB, command=perceptionProfButton)
pPerception.grid(row=4, column=1, sticky="W")
pPerception_Num = tk.Entry(pWisdom_Frame, width=2)
pPerception_Num.grid(row=4, column=2, sticky="W")
pSurvival = tk.Checkbutton(pWisdom_Frame, text = "Survival", variable=SurvivalCB, command=survivalProfButton)
pSurvival.grid(row=5, column=1, sticky="W")
pSurvival_Num = tk.Entry(pWisdom_Frame, width=2)
pSurvival_Num.grid(row=5, column=2, sticky="W")


#Characters Charisma Stats
pCharisma_Frame = tk.LabelFrame(stats_Frame, text="Charisma")
pCharisma_Frame.grid(row=7, column=0, columnspan=2, padx=10, pady=2)

pRollc = tk.Button(pCharisma_Frame, text = "Roll", command=chrRoll_window)
pRollc.grid(row=4, column=0, pady=(5), padx=5, sticky="news")

pChr_input = tk.Entry(pCharisma_Frame, font=("", 64), width=2)
pChr_input.grid(row=0, column=0, rowspan=4, padx=5)

pChr_ST = tk.Checkbutton(pCharisma_Frame, text = "Saving Throw", variable=ChrSavingThrowCB, command=chrProfButton)
pChr_ST.grid(row=0, column=1, sticky="W")
pChr_ST_Num = tk.Entry(pCharisma_Frame, width=2)
pChr_ST_Num.grid(row=0, column=2, sticky="E", padx=15)
pDeception = tk.Checkbutton(pCharisma_Frame, text = "Deception", variable=DeceptionCB, command=deceptionProfButton)
pDeception.grid(row=1, column=1, sticky="W")
pDeception_Num = tk.Entry(pCharisma_Frame, width=2)
pDeception_Num.grid(row=1, column=2, sticky="E", padx=15)
pIntimidation = tk.Checkbutton(pCharisma_Frame, text = "Intimidation", variable=IntimidationCB, command=intimidationProfButton)
pIntimidation.grid(row=2, column=1, sticky="W")
pIntimidation_Num = tk.Entry(pCharisma_Frame, width=2)
pIntimidation_Num.grid(row=2, column=2, sticky="E", padx=15)
pPerformance = tk.Checkbutton(pCharisma_Frame, text = "Performance", variable=PerformanceCB, command=performanceProfButton)
pPerformance.grid(row=3, column=1, sticky="W")
pPerformance_Num = tk.Entry(pCharisma_Frame, width=2)
pPerformance_Num.grid(row=3, column=2, sticky="E", padx=15)
pPersuasion = tk.Checkbutton(pCharisma_Frame, text = "Persuasion",variable=PersuasionCB, command=persuasionProfButton)
pPersuasion.grid(row=4, column=1, sticky="W")
pPersuasion_Num = tk.Entry(pCharisma_Frame, width=2)
pPersuasion_Num.grid(row=4, column=2, sticky="E", padx=15)

pPassiveWisdom = tk.Label(stats_Frame, text="Passive Wisdom/Perception")
pPassiveWisdom.grid(row=8, column=0, padx=5, pady=5)
pPassiveWisdom_Num = tk.Entry(stats_Frame, width=2)
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
pAC_input = tk.Entry(ac_i_s_Frame, font=("", 40), width=2)
pAC_input.grid(row=1, column=0, padx=5, pady=5)
ACequalSign = tk.Label(ac_i_s_Frame, text=" = ")
ACequalSign.grid(row=1, column=1)
ACdexModifier = tk.Label(ac_i_s_Frame, text="Dexterity Modifier")
ACdexModifier.grid(row=0, column=2)
ACdexModifier_input = tk.Entry(ac_i_s_Frame, width=2)
ACdexModifier_input.grid(row=1, column=2)
ACplus1 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus1.grid(row=1, column=3)
ACarmor = tk.Label(ac_i_s_Frame, text="Armor")
ACarmor.grid(row=0, column=4)
ACarmor_input = tk.Entry(ac_i_s_Frame, width=2)
ACarmor_input.grid(row=1, column=4)
ACplus2 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus2.grid(row=1, column=5)
ACshield = tk.Label(ac_i_s_Frame, text="Shield")
ACshield.grid(row=0, column=6)
ACshield_input = tk.Entry(ac_i_s_Frame, width=2)
ACshield_input.grid(row=1, column=6)
ACplus3 = tk.Label(ac_i_s_Frame, text=" + ")
ACplus3.grid(row=1, column=7)
ACMisc = tk.Label(ac_i_s_Frame, text="Misc.")
ACMisc.grid(row=0, column=8)
ACMisc_input = tk.Entry(ac_i_s_Frame, width=2)
ACMisc_input.grid(row=1, column=8)

acCalculateButton = tk.Button(ac_i_s_Frame, text="Calculate", command=acFormula)
acCalculateButton.grid(row=1, column=1, columnspan=8, sticky="wse")

pInitiative = tk.Button(ac_i_s_Frame, text="Initiative", command=initiative_button)
pInitiative.grid(row=0, column=9, padx=(160, 0))
pInitiative_input = tk.Entry(ac_i_s_Frame, font=("", 40), width=2)
pInitiative_input.grid(row=1, column=9, padx=(160, 0))

pSpeed = tk.Label(ac_i_s_Frame, text="Speed")
pSpeed.grid(row=0, column=10, padx=20)
pSpeed_input = tk.Entry(ac_i_s_Frame, font=("", 40), width=2)
pSpeed_input.grid(row=1, column=10, padx=20)

########################################################################################################################


#Hit points and death saves
health_Frame = tk.Frame(dndPlayerSheet)
health_Frame.grid(row=2, column=1, padx=5, pady=(5,0), sticky="news")

#hitpoints frame
hitPoint_Frame = tk.Frame(health_Frame)
hitPoint_Frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

hpm_label = tk.Label(hitPoint_Frame, text="Hit Points Maximum")
hpm_label.grid(row=0, column=0, padx=85)
hpm_label_input = tk.Entry(hitPoint_Frame, width=4)
hpm_label_input.grid(row=0, column=1)
chp_input = tk.Entry(hitPoint_Frame, width=4, font=("", 64))
chp_input.grid(row=1, column=0, columnspan=2, rowspan=2, padx=85)
chp_label = tk.Label(hitPoint_Frame, text="Current Hit Points")
chp_label.grid(row=3, column=0, columnspan=2)
healthUp_button = tk.Button(hitPoint_Frame,text="+1", command=addHealth)
healthUp_button.grid(row=1, column=1, sticky="news")
healthDown_button = tk.Button(hitPoint_Frame,text="-1", command=subHealth)
healthDown_button.grid(row=2, column=1, sticky="news")

#Hit dice frame
hd_Frame = tk.Frame(health_Frame)
hd_Frame.grid(row=1, column=0, padx=5, pady=5)

totalHD_Label = tk.Label(hd_Frame, text="Total")
totalHD_Label.grid(row=0, column=0)
totalHD_input = tk.Entry(hd_Frame, width=4)
totalHD_input.grid(row=0, column=1)
hd_input = tk.Entry(hd_Frame, width=3, font=("", 40))
hd_input.grid(row=1, column=0, columnspan=2)
hd_Label = tk.Label(hd_Frame, text="Hit Dice")
hd_Label.grid(row=2, column=0, columnspan=2)

#Death saves frame
ds_Frame = tk.Frame(health_Frame)
ds_Frame.grid(row=1, column=1, padx=5, pady=(0,5))

success_Label = tk.Label(ds_Frame, text="Successes")
success_Label.grid(row=0, column=0)
success_1 = tk.Checkbutton(ds_Frame, variable=dSave1)
success_1.grid(row=0, column=1, padx=5)
success_2 = tk.Checkbutton(ds_Frame, variable=dSave2)
success_2.grid(row=0, column=2, padx=5)
success_3 = tk.Checkbutton(ds_Frame, variable=dSave3)
success_3.grid(row=0, column=3, padx=5)

failure_Label = tk.Label(ds_Frame, text="Failures")
failure_Label.grid(row=1, column=0)
failure_1 = tk.Checkbutton(ds_Frame, variable=dFail1)
failure_1.grid(row=1, column=1, padx=5)
failure_2 = tk.Checkbutton(ds_Frame, variable=dFail2)
failure_2.grid(row=1, column=2, padx=5)
failure_3 = tk.Checkbutton(ds_Frame, variable=dFail3)
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
pWeapon1.grid(row=0, column=0, padx=(5,0), sticky="news")

pWeapon1_Num = tk.Entry(pWeapon1, width=32)
pWeapon1_Num.pack(padx=5, pady=5)
pWeapon1Range = tk.LabelFrame(playerWeapon1, text="Range")
pWeapon1Range.grid(row=0, column=2, columnspan=2, padx=5)
pWeapon1Range_Num = tk.Entry(pWeapon1Range, width=20)
pWeapon1Range_Num.pack(padx=5, pady=5)
pWeapon1Type = tk.LabelFrame(playerWeapon1, text="Type")
pWeapon1Type.grid(row=1, column=0, padx=(5,0), pady=5, sticky="w")
pWeapon1Type_Num = tk.Entry(pWeapon1Type, width=30)
pWeapon1Type_Num.pack(padx=5, pady=5)
pWeapon1AB = tk.LabelFrame(playerWeapon1, text="Attack Bonus")
pWeapon1AB.grid(row=1, column=1, columnspan=2)
pWeapon1AB_Num = tk.Entry(pWeapon1AB, width=10)
pWeapon1AB_Num.pack(padx=5, pady=5)
pWeapon1Damage = tk.LabelFrame(playerWeapon1, text="Damage")
pWeapon1Damage.grid(row=1, column=3, padx=(5))
pWeapon1Damage_Num = tk.Entry(pWeapon1Damage, width=7)
pWeapon1Damage_Num.pack(padx=5, pady=5)

pWeapon1AttackButton = tk.Button(playerWeapon1, text="Attack", command=attack_1)
pWeapon1AttackButton.grid(row=2, column=0, columnspan=5, padx=5, pady=(0,5), sticky="news")


playerWeapon2 = tk.LabelFrame(weapon_Frame, text="Weapon 2")
playerWeapon2.grid(row=1, column=0, padx=5, pady=5)

pWeapon2 = tk.LabelFrame(playerWeapon2, text="Weapon/Spell")
pWeapon2.grid(row=0, column=0, padx=(5,0), sticky="news")

pWeapon2_Num = tk.Entry(pWeapon2, width=32)
pWeapon2_Num.pack(padx=5, pady=5)
pWeapon2Range = tk.LabelFrame(playerWeapon2, text="Range")
pWeapon2Range.grid(row=0, column=2, columnspan=2, padx=5)
pWeapon2Range_Num = tk.Entry(pWeapon2Range, width=20)
pWeapon2Range_Num.pack(padx=5, pady=5)
pWeapon2Type = tk.LabelFrame(playerWeapon2, text="Type")
pWeapon2Type.grid(row=1, column=0, padx=(5,0), pady=5, sticky="w")
pWeapon2Type_Num = tk.Entry(pWeapon2Type, width=30)
pWeapon2Type_Num.pack(padx=5, pady=5)
pWeapon2AB = tk.LabelFrame(playerWeapon2, text="Attack Bonus")
pWeapon2AB.grid(row=1, column=1, columnspan=2)
pWeapon2AB_Num = tk.Entry(pWeapon2AB, width=10)
pWeapon2AB_Num.pack(padx=5, pady=5)
pWeapon2Damage = tk.LabelFrame(playerWeapon2, text="Damage")
pWeapon2Damage.grid(row=1, column=3, padx=(5))
pWeapon2Damage_Num = tk.Entry(pWeapon2Damage, width=7)
pWeapon2Damage_Num.pack(padx=5, pady=5)

pWeapon2AttackButton = tk.Button(playerWeapon2, text="Attack", command=attack_2)
pWeapon2AttackButton.grid(row=4, column=0, columnspan=5, padx=5, pady=(0,5), sticky="news")


playerWeapon3 = tk.LabelFrame(weapon_Frame, text="Weapon 3")
playerWeapon3.grid(row=2, column=0, padx=5, pady=5)

pWeapon3 = tk.LabelFrame(playerWeapon3, text="Weapon/Spell")
pWeapon3.grid(row=0, column=0, padx=(5,0), sticky="news")

pWeapon3_Num = tk.Entry(pWeapon3, width=32)
pWeapon3_Num.pack(padx=5, pady=5)
pWeapon3Range = tk.LabelFrame(playerWeapon3, text="Range")
pWeapon3Range.grid(row=0, column=2, columnspan=2, padx=5)
pWeapon3Range_Num = tk.Entry(pWeapon3Range, width=20)
pWeapon3Range_Num.pack(padx=5, pady=5)
pWeapon3Type = tk.LabelFrame(playerWeapon3, text="Type")
pWeapon3Type.grid(row=1, column=0, padx=(5,0), pady=5, sticky="w")
pWeapon3Type_Num = tk.Entry(pWeapon3Type, width=30)
pWeapon3Type_Num.pack(padx=5, pady=5)
pWeapon3AB = tk.LabelFrame(playerWeapon3, text="Attack Bonus")
pWeapon3AB.grid(row=1, column=1, columnspan=2)
pWeapon3AB_Num = tk.Entry(pWeapon3AB, width=10)
pWeapon3AB_Num.pack(padx=5, pady=5)
pWeapon3Damage = tk.LabelFrame(playerWeapon3, text="Damage")
pWeapon3Damage.grid(row=1, column=3, padx=(5))
pWeapon3Damage_Num = tk.Entry(pWeapon3Damage, width=7)
pWeapon3Damage_Num.pack(padx=5, pady=5)

pWeapon3AttackButton = tk.Button(playerWeapon3, text="Attack", command=attack_3)
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

########################################################################################################################
########################################################################################################################
#Creation of the Characters spellbook
########################################################################################################################
########################################################################################################################
#General info frame
spell_generalInfo_frame = tk.Frame(dndSpellSheet_tab)
spell_generalInfo_frame.pack()

spellcasting_ability = tk.Entry(spell_generalInfo_frame, font=("", 40), width=2, borderwidth=10)
spellcasting_ability.grid(row=0, column=0, padx=80, pady=(20, 0))
spellcasting_ability_label = tk.Label(spell_generalInfo_frame, text="Spellcasting Ability", font=("", 16))
spellcasting_ability_label.grid(row=1, column=0)

spell_save_dc = tk.Entry(spell_generalInfo_frame, font=("", 40), width=2, borderwidth=10)
spell_save_dc.grid(row=0, column=1, padx=80, pady=(20, 0))
spell_save_dc_label = tk.Label(spell_generalInfo_frame, text="Spell Save DC", font=("", 16))
spell_save_dc_label.grid(row=1, column=1)

spell_attack_bonus = tk.Entry(spell_generalInfo_frame, font=("", 40), width=2, borderwidth=10)
spell_attack_bonus.grid(row=0, column=2, padx=80, pady=(20, 0))
spell_attack_bonus_label = tk.Label(spell_generalInfo_frame, text="Spell Attack Bonus", font=("", 16))
spell_attack_bonus_label.grid(row=1, column=2)

########################################################################################################################

dynamic_slots_1 = []
dynamic_slots_2 = []
dynamic_slots_3 = []
dynamic_slots_4 = []
dynamic_slots_5 = []
dynamic_slots_6 = []
dynamic_slots_7 = []
dynamic_slots_8 = []
dynamic_slots_9 = []

first_slots = 0
second_slots = 0
third_slots = 0
fourth_slots = 0
fifth_slots = 0
sixth_slots = 0
seventh_slots = 0
eigth_slots = 0
ninth_slots = 0

spelldict = {}
spelldict["Cantrips"] = []
spelldict["1st Level Spells"] = []
spelldict["2nd Level Spells"] = []
spelldict["3rd Level Spells"] = []
spelldict["4th Level Spells"] = []
spelldict["5th Level Spells"] = []
spelldict["6th Level Spells"] = []
spelldict["7th Level Spells"] = []
spelldict["8th Level Spells"] = []
spelldict["9th Level spells"] = []


def saveSpellSheet():
    json.dump(spelldict, open('spells.json', 'w'), indent=2)

def add_slots_1():
    global first_slots
    if first_slots != 6:
        button = tk.Checkbutton(button_frames1, border=5, variable=first_slots)
        dynamic_slots_1.append(button)
        button.pack(side=tk.LEFT)
        first_slots = first_slots + 1
    
def remove_slots_1():
    global first_slots
    dynamic_slots_1[first_slots - 1].destroy()
    del dynamic_slots_1[-1]
    first_slots = first_slots - 1

def add_slots_2():
    global second_slots
    if second_slots != 6:
        button = tk.Checkbutton(button_frames2, border=5, variable=(7 + second_slots))
        dynamic_slots_2.append(button)
        button.pack(side=tk.LEFT)
        second_slots = second_slots + 1
    
def remove_slots_2():
    global second_slots
    dynamic_slots_2[second_slots - 1].destroy()
    del dynamic_slots_2[-1]
    second_slots = second_slots - 1

def add_slots_3():
    global third_slots
    if third_slots != 6:
        button = tk.Checkbutton(button_frames3, border=5, variable=(14 + third_slots))
        dynamic_slots_3.append(button)
        button.pack(side=tk.LEFT)
        third_slots = third_slots + 1
    
def remove_slots_3():
    global third_slots
    dynamic_slots_3[third_slots - 1].destroy()
    del dynamic_slots_3[-1]
    third_slots = third_slots - 1

def add_slots_4():
    global fourth_slots
    if fourth_slots != 6:
        button = tk.Checkbutton(button_frames4, border=5, variable=(21 + fourth_slots))
        dynamic_slots_4.append(button)
        button.pack(side=tk.LEFT)
        fourth_slots = fourth_slots + 1
    
def remove_slots_4():
    global fourth_slots
    dynamic_slots_4[fourth_slots - 1].destroy()
    del dynamic_slots_4[-1]
    fourth_slots = fourth_slots - 1

def add_slots_5():
    global fifth_slots
    if fifth_slots != 6:
        button = tk.Checkbutton(button_frames5, border=5, variable=(28 + fifth_slots))
        dynamic_slots_5.append(button)
        button.pack(side=tk.LEFT)
        fifth_slots = fifth_slots + 1
    
def remove_slots_5():
    global fifth_slots
    dynamic_slots_5[fifth_slots - 1].destroy()
    del dynamic_slots_5[-1]
    fifth_slots = fifth_slots - 1

def add_slots_6():
    global sixth_slots
    if sixth_slots != 6:
        button = tk.Checkbutton(button_frames6, border=5, variable=(35 + sixth_slots))
        dynamic_slots_6.append(button)
        button.pack(side=tk.LEFT)
        sixth_slots = sixth_slots + 1
    
def remove_slots_6():
    global sixth_slots
    dynamic_slots_6[sixth_slots - 1].destroy()
    del dynamic_slots_6[-1]
    sixth_slots = sixth_slots - 1

def add_slots_7():
    global seventh_slots
    if seventh_slots != 6:
        button = tk.Checkbutton(button_frames7, border=5, variable=(42 + seventh_slots))
        dynamic_slots_7.append(button)
        button.pack(side=tk.LEFT)
        seventh_slots = seventh_slots + 1
    
def remove_slots_7():
    global seventh_slots
    dynamic_slots_7[seventh_slots - 1].destroy()
    del dynamic_slots_7[-1]
    seventh_slots = seventh_slots - 1

def add_slots_8():
    global eigth_slots
    if eigth_slots != 6:
        button = tk.Checkbutton(button_frames8, border=5, variable=(49 + eigth_slots))
        dynamic_slots_8.append(button)
        button.pack(side=tk.LEFT)
        eigth_slots = eigth_slots + 1
    
def remove_slots_8():
    global eigth_slots
    dynamic_slots_8[eigth_slots - 1].destroy()
    del dynamic_slots_8[-1]
    eigth_slots = eigth_slots - 1

def add_slots_9():
    global ninth_slots
    if ninth_slots != 6:
        button = tk.Checkbutton(button_frames9, border=5, variable=(56 + ninth_slots))
        dynamic_slots_9.append(button)
        button.pack(side=tk.LEFT)
        ninth_slots = ninth_slots + 1
    
def remove_slots_9():
    global ninth_slots
    dynamic_slots_9[ninth_slots - 1].destroy()
    del dynamic_slots_9[-1]
    ninth_slots = ninth_slots - 1

def cancel_addspell():
    add_spell_window.destroy()

def save_addspell():

    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="Cantrips"):
        addspell_frame(cantrips_frame)
        spelldict["Cantrips"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="1st Level"):
        addspell_frame(firstlevel_frame)
        spelldict["1st Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="2nd Level"):
        addspell_frame(secondlevel_frame)
        spelldict["2nd Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="3rd Level"):
        addspell_frame(thirdlevel_frame)
        spelldict["3rd Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="4th Level"):
        addspell_frame(fourthlevel_frame)
        spelldict["4th Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="5th Level"):
        addspell_frame(fifthlevel_frame)
        spelldict["5th Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="6th Level"):
        addspell_frame(sixthlevel_frame)
        spelldict["6th Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="7th Level"):
        addspell_frame(seventhlevel_frame)
        spelldict["7th Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="8th Level"):
        addspell_frame(eigthlevel_frame)
        spelldict["8th Level Spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()
    if (spelllevel_listbox.get(spelllevel_listbox.curselection())=="9th Level"):
        addspell_frame(ninthlevel_frame)
        spelldict["9th Level spells"].append(
            {
                "Name":spell_name_input.get(),
                "Description":spell_description_input.get(1.0, "end-1c"),
                "Damage":spell_damage_input.get()
            })
        saveSpellSheet()


def addspell_frame(frame):
    newspell_frame = tk.Frame(frame)
    newspell_frame.pack()
    spell_name_saved = tk.Label(newspell_frame, text="Name")
    spell_name_saved.grid(row=0, column=0, sticky="w", padx=10)
    spell_name_input_saved = tk.Entry(newspell_frame, width=22)
    spell_name_input_saved.insert(tk.END, spell_name_input.get())
    spell_name_input_saved["state"] = tk.DISABLED
    spell_name_input_saved.grid(row=1, column=0, sticky="new", padx=10)
    spell_description_saved = tk.Label(newspell_frame, text="Description")
    spell_description_saved.grid(row=0, column=1, sticky="w")
    spell_description_input_saved = tk.Text(newspell_frame, width=60, height=20)
    spell_description_input_saved.insert(tk.END, spell_description_input.get(1.0, "end-1c"))
    spell_description_input_saved["state"] = tk.DISABLED
    spell_description_input_saved.grid(row=1, column=1)
    spell_damage_saved = tk.Label(newspell_frame, text="Damage")
    spell_damage_saved.grid(row=0, column=2, sticky="w", padx=10)
    spell_damage_input_saved = tk.Entry(newspell_frame, width=21)
    spell_damage_input_saved.insert(tk.END, spell_damage_input.get())
    spell_damage_input_saved["state"] = tk.DISABLED
    spell_damage_input_saved.grid(row=1, column=2, sticky="new", padx=10)


def add_spell_toplevel():
    global add_spell_window, spell_name_input, spell_description_input, spell_damage_input, spelllevel_listbox
    add_spell_window = tk.Toplevel()
    spell_name = tk.Label(add_spell_window, text="Name")
    spell_name.grid(row=0, column=0, sticky="w", padx=10)
    spell_name_input = tk.Entry(add_spell_window)
    spell_name_input.grid(row=1, column=0, sticky="new", padx=10)
    spell_description = tk.Label(add_spell_window, text="Description")
    spell_description.grid(row=0, column=1, sticky="w")
    spell_description_input = tk.Text(add_spell_window, height=5, width=60)
    spell_description_input.grid(row=1, column=1, rowspan=2, sticky="n")
    spell_damage = tk.Label(add_spell_window, text="Damage")
    spell_damage.grid(row=0, column=2, sticky="w", padx=10)
    spell_damage_input = tk.Entry(add_spell_window)
    spell_damage_input.grid(row=1, column=2, sticky="new", padx=10)
    addspell_cancel_button = tk.Button(add_spell_window, text="Cancel", command=cancel_addspell)
    addspell_cancel_button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
    addspell_save_button = tk.Button(add_spell_window, text="Save", command=save_addspell)
    addspell_save_button.grid(row=3, column=2, sticky="news", padx=10, pady=10)
    spelllevel_listbox = tk.Listbox(add_spell_window)
    spelllevel_listbox.config(height=spelllevel_listbox.size())
    spelllevel_listbox.grid(row=2, column=2)
    spelllevel_listbox.insert(1, "Cantrips")
    spelllevel_listbox.insert(2, "1st Level")
    spelllevel_listbox.insert(3, "2nd Level")
    spelllevel_listbox.insert(4, "3rd Level")
    spelllevel_listbox.insert(5, "4th Level")
    spelllevel_listbox.insert(6, "5th Level")
    spelllevel_listbox.insert(7, "6th Level")
    spelllevel_listbox.insert(8, "7th Level")
    spelllevel_listbox.insert(9, "8th Level")
    spelllevel_listbox.insert(10, "9th Level")



#Spell slots frame
spell_slots_frame = tk.LabelFrame(dndSpellSheet_tab, text="Spell Slots", font=("", 20))
spell_slots_frame.pack()

first_level_frame = tk.Frame(spell_slots_frame)
first_level_frame.grid(row=0, column=0, padx=20)
first_level_label = tk.Label(first_level_frame, text="1st Level", font=("", 16))
first_level_label.grid(row=0, column=0, padx=20)
add_slot1 = tk.Button(first_level_frame, text=">", command=add_slots_1, width=5)
add_slot1.grid(row=0, column=2)
remove_slot1 = tk.Button(first_level_frame, text="<", command=remove_slots_1, width=5)
remove_slot1.grid(row=0, column=1)
button_frames1 = tk.Frame(first_level_frame)
button_frames1.grid(row=2, column=0, columnspan=6)

second_level_frame = tk.Frame(spell_slots_frame)
second_level_frame.grid(row=1, column=0, padx=20)
second_level_label = tk.Label(second_level_frame, text="2nd Level", font=("", 16))
second_level_label.grid(row=0, column=0, padx=20)
add_slot2 = tk.Button(second_level_frame, text=">", command=add_slots_2, width=5)
add_slot2.grid(row=0, column=2)
remove_slot2 = tk.Button(second_level_frame, text="<", command=remove_slots_2, width=5)
remove_slot2.grid(row=0, column=1)
button_frames2 = tk.Frame(second_level_frame)
button_frames2.grid(row=2, column=0, columnspan=6)

third_level_frame = tk.Frame(spell_slots_frame)
third_level_frame.grid(row=2, column=0, padx=20)
third_level_label = tk.Label(third_level_frame, text="3rd Level", font=("", 16))
third_level_label.grid(row=0, column=0, padx=20)
add_slot3 = tk.Button(third_level_frame, text=">", command=add_slots_3, width=5)
add_slot3.grid(row=0, column=2)
remove_slot3 = tk.Button(third_level_frame, text="<", command=remove_slots_3, width=5)
remove_slot3.grid(row=0, column=1)
button_frames3 = tk.Frame(third_level_frame)
button_frames3.grid(row=2, column=0, columnspan=6)

fourth_level_frame = tk.Frame(spell_slots_frame)
fourth_level_frame.grid(row=0, column=1, padx=20)
fourth_level_label = tk.Label(fourth_level_frame, text="4th Level", font=("", 16))
fourth_level_label.grid(row=0, column=0, padx=20)
add_slot4 = tk.Button(fourth_level_frame, text=">", command=add_slots_4, width=5)
add_slot4.grid(row=0, column=2)
remove_slot4 = tk.Button(fourth_level_frame, text="<", command=remove_slots_4, width=5)
remove_slot4.grid(row=0, column=1)
button_frames4 = tk.Frame(fourth_level_frame)
button_frames4.grid(row=2, column=0, columnspan=6)

fifth_level_frame = tk.Frame(spell_slots_frame)
fifth_level_frame.grid(row=1, column=1, padx=20)
fifth_level_label = tk.Label(fifth_level_frame, text="5th Level", font=("", 16))
fifth_level_label.grid(row=0, column=0, padx=20)
add_slot5 = tk.Button(fifth_level_frame, text=">", command=add_slots_5, width=5)
add_slot5.grid(row=0, column=2)
remove_slot5 = tk.Button(fifth_level_frame, text="<", command=remove_slots_5, width=5)
remove_slot5.grid(row=0, column=1)
button_frames5 = tk.Frame(fifth_level_frame)
button_frames5.grid(row=2, column=0, columnspan=6)

sixth_level_frame = tk.Frame(spell_slots_frame)
sixth_level_frame.grid(row=2, column=1, padx=20)
sixth_level_label = tk.Label(sixth_level_frame, text="6th Level", font=("", 16))
sixth_level_label.grid(row=0, column=0, padx=20)
add_slot6 = tk.Button(sixth_level_frame, text=">", command=add_slots_6, width=5)
add_slot6.grid(row=0, column=2)
remove_slot6 = tk.Button(sixth_level_frame, text="<", command=remove_slots_6, width=5)
remove_slot6.grid(row=0, column=1)
button_frames6 = tk.Frame(sixth_level_frame)
button_frames6.grid(row=2, column=0, columnspan=6)

seventh_level_frame = tk.Frame(spell_slots_frame)
seventh_level_frame.grid(row=0, column=2, padx=20)
seventh_level_label = tk.Label(seventh_level_frame, text="7th Level", font=("", 16))
seventh_level_label.grid(row=0, column=0, padx=20)
add_slot7 = tk.Button(seventh_level_frame, text=">", command=add_slots_7, width=5)
add_slot7.grid(row=0, column=2)
remove_slot7 = tk.Button(seventh_level_frame, text="<", command=remove_slots_7, width=5)
remove_slot7.grid(row=0, column=1)
button_frames7 = tk.Frame(seventh_level_frame)
button_frames7.grid(row=2, column=0, columnspan=6)

eigth_level_frame = tk.Frame(spell_slots_frame)
eigth_level_frame.grid(row=1, column=2, padx=20)
eigth_level_label = tk.Label(eigth_level_frame, text="8th Level", font=("", 16))
eigth_level_label.grid(row=0, column=0, padx=20)
add_slot8 = tk.Button(eigth_level_frame, text=">", command=add_slots_8, width=5)
add_slot8.grid(row=0, column=2)
remove_slot8 = tk.Button(eigth_level_frame, text="<", command=remove_slots_8, width=5)
remove_slot8.grid(row=0, column=1)
button_frames8 = tk.Frame(eigth_level_frame)
button_frames8.grid(row=2, column=0, columnspan=6)

ninth_level_frame = tk.Frame(spell_slots_frame)
ninth_level_frame.grid(row=2, column=2, padx=20)
ninth_level_label = tk.Label(ninth_level_frame, text="9th Level", font=("", 16))
ninth_level_label.grid(row=0, column=0, padx=20)
add_slot9 = tk.Button(ninth_level_frame, text=">", command=add_slots_9, width=5)
add_slot9.grid(row=0, column=2)
remove_slots9 = tk.Button(ninth_level_frame, text="<", command=remove_slots_9, width=5)
remove_slots9.grid(row=0, column=1)
button_frames9 = tk.Frame(ninth_level_frame)
button_frames9.grid(row=2, column=0, columnspan=6)


########################################################################################################################

#Creation of the scroll bar for the dndSpellSheet_tab
main_frame = tk.Frame(dndSpellSheet_tab)
main_frame.pack(fill=tk.BOTH, expand=1)
dndSpellSheet_Canvas = tk.Canvas(main_frame)
dndSpellSheet_Canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
playersheet_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=dndSpellSheet_Canvas.yview)
playersheet_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
dndSpellSheet_Canvas.configure(yscrollcommand=playersheet_scrollbar.set)
dndSpellSheet_Canvas.bind('<Configure>', lambda e:dndSpellSheet_Canvas.configure(scrollregion=dndSpellSheet_Canvas.bbox('all')))
dndSpellSheet = tk.Frame(dndSpellSheet_Canvas)
dndSpellSheet_Canvas.create_window((0,0), window=dndSpellSheet, anchor="nw")

########################################################################################################################
#Save new spell frame

spellbook_frame = tk.LabelFrame(dndSpellSheet, text="Spellbook")
spellbook_frame.pack(padx=115)

cantrips_frame = tk.Frame(spellbook_frame)
cantrips_frame.pack()
cantrips_tab = tk.Button(cantrips_frame, text="Cantrips", padx=372)
cantrips_tab.pack()

firstlevel_frame = tk.Frame(spellbook_frame)
firstlevel_frame.pack()
firstlevel_tab = tk.Button(firstlevel_frame, text="1st Level Spells", padx=355)
firstlevel_tab.pack()

secondlevel_frame = tk.Frame(spellbook_frame)
secondlevel_frame.pack()
secondlevel_tab = tk.Button(secondlevel_frame, text="2nd Level Spells", padx=353)
secondlevel_tab.pack()

thirdlevel_frame = tk.Frame(spellbook_frame)
thirdlevel_frame.pack()
thirdlevel_tab = tk.Button(thirdlevel_frame, text="3rd Level Spells", padx=355)
thirdlevel_tab.pack()

fourthlevel_frame = tk.Frame(spellbook_frame)
fourthlevel_frame.pack()
fourthlevel_tab = tk.Button(fourthlevel_frame, text="4th Level Spells", padx=355)
fourthlevel_tab.pack()

fifthlevel_frame = tk.Frame(spellbook_frame)
fifthlevel_frame.pack()
fifthlevel_tab = tk.Button(fifthlevel_frame, text="5th Level Spells", padx=355)
fifthlevel_tab.pack()

sixthlevel_frame = tk.Frame(spellbook_frame)
sixthlevel_frame.pack()
sixthlevel_tab = tk.Button(sixthlevel_frame, text="6th Level Spells", padx=355)
sixthlevel_tab.pack()

seventhlevel_frame = tk.Frame(spellbook_frame)
seventhlevel_frame.pack()
seventhlevel_tab = tk.Button(seventhlevel_frame, text="7th Level Spells", padx=355)
seventhlevel_tab.pack()

eigthlevel_frame = tk.Frame(spellbook_frame)
eigthlevel_frame.pack()
eigthlevel_tab = tk.Button(eigthlevel_frame, text="8th Level Spells", padx=355)
eigthlevel_tab.pack()

ninthlevel_frame = tk.Frame(spellbook_frame)
ninthlevel_frame.pack()
ninthlevel_tab = tk.Button(ninthlevel_frame, text="9th Level Spells", padx=355)
ninthlevel_tab.pack()


add_Button = tk.Button(dndSpellSheet, text="Add Spell", command=add_spell_toplevel)
add_Button.pack()


########################################################################################################################














openInfoFile()

root.mainloop()
