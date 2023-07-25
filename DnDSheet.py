import tkinter as tk
from tkinter import ttk
import json




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
        pPerception_Num.insert(tk.END, cInfo_d['Performance'])
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
    )   
    
    json.dump(cInfo_d, open('info.json', 'w'), indent=2)


def strProfButton():
    if(strSavingThrowCB.get()==1):
        isProficient = (int(pStr_ST_Num.get()) + int(pBonus_input.get()))
        pStr_ST_Num.delete(0, tk.END)
        pStr_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pStr_ST_Num.get()) - int(pBonus_input.get()))
        pStr_ST_Num.delete(0, tk.END)
        pStr_ST_Num.insert(tk.END, isNotProficient)
    
def athleticsProfButton():
    if(AthleticsCB.get()==1):
        isProficient = (int(pAthletics_Num.get()) + int(pBonus_input.get()))
        pAthletics_Num.delete(0, tk.END)
        pAthletics_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pAthletics_Num.get()) - int(pBonus_input.get()))
        pAthletics_Num.delete(0, tk.END)
        pAthletics_Num.insert(tk.END, isNotProficient)

def dexProfButton():
    if(dexSavingThrowCB.get()==1):
        isProficient = (int(pDex_ST_Num.get()) + int(pBonus_input.get()))
        pDex_ST_Num.delete(0, tk.END)
        pDex_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pDex_ST_Num.get()) - int(pBonus_input.get()))
        pDex_ST_Num.delete(0, tk.END)
        pDex_ST_Num.insert(tk.END, isNotProficient)

def acrobaticsProfButton():
    if(AcrobaticsCB.get()==1):
        isProficient = (int(pAcrobatics_Num.get()) + int(pBonus_input.get()))
        pAcrobatics_Num.delete(0, tk.END)
        pAcrobatics_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pAcrobatics_Num.get()) - int(pBonus_input.get()))
        pAcrobatics_Num.delete(0, tk.END)
        pAcrobatics_Num.insert(tk.END, isNotProficient)

def slightofHandProfButton():
    if(SlightofHandCB.get()==1):
        isProficient = (int(pSlight_of_Hand_Num.get()) + int(pBonus_input.get()))
        pSlight_of_Hand_Num.delete(0, tk.END)
        pSlight_of_Hand_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pSlight_of_Hand_Num.get()) - int(pBonus_input.get()))
        pSlight_of_Hand_Num.delete(0, tk.END)
        pSlight_of_Hand_Num.insert(tk.END, isNotProficient)

def stealthProfButton():
    if(StealthCB.get()==1):
        isProficient = (int(pStealth_Num.get()) + int(pBonus_input.get()))
        pStealth_Num.delete(0, tk.END)
        pStealth_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pStealth_Num.get()) - int(pBonus_input.get()))
        pStealth_Num.delete(0, tk.END)
        pStealth_Num.insert(tk.END, isNotProficient)

def conProfButton():
    if(ConSavingThrowCB.get()==1):
        isProficient = (int(pCon_ST_Num.get()) + int(pBonus_input.get()))
        pCon_ST_Num.delete(0, tk.END)
        pCon_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pCon_ST_Num.get()) - int(pBonus_input.get()))
        pCon_ST_Num.delete(0, tk.END)
        pCon_ST_Num.insert(tk.END, isNotProficient)

def intProfButton():
    if(IntSavingThrowCB.get()==1):
        isProficient = (int(pInt_ST_Num.get()) + int(pBonus_input.get()))
        pInt_ST_Num.delete(0, tk.END)
        pInt_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pInt_ST_Num.get()) - int(pBonus_input.get()))
        pInt_ST_Num.delete(0, tk.END)
        pInt_ST_Num.insert(tk.END, isNotProficient)

def arcanaProfButton():
    if(ArcanaCB.get()==1):
        isProficient = (int(pArcana_Num.get()) + int(pBonus_input.get()))
        pArcana_Num.delete(0, tk.END)
        pArcana_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pArcana_Num.get()) - int(pBonus_input.get()))
        pArcana_Num.delete(0, tk.END)
        pArcana_Num.insert(tk.END, isNotProficient)

