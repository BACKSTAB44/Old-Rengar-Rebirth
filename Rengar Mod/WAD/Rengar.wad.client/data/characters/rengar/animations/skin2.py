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
            "Crit" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Tiamat_Logic_Off"
                    "Crit_BASE"
                }
            }
            "Crit_BASE" = AtomicClipData {
                mFlags: u32 = 1
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
            "Dance_BASE" = AtomicClipData {
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
                mTrackDataName: hash = "Channel"
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
            "Idle1_BASE" = AtomicClipData {
                mFlags: u32 = 3
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            "Laugh_BASE" = AtomicClipData {
                mFlags: u32 = 1
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
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_run1.anm"
                }
            }
            "Run2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = SubmeshVisibilityBoolDriver {
                        Submeshes: list[hash] = {
                            "MinimalMesh"
                        }
                        VISIBLE: bool = true
                    }
                }
                mChangeAnimationMidPlay: bool = true
                mPlayAnimChangeFromBeginning: bool = true
                mTrueConditionClipName: hash = "Run2_Parallel"
                mFalseConditionClipName: hash = "Run1_Fast"
            }
            "Run2_Parallel" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Run2_TASSEL"
                    "Run2_BASE"
                }
            }
            "Run2_TASSEL" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Run2.anm"
                }
            }
            "Run2_BASE" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopE2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3_Idle"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run2.anm"
                }
            }
            "Spell2" = AtomicClipData {
                mMaskDataName: hash = "TopBody"
                mTrackDataName: hash = "Spell"
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
            "Attack4" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Attack4_Actions"
                    "Attack4_Default"
                    "Tiamat_Logic_On"
                }
            }
            "Attack4_Actions" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Attack4_Default" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Q" = ParticleEventData {
                        mStartFrame: f32 = 4
                        mEffectKey: hash = "Rengar_Q_Cas2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Tiamat_Logic_On" = AtomicClipData {
                mMaskDataName: hash = "Void"
                mTrackDataName: hash = "Void"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Taunt_BASE" = AtomicClipData {
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
                                        mScriptName: string = "RengarQ"
                                    }
                                    HasBuffDynamicMaterialBoolDriver {
                                        mScriptName: string = "RengarQEmp"
                                    }
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
                mFalseConditionClipName: hash = "Attack1_BASE"
            }
            "Tiamat_Override" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarQ"
                            }
                            HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarQEmp"
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack4"
                mFalseConditionClipName: hash = "Tiamat_StateCheck"
            }
            "Tiamat_StateCheck" = ConditionBoolClipData {
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
                                    "Spell5_Bush"
                                    "Spell5_Ult"
                                    "Tiamat_Logic_Off"
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Tiamat_LeapCheck"
                mFalseConditionClipName: hash = "Attack4"
            }
            "Tiamat_LeapCheck" = ConditionBoolClipData {
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
                mFalseConditionClipName: hash = "Attack1_BASE"
            }
            "Attack1_BASE" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Tiamat_Logic_Off"
                    "Attack1_Actions"
                }
            }
            "Attack1_Actions" = AtomicClipData {
                mFlags: u32 = 1
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
            "Tiamat_Logic_Off" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Void"
                mTrackDataName: hash = "Void"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack1.anm"
                }
            }
            "Attack2" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Tiamat_Logic_Off"
                    "Attack2_BASE"
                }
            }
            "Attack2_BASE" = AtomicClipData {
                mFlags: u32 = 1
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
            "Attack3" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Tiamat_Logic_Off"
                    "Attack3_BASE"
                }
            }
            "Attack3_BASE" = AtomicClipData {
                mFlags: u32 = 1
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
            "Joke" = AtomicClipData {
                mFlags: u32 = 1
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
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Joke.anm"
                }
            }
            "Idle3_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
                }
            }
            "Run1_Fast_BASE" = AtomicClipData {
                mFlags: u32 = 3
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "StopE2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3_Idle"
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
                    "StopAttack1" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack1_BASE"
                        mEndFrame: f32 = 1
                    }
                    "StopAttack2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack2"
                        mEndFrame: f32 = 1
                    }
                    "StopAttack3" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack3"
                        mEndFrame: f32 = 1
                    }
                    "StopAttack4" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack4"
                        mEndFrame: f32 = 1
                    }
                    "StopCrit" = StopAnimationEventData {
                        mStopAnimationName: hash = "Crit"
                        mEndFrame: f32 = 1
                    }
                    "StopLeap1" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell5"
                        mEndFrame: f32 = 1
                    }
                    "StopLeap2" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell5_Check"
                        mEndFrame: f32 = 1
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_recall.anm"
                }
            }
            "Run1_Fast" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Run1_Fast_TASSEL"
                    "Run1_Fast_BASE"
                }
            }
            "Run1_Fast_TASSEL" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_run1_Fast.anm"
                }
            }
            "Idle1_TASSEL" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle1.anm"
                }
            }
            "Idle2_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle2.anm"
                }
            }
            "Idle3_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Idle3.anm"
                }
            }
            "Taunt_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Taunt.anm"
                }
            }
            "taunt" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Taunt_BASE"
                    "Taunt_TASSEL"
                }
            }
            "Laugh_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin02/Animations/Rengar_skin02_Laugh.anm"
                }
            }
            "Laugh" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Laugh_BASE"
                    "Laugh_TASSEL"
                }
            }
            "Dance" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Dance_BASE"
                    "Dance_TASSEL"
                }
            }
            "Dance_TASSEL" = AtomicClipData {
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
                    "HoodLoop" = SubmeshVisibilityEventData {
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
            "Hood_On_BASE" = AtomicClipData {
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
            "Hood_On" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Hood_On_BASE"
                    "Hood_Loop"
                }
            }
            "Idle1" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle1_BASE"
                    "Idle1_TASSEL"
                }
            }
            "Idle2" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle2_BASE"
                    "Idle2_TASSEL"
                }
            }
            "Idle3" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Idle3_TASSEL"
                    "Idle3_BASE"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
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
                    1
                    1
                }
            }
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
            "Void" = MaskData {
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
                    0
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
            "Tassel" = TrackData {
                mPriority: u8 = 3
            }
            "Actions" = TrackData {
                mPriority: u8 = 4
            }
            "Spell" = TrackData {
                mPriority: u8 = 5
            }
            "Default" = TrackData {
                mPriority: u8 = 6
            }
            "Void" = TrackData {
                mPriority: u8 = 7
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            13987674969707957024 = TimeBlendData {
                mTime: f32 = 0.2
            }
            893241263926594336 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7893826270353476384 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7714889501781314336 = TimeBlendData {
                mTime: f32 = 0.2
            }
            897461253978508064 = TimeBlendData {
                mTime: f32 = 0.2
            }
            1548379791253621536 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7174843320459381536 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675253965507360 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10046748850188765984 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17825496520931199776 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734578875255584 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5488735964317666080 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569502590913312 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11422514324926679840 = TimeBlendData {
                mTime: f32 = 0.2
            }
            934847977922546464 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207951105280800 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11409204719492582176 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709915118586656 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375147268393760 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352412443200288 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6664513966318865184 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6347110896687434528 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733633453968160 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13022361218593114912 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13987674969749618987 = TimeBlendData {
                mTime: f32 = 0.2
            }
            893241263968256299 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7893826270395138347 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7714889501822976299 = TimeBlendData {
                mTime: f32 = 0.2
            }
            897461254020170027 = TimeBlendData {
                mTime: f32 = 0.2
            }
            1548379791295283499 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7174843320501043499 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675254007169323 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10046748850230427947 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17825496520972861739 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734578916917547 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5488735964359328043 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569502632575275 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11422514324968341803 = TimeBlendData {
                mTime: f32 = 0.2
            }
            934847977964208427 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207951146942763 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11409204719534244139 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709915160248619 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375147310055723 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352412484862251 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6664513966360527147 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6347110896729096491 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733633495630123 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13022361218634776875 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13987674968119668274 = TimeBlendData {
                mTime: f32 = 0.2
            }
            893241262338305586 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7893826268765187634 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7714889500193025586 = TimeBlendData {
                mTime: f32 = 0.2
            }
            897461252390219314 = TimeBlendData {
                mTime: f32 = 0.2
            }
            1548379789665332786 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7174843318871092786 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13039675252377218610 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10046748848600477234 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17825496519342911026 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13111734577286966834 = TimeBlendData {
                mTime: f32 = 0.2
            }
            5488735962729377330 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569501002624562 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11422514323338391090 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207949516992050 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11409204717904293426 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709913530297906 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375145680105010 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352410854911538 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6664513964730576434 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6347110895099145778 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11831733631865679410 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13022361217004826162 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352412601147637 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412638955168 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413954706408 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352414403126833 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412948705419 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352412461706982 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300975292661 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301013100192 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302328851432 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302777271857 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301322850443 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300835852006 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301854066283 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            13022361219970415949 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            6347110898064735565 = TimeBlendData {
                mTime: f32 = 0
            }
            6664513967696166221 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            11409204720869883213 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData {
                mTime: f32 = 0
            }
            11422514326303980877 = TimeBlendData {
                mTime: f32 = 0
            }
            5488735965694967117 = TimeBlendData {
                mTime: f32 = 0
            }
            13111734580252556621 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            10046748851566067021 = TimeBlendData {
                mTime: f32 = 0
            }
            17825496522308500813 = TimeBlendData {
                mTime: f32 = 0
            }
            1548379792630922573 = TimeBlendData {
                mTime: f32 = 0
            }
            7174843321836682573 = TimeBlendData {
                mTime: f32 = 0
            }
            897461255355809101 = TimeBlendData {
                mTime: f32 = 0
            }
            7714889503158615373 = TimeBlendData {
                mTime: f32 = 0
            }
            7893826271730777421 = TimeBlendData {
                mTime: f32 = 0
            }
            893241265303895373 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData {
                mTime: f32 = 0
            }
            8987452303957605709 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData {
                mTime: f32 = 0
            }
            17615913048955469133 = TimeBlendData {
                mTime: f32 = 0
            }
            9886017508763811149 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData {
                mTime: f32 = 0
            }
            14206758856262466893 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304930492628301 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605582880077 = TimeBlendData {
                mTime: f32 = 0
            }
            8393268201603513677 = TimeBlendData {
                mTime: f32 = 0
            }
            2996329683201080653 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            18356609218899393869 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            15317750832836427085 = TimeBlendData {
                mTime: f32 = 0
            }
            12167572168680979789 = TimeBlendData {
                mTime: f32 = 0
            }
            12771797303277698381 = TimeBlendData {
                mTime: f32 = 0
            }
            350652854184754509 = TimeBlendData {
                mTime: f32 = 0
            }
            15601811869485546829 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
