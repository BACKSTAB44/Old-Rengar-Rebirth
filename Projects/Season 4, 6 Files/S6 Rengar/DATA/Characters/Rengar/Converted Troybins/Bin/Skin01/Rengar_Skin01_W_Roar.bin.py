#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_W_Roar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
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
                emitterName: string = "Base_Hunter"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                    }
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Fade_RGB.dds"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                isLocalOrientation: flag = false
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 600, 600 }
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
                texture: string = "Assets/Particles/Rengar_Skin01_W_ShoutRing_Spikes.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    orientation: u8 = 2
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "ShellRing_Add_Hunter"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.7
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
                pass: i16 = 20
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 350, 350 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.4, 0.4, 0.4 }
                            { 0.5, 0.5, 0.5 }
                            { 1.2, 1.2, 1.2 }
                            { 1.4, 1.4, 1.4 }
                        }
                    }
                }
                texture: string = "Assets/Particles/Rengar_Skin01_W_Decal.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                }
                emitterName: string = "ShellDistort"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Rampdown_RGBA.dds"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                pass: i16 = 100
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.03999999910593033
                    distortionMode: u8 = 1
                    normalMapTexture: string = "Assets/Particles/Rengar_Skin01_Z_Distortion_NormalMap.dds"
                }
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_Z_Distortion.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 450
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.4
                                0.6
                                1
                            }
                            values: list[f32] = {
                                0
                                0.7
                                0.9
                                1
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.1
                }
                isSingleParticle: flag = true
                emitterName: string = "ShellRing_Hunter"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Fade_RGB.dds"
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_W_Decal_NoAlpha.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 350
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.3
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.4
                                0.5
                                1.2
                                1.4
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing_Sub_Hunter"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_RGB.dds"
                blendMode: u8 = 2
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_W_Ring_Sub.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 575
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.4
                                0.6
                                1
                            }
                            values: list[f32] = {
                                0
                                0.7
                                0.9
                                1
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
        }
        particleName: string = "Rengar_Skin01_W_Roar"
        particlePath: string = "Rengar_Skin01_W_Roar"
    }
}
