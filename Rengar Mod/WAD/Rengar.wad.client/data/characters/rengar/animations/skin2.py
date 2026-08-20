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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_dance.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_death.anm"
                }
            }
            "Idle1_BASE" = AtomicClipData {
                mFlags: u32 = 3
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle1.anm"
                }
            }
            "Idle2_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle2.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_run1.anm"
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
            "Taunt_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_joke.anm"
                }
            }
            "Idle3_BASE" = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle3.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_run1_fast.anm"
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
                    "StopAttack4_A" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack4_Actions"
                        mEndFrame: f32 = 1
                    }
                    "StopAttack4_D" = StopAnimationEventData {
                        mStopAnimationName: hash = "Attack4_Default"
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
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_recall.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_run1_fast.anm"
                }
            }
            "Idle1_TASSEL" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_idle1.anm"
                }
            }
            "Idle2_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_idle2.anm"
                }
            }
            "Idle3_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_idle3.anm"
                }
            }
            "Taunt_TASSEL" = AtomicClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = "Tassel"
                mTrackDataName: hash = "Tassel"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_taunt.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_laugh.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_dance.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/base/animations/rengar_idle1.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_hood_loop.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_hood_off.anm"
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
                    mAnimationFilePath: file = "assets/repath/characters/rengar/skins/skin02/animations/rengar_skin02_hood_on.anm"
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
                    0
                    1
                    1
                    0
                    0
                    1
                    0
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
                    0
                    1
                    0
                    0
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
            "Null" = TrackData {
                mPriority: u8 = 7
            }
            "Midair" = TrackData {
                mPriority: u8 = 8
            }
            "TransFix" = TrackData {
                mPriority: u8 = 9
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            13987674969707957024 = TimeBlendData { # "Joke" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            893241263926594336 = TimeBlendData { # "Attack3_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            7893826270353476384 = TimeBlendData { # "Attack2_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            7714889501781314336 = TimeBlendData { # "Attack1_Actions" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            897461253978508064 = TimeBlendData { # "Taunt_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            1548379791253621536 = TimeBlendData { # "Spell5_Bush" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            7174843320459381536 = TimeBlendData { # "Spell5_Ult" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            13039675253965507360 = TimeBlendData { # "Spell3" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            10046748850188765984 = TimeBlendData { # "Spell3_Idle" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            17825496520931199776 = TimeBlendData { # "Spell3_Run" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            13111734578875255584 = TimeBlendData { # "Spell2" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            5488735964317666080 = TimeBlendData { # "Attack4_Actions" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            6427569502590913312 = TimeBlendData { # "Run2" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            934847977922546464 = TimeBlendData { # "Run2_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            3084207951105280800 = TimeBlendData { # "Run" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            11409204719492582176 = TimeBlendData { # "Laugh_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            16132709915118586656 = TimeBlendData { # "Idle2_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            7794375147268393760 = TimeBlendData { # "Idle1_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            13630352412443200288 = TimeBlendData { # "death" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            6664513966318865184 = TimeBlendData { # "Dance_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            6347110896687434528 = TimeBlendData { # "Crit_BASE" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            11831733633453968160 = TimeBlendData { # "Channel_Wndup" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            13022361218593114912 = TimeBlendData { # "Channel_Channel" To "Attack1_Actions"
                mTime: f32 = 0.2
            }
            13987674969749618987 = TimeBlendData { # "Joke" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            893241263968256299 = TimeBlendData { # "Attack3_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            7893826270395138347 = TimeBlendData { # "Attack2_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            7714889501822976299 = TimeBlendData { # "Attack1_Actions" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            897461254020170027 = TimeBlendData { # "Taunt_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            1548379791295283499 = TimeBlendData { # "Spell5_Bush" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            7174843320501043499 = TimeBlendData { # "Spell5_Ult" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            13039675254007169323 = TimeBlendData { # "Spell3" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            10046748850230427947 = TimeBlendData { # "Spell3_Idle" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            17825496520972861739 = TimeBlendData { # "Spell3_Run" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            13111734578916917547 = TimeBlendData { # "Spell2" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            5488735964359328043 = TimeBlendData { # "Attack4_Actions" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            6427569502632575275 = TimeBlendData { # "Run2" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            934847977964208427 = TimeBlendData { # "Run2_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            3084207951146942763 = TimeBlendData { # "Run" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            11409204719534244139 = TimeBlendData { # "Laugh_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            16132709915160248619 = TimeBlendData { # "Idle2_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            7794375147310055723 = TimeBlendData { # "Idle1_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            13630352412484862251 = TimeBlendData { # "death" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            6664513966360527147 = TimeBlendData { # "Dance_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            6347110896729096491 = TimeBlendData { # "Crit_BASE" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            11831733633495630123 = TimeBlendData { # "Channel_Wndup" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            13022361218634776875 = TimeBlendData { # "Channel_Channel" To "Attack2_BASE"
                mTime: f32 = 0.2
            }
            13987674968119668274 = TimeBlendData { # "Joke" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            893241262338305586 = TimeBlendData { # "Attack3_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            7893826268765187634 = TimeBlendData { # "Attack2_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            7714889500193025586 = TimeBlendData { # "Attack1_Actions" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            897461252390219314 = TimeBlendData { # "Taunt_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            1548379789665332786 = TimeBlendData { # "Spell5_Bush" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            7174843318871092786 = TimeBlendData { # "Spell5_Ult" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            13039675252377218610 = TimeBlendData { # "Spell3" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            10046748848600477234 = TimeBlendData { # "Spell3_Idle" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            17825496519342911026 = TimeBlendData { # "Spell3_Run" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            13111734577286966834 = TimeBlendData { # "Spell2" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            5488735962729377330 = TimeBlendData { # "Attack4_Actions" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            6427569501002624562 = TimeBlendData { # "Run2" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            3084207949516992050 = TimeBlendData { # "Run" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            11409204717904293426 = TimeBlendData { # "Laugh_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            16132709913530297906 = TimeBlendData { # "Idle2_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            7794375145680105010 = TimeBlendData { # "Idle1_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            13630352410854911538 = TimeBlendData { # "death" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            6664513964730576434 = TimeBlendData { # "Dance_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            6347110895099145778 = TimeBlendData { # "Crit_BASE" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            11831733631865679410 = TimeBlendData { # "Channel_Wndup" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            13022361217004826162 = TimeBlendData { # "Channel_Channel" To "Attack3_BASE"
                mTime: f32 = 0.2
            }
            13630352412601147637 = TimeBlendData { # "death" To "Idle3_TASSEL"
                mTime: f32 = 0
            }
            13630352412638955168 = TimeBlendData { # "death" To "Idle3_BASE"
                mTime: f32 = 0
            }
            13630352413954706408 = TimeBlendData { # "death" To "Idle2_TASSEL"
                mTime: f32 = 0
            }
            13630352414403126833 = TimeBlendData { # "death" To "Idle2_BASE"
                mTime: f32 = 0
            }
            13630352412948705419 = TimeBlendData { # "death" To "Idle1_TASSEL"
                mTime: f32 = 0
            }
            13630352412461706982 = TimeBlendData { # "death" To "Idle1_BASE"
                mTime: f32 = 0
            }
            6521702300975292661 = TimeBlendData { # "Recall" To "Idle3_TASSEL"
                mTime: f32 = 0
            }
            6521702301013100192 = TimeBlendData { # "Recall" To "Idle3_BASE"
                mTime: f32 = 0
            }
            6521702302328851432 = TimeBlendData { # "Recall" To "Idle2_TASSEL"
                mTime: f32 = 0
            }
            6521702302777271857 = TimeBlendData { # "Recall" To "Idle2_BASE"
                mTime: f32 = 0
            }
            6521702301322850443 = TimeBlendData { # "Recall" To "Idle1_TASSEL"
                mTime: f32 = 0
            }
            6521702300835852006 = TimeBlendData { # "Recall" To "Idle1_BASE"
                mTime: f32 = 0
            }
            6521702301854066283 = TimeBlendData { # "Recall" To "Recall_Winddown"
                mTime: f32 = 0
            }
            6521702300539534768 = TimeBlendData { # "Recall" To "Recall"
                mTime: f32 = 0
            }
            13022361219970415949 = TimeBlendData { # "Channel_Channel" To "death"
                mTime: f32 = 0
            }
            11831733634831269197 = TimeBlendData { # "Channel_Wndup" To "death"
                mTime: f32 = 0
            }
            6347110898064735565 = TimeBlendData { # "Crit_BASE" To "death"
                mTime: f32 = 0
            }
            6664513967696166221 = TimeBlendData { # "Dance_BASE" To "death"
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData { # "death" To "death"
                mTime: f32 = 0
            }
            7794375148645694797 = TimeBlendData { # "Idle1_BASE" To "death"
                mTime: f32 = 0
            }
            16132709916495887693 = TimeBlendData { # Idle2_BASE" To "death"
                mTime: f32 = 0
            }
            11409204720869883213 = TimeBlendData { # "Laugh_BASE" To "death"
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData { # "Run" To "death"
                mTime: f32 = 0
            }
            6427569503968214349 = TimeBlendData { # "Run2" To "death"
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
            897461255355809101 = TimeBlendData { # "Taunt_BASE" To "death"
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
            13987674971085258061 = TimeBlendData { # "Joke" To "death"
                mTime: f32 = 0
            }
            8555650310791019853 = TimeBlendData { # "Idle3_BASE" To "death"
                mTime: f32 = 0
            }
            8987452303957605709 = TimeBlendData { # "Run1_Fast_BASE" To "death"
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData { # "Recall" To "death"
                mTime: f32 = 0
            }
            3405941504494583117 = TimeBlendData { # "Run1_Fast" To "death"
                mTime: f32 = 0
            }
            17615913048955469133 = TimeBlendData { # "Run1_Fast_TASSEL" To "death"
                mTime: f32 = 0
            }
            9886017508763811149 = TimeBlendData { # "Idle1_TASSEL" To "death"
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData { # "Idle1" To "death"
                mTime: f32 = 0
            }
            14206758856262466893 = TimeBlendData { # "Idle2_TASSEL" To "death"
                mTime: f32 = 0
            }
            11302304930492628301 = TimeBlendData { # "Idle2" To "death"
                mTime: f32 = 0
            }
            11230245605582880077 = TimeBlendData { # "Idle3" To "death"
                mTime: f32 = 0
            }
            8393268201603513677 = TimeBlendData { # "Idle3_TASSEL" To "death"
                mTime: f32 = 0
            }
            2996329683201080653 = TimeBlendData { # "Taunt_TASSEL" To "death"
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData { # "taunt" To "death"
                mTime: f32 = 0
            }
            18356609218899393869 = TimeBlendData { # "Laugh_TASSEL" To "death"
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData { # "Laugh" To "death"
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData { # "Dance" To "death"
                mTime: f32 = 0
            }
            15317750832836427085 = TimeBlendData { # "Dance_TASSEL" To "death"
                mTime: f32 = 0
            }
            12167572168680979789 = TimeBlendData { # "Recall_Winddown" To "death"
                mTime: f32 = 0
            }
            12771797303277698381 = TimeBlendData { # "Hood_Loop" To "death"
                mTime: f32 = 0
            }
            350652854184754509 = TimeBlendData { # "Hood_Off" To "death"
                mTime: f32 = 0
            }
            15601811869485546829 = TimeBlendData { # "Hood_On_BASE" To "death"
                mTime: f32 = 0
            }
        }
        objectPath: hash = "Characters/Rengar/Animations/Skin2"
    }
}