def historyProfButton():
    if(HistoryCB.get()==1):
        isProficient = (int(pHistory_Num.get()) + int(pBonus_input.get()))
        pHistory_Num.delete(0, tk.END)
        pHistory_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pHistory_Num.get()) - int(pBonus_input.get()))
        pHistory_Num.delete(0, tk.END)
        pHistory_Num.insert(tk.END, isNotProficient)

def investigationProfButton():
    if(InvestigationCB.get()==1):
        isProficient = (int(pInvestigation_Num.get()) + int(pBonus_input.get()))
        pInvestigation_Num.delete(0, tk.END)
        pInvestigation_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pInvestigation_Num.get()) - int(pBonus_input.get()))
        pInvestigation_Num.delete(0, tk.END)
        pInvestigation_Num.insert(tk.END, isNotProficient)

def natureProfButton():
    if(NatureCB.get()==1):
        isProficient = (int(pNature_Num.get()) + int(pBonus_input.get()))
        pNature_Num.delete(0, tk.END)
        pNature_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pNature_Num.get()) - int(pBonus_input.get()))
        pNature_Num.delete(0, tk.END)
        pNature_Num.insert(tk.END, isNotProficient)

def religionProfButton():
    if(ReligionCB.get()==1):
        isProficient = (int(pReligion_Num.get()) + int(pBonus_input.get()))
        pReligion_Num.delete(0, tk.END)
        pReligion_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pReligion_Num.get()) - int(pBonus_input.get()))
        pReligion_Num.delete(0, tk.END)
        pReligion_Num.insert(tk.END, isNotProficient)

def wisProfButton():
    if(WisSavingThrowCB.get()==1):
        isProficient = (int(pWis_ST_Num.get()) + int(pBonus_input.get()))
        pWis_ST_Num.delete(0, tk.END)
        pWis_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pWis_ST_Num.get()) - int(pBonus_input.get()))
        pWis_ST_Num.delete(0, tk.END)
        pWis_ST_Num.insert(tk.END, isNotProficient)

def ahProfButton():
    if(AnimalHandlingCB.get()==1):
        isProficient = (int(pAnimal_Handling_Num.get()) + int(pBonus_input.get()))
        pAnimal_Handling_Num.delete(0, tk.END)
        pAnimal_Handling_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pAnimal_Handling_Num.get()) - int(pBonus_input.get()))
        pAnimal_Handling_Num.delete(0, tk.END)
        pAnimal_Handling_Num.insert(tk.END, isNotProficient)

def insightProfButton():
    if(InsightCB.get()==1):
        isProficient = (int(pInsight_Num.get()) + int(pBonus_input.get()))
        pInsight_Num.delete(0, tk.END)
        pInsight_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pInsight_Num.get()) - int(pBonus_input.get()))
        pInsight_Num.delete(0, tk.END)
        pInsight_Num.insert(tk.END, isNotProficient)

def medicineProfButton():
    if(MedicineCB.get()==1):
        isProficient = (int(pMedicine_Num.get()) + int(pBonus_input.get()))
        pMedicine_Num.delete(0, tk.END)
        pMedicine_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pMedicine_Num.get()) - int(pBonus_input.get()))
        pMedicine_Num.delete(0, tk.END)
        pMedicine_Num.insert(tk.END, isNotProficient)

def perceptionProfButton():
    if(PerceptionCB.get()==1):
        isProficient = (int(pPerception_Num.get()) + int(pBonus_input.get()))
        pPerception_Num.delete(0, tk.END)
        pPerception_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pPerception_Num.get()) - int(pBonus_input.get()))
        pPerception_Num.delete(0, tk.END)
        pPerception_Num.insert(tk.END, isNotProficient)

def survivalProfButton():
    if(SurvivalCB.get()==1):
        isProficient = (int(pSurvival_Num.get()) + int(pBonus_input.get()))
        pSurvival_Num.delete(0, tk.END)
        pSurvival_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pSurvival_Num.get()) - int(pBonus_input.get()))
        pSurvival_Num.delete(0, tk.END)
        pSurvival_Num.insert(tk.END, isNotProficient)

