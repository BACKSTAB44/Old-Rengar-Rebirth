#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_R_Buf" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        baseTexture: string = "Assets/Particles/Rengar_Skin01_Z_Avatar.dds"
                    }
                }
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.05
                }
                particleLinger: option[f32] = {
                    10.05
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                }
                emitterName: string = "base_Hunter"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_White.dds"
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = 0
                }
                texture: string = "Assets/Particles/Rengar_Skin01_Z_White.dds"
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                }
                emitterName: string = "Type11_Hunter"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Bellcurve_RGB.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 100
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_Z_Avatar.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 1.0299999713897705
                    }
                    particleBind: vec2 = { 0, 0 }
                    orientation: u8 = 3
                }
            }
        }
        particleName: string = "Rengar_Skin01_R_Buf"
        particlePath: string = "Rengar_Skin01_R_Buf"
    }
}


Troygrade was unable to translate the following properties: 
base_Hunter: MaterialOverride1BlendMode = 3
