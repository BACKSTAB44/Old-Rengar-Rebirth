#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin02_Q_Buf_AttackSpeed" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                particleLinger: option[f32] = {
                    10
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3
                }
                emitterLinger: option[f32] = {
                }
                emitterName: string = "AS_Mesh_ADD"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.76
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 10
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.2
                    fresnelColor: vec4 = { -0.8, -0.8, -0.8, -0.8 }
                }
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "Assets/Particles/Rengar_Skin02_Q_Buf_Blade_Flame_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.25 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.25, 0.25 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.7
                }
                particleLinger: option[f32] = {
                    0.7
                }
                lifetime: option[f32] = {
                    3
                }
                emitterLinger: option[f32] = {
                }
                emitterName: string = "AS_Mesh_Sub"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                blendMode: u8 = 2
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.76
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -10
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.01
                    fresnelColor: vec4 = { -0.8, -0.5, -0.8, -0.8 }
                }
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "Assets/Particles/Rengar_Skin02_Q_Buf_Blade_Flame_2x2_Sub.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.25 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.25, 0.25 }
                        }
                    }
                }
            }
        }
        particleName: string = "Rengar_Skin02_Q_Buf_AttackSpeed"
        particlePath: string = "Rengar_Skin02_Q_Buf_AttackSpeed"
        soundPersistentDefault: string = "Play_sfx_Rengar_RengarQ_buffactivate"
    }
}
