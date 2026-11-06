#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_R_Cas" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    ".1w"
                }
                emitterName: string = "base_Hunter"
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
        particleName: string = "Rengar_Skin01_R_Cas"
        particlePath: string = "Rengar_Skin01_R_Cas"
    }
}
