#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_W_Buf" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "base_Hunter"
                importance: u8 = 2
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_Z_Bellcurve_RGB.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 100
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_Z_Avatar.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 1.1
                    }
                    particleBind: vec2 = { 0.5, 0.5 }
                    orientation: u8 = 3
                }
            }
        }
        particleName: string = "Rengar_Skin01_W_Buf"
        particlePath: string = "Rengar_Skin01_W_Buf"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarWArmorMR_buffactivate"
    }
}
