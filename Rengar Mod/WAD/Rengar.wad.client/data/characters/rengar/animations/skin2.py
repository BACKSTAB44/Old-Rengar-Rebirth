#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Animations/Skin2" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Channel" = ParallelClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "ArenaGateFix"
                    "Channel_Actions"
                    "Channel_Channel"
                    "ArenaAugmentFix"
                }
            }
            "ArenaGateFix" = AtomicClipData {
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "ArenaAugmentFix" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Channel_Channel" = AtomicClipData {
                mTrackDataName: hash = "Channel"
                mEventDataMap: map[hash,pointer] = {
                    "StopChannel_A" = StopAnimationEventData {
                        mStopAnimationName: hash = "Channel_Actions"
                        mStartFrame: f32 = 1
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Channel_Actions" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel_WNDPUP.anm"
                }
            }
            "Crit" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "Crit" = ParticleEventData {
                        mStartFrame: f32 = 5
                        mEffectKey: hash = "Rengar_C_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_crit.anm"
                }
            }
            "Dance_Base" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xbc45bbc5 = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Dance3D_buffactivate"
                    }
                    "StopW" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell2"
                    }
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Dance.anm"
                }
            }
            "death" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "StopChannel" = StopAnimationEventData {
                        mStopAnimationName: hash = "Channel"
                    }
                    "StopChannel_W" = StopAnimationEventData {
                        mStopAnimationName: hash = "Channel_Wndup"
                    }
                    "Audio_Death" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Death3D_cast"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_death.anm"
                }
            }
            "Idle1_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2_Base" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            0x9e55a33e = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x0cf0606b = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Laugh3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    "StopW" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell2"
                    }
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Laugh.anm"
                }
            }
            "Run" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopE2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3_Idle"
                    }
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_run1.anm"
                }
            }
            "Run2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = HasBuffDynamicMaterialBoolDriver {
                        mScriptName: string = "RengarPassiveBuff"
                    }
                }
                mPlayAnimChangeFromBeginning: bool = true
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "Run2_Core"
                mFalseConditionClipName: hash = "Run1_Fast"
            }
            "Run2_Core" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Run2_Tassel"
                    "Run2_Default"
                }
            }
            "Run2_Tassel" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Run2.anm"
                }
            }
            "Run2_Default" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopE2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3_Idle"
                    }
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run2.anm"
                }
            }
            "Spell2" = AtomicClipData {
                mTrackDataName: hash = "Spell"
                mMaskDataName: hash = "UpperBody"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mTickDuration: f32 = 0.0333333
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_spell2.anm"
                }
            }
            "Spell3" = ConditionBoolClipData {
                Updater: pointer = IsMovingParametricUpdater {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "Spell3_Run"
                mFalseConditionClipName: hash = "Spell3_Idle"
            }
            "Spell3_Run" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_spell3.anm"
                }
            }
            "Spell3_Idle" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_spell3.anm"
                }
            }
            "Spell5" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = HasBuffDynamicMaterialBoolDriver {
                        mScriptName: string = "RengarR"
                    }
                }
                mTrueConditionClipName: hash = "Spell5_Check"
                mFalseConditionClipName: hash = "Spell5_Bush"
            }
            "Spell5_Check" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = IsInGrassDynamicMaterialBoolDriver {}
                }
                mChangeAnimationMidPlay: bool = true
                mFalseConditionClipName: hash = "Spell5_Ult"
                mTrueConditionClipName: hash = "Spell5_Bush"
            }
            "Spell5_Bush" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                        mEndFrame: f32 = 24
                    }
                    "LockSpell3" = LockRootOrientationEventData {
                        JointName: hash = "root"
                        mEndFrame: f32 = 21
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_dash1.anm"
                }
            }
            "Spell5_Ult" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "TransFix" = ParticleEventData {
                        mEffectKey: hash = "Rengar_R_LeapMat"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mFireIfAnimationEndsEarly: bool = true
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                        mEndFrame: f32 = 24
                    }
                    "LockSpell3" = LockRootOrientationEventData {
                        JointName: hash = "root"
                        mEndFrame: f32 = 21
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_dash1.anm"
                }
            }
            "Attack4" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "A4_VO"
                        mProbability: f32 = 50
                    }
                    SelectorPairData {
                        mClipName: hash = "A4"
                        mProbability: f32 = 50
                    }
                }
            }
            "A4_VO" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "A4_Actions"
                    "A4_VO_Default"
                }
            }
            "A4_Actions" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "A4_VO_Default" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "QVFX" = ParticleEventData {
                        mStartFrame: f32 = 6
                        mEffectKey: hash = "Rengar_Q_Cas2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "QSFX" = SoundEventData {
                        mStartFrame: f32 = 4
                        mSoundName: string = "Play_sfx_Old_RengarQ_Stab"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "QVO" = SoundEventData {
                        mStartFrame: f32 = 4
                        mSoundName: string = "Play_vo_Rengar_RengarQ_cast3D"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "A4" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "A4_Actions"
                    "A4_Default"
                }
            }
            "A4_Default" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "QVFX" = ParticleEventData {
                        mStartFrame: f32 = 6
                        mEffectKey: hash = "Rengar_Q_Cas2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "QSFX" = SoundEventData {
                        mStartFrame: f32 = 4
                        mSoundName: string = "Play_sfx_Old_RengarQ_Stab"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Taunt_Base" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Taunt.anm"
                }
            }
            "Attack1" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmpASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQ"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmp"
                                    }
                                }
                            }
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 6
                                    }
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 7
                                    }
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 8
                                    }
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 9
                                    }
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 10
                                    }
                                    IsCastingBoolDriver {
                                        SpellSlot: u32 = 11
                                    }
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Tiamat_Override"
                mFalseConditionClipName: hash = "Attack1_Base"
            }
            "Tiamat_Override" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarQEmp"
                            }
                            HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarQ"
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack4"
                mFalseConditionClipName: hash = "Tiamat_LeapChk"
            }
            "Tiamat_LeapChk" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmpASBuff"
                                    }
                                }
                            }
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Attack1_Base"
                                    "Attack2"
                                    "Attack3"
                                    "Crit"
                                    "Run"
                                    "Run1_Fast"
                                    "Run2_Core"
                                    "Spell5_Ult"
                                    "Spell5_Bush"
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Tiamat_LeapWrap"
                mFalseConditionClipName: hash = "Attack4"
            }
            "Tiamat_LeapWrap" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmpASBuff"
                                    }
                                }
                            }
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    FloatComparisonMaterialDriver {
                                        mOperator: u32 = 2
                                        mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                            mAnimationName: hash = "Spell5_Bush"
                                        }
                                        mValueB: pointer = FloatLiteralMaterialDriver {
                                            mValue: f32 = 0.472
                                        }
                                    }
                                    FloatComparisonMaterialDriver {
                                        mOperator: u32 = 2
                                        mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                            mAnimationName: hash = "Spell5_Ult"
                                        }
                                        mValueB: pointer = FloatLiteralMaterialDriver {
                                            mValue: f32 = 0.472
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack4"
                mFalseConditionClipName: hash = "Tiamat_RunChk"
            }
            "Tiamat_RunChk" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmpASBuff"
                                    }
                                }
                            }
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Attack1_Base"
                                    "Attack2"
                                    "Attack3"
                                    "Crit"
                                    "Run2_Core"
                                    "Spell5_Ult"
                                    "Spell5_Bush"
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack1_Base"
                mFalseConditionClipName: hash = "Tiamat_RunWrap"
            }
            "Tiamat_RunWrap" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQASBuff"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmpASBuff"
                                    }
                                }
                            }
                            OneTrueMaterialDriver {
                                mDrivers: list[pointer] = {
                                    FloatComparisonMaterialDriver {
                                        mOperator: u32 = 1
                                        mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                            mAnimationName: hash = "Run"
                                        }
                                        mValueB: pointer = FloatLiteralMaterialDriver {
                                            mValue: f32 = 0.3
                                        }
                                    }
                                    FloatComparisonMaterialDriver {
                                        mOperator: u32 = 1
                                        mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                            mAnimationName: hash = "Run1_Fast"
                                        }
                                        mValueB: pointer = FloatLiteralMaterialDriver {
                                            mValue: f32 = 0.4
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack1_Base"
                mFalseConditionClipName: hash = "Attack4"
            }
            "Attack1_Base" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    0xb5b7e047 = ParticleEventData {
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA1_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack1.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    0xb6b7e1da = ParticleEventData {
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA2_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack2.anm"
                }
            }
            "Attack3" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    0xb7b7e36d = ParticleEventData {
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Rengar_BA3_Cas"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack3.anm"
                }
            }
            "Joke" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Joke3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    "StopW" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell2"
                    }
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Joke.anm"
                }
            }
            "Idle3_Base" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
                }
            }
            0x7cb9d840 = AtomicClipData {
                mFlags: u32 = 3
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopE2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3_Idle"
                    }
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run1_Fast.anm"
                }
            }
            "Recall" = AtomicClipData {
                mTrackDataName: hash = "Recall"
                mEventDataMap: map[hash,pointer] = {
                    "Hood" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 67
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                    "Audio_Recall" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Recall3D_buffactivate"
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_recall.anm"
                }
            }
            "Run1_Fast" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0xf4784b95
                    0x7cb9d840
                }
            }
            0xf4784b95 = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_run1_Fast.anm"
                }
            }
            0x8932308b = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle1.anm"
                }
            }
            "Idle1" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Idle_NoIdle3"
                    0x1b254ae6
                    0x1b254ae6
                    "Idle_WIdle3"
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    "Idle3_NH"
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    "Idle_WIdle3"
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    0x1b254ae6
                    "Idle3_NH"
                }
            }
            "Idle_NoIdle3" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x1b254ae6
                        mProbability: f32 = 75
                    }
                    SelectorPairData {
                        mClipName: hash = 0x2c00f6af
                        mProbability: f32 = 25
                    }
                }
            }
            "Idle_WIdle3" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x1b254ae6
                        mProbability: f32 = 10
                    }
                    SelectorPairData {
                        mClipName: hash = 0x2c00f6af
                        mProbability: f32 = 30
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle3_NH"
                        mProbability: f32 = 60
                    }
                }
            }
            0xc5288be8 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle2.anm"
                }
            }
            "Idle3" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle3.anm"
                }
            }
            0x299519f8 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Taunt.anm"
                }
            }
            "taunt" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Taunt_Base"
                    0x299519f8
                }
            }
            0xfebfc6d3 = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Laugh.anm"
                }
            }
            "Laugh" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x9e55a33e
                    0xfebfc6d3
                }
            }
            "Dance" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Dance_Base"
                    0xd4939539
                }
            }
            0xd4939539 = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Dance.anm"
                }
            }
            "Recall_Winddown" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Winddown" = SubmeshVisibilityEventData {
                        mEndFrame: f32 = 2
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Hood_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mMaskDataName: hash = "Hood"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    0xe6fda1e1 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_hood_loop.anm"
                }
            }
            "Hood_Off" = AtomicClipData {
                mMaskDataName: hash = "Arm"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    "hoodoff" = SubmeshVisibilityEventData {
                        mEndFrame: f32 = 17
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_hood_off.anm"
                }
            }
            0xd884c53b = AtomicClipData {
                mFlags: u32 = 8
                mMaskDataName: hash = "Arm"
                mTrackDataName: hash = "Hood"
                mEventDataMap: map[hash,pointer] = {
                    "hoodon" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 14
                        mShowSubmeshList: list[hash] = {
                            "Hood"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_hood_on.anm"
                }
            }
            0x1d902a0d = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xd884c53b
                    "Hood_Loop"
                }
            }
            0x1b254ae6 = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle1_Base"
                    0x8932308b
                }
            }
            0x2c00f6af = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle2_Base"
                    0xc5288be8
                }
            }
            "Idle3_NH" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle3"
                    "Idle3_Base"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "Hood" = MaskData {
                mWeightList: list[f32] = {
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
                    1
                    1
                }
            }
            "Tassel" = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
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
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    0
                    0
                    1
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
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            "Arm" = MaskData {
                mId: u32 = 2
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
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
                    1
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
                    1
                    0
                    0
                    1
                    1
                }
            }
            0x26a07077 = MaskData {
                mWeightList: list[f32] = {
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
                    0.25
                    0.6
                    0.75
                    0.85
                    1
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
            }
            "UpperBody" = MaskData {
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
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
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    0
                    1
                    1
                    0
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Channel" = TrackData {}
            "Recall" = TrackData {
                mPriority: u8 = 1
            }
            "Hood" = TrackData {
                mPriority: u8 = 2
            }
            "Actions" = TrackData {
                mPriority: u8 = 3
            }
            "Spell" = TrackData {
                mPriority: u8 = 4
            }
            "Tassel" = TrackData {
                mPriority: u8 = 5
            }
            "Default" = TrackData {
                mPriority: u8 = 6
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            350652854184754509 = TimeBlendData {
                mTime: f32 = 0
            }
            897461255355809101 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616235167053 = TimeBlendData {
                mTime: f32 = 0
            }
            2996329683201080653 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData {
                mTime: f32 = 0
            }
            5406481393446862157 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502141246797 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151960743245 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300835852006 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300975292661 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301013100192 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301322850443 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301854066283 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302328851432 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302777271857 = TimeBlendData {
                mTime: f32 = 0
            }
            6664513967696166221 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313875975501 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776836431181 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            8393268201603513677 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData {
                mTime: f32 = 0
            }
            8987452303957605709 = TimeBlendData {
                mTime: f32 = 0
            }
            9886017508763811149 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110054976845 = TimeBlendData {
                mTime: f32 = 0
            }
            11409204720869883213 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168680979789 = TimeBlendData {
                mTime: f32 = 0
            }
            12217611127544659277 = TimeBlendData {
                mTime: f32 = 0
            }
            12771797303277698381 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556603804248356 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556603837803594 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556603854581213 = TimeBlendData {
                mTime: f32 = 0.1
            }
            12895556605523311949 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793905162304845 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230072053069 = TimeBlendData {
                mTime: f32 = 0
            }
            13399971879891549517 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412461706982 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412601147637 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412638955168 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412948705419 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413954706408 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352414403126833 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            14206758856262466893 = TimeBlendData {
                mTime: f32 = 0
            }
            15317750832836427085 = TimeBlendData {
                mTime: f32 = 0
            }
            15601811869485546829 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            17615913048955469133 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            18356609218899393869 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605538995048 = TimeBlendData {
                mTime: f32 = 0
            }
            13093444449137638733 = TimeBlendData {
                mTime: f32 = 0
            }
            15677482531746790733 = TimeBlendData {
                mTime: f32 = 0
            }
            1956051968038845773 = TimeBlendData {
                mTime: f32 = 0
            }
            3170805372322102605 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
