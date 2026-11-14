#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Rengar_Skin02_R_Buf" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    0.4
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                }
                particleColorTexture: string = "Assets/Particles/color-hold.dds"
                blendMode: u8 = 1
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.1, 1.1, 1.1 }
                }
                texture: string = "Assets/Particles/Rengar_Skin02_R_MatOverride_Self.dds"
                LegacySimple: pointer = VfxEmitterLegacySimple {
                    orientation: u8 = 3
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                particleLinger: option[f32] = {
                    10
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            20
                            40
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.3
                }
                emitterLinger: option[f32] = {
                }
                emitterName: string = "Stealth_Swirls"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -100 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 150, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin02_Z_RGB.dds"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                blendMode: u8 = 2
                colorLookUpTypeY: u8 = 3
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -90, 90 }
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
                            { 1, -90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "Assets/Particles/Rengar_Skin02_R_Cas.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.1 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            25
                            50
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.3
                }
                emitterLinger: option[f32] = {
                }
                emitterName: string = "Stealth_Swirls_Add"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -100 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 150, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "Assets/Particles/Rengar_Skin02_Z_RGB_add.dds"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "Assets/Particles/Rengar_Skin02_Z_Sphere.sco"
                    }
                }
                colorLookUpTypeY: u8 = 3
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.05
                    fresnelColor: vec4 = { -1, -1, -1, -1 }
                }
                disableBackfaceCull: bool = false
                isLocalOrientation: flag = true
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -90, 90 }
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
                            { 1, -90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "Assets/Particles/Rengar_Skin02_R_Cas.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.25, 0.1 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
        }
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        priority: i32 = 2000
                        baseTexture: string = "Assets/Particles/Rengar_Skin02_R_MatOverride_Self.dds"
                        transitionTexture: string = "Assets/Particles/Rengar_Skin02_R_MaterialOverrideTrans.dds"
                        transitionSample: f32 = 0.5
                    }
                }
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    7
                }
                emitterName: string = "Glows"
                particleColorTexture: string = "Assets/Particles/color-bellcurve3.dds"
                blendMode: u8 = 4
                meshRenderFlags: u8 = 0
            }
        }
        particleName: string = "Rengar_Skin02_R_Buf"
        particlePath: string = "Rengar_Skin02_R_Buf"
    }
}