def chrProfButton():
    if(ChrSavingThrowCB.get()==1):
        isProficient = (int(pChr_ST_Num.get()) + int(pBonus_input.get()))
        pChr_ST_Num.delete(0, tk.END)
        pChr_ST_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pChr_ST_Num.get()) - int(pBonus_input.get()))
        pChr_ST_Num.delete(0, tk.END)
        pChr_ST_Num.insert(tk.END, isNotProficient)

def deceptionProfButton():
    if(DeceptionCB.get()==1):
        isProficient = (int(pDeception_Num.get()) + int(pBonus_input.get()))
        pDeception_Num.delete(0, tk.END)
        pDeception_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pDeception_Num.get()) - int(pBonus_input.get()))
        pDeception_Num.delete(0, tk.END)
        pDeception_Num.insert(tk.END, isNotProficient)

def intimidationProfButton():
    if(IntimidationCB.get()==1):
        isProficient = (int(pIntimidation_Num.get()) + int(pBonus_input.get()))
        pIntimidation_Num.delete(0, tk.END)
        pIntimidation_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pIntimidation_Num.get()) - int(pBonus_input.get()))
        pIntimidation_Num.delete(0, tk.END)
        pIntimidation_Num.insert(tk.END, isNotProficient)

def performanceProfButton():
    if(PerformanceCB.get()==1):
        isProficient = (int(pPerformance_Num.get()) + int(pBonus_input.get()))
        pPerformance_Num.delete(0, tk.END)
        pPerformance_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pPerformance_Num.get()) - int(pBonus_input.get()))
        pPerformance_Num.delete(0, tk.END)
        pPerformance_Num.insert(tk.END, isNotProficient)

def persuasionProfButton():
    if(PersuasionCB.get()==1):
        isProficient = (int(pPersuasion_Num.get()) + int(pBonus_input.get()))
        pPersuasion_Num.delete(0, tk.END)
        pPersuasion_Num.insert(tk.END, isProficient)
    else:
        isNotProficient = (int(pPersuasion_Num.get()) - int(pBonus_input.get()))
        pPersuasion_Num.delete(0, tk.END)
        pPersuasion_Num.insert(tk.END, isNotProficient)





window = tk.Tk()
window.title("Character Sheet")


notebook = ttk.Notebook(window)


dndPlayerSheet = tk.Label(notebook, background="grey")
dndSpellSheet = tk.Label(notebook)
dndMonsterSheet = tk.Label(notebook)

notebook.add(dndPlayerSheet, text = "Playercard")
notebook.add(dndSpellSheet, text = "Spell Sheet")
notebook.add(dndMonsterSheet, text = "Monster Data")

notebook.pack(expand=True, fill="both")


########################################################################################################################
#Checkbox variables
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
pInpiration = tk.Checkbutton(stats_Frame, text="Inspiration")
pInpiration.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

#Character Strength Stats
pStrength_Frame = tk.LabelFrame(stats_Frame, text="Strength")
pStrength_Frame.grid(row=2, column=0, columnspan=2, padx=10, pady=2)

pRolls = tk.Button(pStrength_Frame, text = "Roll")
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

pRolld = tk.Button(pDexterity_Frame, text = "Roll")
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

pRollcon = tk.Button(pConstitution_Frame, text = "Roll")
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

pRolli = tk.Button(pIntelligence_Frame, text = "Roll")
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

pRollw = tk.Button(pWisdom_Frame, text = "Roll")
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

pRollc = tk.Button(pCharisma_Frame, text = "Roll")
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

pInitiative = tk.Label(ac_i_s_Frame, text="Initiative")
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
hpm_label.grid(row=0, column=0, sticky="E")
hpm_label_input = tk.Entry(hitPoint_Frame, width=4)
hpm_label_input.grid(row=0, column=1, sticky="W")
chp_input = tk.Entry(hitPoint_Frame, width=4, font=("", 64))
chp_input.grid(row=1, column=0, columnspan=2, padx=86)
chp_label = tk.Label(hitPoint_Frame, text="Current Hit Points")
chp_label.grid(row=2, column=0, columnspan=2)

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

pWeapon1AttackButton = tk.Button(playerWeapon1, text="Attack")
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

pWeapon2AttackButton = tk.Button(playerWeapon2, text="Attack")
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


openInfoFile()

window.mainloop()
