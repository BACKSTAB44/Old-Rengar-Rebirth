#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_R_Alert_Sound" = VfxSystemDefinitionData {
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
        particleName: string = "Rengar_Base_R_Alert_Sound"
        particlePath: string = "Rengar_Base_R_Alert_Sound"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarRTeamIndicator_buffactivate"
        flags: u16 = 132
    }
}
