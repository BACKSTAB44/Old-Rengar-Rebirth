#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Screen_Overlay_Target" = TextureResource {
        texturePath: string = "ASSETS/Repath/Characters/Rengar/HUD/Rengar_Base_R_screen_overlay_target.tex"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "eyes"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.4353 }
                        }
                    }
                }
                pass: i16 = 100
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 0 }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_tar_vision_eye.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.4
                }
                particleLinger: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "wisp1"
                importance: u8 = 3
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.6667, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.6667, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 200
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 90, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec3] = {
                            { 2, 0.6, 1 }
                            { 2, 1, 1 }
                            { 2, 1.2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/talon_base_w_mis_02_spark.tex"
            }
        }
        particleName: string = "Rengar_Base_R_Primary_Target"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target"
        flags: u16 = 197
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target_Enhanced" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Heart"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 120, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 1
                pass: i16 = 61
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.4
                            0.45
                            1
                        }
                        values: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 2.5, 2.5, 2.5 }
                            { 1, 1, 1 }
                            { 4, 4, 4 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_Heart.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "HeartAdd"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 120, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                }
                pass: i16 = 100
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.4
                            0.45
                            1
                        }
                        values: list[vec3] = {
                            { 0.2, 0.2, 0.2 }
                            { 2.5, 2.5, 2.5 }
                            { 1, 1, 1 }
                            { 4, 4, 4 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_Heart.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                importance: u8 = 3
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.28, 0, 0, 1 }
                }
                meshRenderFlags: u8 = 0
                blendMode: u8 = 1
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Repath/Shared/Particles/3161common_color-hold.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "VeinsAdd"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                importance: u8 = 3
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.6, 0, 0, 1 }
                }
                blendMode: u8 = 4
                pass: i16 = 60
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_Veins_Add.tex"
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.4
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 1.03, 1.03, 1.03 }
                            { 1.1, 1.1, 1.1 }
                            { 1.03, 1.03, 1.03 }
                            { 1.1, 1.1, 1.1 }
                            { 1.03, 1.03, 1.03 }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Base_R_Primary_Target_Enhanced"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Primary_Target_Enhanced"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarR_buffactivateheartbeat"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_On" = VfxSystemDefinitionData {
        particleName: string = "Rengar_Base_R_Secondary_Target_Sound_On"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_On"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarRSecondaryTarget_start"
        flags: u16 = 132
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Armor_shred_tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.15
                }
                lifetime: option[f32] = {
                    2
                }
                emitterName: string = "fireLine"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.502 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.85 }
                            { 0.5, 0.5, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 65, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.8, 0 }
                            { 1, 1, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/Item_BlackCleaver_shield_laser.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                isSingleParticle: flag = true
                emitterName: string = "fireLine1"
                importance: u8 = 3
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.43, 0.24, 0.51, 0.41 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.05
                            0.95
                            1
                        }
                        values: list[vec4] = {
                            { 0.43, 0.24, 0.51, 0 }
                            { 0.43, 0.24, 0.51, 0.41 }
                            { 0.43, 0.24, 0.51, 0.3485 }
                            { 0.215, 0.12, 0.51, 0 }
                        }
                    }
                }
                pass: i16 = 4
                depthBiasFactors: vec2 = { -1, -60 }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 36, 30, 30 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0117
                            0.9558
                            0.9795
                            0.9932
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.9398, 0.5538, 0.5538 }
                            { 0.6054, 0.063, 0.063 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/Armor_Pen.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                lifetime: option[f32] = {
                    2
                }
                emitterName: string = "fireLine2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.3333, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.4
                            1
                        }
                        values: list[vec4] = {
                            { 0.3333, 0, 0, 0 }
                            { 0.3333, 0, 0, 1 }
                            { 0.3333, 0, 0, 0.85 }
                            { 0.1667, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 65, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.8, 0 }
                            { 1, 1, 0 }
                            { 0.5, 0.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Distortion.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.7
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.15
                }
                lifetime: option[f32] = {
                    4
                }
                emitterName: string = "fireLine3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.85 }
                            { 0.5, 0.5, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 65, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.8, 0 }
                            { 1, 1, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/Item_BlackCleaver_shield_laser.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                isSingleParticle: flag = true
                emitterName: string = "fireLine4"
                importance: u8 = 3
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.82 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.05
                            0.95
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.82 }
                            { 1, 1, 1, 0.697 }
                            { 0.5, 0.5, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                depthBiasFactors: vec2 = { -1, -60 }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 32, 30, 30 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0117
                            0.9558
                            0.9795
                            0.9932
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.9398, 0.5538, 0.5538 }
                            { 0.6054, 0.063, 0.063 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/Armor_Pen.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Flare"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.75 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.75 }
                            { 1, 1, 1, 0.75 }
                            { 1, 1, 1, 0.6 }
                            { 0.3333, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    6
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 150, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 150, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.7, 0.7, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.56, 0.56, 0.8 }
                            { 0.07, 1.05, 1.3 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/SRUAP_Order_Nexus_sparkleGold.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    0.75
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.2
                }
                lifetime: option[f32] = {
                    2
                }
                emitterName: string = "SoftBeams"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, -50 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    0.6
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.9059, 0.3608, 0.4 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.9059, 0.3608, 0 }
                            { 1, 0.9059, 0.3608, 0.4 }
                            { 1, 0.9059, 0.3608, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5001
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0
                                    -45
                                    -135
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0
                                    -180
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 35, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.8
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 35, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                            { 8, 3, 0 }
                            { 3, 5, 0 }
                            { 1, 7, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/Item_BlackCleaver_SoftRays_4x1.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 1 }
            }
        }
        particleName: string = "Rengar_Base_R_Armor_shred_tar"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Armor_shred_tar"
        flags: u16 = 204
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Enhanced_Ring" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Ring"
                importance: u8 = 3
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Ring_RGB.tex"
                colorRenderFlags: u8 = 1
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 855, 855, 0 }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Ring.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Ring_FX"
                importance: u8 = 3
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 805, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Heal_Spark_RGBA.tex"
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 20, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 10, 5, 1 }
                            { 30, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "Rengar_Base_P_Buf_Enhanced_Ring"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Buf_Enhanced_Ring"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_LeapSound" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "empty"
                meshRenderFlags: u8 = 0
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0 }
                }
                isUniformScale: flag = true
                texture: string = "ASSETS/Repath/Shared/Particles/3161common_color-hold.tex"
            }
        }
        particleName: string = "Rengar_LeapSound"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_LeapSound"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarP_cast"
        flags: u16 = 148
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_Off" = VfxSystemDefinitionData {
        particleName: string = "Rengar_Base_R_Secondary_Target_Sound_Off"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target_Sound_Off"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarRSecondaryTarget_end"
        flags: u16 = 132
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_crit_01" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.55
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.55
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.55
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "fluid"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 3
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 15
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isDirectionOriented: flag = true
                IsRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 8, 8, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-firefade.tex"
                blendMode: u8 = 4
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_hiteffect.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "ring"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Rampdown_RGB.tex"
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 0.5, 1 }
                colorLookUpOffsets: vec2 = { 0.5, 0 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_blast_nova_bunny_04.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            30
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "blood_drops"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            40
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_z_rampdown_rgba.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_blurdrops.tex"
                frameRate: f32 = 1
                numFrames: u16 = 16
                startFrame: u16 = 15
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 800
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.7
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.1
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "soft"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 16
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 8, 8, 8 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Rengar_Base_BA_tar_crit_01"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_crit_01"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_01" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.55
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.55
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.55
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "fluid"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        valueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 3
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 15
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22.5, 22.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 22.5, 22.5, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 8, 8, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-hit-physical.tex"
                pass: i16 = 10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 150 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_hiteffect.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "blood_drops"
                importance: u8 = 1
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            40
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_z_rampdown_rgba.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_blurdrops.tex"
                frameRate: f32 = 1
                numFrames: u16 = 16
                startFrame: u16 = 15
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "soft"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 16
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 8, 8, 8 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Rengar_Base_BA_tar_01"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_BA_tar_01"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_Grass" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.15
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Grass_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 300, 1000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.3
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 300, 1000 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.2
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 90, 40 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 90, 40 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 300, 300 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 22, 22 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 22, 22, 22 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_P_Leap_Grass.tex"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
        }
        particleName: string = "Rengar_Base_P_Leap_Grass"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_P_Leap_Grass"
        soundOnCreateDefault: string = "Play_sfx_Old_RengarP_Leap_Grass"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Heal" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterName: string = "healspark"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 800, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1, 3 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 60, 25, 60 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.51
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        -0.5
                                        0.5
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        0.51
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        -0.5
                                        0.5
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 60, 25, 60 }
                            }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Heal_Spark_RGBA.tex"
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.3
                            0.6
                            1
                        }
                        values: list[vec3] = {
                            { 0.1, 0.1, 0.1 }
                            { 0.3, 0.3, 0.3 }
                            { 1, 10, 1 }
                            { 0.3, 0.3, 0.3 }
                            { 0.1, 0.1, 0.1 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Heal_Spark.tex"
            }
        }
        particleName: string = "Rengar_Base_W_Heal"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Heal"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Tar_Visuals" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 600
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.55
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.55
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "fluid"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 3
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 15
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 8, 8, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 125, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-hit-physical.tex"
                pass: i16 = 10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 150 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_hiteffect.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            30
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "blood_drops"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.7
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            40
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_z_rampdown_rgba.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_blurdrops.tex"
                frameRate: f32 = 1
                numFrames: u16 = 16
                startFrame: u16 = 15
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.8
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            isLocalSpace: bool = false
                            acceleration: embed = ValueVector3 {
                                constantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 300, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            strength: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                        }
                    }
                }
                emitterName: string = "soft"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.3
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Shared/Particles/common_color-whiteweb32.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 16
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 8, 8, 8 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Shared/Particles/common_0fluid.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.15
                }
                emitterName: string = "blood_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 1 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Rampdown_RGBA.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                texture: string = "ASSETS/Repath/Shared/Particles/common_blurdrops.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 180, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 6, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 450
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.3
                }
                emitterLinger: option[f32] = {
                    -1
                }
                emitterName: string = "blood_02"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            10
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1 }
                        { 0, 1, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_Rampdown_RGBA.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                texture: string = "ASSETS/Repath/Shared/Particles/common_blurdrops.tex"
                frameRate: f32 = 16
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 180, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.4
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 6, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Base_Q_Tar_Visuals"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Tar_Visuals"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.75
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Net"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.006
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Net.scb"
                    }
                }
                blendMode: u8 = 1
                doesCastShadow: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 80, 150 }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Net.tex"
            }
        }
        particleName: string = "Rengar_Base_E_Max_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Max_Tar"
        overrideScaleCap: option[f32] = {
            500
        }
        soundOnCreateDefault: string = "Play_sfx_Old_RengarEEmp_OnHit"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    11.5
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "cursebandages"
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.007
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.007
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Wrap.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 1, 30 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 0.5, 0.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.9
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                            { 0.4, 0.4, 0.4 }
                            { 0.5, 0, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Wrap.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLinger: option[f32] = {
                    12.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Bola"
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.0075
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.0075
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Bola.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.7
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                doesCastShadow: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, -1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, -40, 0 }
                            { 0, -0, 0 }
                            { 0, -0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.8, 0.8, 0.8 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_E_Bola.tex"
            }
        }
        particleName: string = "Rengar_Base_E_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_E_Tar"
        overrideScaleCap: option[f32] = {
            375
        }
        soundOnCreateDefault: string = "Play_sfx_Old_RengarE_hit"
        flags: u16 = 198
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    10.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_RGB.tex"
                blendMode: u8 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_ShoutRing.tex"
            }
        }
        particleName: string = "Rengar_Base_W_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Tar"
    }
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.65
                }
                particleLinger: option[f32] = {
                    10.65
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_RGB.tex"
                blendMode: u8 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.34
                            0.55
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.7, 0.7, 0.7 }
                            { 0.9, 0.9, 0.9 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_ShoutRing.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 32
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.2
                }
                lifetime: option[f32] = {
                    0.2
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "Zap"
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 2, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        30
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 2, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                particleColorTexture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Z_RGB.tex"
                blendMode: u8 = 2
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.65
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 65, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 4, 0, 0 }
                            { 4, 3, 0 }
                            { 0, 5.5, 0 }
                        }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                }
                texture: string = "ASSETS/Repath/Characters/Rengar/Skins/Base/Particles/Rengar_Base_W_Barbs.tex"
            }
        }
        particleName: string = "Rengar_Base_W_Max_Tar"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_W_Max_Tar"
    }
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
