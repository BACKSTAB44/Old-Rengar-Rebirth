#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_BA1_Cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                particleLinger: option[f32] = {
                    10
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3499999940395355
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashBase_Hunter"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 110, 80, 50 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin01_BA_WeaponTrail.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, -120, -10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "Assets/Particles/Rengar_Skin01_Z_WeaponTrail.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 1 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3499999940395355
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    0.2
                }
                isSingleParticle: flag = true
                emitterName: string = "SlashAdd_Hunter"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 110, 80, 50 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin01_BA_WeaponTrail.sco"
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, -120, -10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 50, 100 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "Assets/Particles/Rengar_Skin01_Z_WeaponTrail.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 1 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    orientation: u8 = 1
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -2.5 }
                }
            }
        }
        particleName: string = "Rengar_Skin01_BA1_Cas"
        particlePath: string = "Rengar_Skin01_BA1_Cas"
        flags: u16 = 198
    }
}


Troygrade was unable to translate the following properties: 
SlashAdd_Hunter: e-censor-modulate = 0.0 0.0 0.0 1.0
SlashBase_Hunter: e-censor-modulate = 0.0 0.0 0.0 1.0
