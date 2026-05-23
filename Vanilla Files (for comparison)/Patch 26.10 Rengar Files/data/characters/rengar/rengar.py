#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Spells/RengarEEmpAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp"
            "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmpMis"
        }
        mName: string = "RengarEEmpAbility"
    }
    "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmpMis" = SpellObject {
        ObjectName: string = "RengarEEmpMis"
        mScriptName: string = "RengarEEmpMis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarE"
            mCoefficient: f32 = 0.7
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E_Emp.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0.25
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                9
                9
                9
                9
                9
                9
                9
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 70
                movementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "head"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1500
                }
                heightSolver: pointer = BlendedLinearHeightSolver {}
                verticalFacing: pointer = VerticalFacingFaceTarget {}
                behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mMissileEffectKey: hash = "Rengar_E_Max_Mis"
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
    }
    "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp" = SpellObject {
        ObjectName: string = "RengarEEmp"
        mScriptName: string = "RengarEEmp"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarE"
            mSpellTags: list[string] = {
                "Trait_ImmobilizingCCSpell"
            }
            mCoefficient: f32 = 0.8
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E_Emp.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0.25
            cooldownTime: list[f32] = {
                0.4
                0.4
                0.4
                0.4
                0.4
                0.4
                0.4
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarEAbility/RengarE"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarEEmp"
        }
    }
    "Characters/Rengar/Spells/RengarRAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarRAbility/RengarR"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarRAbility/RengarR"
        }
        mLifetimeManuallyManaged: bool = true
        mName: string = "RengarRAbility"
        mType: u8 = 2
        AbilityTraits: u32 = 128
    }
    "Characters/Rengar/Spells/RengarQAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
            "Characters/Rengar/Spells/RengarQAbility/RengarQEmpASBuff"
        }
        mName: string = "RengarQAbility"
    }
    0x254b0092 = SpellObject {
        ObjectName: string = "RengarHatredReward"
        mScriptName: string = "RengarHatredReward"
        mSpell: pointer = SpellDataResource {
            ImgIconPath: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntVictoryR"
        }
    }
    0x2aa33976 = SpellObject {
        ObjectName: string = "RengarHatredWins"
        mScriptName: string = "RengarHatredWins"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntVictoryR"
        }
    }
    "Characters/Rengar/Spells/RengarRShred" = SpellObject {
        ObjectName: string = "RengarRShred"
        mScriptName: string = "RengarRShred"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarRShred"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff5" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff5"
        mScriptName: string = "RengarPassiveBonetoothBuff5"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff5"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff4" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff4"
        mScriptName: string = "RengarPassiveBonetoothBuff4"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff4"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff3" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff3"
        mScriptName: string = "RengarPassiveBonetoothBuff3"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff3"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff2" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff2"
        mScriptName: string = "RengarPassiveBonetoothBuff2"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff2"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff1" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff1"
        mScriptName: string = "RengarPassiveBonetoothBuff1"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff1"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarQSound" = SpellObject {
        ObjectName: string = "RengarQSound"
        mScriptName: string = "RengarQSound"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                ""
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 2.3666
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                2000
                                2000
                                2000
                                2000
                                2000
                                2000
                            }
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionRange {
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1100
                                1100
                                1100
                                1100
                                1100
                                1100
                            }
                            mValueType: u32 = 1
                        }
                        textureOverrideName: string = "ASSETS/Spells/Textures/CircularRangeIndicator_Dark.tex"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
    }
    "Characters/Rengar/Spells/RengarRBuff" = SpellObject {
        ObjectName: string = "RengarRBuff"
        mScriptName: string = "RengarRBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmpASBuff"
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBuff" = SpellObject {
        ObjectName: string = "RengarPassiveBuff"
        mScriptName: string = "RengarPassiveBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBuff"
        }
    }
    "Characters/Rengar/Spells/RengarWAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarWAbility/RengarW"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarWAbility/RengarW"
            "Characters/Rengar/Spells/RengarWAbility/RengarWEmp"
        }
        mName: string = "RengarWAbility"
    }
    "Characters/Rengar/Spells/RengarWAbility/RengarWEmp" = SpellObject {
        ObjectName: string = "RengarWEmp"
        mScriptName: string = "RengarWEmp"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarW"
            mSpellTags: list[string] = {
                "SpecialCase_StasisLocked"
            }
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_W_Emp.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoCountHiddenInUI: bool = true
            cannotBeSuppressed: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 7.5
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarWAbility/RengarW"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarWEmp"
        }
    }
    "Characters/Rengar/Spells/RengarWAbility/RengarW" = SpellObject {
        ObjectName: string = "RengarW"
        mScriptName: string = "RengarW"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarW"
            mSpellTags: list[string] = {
                "SpecialCase_StasisLocked"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    name: string = "BaseDamage"
                    values: list[f32] = {
                        20
                        50
                        80
                        110
                        140
                        170
                        200
                    }
                }
                SpellDataValue {
                    name: string = "DamagePercentageHealed"
                    values: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellDataValue {
                    name: string = "APRatio"
                    values: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
                SpellDataValue {
                    name: string = "EmpoweredAPRatio"
                    values: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
                SpellDataValue {
                    name: string = "HealingWindow"
                    values: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellDataValue {
                    name: string = "CCImmuneDuration"
                    values: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellDataValue {
                    name: string = "MonsterHealingMod"
                    values: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BaseDamage"
                            values: list[f32] = {
                                20
                                60
                                100
                                140
                                180
                                220
                                260
                            }
                        }
                        SpellDataValue {
                            name: string = "DamagePercentageHealed"
                            values: list[f32] = {
                                60
                                60
                                60
                                60
                                60
                                60
                                60
                            }
                        }
                        SpellDataValue {
                            name: string = "APRatio"
                            values: list[f32] = {
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                                0.95
                            }
                        }
                        SpellDataValue {
                            name: string = "EmpoweredAPRatio"
                            values: list[f32] = {
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                                1.05
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "BonusMonsterDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelInterpolationCalculationPart {
                            mStartValue: f32 = 65
                            mEndValue: f32 = 130
                        }
                    }
                }
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mDataValue: hash = "APRatio"
                        }
                    }
                }
                "TotalDamageEmpowered" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelFormulaCalculationPart {
                            values: list[f32] = {
                                0
                                50
                                60
                                70
                                80
                                90
                                100
                                110
                                120
                                130
                                140
                                150
                                160
                                170
                                180
                                190
                                200
                                210
                                220
                                230
                                240
                                250
                                260
                                270
                                280
                                290
                                300
                                310
                                320
                                330
                                340
                            }
                        }
                        StatByNamedDataValueCalculationPart {
                            mDataValue: hash = "EmpoweredAPRatio"
                        }
                    }
                }
            }
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_W.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                22
                16
                14.5
                13
                11.5
                10
                10
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 7.5
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarW"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarW_Name"
                        "keySummary" = "Spell_RengarW_Summary"
                        "keyTooltip" = "Spell_RengarW_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarW_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "BaseDamage"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "AmmoRechargeTime"
                                    nameOverride: string = "Spell_ListType_Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 1
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 8
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 2
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 2097152
                    EffectCalculation: pointer = GameCalculation {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQ" = SpellObject {
        ObjectName: string = "RengarQ"
        mScriptName: string = "RengarQ"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "Trait_AttackReset"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    name: string = "BaseDamage"
                    values: list[f32] = {
                        -15
                        20
                        55
                        90
                        125
                        160
                        195
                    }
                }
                SpellDataValue {
                    name: string = "BaseADRatio"
                    values: list[f32] = {
                        0.05
                        0.05
                        0.05
                        0.05
                        0.05
                        0.05
                        0.05
                    }
                }
                SpellDataValue {
                    name: string = "BaseADRatioTooltip"
                    values: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellDataValue {
                    name: string = "EmpoweredADRatio"
                    values: list[f32] = {
                        0.2
                        0.2
                        0.2
                        0.2
                        0.2
                        0.2
                        0.2
                    }
                }
                SpellDataValue {
                    name: string = "TowerMod"
                    values: list[f32] = {
                        0.6
                        0.6
                        0.6
                        0.6
                        0.6
                        0.6
                        0.6
                    }
                }
                SpellDataValue {
                    name: string = "ASDuration"
                    values: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellDataValue {
                    name: string = "ASBonus"
                    values: list[f32] = {
                        40
                        40
                        40
                        40
                        40
                        40
                        40
                    }
                }
                SpellDataValue {
                    name: string = "BuffDuration"
                    values: list[f32] = {
                        3
                        3
                        3
                        3
                        3
                        3
                        3
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BaseDamage"
                            values: list[f32] = {
                                0
                                40
                                80
                                120
                                160
                                200
                                240
                            }
                        }
                        SpellDataValue {
                            name: string = "BaseADRatio"
                            values: list[f32] = {
                                0
                                0.05
                                0.1
                                0.15
                                0.2
                                0.25
                                0.3
                            }
                        }
                        SpellDataValue {
                            name: string = "EmpoweredADRatio"
                            values: list[f32] = {
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                                0.55
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalADRatio"
                            values: list[f32] = {
                                1
                                1.05
                                1.1
                                1.15
                                1.2
                                1.25
                                1.3
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalEmpoweredADRatio"
                            values: list[f32] = {
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                                1.55
                            }
                        }
                    }
                }
                "ARAM" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BaseADRatio"
                            values: list[f32] = {
                                0.0625
                                0.1
                                0.1375
                                0.175
                                0.2125
                                0.25
                                0.2875
                            }
                        }
                        SpellDataValue {
                            name: string = "EmpoweredADRatio"
                            values: list[f32] = {
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalADRatio"
                            values: list[f32] = {
                                0.0625
                                0.1
                                0.1375
                                0.175
                                0.2125
                                0.25
                                0.2875
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalEmpoweredADRatio"
                            values: list[f32] = {
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                            }
                        }
                    }
                }
                0xbffdf499 = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BaseADRatio"
                            values: list[f32] = {
                                0.0625
                                0.1
                                0.1375
                                0.175
                                0.2125
                                0.25
                                0.2875
                            }
                        }
                        SpellDataValue {
                            name: string = "EmpoweredADRatio"
                            values: list[f32] = {
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                                0.4
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalADRatio"
                            values: list[f32] = {
                                1.0625
                                1.1
                                1.1375
                                1.175
                                1.2125
                                1.25
                                1.2875
                            }
                        }
                        SpellDataValue {
                            name: string = "TotalEmpoweredADRatio"
                            values: list[f32] = {
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                                1.4
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "EmpoweredQAS" = GameCalculation {
                    mMultiplier: pointer = NumberCalculationPart {
                        mNumber: f32 = 0.01
                    }
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 50
                            mInitialBonusPerLevel: f32 = 3
                        }
                    }
                    mDisplayAsPercent: bool = true
                }
                "QBonusDamage" = GameCalculation {
                    mSimpleTooltipCalculationDisplay: u8 = 5
                    0x72c5c2a8: u32 = 0
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "BaseADRatio"
                        }
                    }
                }
                0xd4a43abe = GameCalculation {
                    0x72c5c2a8: u32 = 0
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 35
                            mInitialBonusPerLevel: f32 = 15
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 9
                                    mBonusPerLevelAtAndAfter: f32 = 10
                                }
                            }
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "EmpoweredADRatio"
                        }
                    }
                }
                0x95c7ca04 = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        SumOfSubPartsCalculationPart {
                            mSubparts: list[pointer] = {
                                ProductOfSubPartsCalculationPart {
                                    mPart1: pointer = 0xf3cbe7b2 {
                                        mSpellCalculationKey: hash = "QBonusDamage"
                                    }
                                    mPart2: pointer = NamedDataValueCalculationPart {
                                        mDataValue: hash = "TowerMod"
                                    }
                                }
                            }
                        }
                    }
                }
                0xf2ca2500 = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        SumOfSubPartsCalculationPart {
                            mSubparts: list[pointer] = {
                                ProductOfSubPartsCalculationPart {
                                    mPart1: pointer = 0xf3cbe7b2 {
                                        mSpellCalculationKey: hash = 0xd4a43abe
                                    }
                                    mPart2: pointer = NamedDataValueCalculationPart {
                                        mDataValue: hash = "TowerMod"
                                    }
                                }
                            }
                        }
                    }
                }
                "QTotalDamage" = GameCalculation {
                    mSimpleTooltipCalculationDisplay: u8 = 6
                    tooltipOnly: bool = true
                    0x72c5c2a8: u32 = 0
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mCoefficient: f32 = 1
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "BaseADRatio"
                        }
                    }
                }
                "EmpoweredQTotalDamage" = GameCalculation {
                    mSimpleTooltipCalculationDisplay: u8 = 6
                    tooltipOnly: bool = true
                    0x72c5c2a8: u32 = 0
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 35
                            mInitialBonusPerLevel: f32 = 15
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 9
                                    mBonusPerLevelAtAndAfter: f32 = 10
                                }
                            }
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mCoefficient: f32 = 1
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mDataValue: hash = "EmpoweredADRatio"
                        }
                    }
                }
            }
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQ.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                6
                6
                5.5
                5
                4.5
                4
                3.5
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarQ"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarQ_Name"
                        "keySummary" = "Spell_RengarQ_Summary"
                        "keyTooltip" = "Spell_RengarQ_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtended" = "Spell_RengarQ_TooltipExtended"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "BaseDamage"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "AmmoRechargeTime"
                                    nameOverride: string = "Spell_ListType_Cooldown"
                                }
                            }
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
            mBuffAttributeFlag: u8 = 32
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {}
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmpASBuff" = SpellObject {
        ObjectName: string = "RengarQEmpASBuff"
        mScriptName: string = "RengarQEmpASBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmpASBuff"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmpAttack" = SpellObject {
        ObjectName: string = "RengarQEmpAttack"
        mScriptName: string = "RengarQEmpAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    value: list[f32] = {
                        10
                        30
                        50
                        70
                        90
                        110
                        130
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                        0.3
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        350
                        350
                        350
                        350
                        350
                        350
                        350
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        90
                        90
                        90
                        90
                        90
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        150
                        150
                        150
                        150
                        150
                        150
                        150
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                        0.15
                    }
                }
                SpellEffectAmount {
                    value: list[f32] = {
                        0.1
                        0.2
                        0.3
                        0.4
                        0.5
                        0.6
                        0.7
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.5
            mCoefficient2: f32 = 0.9
            mAnimationName: string = "Attack4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQEmp.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mApplyAttackDamage: bool = true
            mApplyAttackEffect: bool = true
            mDisableCastBar: bool = true
            alwaysSnapFacing: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            mConsideredAsAutoAttack: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8.5
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            mHitEffectName: string = "DATA/Shared/Particles/globalhit_yellow_tar.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.tex"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                625
                                625
                                625
                                625
                                625
                                625
                            }
                            mValueType: u32 = 2
                        }
                        textureBaseOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileBase_Dark.tex"
                        textureTargetOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileTarget_Dark.tex"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQAttack" = SpellObject {
        ObjectName: string = "RengarQAttack"
        mScriptName: string = "RengarQAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mAnimationName: string = "Attack4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQ.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            mAmmoCountHiddenInUI: bool = true
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mApplyAttackDamage: bool = true
            mApplyAttackEffect: bool = true
            mDisableCastBar: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            mConsideredAsAutoAttack: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                325
                325
                325
                325
                325
                325
                325
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8.5
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            mHitEffectName: string = "DATA/Shared/Particles/globalhit_yellow_tar.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.tex"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        alwaysDraw: bool = true
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                625
                                625
                                625
                                625
                                625
                                625
                            }
                            mValueType: u32 = 2
                        }
                        textureBaseOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileBase_Dark.tex"
                        textureTargetOverrideName: string = "ASSETS/Spells/Textures/LocalLineMissileTarget_Dark.tex"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarQAbility/RengarQEmp" = SpellObject {
        ObjectName: string = "RengarQEmp"
        mScriptName: string = "RengarQEmp"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
                "Trait_AttackReset"
            }
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/RengarQEmp.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            mDisableCastBar: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                mUseTooltipFromAnotherSpell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQEmp"
            mBuffAttributeFlag: u8 = 32
        }
    }
    0x62b7fb36 = SpellObject {
        ObjectName: string = "RengarHatredDefeat"
        mScriptName: string = "RengarHatredDefeat"
        mSpell: pointer = SpellDataResource {
            ImgIconPath: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_KhazixHuntDefeatK"
        }
    }
    0x77cee58a = SpellObject {
        ObjectName: string = "RengarHatredGoTime"
        mScriptName: string = "RengarHatredGoTime"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_VolibearHatredZilean"
        }
    }
    "Characters/Rengar/Spells/RengarEAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarEAbility/RengarE"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarEAbility/RengarE"
            "Characters/Rengar/Spells/RengarEAbility/RengarEMis"
        }
        mName: string = "RengarEAbility"
    }
    "Characters/Rengar/Spells/RengarEAbility/RengarE" = SpellObject {
        ObjectName: string = "RengarE"
        mScriptName: string = "RengarE"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarE"
            mSpellTags: list[string] = {
                "Trait_SwapsIntoImmobilizingCCSpell"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    name: string = "RevealDuration"
                    values: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellDataValue {
                    name: string = "BaseDamage"
                    values: list[f32] = {
                        10
                        55
                        100
                        145
                        190
                        235
                        280
                    }
                }
                SpellDataValue {
                    name: string = "SlowAmount"
                    values: list[f32] = {
                        15
                        30
                        45
                        60
                        75
                        90
                        105
                    }
                }
                SpellDataValue {
                    name: string = "CCDuration"
                    values: list[f32] = {
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                        1.75
                    }
                }
                SpellDataValue {
                    name: string = "BonusADRatio"
                    values: list[f32] = {
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                        0.8
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "ARAM" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BonusADRatio"
                            values: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                        }
                    }
                }
                0xbffdf499 = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "BonusADRatio"
                            values: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "baseDamage"
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mDataValue: hash = "BonusADRatio"
                        }
                    }
                }
                "TotalEmpoweredDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 50
                            mInitialBonusPerLevel: f32 = 15
                        }
                        StatByNamedDataValueCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mDataValue: hash = "BonusADRatio"
                        }
                    }
                }
            }
            mCoefficient: f32 = 0.8
            mCoefficient2: f32 = 0.6
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0.25
            cooldownTime: list[f32] = {
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
                0.25
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                10
                10
                10
                10
                10
                10
                10
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mCastingBreaksStealth: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarE"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarE_Name"
                        "keySummary" = "Spell_RengarE_Summary"
                        "keyTooltip" = "Spell_RengarE_Tooltip"
                        "keyCooldown" = "Spell_AmmoRecharge_As_Cooldown"
                        "keyCost" = "Spell_RengarQWE_Cost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarE_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 5
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "BaseDamage"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    type: string = "SlowAmount"
                                    typeIndex: i32 = 2
                                    nameOverride: string = "Spell_ListType_Slow"
                                    Style: u32 = 1
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 1
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 3
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 4096
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 3
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 32768
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NumberCalculationPart {
                                mNumber: f32 = 70
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 2048
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4096
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 8192
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarEAbility/RengarEMis" = SpellObject {
        ObjectName: string = "RengarEMis"
        mScriptName: string = "RengarEMis"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarE"
            mCoefficient: f32 = 0.7
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_E.dds"
            }
            mCastTime: f32 = 0.25
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0.25
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                9
                9
                9
                9
                9
                9
                9
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 70
                movementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "head"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 1500
                }
                heightSolver: pointer = BlendedLinearHeightSolver {}
                verticalFacing: pointer = VerticalFacingFaceTarget {}
                behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            castFrame: f32 = 8.5
            missileSpeed: f32 = 1500
            mMissileEffectKey: hash = "Rengar_E_Mis"
            mLineWidth: f32 = 70
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        hideWithLineIndicator: bool = true
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        endLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                        }
                        lineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                70
                                70
                                70
                                70
                                70
                                70
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarE"
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack" = SpellObject {
        ObjectName: string = "RengarBasicAttack"
        mScriptName: string = "RengarBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            0x11704a2b: f32 = 0.413
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothManager" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothManager"
        mScriptName: string = "RengarPassiveBonetoothManager"
    }
    "Characters/Rengar/Spells/RengarPassiveBuffDash" = SpellObject {
        ObjectName: string = "RengarPassiveBuffDash"
        mScriptName: string = "RengarPassiveBuffDash"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6826
            mAlternateName: string = "RengarPassiveBuffDash"
            mSpellTags: list[string] = {
                "PositiveEffect_MoveBlock"
            }
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Passive.dds"
            }
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            canCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mCantCancelWhileWindingUpTargetingChampion: bool = true
            mChannelIsInterruptedByDisables: bool = false
            mChannelIsInterruptedByAttacking: bool = false
            mSpellRevealsChampion: bool = false
            mCanMoveWhileChanneling: bool = true
            mShowChannelBar: bool = false
            mOverrideAttackTime: pointer = OverrideAttackTimeData {
                mTotalAttackTimeSecs: pointer = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NumberCalculationPart {}
                    }
                }
            }
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castConeDistance: f32 = 100
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuff" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuff"
        mScriptName: string = "RengarPassiveBonetoothBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuff"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveEmpowered" = SpellObject {
        ObjectName: string = "RengarPassiveEmpowered"
        mScriptName: string = "RengarPassiveEmpowered"
    }
    0xa05f165c = SpellObject {
        ObjectName: string = "RengarRPassive"
        mScriptName: string = "RengarRPassive"
    }
    "Characters/Rengar/Spells/RengarRAbility/RengarR" = SpellObject {
        ObjectName: string = "RengarR"
        mScriptName: string = "RengarR"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mSpellTags: list[string] = {
                "Trait_Ultimate"
            }
            DataValues: list2[embed] = {
                SpellDataValue {
                    name: string = "StealthDuration"
                    values: list[f32] = {
                        8
                        12
                        16
                        20
                        24
                        28
                        32
                    }
                }
                SpellDataValue {
                    name: string = "EnemyDetectionRange"
                    values: list[f32] = {
                        1600
                        1600
                        1600
                        1600
                        1600
                        1600
                        1600
                    }
                }
                SpellDataValue {
                    name: string = "SelfVisionRange"
                    values: list[f32] = {
                        2000
                        2500
                        3000
                        3500
                        4000
                        4500
                        5000
                    }
                }
                SpellDataValue {
                    name: string = "SelfRevealRange"
                    values: list[f32] = {
                        750
                        750
                        750
                        750
                        750
                        750
                        750
                    }
                }
                SpellDataValue {
                    name: string = "StealthMS"
                    values: list[f32] = {
                        30
                        40
                        50
                        60
                        70
                        80
                        90
                    }
                }
                SpellDataValue {
                    name: string = "FadeTime"
                    values: list[f32] = {
                        2
                        2
                        2
                        2
                        2
                        2
                        2
                    }
                }
                SpellDataValue {
                    name: string = "ArmorShred"
                    values: list[f32] = {
                        10
                        15
                        20
                        25
                        30
                        35
                        40
                    }
                }
                SpellDataValue {
                    name: string = "ArmorShredDuration"
                    values: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    name: string = "LeapRange"
                    values: list[f32] = {
                        725
                        725
                        725
                        725
                        725
                        725
                        725
                    }
                }
            }
            DataValuesModeOverride: map[hash,embed] = {
                "cherry" = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            name: string = "StealthMS"
                            values: list[f32] = {
                                30
                                50
                                70
                                90
                                110
                                130
                                150
                            }
                        }
                    }
                }
            }
            0xf9c2333e: map[hash,embed] = {
                "cherry" = SpellEffectAmount {
                    value: list[f32] = {
                        80
                        80
                        70
                        60
                        50
                        40
                        30
                    }
                }
                "ARAM" = SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        80
                        70
                        70
                        70
                        70
                    }
                }
                0xa110bc47 = SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        75
                        60
                        60
                        60
                        60
                    }
                }
                0xbffdf499 = SpellEffectAmount {
                    value: list[f32] = {
                        90
                        90
                        80
                        70
                        70
                        70
                        70
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "BonusDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mCoefficient: f32 = 1
                        }
                    }
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_R.dds"
            }
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 2.3666
            cooldownTime: list[f32] = {
                100
                100
                90
                80
                80
                80
                80
            }
            mCantCancelWhileWindingUp: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                2500
                2500
                3000
                3500
                2500
                2500
                2500
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarR"
                    mFormat: link = 0xd7c27163
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarR_Name"
                        "keySummary" = "Spell_RengarR_Summary"
                        "keyTooltip" = "Spell_RengarR_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                        "keyTooltipExtendedBelowLine" = "Spell_RengarR_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            levelCount: u32 = 3
                            elements: list[embed] = {
                                TooltipInstanceListElement {
                                    type: string = "ArmorShred"
                                    typeIndex: i32 = 8
                                    nameOverride: string = "Spell_ListType_ArmorReduction"
                                }
                                TooltipInstanceListElement {
                                    type: string = "StealthDuration"
                                    typeIndex: i32 = 2
                                    nameOverride: string = "Spell_ListType_Duration"
                                }
                                TooltipInstanceListElement {
                                    type: string = "StealthMS"
                                    typeIndex: i32 = 1
                                    nameOverride: string = "Spell_ListType_MovementSpeed"
                                    Style: u32 = 1
                                }
                                TooltipInstanceListElement {
                                    type: string = "SelfVisionRange"
                                    typeIndex: i32 = 9
                                    nameOverride: string = "Spell_ListType_RengarTrackingRange"
                                }
                                TooltipInstanceListElement {
                                    type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarR"
        }
        BotData: pointer = BotsSpellData {
            DamageTag: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        mSpellCalculationKey: hash = "BonusDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    EffectTag: u32 = 2
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "StealthMS"
                            }
                        }
                    }
                }
                0xb09016f6 {
                    EffectTag: u32 = 1024
                    EffectCalculation: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = "StealthDuration"
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0xe38f54f7: u32 = 1
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 4
                    0x0717e686: bool = false
                }
                0x150d1b92 {
                    0xe38f54f7: u32 = 1024
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveEmpoweredMS" = SpellObject {
        ObjectName: string = "RengarPassiveEmpoweredMS"
        mScriptName: string = "RengarPassiveEmpoweredMS"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveEmpoweredMS"
        }
    }
    "Characters/Rengar/Spells/RengarQEmpowered" = SpellObject {
        ObjectName: string = "RengarQEmpowered"
        mScriptName: string = "RengarQEmpowered"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "RengarQ"
            mSpellTags: list[string] = {
                "PositiveEffect_EmpowerAttack"
            }
            mCoefficient: f32 = 0.6
            mCoefficient2: f32 = 0.4
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_Q.dds"
            }
            mCastTime: f32 = 0.2
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 0.25
            cooldownTime: list[f32] = {
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
                0.5
            }
            mMaxAmmo: list[i32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            mAmmoRechargeTime: list[f32] = {
                0.1
                0.1
                0.1
                0.1
                0.1
                0.1
                0.1
            }
            mAmmoCountHiddenInUI: bool = true
            mCantCancelWhileWindingUp: bool = true
            alwaysSnapFacing: bool = true
            useAnimatorFramerate: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            castRangeDisplayOverride: list[f32] = {
                450
                450
                450
                450
                450
                450
                450
            }
            castRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            castConeAngle: f32 = 90
            castConeDistance: f32 = 325
            castFrame: f32 = 8
            missileSpeed: f32 = 3000
            mLineWidth: f32 = 55
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        centerLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        textureOrientation: u32 = 3
                        constraintPosLocator: embed = DrawablePositionLocator {
                            basePosition: u32 = 3
                            orientationType: u32 = 2
                        }
                        overrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                325
                                325
                                325
                                325
                                325
                                325
                            }
                        }
                        textureRadiusOverrideName: string = "ASSETS/Spells/Textures/SemicircleRangeIndicator.tex"
                    }
                    TargeterDefinitionLine {
                        startLocator: embed = DrawablePositionLocator {
                            orientationType: u32 = 3
                        }
                        endLocator: embed = DrawablePositionLocator {
                            distanceOffset: f32 = 450
                            orientationType: u32 = 3
                        }
                        fallbackDirection: u32 = 3
                        lineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                75
                                75
                                75
                                75
                                75
                                75
                            }
                            mValueType: u32 = 2
                        }
                        overrideBaseRange: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                450
                                450
                                450
                                450
                                450
                                450
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarQ"
        }
    }
    "Characters/Rengar/Spells/RengarRSpeed" = SpellObject {
        ObjectName: string = "RengarRSpeed"
        mScriptName: string = "RengarRSpeed"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                mObjectTagList: list2[hash] = {
                    "champion"
                }
            }
            mAlternateName: string = "RengarR"
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1"
            0x11704a2b: f32 = 0.25
            0xf26881a0: f32 = 2.3666
            cooldownTime: list[f32] = {
                175
                140
                105
                70
                11
                11
                11
            }
            mCantCancelWhileWindingUp: bool = true
            mUseMinimapTargeting: bool = true
            bIsToggleSpell: bool = true
            castRange: list[f32] = {
                1000
                2000
                3000
                4000
                2000
                2000
                3000
            }
            castRadius: list[f32] = {
                75
                75
                75
                75
                75
                75
                75
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 0.145
            missileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionMinimap {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarRSpeed"
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack3" = SpellObject {
        ObjectName: string = "RengarBasicAttack3"
        mScriptName: string = "RengarBasicAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Attack3"
            0x11704a2b: f32 = 0.413
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarBasicAttack2" = SpellObject {
        ObjectName: string = "RengarBasicAttack2"
        mScriptName: string = "RengarBasicAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Attack2"
            0x11704a2b: f32 = 0.413
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.4
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    0xddd932f3 = SpellObject {
        ObjectName: string = "RengarCombatTracker"
        mScriptName: string = "RengarCombatTracker"
    }
    "Characters/Rengar/Spells/RengarPassiveBonetoothBuffKhazix" = SpellObject {
        ObjectName: string = "RengarPassiveBonetoothBuffKhazix"
        mScriptName: string = "RengarPassiveBonetoothBuffKhazix"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassiveBonetoothBuffKhazix"
            mBuffAttributeFlag: u8 = 8
        }
    }
    "Characters/Rengar/Spells/RengarPassiveAbility" = AbilityObject {
        mRootSpell: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        mChildSpells: list[link] = {
            "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        }
        mName: string = "RengarPassiveAbility"
        mType: u8 = 3
    }
    "Characters/Rengar/Spells/RengarCritAttack" = SpellObject {
        ObjectName: string = "RengarCritAttack"
        mScriptName: string = "RengarCritAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7375
            mAnimationName: string = "Crit"
            0x11704a2b: f32 = 0.413
            cooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            bHaveHitEffect: bool = true
            castRange: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            castConeDistance: f32 = 100
            castFrame: f32 = 8.4
            missileSpeed: f32 = 0
            mHitEffectKey: hash = "Rengar_BA_tar_crit_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveAttack" = SpellObject {
        ObjectName: string = "RengarPassiveAttack"
        mScriptName: string = "RengarPassiveAttack"
        mSpell: pointer = SpellDataResource {
            flags: u32 = 4
            mAffectsTypeFlags: u32 = 6826
            mSpellTags: list[string] = {
                "Trait_AttackReset"
            }
            mAnimationName: string = ""
            0x11704a2b: f32 = 0
            0xf26881a0: f32 = 0
            mChannelIsInterruptedByAttacking: bool = false
            mApplyAttackDamage: bool = true
            mApplyAttackEffect: bool = true
            mConsideredAsAutoAttack: bool = true
            castRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
        }
    }
    "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive" = SpellObject {
        ObjectName: string = "RengarPassive"
        mScriptName: string = "RengarPassive"
        mSpell: pointer = SpellDataResource {
            DataValues: list2[embed] = {
                SpellDataValue {
                    name: string = "MaxFerocity"
                    values: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    name: string = "InCombatTimer"
                    values: list[f32] = {
                        10
                        10
                        10
                        10
                        10
                        10
                        10
                    }
                }
                SpellDataValue {
                    name: string = "InCombatTimerVisual"
                    values: list[f32] = {
                        10
                        10
                        10
                        10
                        10
                        10
                        10
                    }
                }
                SpellDataValue {
                    name: string = "EmpoweredMSDuration"
                    values: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellDataValue {
                    name: string = "RengarPassiveRangeIncrease"
                    values: list[f32] = {
                        620
                        620
                        620
                        620
                        620
                        620
                        620
                    }
                }
                SpellDataValue {
                    name: string = "LeapFerocityGeneration"
                    values: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
                SpellDataValue {
                    name: string = "BonusLeapRange"
                    values: list[f32] = {
                        620
                        620
                        620
                        620
                        620
                        620
                        620
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "EmpoweredMS" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 0.3
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 7
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 13
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 19
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                                Breakpoint {
                                    mLevel: u32 = 25
                                    mAdditionalBonusAtThisLevel: f32 = 0.1
                                }
                            }
                        }
                    }
                    mDisplayAsPercent: bool = true
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_P.dds"
            }
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
                0
            }
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "RengarPassive"
                    mFormat: link = 0x476ec0b8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_RengarPassive_Name"
                        "keyTooltip" = "Spell_RengarPassive_Tooltip"
                        "keyTooltipExtended" = "Spell_RengarPassive_TooltipExtended"
                        "keySummary" = "Spell_RengarPassive_Summary"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RengarPassive"
        }
    }
    0xfdf22d51 = SpellObject {
        ObjectName: string = "RengarRBonusDamage"
        mScriptName: string = "RengarRBonusDamage"
    }
    0x4f9cd28b = StatStoneSet {
        name: string = "stat_stone_set_name_1"
        catalogEntry: embed = catalogEntry {
            contentId: string = "5e16e630-e328-480e-857a-f4625eec5add"
            itemID: u32 = 66600094
        }
        statStones: list[link] = {
            0x176cfeb2
            0xf7ea7750
            0xd859dffb
        }
    }
    0x176cfeb2 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarRKills"
        catalogEntry: embed = catalogEntry {
            contentId: string = "ce658030-b956-47fd-b78b-c21a39ccb397"
            itemID: u32 = 3166
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarRKills"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x024e22b2
        Milestones: list[u64] = {
            6
            15
            30
            35
            45
            20
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarRKills"
    }
    0xd859dffb = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarCCWCancels"
        catalogEntry: embed = catalogEntry {
            contentId: string = "add97e64-dd42-4a99-b118-24befd1b17d5"
            itemID: u32 = 196
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarCCWCancels"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            7
            20
            35
            45
            55
            20
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarCCWCancels"
    }
    0xf7ea7750 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarQuickP"
        catalogEntry: embed = catalogEntry {
            contentId: string = "1c5890f6-8d0e-4f7b-839e-23fd9ac64267"
            itemID: u32 = 194
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarQuickP"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            1
            3
            6
            8
            9
            4
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarQuickP"
    }
    0x509cd41e = StatStoneSet {
        name: string = "stat_stone_set_name_2"
        catalogEntry: embed = catalogEntry {
            contentId: string = "6211bd8a-b2f1-4ff8-92de-980869235029"
            itemID: u32 = 66600467
        }
        statStones: list[link] = {
            0x756274ee
            0xc1e0cd13
            0xdb172aa8
        }
    }
    0xdcc9c9f3 = StatStoneSet {
        name: string = "stat_stone_set_name_starter"
        catalogEntry: embed = catalogEntry {
            contentId: string = "18696f82-140d-44aa-a421-da317e5464ae"
            itemID: u32 = 66600261
        }
        statStones: list[link] = {
            0xb164e242
            0x6b2e866b
            0x6f223a0a
        }
    }
    0x6b2e866b = StatStoneData {
        mNameTraKey: string = "stat_stone_name_takedowns"
        catalogEntry: embed = catalogEntry {
            contentId: string = "165b4624-1bc7-4798-98c5-0b529872157e"
            itemID: u32 = 125721
        }
        mDescriptionTraKey: string = "stat_stone_description_Takedowns"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 7
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 86
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        MinionsAreValid: bool = false
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 227
            }
        }
        category: link = 0x5c6e96a2
        Milestones: list[u64] = {
            25
            65
            125
            150
            185
            75
        }
        stoneName: string = "RengarTakedowns"
    }
    0x6f223a0a = StatStoneData {
        mNameTraKey: string = "stat_stone_name_structures_destroyed"
        catalogEntry: embed = catalogEntry {
            contentId: string = "6fffce2d-09d2-4204-9352-aa445a35d376"
            itemID: u32 = 125722
        }
        mDescriptionTraKey: string = "stat_stone_description_StructuresDestroyed"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 63
            }
        }
        category: link = 0x6ce57a50
        Milestones: list[u64] = {
            5
            15
            25
            30
            40
            15
        }
        stoneName: string = "RengarStructuresDestroyed"
    }
    0xb164e242 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_EpicMonstersKilled"
        catalogEntry: embed = catalogEntry {
            contentId: string = "d1495dcd-b159-4c01-bc2e-c9a2a3742278"
            itemID: u32 = 125720
        }
        mDescriptionTraKey: string = "stat_stone_description_EpicMonstersKilled"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 66
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 86
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        ChampionsAreValid: bool = false
                    }
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 64
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            mObjectTagList: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
        }
        category: link = 0x6ce57a50
        Milestones: list[u64] = {
            3
            10
            20
            22
            25
            10
        }
        stoneName: string = "RengarEpicMonstersKilled"
    }
    0x756274ee = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarERoots"
        catalogEntry: embed = catalogEntry {
            contentId: string = "4e93d1bb-a5b7-492e-bb27-c2bc5efc5e0c"
            itemID: u32 = 126186
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarERoots"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x2eeaa87d
        Milestones: list[u64] = {
            8
            20
            40
            50
            60
            25
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarERoots"
    }
    0xc1e0cd13 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarPSubsequent"
        catalogEntry: embed = catalogEntry {
            contentId: string = "7c269156-4371-46f3-b6f3-41beaac0ac2f"
            itemID: u32 = 126185
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarPSubsequent"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x1dab670a
        Milestones: list[u64] = {
            10
            25
            50
            60
            75
            30
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarPSubsequent"
    }
    0xdb172aa8 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_RengarQKills"
        catalogEntry: embed = catalogEntry {
            contentId: string = "fa74b68c-5386-458d-ac68-878596cc6b6a"
            itemID: u32 = 126187
        }
        mDescriptionTraKey: string = "stat_stone_description_RengarQKills"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 250
            }
        }
        category: link = 0x06fc9407
        Milestones: list[u64] = {
            10000
            26000
            51000
            62000
            77000
            31000
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        stoneName: string = "RengarQDamage"
    }
    "Characters/Rengar/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Rengar"
        baseHPModifiable: embed = ModifiableFloat {
            baseValue: f32 = 590
        }
        hpPerLevelModifiable: embed = ModifiableFloat {
            baseValue: f32 = 104
        }
        baseStaticHPRegenModifiable: embed = ModifiableFloat {
            baseValue: f32 = 1.2
        }
        hpRegenPerLevelModifiable: embed = ModifiableFloat {
            baseValue: f32 = 0.1
        }
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 9
            0x726ee5cd: embed = ModifiableFloat {
                baseValue: f32 = 4
            }
            0xc4ab3550: embed = ModifiableFloat {
                baseValue: f32 = 0
            }
            arIncrements: f32 = 1
            arMaxSegments: i32 = 4
            arHasRegenText: bool = false
            0x4eb6a404: u8 = 2
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 14
            0x726ee5cd: embed = ModifiableFloat {
                baseValue: f32 = 4
            }
            0xc4ab3550: embed = ModifiableFloat {
                baseValue: f32 = 0
            }
            arIncrements: f32 = 4
            arMaxSegments: i32 = 4
            arDisplayAsPips: bool = true
            arOverrideSmallPipName: string = "GenericLargeUncolored"
            arOverrideMediumPipName: string = "GenericLargeUncolored"
            arOverrideLargePipName: string = "GenericLarge"
            arOverrideSpacerName: string = "PipSpacer1"
            0x4eb6a404: u8 = 2
        }
        baseDamageModifiable: embed = ModifiableFloat {
            baseValue: f32 = 68
        }
        damagePerLevelModifiable: embed = ModifiableFloat {
            baseValue: f32 = 3
        }
        baseArmorModifiable: embed = ModifiableFloat {
            baseValue: f32 = 34
        }
        armorPerLevelModifiable: embed = ModifiableFloat {
            baseValue: f32 = 4.2
        }
        baseMR: embed = ModifiableFloat {
            baseValue: f32 = 32
        }
        0x01262a25: embed = ModifiableFloat {
            baseValue: f32 = 2.05
        }
        critDamageMultiplier: f32 = 2
        baseMoveSpeedModifiable: embed = ModifiableFloat {
            baseValue: f32 = 345
        }
        attackRangeModifiable: embed = ModifiableFloat {
            baseValue: f32 = 125
        }
        attackSpeedModifiable: embed = ModifiableFloat {
            baseValue: f32 = 0.667
        }
        attackSpeedRatioModifiable: embed = ModifiableFloat {
            baseValue: f32 = 0.667
        }
        attackSpeedPerLevelModifiable: embed = ModifiableFloat {
            baseValue: f32 = 3
        }
        acquisitionRange: f32 = 600
        basicAttack: embed = AttackSlotData {
            mAttackTotalTime: option[f32] = {
                1.5
            }
            mAttackCastTime: option[f32] = {
                0.3
            }
            mAttackProbability: option[f32] = {
                0.45
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0.45
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0.1
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "RengarPassiveAttack"
                }
            }
        }
        critAttacks: list[embed] = {
            AttackSlotData {
                mAttackName: option[string] = {
                    "RengarCritAttack"
                }
            }
        }
        spellNames: list[string] = {
            "RengarQAbility/RengarQ"
            "RengarWAbility/RengarW"
            "RengarEAbility/RengarE"
            "RengarRAbility/RengarR"
        }
        spells: list[link] = {
            "Characters/Rengar/Spells/RengarQAbility/RengarQ"
            "Characters/Rengar/Spells/RengarWAbility/RengarW"
            "Characters/Rengar/Spells/RengarEAbility/RengarE"
            "Characters/Rengar/Spells/RengarRAbility/RengarR"
        }
        extraSpells: list[string] = {
            "RengarPassiveBuffDash"
            "RengarQSound"
            ""
            ""
            "RengarEMis"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
        }
        0xc1984296: list[link] = {
            "Characters/Rengar/Spells/RengarPassiveBuffDash"
            "Characters/Rengar/Spells/RengarQSound"
            0x00000000
            0x00000000
            "Characters/Rengar/Spells/RengarEAbility/RengarEMis"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
            "Shared/Spells/BaseSpell"
        }
        mAbilities: list[link] = {
            "Characters/Rengar/Spells/RengarRAbility"
            "Characters/Rengar/Spells/RengarQAbility"
            "Characters/Rengar/Spells/RengarWAbility"
            "Characters/Rengar/Spells/RengarEAbility"
            "Characters/Rengar/Spells/RengarPassiveAbility"
            "Characters/Rengar/Spells/RengarEEmpAbility"
        }
        passiveName: string = "game_character_passiveName_Rengar"
        passiveLuaName: string = ""
        passiveToolTip: string = "game_character_passiveDescription_Rengar"
        passiveSpell: string = "RengarPassive"
        passive1IconName: string = "ASSETS/Characters/Rengar/HUD/Icons2D/Rengar_P.dds"
        name: string = "game_character_displayname_Rengar"
        weaponMaterials: list[string] = {
            "RengarBasicAttack"
            "None"
            "RengarBasicAttack2"
            "RengarBasicAttack3"
        }
        selectionHeight: f32 = 225
        selectionRadius: f32 = 120
        pathfindingCollisionRadius: f32 = 35
        0xeb74898c: option[f32] = {
            0
        }
        unitTagsString: string = "Champion"
        mEducationToolData: embed = ToolEducationData {
            firstItem: i32 = 1055
        }
        characterToolData: embed = characterToolData {
            spellData: list[embed] = {
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
                ToolSpellDesc {
                    desc: string = "Warwick lunges at an enemy Champion, stunning them and dealing damage for a few seconds."
                    displayName: string = "Infinite Duress"
                }
            }
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                3 = ToolAiPresence {}
                4 = ToolAiPresence {}
            }
            passiveData: list[embed] = {
                ToolPassiveData {
                    name: string = "game_character_passiveName_Rengar"
                    level: list[i32] = {
                        1
                        6
                        11
                        16
                    }
                }
            }
            searchTags: string = "assassin"
            searchTagsSecondary: string = "fighter"
            championId: i32 = 107
            roles: string = "BRAWLER"
            PARFadeColor: string = "55 55 55"
            magicRank: i32 = 2
            LevelSpellEffectiveness: f32 = 2
            difficultyRank: i32 = 8
            description: string = "game_character_description_Rengar"
            defenseRank: i32 = 4
            classification: string = "Deadly"
            0xaa75da9d: bool = false
            attackRank: i32 = 7
        }
        platformEnabled: bool = true
        flags: u32 = 8398088
        purchaseIdentities: list[hash] = {
            "Melee"
        }
        mPreferredPerkStyle: link = "Perks/Styles/Domination"
        mPerkReplacements: embed = PerkReplacementList {
            mReplacements: list[pointer] = {
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Sorcery/ManaflowBand"
                    mReplaceWith: hash = "Perks/Styles/Sorcery/NullifyingOrb"
                }
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Precision/PresenceOfMind"
                    mReplaceWith: hash = "Perks/Styles/Precision/Triumph"
                }
            }
        }
        mCharacterPassiveSpell: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
        mCharacterPassiveBuffs: list[embed] = {
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Rengar/Spells/RengarPassiveAbility/RengarPassive"
                mComponentBuffs: list[link] = {
                    "Characters/Rengar/Spells/RengarPassiveEmpowered"
                    0xddd932f3
                }
            }
            CharacterPassiveData {
                mParentPassiveBuff: link = "Characters/Rengar/Spells/RengarPassiveBonetoothManager"
                mAllowOnClones: bool = false
            }
        }
        0xc5c48b41: u8 = 1
        0x6854087e: list2[embed] = {
            0x47f13ab0 {
                0xe4f7105d: link = "Maps/Shipping/Map11/Modes/SWIFTPLAY"
                0xcf19cb5d: embed = 0x770f7888 {
                    damagePerLevel: f32 = 0.5
                    baseHP: f32 = 30
                    hpPerLevel: f32 = 6
                }
            }
        }
    }
    0x3330715f = ItemRecommendationOverrideSet {
        mOverrides: list[embed] = {
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 11
                        mModeNameStringId: hash = "CLASSIC"
                        mPosition: hash = "jungle"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1102"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1101"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1103"
                            "Items/2003"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6697"
                            "Items/6699"
                        }
                        MaxCompletedItems: u32 = 1
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3009"
                            "Items/3158"
                            "Items/3010"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6698"
                            "Items/3814"
                            "Items/6696"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/6698"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/3031"
                            "Items/3072"
                            "Items/3026"
                        }
                        MaxCompletedItems: u32 = 5
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6694"
                            "Items/6673"
                            "Items/3026"
                            "Items/3156"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 11
                        mModeNameStringId: hash = "CLASSIC"
                        mPosition: hash = "Top"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1055"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/1054"
                            "Items/2003"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3074"
                            "Items/6698"
                            "Items/6697"
                        }
                        MaxCompletedItems: u32 = 1
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3158"
                            "Items/3047"
                            "Items/3111"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6692"
                            "Items/6701"
                            "Items/3074"
                            "Items/6699"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3036"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3031"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6701"
                            "Items/6699"
                            "Items/3036"
                            "Items/3814"
                            "Items/6673"
                            "Items/3026"
                            "Items/3161"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 12
                        mModeNameStringId: hash = "ARAM"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3177"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3134"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/3184"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6691"
                            "Items/6693"
                            "Items/6692"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3111"
                            "Items/3047"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3142"
                            "Items/3814"
                            "Items/3071"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/3142"
                            "Items/3814"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6333"
                            "Items/3156"
                            "Items/3026"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/6694"
                            "Items/6609"
                            "Items/6035"
                            "Items/3071"
                            "Items/6333"
                            "Items/3026"
                            "Items/3156"
                        }
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapID: u32 = 30
                        mModeNameStringId: hash = "cherry"
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/223177"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        items: list[hash] = {
                            "Items/223184"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223111"
                            "Items/223047"
                            "Items/223005"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226691"
                            "Items/226693"
                            "Items/226692"
                        }
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223142"
                            "Items/223071"
                            "Items/226696"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/223142"
                            "Items/223814"
                            "Items/226696"
                        }
                        MaxCompletedItems: u32 = 4
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226333"
                            "Items/223156"
                            "Items/223026"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    ItemRecOverrideRange {
                        items: list[hash] = {
                            "Items/226694"
                            "Items/226609"
                            "Items/226035"
                            "Items/223071"
                            "Items/226333"
                            "Items/223026"
                            "Items/223156"
                        }
                    }
                }
            }
        }
    }
    0x4ebd1ade = RecSpellRankUpInfolist {
        RecSpellRankUpInfos: list[embed] = {
            recSpellRankUpInfo {
                MapId: u32 = 11
                position: hash = "jungle"
                IsDefaultRecommendation: bool = true
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
            recSpellRankUpInfo {
                MapId: u32 = 12
                position: hash = "None"
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
        }
    }
    0x79fd0c7a = ChampionRuneRecommendationsContext {}
    0x9ac98f63 = JunglePathRecommendation {
        OrderJunglePath: list[pointer] = {
            TakeCamp {
                Camp: u8 = 1
            }
            TakeCamp {}
            TakeCamp {
                Camp: u8 = 2
            }
            TakeCamp {
                Camp: u8 = 3
            }
            TakeCamp {
                Camp: u8 = 4
            }
            TakeCamp {
                Camp: u8 = 5
            }
            TerminatePath {}
        }
        ChaosJunglePath: list[pointer] = {
            TakeCamp {
                Camp: u8 = 10
            }
            TakeCamp {
                Camp: u8 = 11
            }
            TakeCamp {
                Camp: u8 = 9
            }
            TakeCamp {
                Camp: u8 = 8
            }
            TakeCamp {
                Camp: u8 = 6
            }
            TakeCamp {
                Camp: u8 = 7
            }
            TerminatePath {}
        }
    }
    "Characters/Rengar/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
