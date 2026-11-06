#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_R_TeamIndicator" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Eye"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 240, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                    scaleBirthScaleByBoundObjectSize: f32 = 0.004999999888241291
                }
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                pass: i16 = 50
                miscRenderFlags: u8 = 1
                texture: string = "Assets/Particles/Rengar_Base_R_TeamIndicator.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 150
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Eye_Glow"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 240, 0 }
                    }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                    scaleBirthScaleByBoundObjectSize: f32 = 0.004999999888241291
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Base_W_Heal_Spark_RGBA.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 50
                miscRenderFlags: u8 = 1
                texture: string = "Assets/Particles/Rengar_Base_R_TeamIndicator_Glow.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 150
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    birthRotation: embed = ValueFloat {
                        constantValue: f32 = 10
                        dynamics: pointer = VfxAnimatedFloatVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[f32] = {
                                10
                            }
                        }
                    }
                    particleBind: vec2 = { 1, 1 }
                    birthRotationalVelocity: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        30
                                        70
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
            }
        }
        particleName: string = "Rengar_Base_R_TeamIndicator"
        particlePath: string = "Rengar_Base_R_TeamIndicator"
    }
}
