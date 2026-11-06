#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin01_R_Tar" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        baseTexture: string = "Assets/Particles/Rengar_Skin01_R_Tar_MaterialOverride.dds"
                    }
                }
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                }
                emitterName: string = "Base_Hunter"
                importance: u8 = 2
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_R_Veins.dds"
                meshRenderFlags: u8 = 0
                pass: i16 = 60
                isRandomStartFrame: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_R.dds"
                uvMode: u8 = 1
                numFrames: u16 = 16
                texDiv: vec2 = { 0.5, 0.5 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 0
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Color_Hunter"
                particleColorTexture: string = "Assets/Particles/Rengar_Skin01_R_RGB.dds"
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                pass: i16 = 5
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                texture: string = "Assets/Particles/Rengar_Skin01_R.dds"
                uvMode: u8 = 1
                numFrames: u16 = 16
                texDiv: vec2 = { 2, 2 }
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 1.0199999809265137
                    }
                    orientation: u8 = 3
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.1, 0 }
                }
            }
        }
        particleName: string = "Rengar_Skin01_R_Tar"
        particlePath: string = "Rengar_Skin01_R_Tar"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarR_buffactivateheartbeat"
    }
}


Troygrade was unable to translate the following properties: 
Base_Hunter: MaterialOverride1BlendMode = 1
