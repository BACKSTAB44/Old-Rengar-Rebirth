#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Strike" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.05
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.35
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1.05
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Swipe1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -50, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_mesh_swipes_02.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.2
                            0.5
                            0.8
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.149, 0.2902, 0.2941, 0 }
                            { 0.1216, 0.251, 0.3529, 0 }
                        }
                    }
                }
                pass: i16 = 2
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.3, 1 }
                            { 1, 1, 1 }
                            { 0.7, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_base_Q_swipe_tex.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -2.8, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.1 }
                }
                texDiv: vec2 = { 1, 1.5 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.05
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    1.05
                }
                isSingleParticle: flag = true
                emitterName: string = "bottom_dark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 300 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.1059, 0.498, 0.6039 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.2
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 260, 120, 0 }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_ground_swipe.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.3
                }
                lifetime: option[f32] = {
                    1.1
                }
                isSingleParticle: flag = true
                emitterName: string = "Bright_glow"
                importance: u8 = 3
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 500 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 60, 300 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.1
                            0.25
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0.498, 0 }
                            { 0.6667, 0.3686, 0.1059, 0.8157 }
                            { 0.4078, 0, 0, 0.4784 }
                            { 0.3333, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 4
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 2, 0 }
                            { 2, 2, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Yorick_Base_R_Aura_self.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.8
                                    0.9
                                }
                                keyValues: list[f32] = {
                                    0.1
                                    0.3
                                    0.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.4
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "mesh_Sparkles_right"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 3000 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 12 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 50, 20, 150 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 70, 150 }
                }
                blendMode: u8 = 5
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.251 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.3
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.3647, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.15
                            1
                        }
                        values: list[vec3] = {
                            { 3, 3, 1 }
                            { 0.3, 2, 1 }
                            { 0.15, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rengar/Skins/Base/Particles/Rengar_Base_Q_Shafts.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Rengar_Base_Q_Strike"
        particlePath: string = "Characters/Rengar/Skins/Skin0/Particles/Rengar_Base_Q_Strike"
    }
}
