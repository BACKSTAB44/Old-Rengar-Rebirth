#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Base_E_Max_Tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.75
                }
                particleLinger: option[f32] = {
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                }
                emitterName: string = "Net"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.006000000052154064
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Base_E_Net.sco"
                    }
                }
                blendMode: u8 = 1
                isLocalOrientation: flag = false
                doesCastShadow: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 80, 150 }
                }
                texture: string = "Assets/Particles/Rengar_Base_E_Net.dds"
            }
        }
        particleName: string = "Rengar_Base_E_Max_Tar"
        particlePath: string = "Rengar_Base_E_Max_Tar"
        soundOnCreateDefault: string = "Play_sfx_Rengar_RengarEFinalMAX_hit"
        flags: u16 = 198
        overrideScaleCap: option[f32] = {
            500
        }
    }
}
