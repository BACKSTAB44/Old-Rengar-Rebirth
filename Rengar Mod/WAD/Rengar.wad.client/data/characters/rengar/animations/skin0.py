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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel.anm"
                }
            }
            "ArenaAugmentFix" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel.anm"
                }
            }
            "Channel_Actions" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Channel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel_wndpup.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_crit.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_dance.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_death.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_laugh.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_run1.anm"
                }
            }
            "Run2" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = SubmeshVisibilityBoolDriver {
                        Submeshes: list[hash] = {
                            "MinimalMesh"
                        }
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_run2.anm"
                }
            }
            "Spell2" = AtomicClipData {
                mMaskDataName: hash = "UpperBody"
                mTrackDataName: hash = "Spell"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_spell2.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_spell3.anm"
                }
            }
            "Spell3_Run" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_spell3.anm"
                }
            }
            "Spell3_Idle" = AtomicClipData {
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_spell3.anm"
                }
            }
            "Spell5" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Characters/Rengar/Spells/RengarRAbility/RengarR"
                            }
                            HasBuffDynamicMaterialBoolDriver {
                                mScriptName: string = "RengarR"
                            }
                        }
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_dash1.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_dash1.anm"
                }
            }
            "TransparencyFix" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "TransFix"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_laugh.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_taunt.anm"
                }
            }
            "Attack1" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = IsAttackingBoolDriver {}
                }
                mTrueConditionClipName: hash = "Attack1_BASE"
                mFalseConditionClipName: hash = "Tiamat_Override"
            }
            "Tiamat_Override" = ConditionBoolClipData {
                Updater: pointer = LogicDriverBoolParametricUpdater {
                    driver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
                            }
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
                            }
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack1.anm"
                }
            }
            "Tiamat_Logic_Off" = AtomicClipData {
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Null"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_channel.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack2.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack3.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_recall.anm"
                }
            }
            "Raw_LionGuy_recall_idle" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Actions"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_recall_idle.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_joke.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_run1_fast.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack4.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack4.anm"
                }
            }
            "Tiamat_Logic_On" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "empty"
                mTrackDataName: hash = "Null"
                mTickDuration: f32 = 0.034
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_attack4.anm"
                }
            }
            "Idle1" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle1.anm"
                }
            }
            "Idle2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle2.anm"
                }
            }
            "Idle3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle3.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
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
                    0
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
            13022361219970415949 = TimeBlendData { # "Channel_Channel" To "death"
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData { # "Channel_Wndup" To "death"
                mTime: f32 = 0
            }
            6347110898064735565 = TimeBlendData { # "Crit_BASE" To "death"
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData { # "Dance" To "death"
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData { # "death" To "death"
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData { # "Idle1" To "death"
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData { # "Idle1_BASE" To "death"
                mTime: f32 = 0
            }
            11302304930492628301 = TimeBlendData { # "Idle2" To "death"
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData { # "Idle2_BASE" To "death"
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData { # "Laugh" To "death"
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData { # "Run" To "death"
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData { # "Run2" To "death"
                mTime: f32 = 0
            }
            934847979299847501 = TimeBlendData { # "Run2_BASE" To "death"
                mTime: f32 = 0
            }
            5488735965694967117 = TimeBlendData { # "Attack4_Actions" To "death"
                mTime: f32 = 0
            }
            13111734580252556621 = TimeBlendData { # "Spell2" To "death"
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData { # "Spell3" To "death"
                mTime: f32 = 0
            }
            10046748851566067021 = TimeBlendData { # "Spell3_Idle" To "death"
                mTime: f32 = 0
            }
            17825496522308500813 = TimeBlendData { # "Spell3_Run" To "death"
                mTime: f32 = 0
            }
            1548379792630922573 = TimeBlendData { # "Spell5_Bush" To "death"
                mTime: f32 = 0
            }
            7174843321836682573 = TimeBlendData { # "Spell5_Ult" To "death"
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData { # "taunt" To "death"
                mTime: f32 = 0
            }
            6929639313875975501 = TimeBlendData { # "Raw_LionGuy_recall" To "death"
                mTime: f32 = 0
            }
            7064088776836431181 = TimeBlendData { # "Raw_LionGuy_recall_idle" To "death"
                mTime: f32 = 0
            }
            7714889503158615373 = TimeBlendData { # "Attack1_Actions" To "death"
                mTime: f32 = 0
            }
            7893826271730777421 = TimeBlendData { # "Attack2_BASE" To "death"
                mTime: f32 = 0
            }
            893241265303895373 = TimeBlendData { # "Attack3_BASE" To "death"
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData { # "Recall" To "death"
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData { # "Joke" To "death"
                mTime: f32 = 0
            }
            11230245605582880077 = TimeBlendData { # "Idle3" To "death"
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData { # "Idle3_BASE" To "death"
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData { # "Run1_Fast" To "death"
                mTime: f32 = 0
            }
        }
        objectPath: hash = "Characters/Rengar/Animations/Skin0"
    }
}
