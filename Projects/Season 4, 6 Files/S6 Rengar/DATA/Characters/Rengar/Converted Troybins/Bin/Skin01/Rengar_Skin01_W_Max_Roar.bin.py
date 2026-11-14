#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_W_Max_Roar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                particleLinger: option[f32] = {
                    10
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
                emitterName: string = "ShellRing_Hunter_Sub"
                importance: u8 = 2
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
                            0.6
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 350, 350 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.45
                            1
                        }
                        values: list[vec3] = {
                            { 0.6, 0.6, 0.6 }
                            { 0.7, 0.7, 0.7 }
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
                    distortion: f32 = 0.1
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
                pass: i16 = 30
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
                                0.6
                                0.7
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
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing_ULT_Add_Hunter"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Fade_RGB.dds"
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                pass: i16 = 20
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_W_Max_Ring.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 500
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                0.45
                                1
                            }
                            values: list[f32] = {
                                { 0.6, 0.6, 0.6 }
                                { 0.7, 0.7, 0.7 }
                                { 1.2, 1.2, 1.2 }
                                { 1.4, 1.4, 1.4 }
                            }
                        }
                    }
                    particleBind: vec2 = { 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.1
                }
                emitterName: string = "ShellRing_Sub"
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
        particleName: string = "Rengar_Skin01_W_Max_Roar"
        particlePath: string = "Rengar_Skin01_W_Max_Roar"
    }
}
