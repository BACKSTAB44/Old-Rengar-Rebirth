#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_W_Max_Buf" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "base"
                importance: u8 = 2
                particleColorTexture: string = "Assets/Particles/Rengar_Base_Z_RGB.dds"
                blendMode: u8 = 2
                meshRenderFlags: u8 = 0
                pass: i16 = 100
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                texture: string = "Assets/Particles/Rengar_Base_Z_Avatar.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 1.1
                    }
                    particleBind: vec2 = { 0.5, 0.5 }
                    orientation: u8 = 3
                }
            }
        }
        particleName: string = "Rengar_Base_W_Max_Buf"
        particlePath: string = "Rengar_Base_W_Max_Buf"
    }
}
