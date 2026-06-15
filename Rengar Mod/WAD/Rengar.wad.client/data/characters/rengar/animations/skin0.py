#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Animations/Skin0" = animationGraphData {
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
                        mStartFrame: f32 = 1
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
            "Dance" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Dance" = SoundEventData {
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
            "Idle1" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Idle_NoIdle3"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle_WIdle3"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle3_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle_WIdle3"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle1_Base"
                    "Idle3_Base"
                }
            }
            "Idle_NoIdle3" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle1_Base"
                        mProbability: f32 = 75
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle2_Base"
                        mProbability: f32 = 25
                    }
                }
            }
            "Idle_WIdle3" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle1_Base"
                        mProbability: f32 = 10
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle2_Base"
                        mProbability: f32 = 30
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle3_Base"
                        mProbability: f32 = 60
                    }
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Laugh" = SoundEventData {
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
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run1.anm"
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
            "Run2_Core" = AtomicClipData {
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
                mMaskDataName: hash = "TopBody"
                mEventDataMap: map[hash,pointer] = {
                    0x26a07077 = ConformToPathEventData {
                        mMaskDataName: hash = 0x26a07077
                        mBlendInTime: f32 = 0.1
                        mBlendOutTime: f32 = 0.2
                    }
                }
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
                mTrueConditionClipName: hash = "Spell5_Bush"
                mFalseConditionClipName: hash = "Spell5_Ult"
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
            "taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
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
                    "BA1" = ParticleEventData {
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
                    "BA2" = ParticleEventData {
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
                    "BA3" = ParticleEventData {
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
            "Recall" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Raw_LionGuy_recall"
                    "Raw_LionGuy_recall_idle"
                }
            }
            "Raw_LionGuy_recall" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_recall.anm"
                }
            }
            "Raw_LionGuy_recall_idle" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_recall_idle.anm"
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Joke" = SoundEventData {
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
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Joke.anm"
                }
            }
            "Run1_Fast" = AtomicClipData {
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
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run1_Fast.anm"
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
            "Idle1_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            "Idle3_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
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
                }
            }
            "TopBody" = MaskData {
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
                    1
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Channel" = TrackData {}
            "Actions" = TrackData {
                mPriority: u8 = 1
            }
            "Spell" = TrackData {
                mPriority: u8 = 2
            }
            "Default" = TrackData {
                mPriority: u8 = 3
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            4930726027702189345 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375146876298347 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709914726491243 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883337026950592 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647003641632192 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3405941502114026944 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675252962252224 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734577872000448 = TimeBlendData {
                mTime: f32 = 0.2
            }
            8175344642410436032 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13183793902781748672 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10832289107674420672 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13987674968704701888 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11230245603202323904 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6391149149580187072 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6463208474489935296 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6247030499760690624 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6030852525031445952 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569501587658176 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207950102025664 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7064088774455875008 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639311495419328 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304928112072128 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364253021820352 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13255853227691496896 = TimeBlendData {
                mTime: f32 = 0.2
            }
            12217611125164103104 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5406481391066305984 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13399971877510993344 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352411439945152 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238947190068672 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733632450713024 = TimeBlendData {
                mTime: f32 = 0.2
            }
            2432597613854610880 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13590883339297213630 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647005911895230 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3405941504384289982 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675255232515262 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734580142263486 = TimeBlendData {
                mTime: f32 = 0.2
            }
            8175344644680699070 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13183793905052011710 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10832289109944683710 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13987674970974964926 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11230245605472586942 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6391149151850450110 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6463208476760198334 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6247030502030953662 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6030852527301708990 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569503857921214 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207952372288702 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7064088776726138046 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639313765682366 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304930382335166 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364255292083390 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13255853229961759934 = TimeBlendData {
                mTime: f32 = 0.2
            }
            12217611127434366142 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5406481393336569022 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13399971879781256382 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352413710208190 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238949460331710 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733634720976062 = TimeBlendData {
                mTime: f32 = 0.2
            }
            2432597616124873918 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13590883339398317155 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647006012998755 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3405941504485393507 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675255333618787 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734580243367011 = TimeBlendData {
                mTime: f32 = 0.2
            }
            8175344644781802595 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13183793905153115235 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10832289110045787235 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13987674971076068451 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11230245605573690467 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6391149151951553635 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6463208476861301859 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6247030502132057187 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6030852527402812515 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569503959024739 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207952473392227 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7064088776827241571 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639313866785891 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304930483438691 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364255393186915 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13255853230062863459 = TimeBlendData {
                mTime: f32 = 0.2
            }
            12217611127535469667 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5406481393437672547 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13399971879882359907 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352413811311715 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238949561435235 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733634822079587 = TimeBlendData {
                mTime: f32 = 0.2
            }
            2432597616225977443 = TimeBlendData {
                mTime: f32 = 0.2
            }
            2432597615709903878 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616147972167 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597615906237590 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614320397870 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616181527405 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634306006022 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634744074311 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634502339734 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733632916500014 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634777629549 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949045361670 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949483429959 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949241695382 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238947655855662 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949516985197 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413295238150 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413733306439 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413491571862 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352411905732142 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413766861677 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364254877113350 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255315181639 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255073447062 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364253487607342 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255348736877 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304929967365126 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304930405433415 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304930163698838 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304928577859118 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304930438988653 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313350712326 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313788780615 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313547046038 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639311961206318 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313822335853 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776311168006 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776749236295 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776507501718 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088774921661998 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776782791533 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207951957318662 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207952395386951 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952153652374 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207950567812654 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952428942189 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503442951174 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503881019463 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503639284886 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569502053445166 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503914574701 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852526886738950 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852527324807239 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852527083072662 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852525497232942 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852527358362477 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030501615983622 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502054051911 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030501812317334 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030500226477614 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502087607149 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476345228294 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476783296583 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476541562006 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208474955722286 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476816851821 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151435480070 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151873548359 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151631813782 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149150045974062 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149151907103597 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605057616902 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605495685191 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605253950614 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245603668110894 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605529240429 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970559994886 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970998063175 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970756328598 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674969170488878 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971031618413 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109529713670 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109967781959 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109726047382 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289108140207662 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110001337197 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793904637041670 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793905075109959 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793904833375382 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793903247535662 = TimeBlendData {
                mTime: f32 = 0
            }
            13183793905108665197 = TimeBlendData {
                mTime: f32 = 0
            }
            8175344644265729030 = TimeBlendData {
                mTime: f32 = 0
            }
            8175344644703797319 = TimeBlendData {
                mTime: f32 = 0
            }
            8175344644462062742 = TimeBlendData {
                mTime: f32 = 0
            }
            8175344642876223022 = TimeBlendData {
                mTime: f32 = 0
            }
            8175344644737352557 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734579727293446 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580165361735 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734579923627158 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734578337787438 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580198916973 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675254817545222 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255255613511 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255013878934 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675253428039214 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255289168749 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941503969319942 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504407388231 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504165653654 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941502579813934 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504440943469 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005496925190 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005934993479 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005693258902 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647004107419182 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005968548717 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883338882243590 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339320311879 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339078577302 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883337492737582 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339353867117 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
