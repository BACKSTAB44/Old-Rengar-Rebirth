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
            "Crit" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Crit_BASE"
                    "Tiamat_Logic_Off"
                }
            }
            "Crit_BASE" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mEventDataMap: map[hash,pointer] = {
                    "Crit" = ParticleEventData {
                        mStartFrame: f32 = 3
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
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run1.anm"
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
                mTrueConditionClipName: hash = "Run2_BASE"
                mFalseConditionClipName: hash = "Run1_Fast"
            }
            "Run2_BASE" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
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
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = AllTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Spell5_BASE"
                                    "Spell5_Null"
                                }
                            }
                            FloatComparisonMaterialDriver {
                                mOperator: u32 = 3
                                mValueA: pointer = AnimationFractionDynamicMaterialFloatDriver {
                                    mAnimationName: hash = "Spell5_Null"
                                }
                                mValueB: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 0.18
                                }
                            }
                        }
                    }
                }
                mTrueConditionClipName: hash = "Spell3_Midair"
                mFalseConditionClipName: hash = "Spell3_Check"
            }
            "Spell3_Check" = ConditionBoolClipData {
                Updater: pointer = IsMovingParametricUpdater {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "Spell3_Run"
                mFalseConditionClipName: hash = "Spell3_Idle"
            }
            "Spell3_Midair" = AtomicClipData {
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Midair"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_spell3.anm"
                }
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
                mTrueConditionClipName: hash = "Spell5_Ult"
                mFalseConditionClipName: hash = "Spell5_Bush"
            }
            "Spell5_Bush" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell5_Null"
                    "Spell5_BASE"
                }
            }
            "Spell5_Ult" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell5_Null"
                    "Spell5_BASE"
                    "TransparencyFix"
                }
            }
            "Spell5_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_dash1.anm"
                }
            }
            "Spell5_Null" = AtomicClipData {
                mFlags: u32 = 1
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Null"
                mEventDataMap: map[hash,pointer] = {
                    "StopE" = StopAnimationEventData {
                        mStopAnimationName: hash = "Spell3"
                        mEndFrame: f32 = 24
                    }
                    "LockSpell3" = LockRootOrientationEventData {
                        JointName: hash = "root"
                        mEndFrame: f32 = 20
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_dash1.anm"
                }
            }
            "TransparencyFix" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "TransFix"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Laugh.anm"
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
                    driver: pointer = OneTrueMaterialDriver {
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
                    driver: pointer = IsAnimationPlayingDynamicMaterialBoolDriver {
                        mAnimationNames: list[hash] = {
                            "Tiamat_Logic_On"
                        }
                    }
                }
                mTrueConditionClipName: hash = "Attack4"
                mFalseConditionClipName: hash = "Attack1_BASE"
            }
            "Attack1_BASE" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Attack1_Actions"
                    "Tiamat_Logic_Off"
                }
            }
            "Attack1_Actions" = AtomicClipData {
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
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Null"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Channel.anm"
                }
            }
            "Attack2" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Attack2_BASE"
                    "Tiamat_Logic_Off"
                }
            }
            "Attack2_BASE" = AtomicClipData {
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
                    "Attack3_BASE"
                    "Tiamat_Logic_Off"
                }
            }
            "Attack3_BASE" = AtomicClipData {
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
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_run1_Fast.anm"
                }
            }
            "Attack4" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Tiamat_Logic_On"
                    "Attack4_Actions"
                    "Attack4_Default"
                }
            }
            "Attack4_Actions" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Actions"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Attack4_Default" = AtomicClipData {
                mFlags: u32 = 1
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
                mFlags: u32 = 6
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Null"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_attack4.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle1.anm"
                }
            }
            "Idle2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle2.anm"
                }
            }
            "Idle3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Animations/Rengar_Idle3.anm"
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
                }
            }
            "empty" = MaskData {
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
            "Null" = TrackData {
                mPriority: u8 = 4
            }
            "Midair" = TrackData {
                mPriority: u8 = 5
            }
            "TransFix" = TrackData {
                mPriority: u8 = 6
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            13987674969707957024 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6521702300817345312 = TimeBlendData {
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
            7064088775459130144 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639312498674464 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13590883338030205728 = TimeBlendData {
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
            934847977922546464 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375147268393760 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207951105280800 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647004644887328 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304929115327264 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709915118586656 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364254025075488 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375147268393760 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352412443200288 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238948193323808 = TimeBlendData {
                mTime: f32 = 0.2
            }
            10832289108677675808 = TimeBlendData {
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
            6521702300859007275 = TimeBlendData {
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
            7064088775500792107 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639312540336427 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13590883338071867691 = TimeBlendData {
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
            5488735964359328043 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6427569502632575275 = TimeBlendData {
                mTime: f32 = 0.2
            }
            934847977964208427 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207951146942763 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647004686549291 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304929156989227 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709915160248619 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364254066737451 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375147310055723 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13630352412484862251 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238948234985771 = TimeBlendData {
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
            6521702299229056562 = TimeBlendData {
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
            7064088773870841394 = TimeBlendData {
                mTime: f32 = 0.2
            }
            6929639310910385714 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13590883336441916978 = TimeBlendData {
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
            934847976334257714 = TimeBlendData {
                mTime: f32 = 0.2
            }
            3084207949516992050 = TimeBlendData {
                mTime: f32 = 0.2
            }
            13156647003056598578 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11302304927527038514 = TimeBlendData {
                mTime: f32 = 0.2
            }
            16132709913530297906 = TimeBlendData {
                mTime: f32 = 0.2
            }
            11374364252436786738 = TimeBlendData {
                mTime: f32 = 0.2
            }
            7794375145680105010 = TimeBlendData {
                mTime: f32 = 0.2
            }
            17876238946605035058 = TimeBlendData {
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
            13022361219970415949 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            6347110898064735565 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData {
                mTime: f32 = 0
            }
            11302304930492628301 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData {
                mTime: f32 = 0
            }
            934847979299847501 = TimeBlendData {
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
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            6929639313875975501 = TimeBlendData {
                mTime: f32 = 0
            }
            7064088776836431181 = TimeBlendData {
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
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            11230245605582880077 = TimeBlendData {
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData {
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
