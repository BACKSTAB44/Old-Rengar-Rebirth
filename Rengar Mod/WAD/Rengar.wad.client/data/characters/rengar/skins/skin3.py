#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Rengar/Rengar.bin"
    "DATA/Characters/Rengar/Old_Allskins.bin"
    "DATA/Characters/Rengar/Animations/Skin0.bin"
    "DATA/Characters/Rengar/Old_Base_SSW.bin"
}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin3" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "rengarSkin03"
        metaDataTags: string = "gender:male,race:vastaya,faction:ixtal,skinline:esports,subskinline:ssw,appearance:feline"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin03/RengarLoadScreen_3.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Rengar"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Rengar_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Repath/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Old/Old_SFX_audio.bnk"
                        "ASSETS/Repath/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Old/Old_SFX_events.bnk"
                        "ASSETS/Repath/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Base/Rengar_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Base/Rengar_Base_SFX_events.bnk"
                    }
                }
                BankUnit {
                    name: string = "Rengar_Skin01_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Repath/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Skin01/Rengar_Skin01_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rengar/Skins/Skin01/Rengar_Skin01_SFX_events.bnk"
                    }
                }
                BankUnit {
                    name: string = "Rengar_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rengar/Skins/Base/Rengar_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Rengar_Attack2DGeneral"
                        "Play_vo_Rengar_Death3D"
                        "Play_vo_Rengar_FirstEncounter3DKhazix"
                        "Play_vo_Rengar_Joke3DGeneral"
                        "Play_vo_Rengar_Laugh3DGeneral"
                        "Play_vo_Rengar_Move2DStandard"
                        "Play_vo_Rengar_RengarBasicAttack2_cast3D"
                        "Play_vo_Rengar_RengarBasicAttack3_cast3D"
                        "Play_vo_Rengar_RengarBasicAttack_cast3D"
                        "Play_vo_Rengar_RengarCritAttack_cast3D"
                        "Play_vo_Rengar_RengarE_cast3D"
                        "Play_vo_Rengar_RengarEEmp_cast3D"
                        "Play_vo_Rengar_RengarQ_cast3D"
                        "Play_vo_Rengar_RengarQEmp_cast3D"
                        "Play_vo_Rengar_RengarR_cast3D"
                        "Play_vo_Rengar_RengarW_cast3D"
                        "Play_vo_Rengar_RengarWEmp_cast3D"
                        "Play_vo_Rengar_Spell3DPStackFive"
                        "Play_vo_Rengar_Spell3DPStackFour"
                        "Play_vo_Rengar_Spell3DPStackOne"
                        "Play_vo_Rengar_Spell3DPStackThree"
                        "Play_vo_Rengar_Spell3DPStackTwo"
                        "Play_vo_Rengar_Taunt3DGeneral"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Rengar/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin03/rengar_Skin03.skl"
            simpleSkin: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin03/rengar_Skin03.skn"
            texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin03/rengar_Skin03_TX_CM.tex"
            skinScale: f32 = 0.95
            selfIllumination: f32 = 0.7
            overrideBoundingBox: option[vec3] = {
                { 180, 250, 180 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "MinimalMesh"
        }
        armorMaterial: string = "Flesh"
        mContextualActionData: link = "Characters/Rengar/CAC/Rengar_Base"
        iconCircle: option[string] = {
            "ASSETS/Repath/Characters/Rengar/HUD/Rengar_Circle_0.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Repath/Characters/Rengar/HUD/Rengar_Square_0.tex"
        }
        iconAvatar: string = "ASSETS/Repath/Characters/Rengar/HUD/Rengar_Circle_3.tex"
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
        }
        mEmblems: list[embed] = {
            SkinEmblem {
                mEmblemData: link = "Emblems/1"
            }
        }
        mResourceResolver: link = "Characters/Rengar/Skins/Skin3/Resources"
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = DelayedBoolMaterialDriver {
                    mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                        mScriptName: string = "RengarR"
                    }
                    mDelayOn: f32 = 2
                }
                SubmeshesToShow: list2[hash] = {
                    "MinimalMesh"
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = AllTrueMaterialDriver {
                    mDrivers: list[pointer] = {
                        IsAnimationPlayingDynamicMaterialBoolDriver {
                            mAnimationNames: list[hash] = {
                                "TransparencyFix"
                            }
                        }
                        NotMaterialDriver {
                            mDriver: pointer = IsInGrassDynamicMaterialBoolDriver {}
                        }
                    }
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        effectKey: hash = "Rengar_R_LeapMat"
                    }
                }
            }
        }
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Skin3_R_Leap" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                isSingleParticle: flag = true
                emitterName: string = "Leap3"
                importance: u8 = 3
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -2001
                meshRenderFlags: u8 = 0
                blendMode: u8 = 1
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Skin03/Rengar_Skin03_TX_CM.tex"
            }
        }
        particleName: string = "Rengar_Skin3_R_Leap"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Skin3_R_Leap"
    }
    "Characters/Rengar/Skins/Skin3/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Rengar_BA1_Cas" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA1_Cas"
            "Rengar_BA2_Cas" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA2_Cas"
            "Rengar_BA3_Cas" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA3_Cas"
            "Rengar_BA_tar_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_01"
            "Rengar_BA_tar_crit_01" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_crit_01"
            "Rengar_C_Cas" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_C_Cas"
            "Rengar_E_Max_Mis" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Max_Mis"
            "Rengar_E_Max_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Max_Tar"
            "Rengar_E_Mis" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Mis"
            "Rengar_E_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Tar"
            "Rengar_P_Buf_Max" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Max_New"
            "Rengar_P_Buf_Enhanced_Ring" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Enhanced_Ring"
            "Rengar_P_Leap_Grass" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_Grass"
            "Rengar_Q_Buf_Blade" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Buf_Blade"
            "Rengar_Q_Buf_Blade_Max" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Buf_Blade"
            "Rengar_Q_Buf_Claw" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Buf_Claw"
            "Rengar_Q_Buf_Claw_Max" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Buf_Claw"
            "Rengar_Q_Cas2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Cas2"
            "Rengar_Q_Max_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Max_Tar"
            "Rengar_Q_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Tar"
            "Rengar_Q_Tar_Visuals" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Tar_Visuals"
            "Rengar_R_Armor_shred_tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Armor_shred_tar"
            "Rengar_R_Buf" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Buf"
            "Rengar_R_LeapMat" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Skin3_R_Leap"
            "Rengar_R_Primary_Target" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target"
            "Rengar_R_Primary_Target_Enhanced" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target_Enhanced"
            "Rengar_R_Secondary_Target_Sound_Off" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_Off"
            "Rengar_R_Secondary_Target_Sound_On" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_On"
            "Rengar_W_Heal" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Heal"
            "Rengar_W_Max_Roar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Max_Roar"
            "Rengar_W_Max_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Max_Tar"
            "Rengar_W_Roar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Roar"
            "Rengar_W_Tar" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Tar"
            "Rengar_LeapSound_BV2" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_LeapSound"
            "Rengar_R_Screen_Overlay_Target" = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Screen_Overlay_Target"
        }
    }
}
