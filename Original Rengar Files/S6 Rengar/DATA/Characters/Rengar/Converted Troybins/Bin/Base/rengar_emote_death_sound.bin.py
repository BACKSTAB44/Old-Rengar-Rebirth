#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "rengar_emote_death_sound" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
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
        particleName: string = "rengar_emote_death_sound"
        particlePath: string = "rengar_emote_death_sound"
        soundOnCreateDefault: string = "Play_sfx_Rengar_Death3D_cast"
        flags: u16 = 132
    }
}
