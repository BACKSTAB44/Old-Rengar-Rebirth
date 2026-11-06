#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_R_Alert" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                particleLinger: option[f32] = {
                    10
                }
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    25000
                }
                isSingleParticle: flag = true
                emitterName: string = "yikes"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 90, 0 }
                    }
                }
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isLocalOrientation: flag = false
                texture: string = "Assets/Particles/Rengar_Base_R_Exclamation.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 30
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    25000
                }
                isSingleParticle: flag = true
                emitterName: string = "yikes2"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 90, 0 }
                    }
                }
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                sliceTechniqueRange: f32 = 0.2
                pass: i16 = 2
                isLocalOrientation: flag = false
                texture: string = "Assets/Particles/Rengar_Base_R_Slice.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 30
                    }
                    particleBind: vec2 = { 1, 1 }
                }
            }
        }
        particleName: string = "Rengar_Base_R_Alert"
        particlePath: string = "Rengar_Base_R_Alert"
    }
}


Troygrade was unable to translate the following properties: 
yikes2: p-texture-pixelate = 1
