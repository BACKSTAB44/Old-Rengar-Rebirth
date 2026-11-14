#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_P_Leap_Dust" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            strength: embed = ValueFloat {
                                constantValue: f32 = 4
                            }
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 0, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                        }
                    }
                }
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.1
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
                            1.1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Dust_Trail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 100, 500 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 100, 500 }
                        }
                    }
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_P_Leap_Dust_RGBA.dds"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                isLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_P_Leap_Dust.dds"
                texDiv: vec2 = { 2, 2 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 80
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.6
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                80
                            }
                        }
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.5
                                1.2
                                1.5
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
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
                    particleBind: vec2 = { 0, 0 }
                }
            }
        }
        particleName: string = "Rengar_Skin01_P_Leap_Dust"
        particlePath: string = "Rengar_Skin01_P_Leap_Dust"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarQ_hit"
    }
}
