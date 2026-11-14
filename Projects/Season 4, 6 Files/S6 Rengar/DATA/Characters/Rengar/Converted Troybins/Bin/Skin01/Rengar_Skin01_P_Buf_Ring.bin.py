#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_P_Buf_Ring" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Ring"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Ring_RGB.dds"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 820, 820, 0 }
                }
                texture: string = "Assets/Particles/Rengar_Skin01_Z_Ring.dds"
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
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Ring_FX"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 700, 0, 0 }
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
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_W_Heal_Spark_RGBA.dds"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 40, 10 }
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
                texture: string = "Assets/Particles/Rengar_Skin01_P_Shafts.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                scaleBias: vec2 = { 1.5, 1 }
            }
        }
        particleName: string = "Rengar_Skin01_P_Buf_Ring"
        particlePath: string = "Rengar_Skin01_P_Buf_Ring"
    }
}


Troygrade was unable to translate the following properties: 
Ring: teamcolor-correction = 1
