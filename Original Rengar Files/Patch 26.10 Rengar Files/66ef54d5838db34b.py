#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/CAC/Rengar_Base" = ContextualActionData {
        mCooldown: f32 = 15
        mSituations: map[hash,embed] = {
            "AttackChampion2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Attack - General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "AttackMinion2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Attack - Minion"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "AttackNeutral2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Attack - Neutral"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Attack2DGeneral"
                        }
                    }
                }
            }
            "MoveOrder2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Move - Standard"
                        mConditions: list[pointer] = {
                            ContextualConditionMoveDistance {
                                mDistance: f32 = 400
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Move2DStandard"
                        }
                    }
                }
            }
            "taunt" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Taunt"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Taunt3DGeneral"
                            mAllyEventName: string = "Taunt3DGeneral"
                            mEnemyEventName: string = "Taunt3DGeneral"
                            mSpectatorEventName: string = "Taunt3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "Laugh" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Laugh"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Laugh3DGeneral"
                            mAllyEventName: string = "Laugh3DGeneral"
                            mEnemyEventName: string = "Laugh3DGeneral"
                            mSpectatorEventName: string = "Laugh3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "Joke" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Joke"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "Joke3DGeneral"
                            mAllyEventName: string = "Joke3DGeneral"
                            mEnemyEventName: string = "Joke3DGeneral"
                            mSpectatorEventName: string = "Joke3DGeneral"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "SpellCast" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Basic Attack"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarBasicAttack"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Basic Attack 2"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarBasicAttack2"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Basic Attack 3"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarBasicAttack3"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Crit Attack"
                        mConditions: list[pointer] = {
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarCritAttack"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Q"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQ"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Q - Empowered"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarQAbility/RengarQEmp"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "W"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarWAbility/RengarW"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "W - Empowered"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarWAbility/RengarWEmp"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "E"
                        mConditions: list[pointer] = {
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarEAbility/RengarE"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "E - Empowered"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarEEmpAbility/RengarEEmp"
                            }
                            ContextualConditionChanceToPlay {
                                mPercentChanceToPlay: u8 = 50
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                            DontResetTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "R"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellName {
                                mSpell: hash = "Characters/Rengar/Spells/RengarRAbility/RengarR"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mSelfEventName: string = "cast3D"
                            mAllyEventName: string = "cast3D"
                            mEnemyEventName: string = "cast3D"
                            mSpectatorEventName: string = "cast3D"
                        }
                        mPriority: option[i32] = {
                            100
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "FirstMove2D" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "First Move"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Move2DFirst"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "EnemyEncounter" = ContextualSituation {
                mCoolDownTime: f32 = 15
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "First Encounter - Khazix"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Khazix/CharacterRecords/Root"
                                        }
                                    }
                                    0xb6da23cb {}
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "FirstEncounter3DKhazix"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
            "SpellBuffCast" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "P Stack One"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellBuffName {
                                SpellBuff: hash = "Characters/Rengar/Spells/RengarPassiveBonetoothBuff1"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Spell3DPStackOne"
                            mEnemyEventName: string = "Spell3DPStackOne"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "P Stack Two"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellBuffName {
                                SpellBuff: hash = "Characters/Rengar/Spells/RengarPassiveBonetoothBuff2"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Spell3DPStackTwo"
                            mEnemyEventName: string = "Spell3DPStackTwo"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "P Stack Three"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellBuffName {
                                SpellBuff: hash = "Characters/Rengar/Spells/RengarPassiveBonetoothBuff3"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Spell3DPStackThree"
                            mEnemyEventName: string = "Spell3DPStackThree"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "P Stack Four"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellBuffName {
                                SpellBuff: hash = "Characters/Rengar/Spells/RengarPassiveBonetoothBuff4"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Spell3DPStackFour"
                            mEnemyEventName: string = "Spell3DPStackFour"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "P Stack Five"
                        mConditions: list[pointer] = {
                            ContextualConditionSpellBuffName {
                                SpellBuff: hash = "Characters/Rengar/Spells/RengarPassiveBonetoothBuff5"
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mSelfEventName: string = "Spell3DPStackFive"
                            mEnemyEventName: string = "Spell3DPStackFive"
                        }
                        CooldownModifications: pointer = ContextualActionCooldownModifications {
                            IgnoreTimer: bool = true
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/Rengar/CAC/Rengar_Base"
    }
}
