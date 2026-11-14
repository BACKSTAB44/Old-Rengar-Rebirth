#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_W_Tar" = VfxSystemDefinitionData {
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
                particleColorTexture: string = "Assets/Particles/Rengar_Base_Z_RGB.dds"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 2
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -250, 0 }
                }
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
                texture: string = "Assets/Particles/Rengar_Base_W_ShoutRing.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    orientation: u8 = 2
                }
            }
        }
        particleName: string = "Rengar_Base_W_Tar"
        particlePath: string = "Rengar_Base_W_Tar"
    }
}
