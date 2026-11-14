#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin02_R_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Heart"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                    scaleBirthScaleByBoundObjectSize: f32 = 0.004999999888241291
                }
                blendMode: u8 = 1
                pass: i16 = 50
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
                texture: string = "Assets/Particles/Rengar_Skin02_R_Heart.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "HeartAdd"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.004999999888241291
                    scaleBirthScaleByBoundObjectSize: f32 = 0.004999999888241291
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
                texture: string = "Assets/Particles/Rengar_Skin02_R_Heart.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        baseTexture: string = "Assets/Particles/Rengar_Skin02_R_MaterialOverride.dds"
                    }
                }
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
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                }
                emitterName: string = "Skin02"
                importance: u8 = 2
                particleColorTexture: string = "Assets/Particles/Rengar_Skin02_R_Veins_Red.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 60
                texture: string = "Assets/Particles/Rengar_Skin02_R_Veins.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 0
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "Veins_Add"
                importance: u8 = 2
                particleColorTexture: string = "Assets/Particles/Rengar_Skin02_R_Veins_Red.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 10
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin02_R_Veins_Add.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 1
                    }
                    scale: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.2
                                0.4
                                0.6
                                1
                            }
                            values: list[f32] = {
                                1
                                1.1
                                1
                                1.1
                                1
                            }
                        }
                    }
                    orientation: u8 = 3
                }
            }
        }
        particleName: string = "Rengar_Skin02_R_Tar"
        particlePath: string = "Rengar_Skin02_R_Tar"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarR_buffactivateheartbeat"
    }
}


Troygrade was unable to translate the following properties: 
Skin02: MaterialOverride1BlendMode = 0.0
