#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.24
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "dArK_bg"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.6471, 0.2314, 0.2314, 1 }
                            { 0.3333, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 70
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1.7, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/SRU_Chaos_activation_flash.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Eye_back"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 130, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.1373, 0, 0, 1 }
                }
                pass: i16 = -5
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 120, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_mult.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.2, 0 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_R_tar_vision_eye_glow.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "groundshadow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.005
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.005
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.3333, 0, 0, 0.5216 }
                }
                pass: i16 = -11
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 120, 10 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_z_alpha_circle.tex"
            }
        }
        particleName: string = "Rengar_Base_R_Secondary_Target"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_R_Secondary_Target"
        flags: u16 = 197
    }
}
