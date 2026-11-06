#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "rengar_emote_taunt_sound" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "Assets/Particles/black.dds"
                meshRenderFlags: u8 = 0
                texture: string = "Assets/Particles/black.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 0
                    }
                }
            }
        }
        particleName: string = "rengar_emote_taunt_sound"
        particlePath: string = "rengar_emote_taunt_sound"
        soundPersistentDefault: string = "Play_sfx_Rengar_Taunt3D_buffactivate"
        flags: u16 = 132
    }
}
