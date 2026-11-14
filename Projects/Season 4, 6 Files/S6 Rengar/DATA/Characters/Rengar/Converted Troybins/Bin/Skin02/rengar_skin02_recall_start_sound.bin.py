#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "rengar_skin02_recall_start_sound" = VfxSystemDefinitionData {
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
        particleName: string = "rengar_skin02_recall_start_sound"
        particlePath: string = "rengar_skin02_recall_start_sound"
        soundPersistentDefault: string = "Play_rengar_skin02_recall_leadin"
        flags: u16 = 164
    }
}
