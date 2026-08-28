#BLND_text
# Legacy r3d2blnd -> human-readable translation
# Legacy evidence corpus: 788 BLND files from patch 4.21
# Modern semantic comparison: patch 8.19 BIN/PY
# Confirmed fields have no evidence comments.
# Unknown fields use concise UNKNOWN/guesses comments; strong-evidence unresolved fields use a two-line UNKNOWN marker.

type: string = "BLND"
file: string = "HunterRengar.blnd"

header: LegacyBlndHeader = {
    magic: string = "r3d2blnd"
    version: u32 = 1
    unknown_0c: u32 = 0
    # UNKNOWN: no strong enough evidence
    # might be: reserved header field - global flags/options field whose default is zero - obsolete/runtime-only metadata field
    unknown_10: string = "0x5a40c9dd"
    # UNKNOWN: no strong enough evidence
    # might be: class/type hash or fixed type tag - serialization schema/format identifier - runtime type-registration identifier
    unknown_14: u32 = 0
    # UNKNOWN: no strong enough evidence
    # might be: reserved header field - global flags/options field whose default is zero - obsolete/runtime-only metadata field - global feature flags/options - obsolete runtime metadata
    clip_count: u32 = 29
    time_blend_count: u32 = 107
    transition_source_group_count: u32 = 0
    track_count: u32 = 4
    resource_count: u32 = 24
    mask_count: u32 = 1
    event_bundle_count: u32 = 10
    use_cascade_blend: bool = false
    use_cascade_blend_raw: u32 = 0
    cascade_blend_value: f32 = 0.0
    time_blend_presence_metadata_3c: u32 = 48
    # UNKNOWN: strong evidence
    # likely: TimeBlend runtime object size - TimeBlend allocation/structure stride - metadata constant enabling the TimeBlend subsystem
    unknown_68: u32 = 0
    # UNKNOWN: no strong enough evidence
    # might be: reserved trailing header field - optional zero-valued offset/pointer slot - runtime/sentinel metadata
    resource_count_2: u32 = 24
    # UNKNOWN: strong evidence
    # likely: reserved field - runtime metadata
    skeleton_hash: hash = "0x4ceab122"
    skeleton_path: string = "characters/rengar/skins/skin01/rengar_hunter.skl"
    skeleton_hash_verified: bool = true
    offsets: embed = {
        transition_table: null = null
        track_table: u32 = 1820
        clip_pointer_table: u32 = 2012
        mask_pointer_table: u32 = 6112
        event_pointer_table: u32 = 7788
        resource_runtime_table: u32 = 7828
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        resource_table: u32 = 7924
        skeleton_string: u32 = 9560
    }
}

mTrackDataList: list[embed] = {
    TrackData {
        index: u32 = 0
        offset: u32 = 1820
        size: u32 = 48
        weight: f32 = 1.0
        blend_mode: u32 = 0
        priority: u32 = 0
        name: string = "channel"
        hash: hash = "0x21c252a4"
    }
    TrackData {
        index: u32 = 1
        offset: u32 = 1868
        size: u32 = 48
        weight: f32 = 1.0
        blend_mode: u32 = 0
        priority: u32 = 1
        name: string = "Actions"
        hash: hash = "0xb5b54664"
    }
    TrackData {
        index: u32 = 2
        offset: u32 = 1916
        size: u32 = 48
        weight: f32 = 1.0
        blend_mode: u32 = 0
        priority: u32 = 2
        name: string = "Spell"
        hash: hash = "0xa96fc6c9"
    }
    TrackData {
        index: u32 = 3
        offset: u32 = 1964
        size: u32 = 48
        weight: f32 = 1.0
        blend_mode: u32 = 0
        priority: u32 = 3
        name: string = "Default"
        hash: hash = "0x933b5bde"
    }
}

mClipDataMap: map[string,pointer] = {
    "Channel" = AtomicClipData {
        index: u32 = 0
        stored_index: u32 = 0
        offset: u32 = 2128
        size: u32 = 80
        hash: hash = "0x21c252a4"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 200
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 0
        animation_path: string = "characters/rengar/skins/base/animations/rengar_channel.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 0
        track_name: string = "channel"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Channel_WNDUP" = AtomicClipData {
        index: u32 = 1
        stored_index: u32 = 1
        offset: u32 = 2208
        size: u32 = 88
        hash: hash = "0xa432c30d"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 91
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 1
        animation_path: string = "characters/rengar/skins/base/animations/rengar_channel_wndpup.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 0
        track_name: string = "channel"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Crit" = AtomicClipData {
        index: u32 = 2
        stored_index: u32 = 2
        offset: u32 = 2296
        size: u32 = 80
        hash: hash = "0x9654058d"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 18
        animation_path: string = "characters/rengar/skins/base/animations/rengar_crit.anm"
        event_bundle_index: u32 = 0
        event_bundle_offset: u32 = 2376
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Crit"
        event_bundle_name_matches: bool = true
    }
    "Dance" = AtomicClipData {
        index: u32 = 3
        stored_index: u32 = 3
        offset: u32 = 2532
        size: u32 = 80
        hash: hash = "0xf815289c"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 323
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 2
        animation_path: string = "characters/rengar/skins/base/animations/rengar_dance.anm"
        event_bundle_index: u32 = 1
        event_bundle_offset: u32 = 2612
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Dance"
        event_bundle_name_matches: bool = true
    }
    "Death" = AtomicClipData {
        index: u32 = 4
        stored_index: u32 = 4
        offset: u32 = 2792
        size: u32 = 80
        hash: hash = "0xbd28bd4d"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 67
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 3
        animation_path: string = "characters/rengar/skins/base/animations/rengar_death.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Idle1" = AtomicClipData {
        index: u32 = 5
        stored_index: u32 = 5
        offset: u32 = 2872
        size: u32 = 80
        hash: hash = "0x9dd9dc06"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 4
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Idle2" = AtomicClipData {
        index: u32 = 6
        stored_index: u32 = 6
        offset: u32 = 2952
        size: u32 = 80
        hash: hash = "0x9cd9da73"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 300
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 5
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle2.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Laugh" = AtomicClipData {
        index: u32 = 7
        stored_index: u32 = 7
        offset: u32 = 3032
        size: u32 = 80
        hash: hash = "0xb695ccbe"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 118
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 6
        animation_path: string = "characters/rengar/skins/base/animations/rengar_laugh.anm"
        event_bundle_index: u32 = 2
        event_bundle_offset: u32 = 3112
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Laugh"
        event_bundle_name_matches: bool = true
    }
    "Run" = AtomicClipData {
        index: u32 = 8
        stored_index: u32 = 8
        offset: u32 = 3292
        size: u32 = 76
        hash: hash = "0x2acd4eca"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 30
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 9
        animation_path: string = "characters/rengar/skins/base/animations/rengar_run1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Run2" = AtomicClipData {
        index: u32 = 9
        stored_index: u32 = 9
        offset: u32 = 3368
        size: u32 = 80
        hash: hash = "0x59335068"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 30
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 10
        animation_path: string = "characters/rengar/skins/base/animations/rengar_run2.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell1" = AtomicClipData {
        index: u32 = 10
        stored_index: u32 = 10
        offset: u32 = 3448
        size: u32 = 80
        hash: hash = "0xb2f63868"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 50
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 11
        animation_path: string = "characters/rengar/skins/base/animations/rengar_spell1.anm"
        event_bundle_index: u32 = 3
        event_bundle_offset: u32 = 3528
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Spell1"
        event_bundle_name_matches: bool = true
    }
    "Spell2" = AtomicClipData {
        index: u32 = 11
        stored_index: u32 = 11
        offset: u32 = 3680
        size: u32 = 80
        hash: hash = "0xb5f63d21"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 40
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 21
        animation_path: string = "characters/rengar/skins/base/animations/rengar_spell2.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: u32 = 0
        mask_name: string = "TopBody"
        track_index: u32 = 2
        track_name: string = "Spell"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell3" = AtomicClipData {
        index: u32 = 12
        stored_index: u32 = 12
        offset: u32 = 3760
        size: u32 = 80
        hash: hash = "0xb4f63b8e"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 56
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 22
        animation_path: string = "characters/rengar/skins/base/animations/rengar_spell3.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell4" = AtomicClipData {
        index: u32 = 13
        stored_index: u32 = 13
        offset: u32 = 3840
        size: u32 = 80
        hash: hash = "0xb7f64047"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 4
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell4_Loop" = AtomicClipData {
        index: u32 = 14
        stored_index: u32 = 14
        offset: u32 = 3920
        size: u32 = 84
        hash: hash = "0xa98dac96"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 4
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell4_Winddown" = AtomicClipData {
        index: u32 = 15
        stored_index: u32 = 15
        offset: u32 = 4004
        size: u32 = 88
        hash: hash = "0x4b07ae2e"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 4
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell5" = AtomicClipData {
        index: u32 = 16
        stored_index: u32 = 16
        offset: u32 = 4092
        size: u32 = 80
        hash: hash = "0xb6f63eb4"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 50
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 19
        animation_path: string = "characters/rengar/skins/base/animations/rengar_dash1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell6" = AtomicClipData {
        index: u32 = 17
        stored_index: u32 = 17
        offset: u32 = 4172
        size: u32 = 80
        hash: hash = "0xb9f6436d"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 4
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Taunt" = AtomicClipData {
        index: u32 = 18
        stored_index: u32 = 18
        offset: u32 = 4252
        size: u32 = 80
        hash: hash = "0xbc9c8463"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 165
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 12
        animation_path: string = "characters/rengar/skins/base/animations/rengar_taunt.anm"
        event_bundle_index: u32 = 4
        event_bundle_offset: u32 = 4332
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Taunt"
        event_bundle_name_matches: bool = true
    }
    "Raw_LionGuy_recall" = AtomicClipData {
        index: u32 = 19
        stored_index: u32 = 19
        offset: u32 = 4512
        size: u32 = 92
        hash: hash = "0x602b063d"
        flags: u32 = 8
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 44
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 7
        animation_path: string = "characters/rengar/skins/base/animations/rengar_recall.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Raw_LionGuy_recall_idle" = AtomicClipData {
        index: u32 = 20
        stored_index: u32 = 20
        offset: u32 = 4604
        size: u32 = 96
        hash: hash = "0x6208af50"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 50
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 8
        animation_path: string = "characters/rengar/skins/base/animations/rengar_recall_idle.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Attack1" = AtomicClipData {
        index: u32 = 21
        stored_index: u32 = 21
        offset: u32 = 4700
        size: u32 = 80
        hash: hash = "0x56b1e924"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 13
        animation_path: string = "characters/rengar/skins/base/animations/rengar_attack1.anm"
        event_bundle_index: u32 = 5
        event_bundle_offset: u32 = 4780
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Attack1"
        event_bundle_name_matches: bool = true
    }
    "Attack2" = AtomicClipData {
        index: u32 = 22
        stored_index: u32 = 22
        offset: u32 = 4932
        size: u32 = 80
        hash: hash = "0x59b1eddd"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 60
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 14
        animation_path: string = "characters/rengar/skins/base/animations/rengar_attack2.anm"
        event_bundle_index: u32 = 6
        event_bundle_offset: u32 = 5012
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Attack2"
        event_bundle_name_matches: bool = true
    }
    "Attack3" = AtomicClipData {
        index: u32 = 23
        stored_index: u32 = 23
        offset: u32 = 5164
        size: u32 = 80
        hash: hash = "0x58b1ec4a"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 62
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 15
        animation_path: string = "characters/rengar/skins/base/animations/rengar_attack3.anm"
        event_bundle_index: u32 = 7
        event_bundle_offset: u32 = 5244
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Attack3"
        event_bundle_name_matches: bool = true
    }
    "Recall" = SequencerClipData {
        index: u32 = 24
        stored_index: u32 = 24
        offset: u32 = 5396
        size: u32 = 48
        hash: hash = "0x5a81bdb0"
        flags: u32 = 2
        type_id: u32 = 3
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: class-specific flags/options - reserved clip payload field - runtime metadata
        child_count: u32 = 2
        children: list[u32] = {
            19
            20
        }
        child_names: list[string] = {
            "Raw_LionGuy_recall"
            "Raw_LionGuy_recall_idle"
        }
    }
    "Joke" = AtomicClipData {
        index: u32 = 25
        stored_index: u32 = 25
        offset: u32 = 5444
        size: u32 = 80
        hash: hash = "0xc21e3446"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 164
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 17
        animation_path: string = "characters/rengar/skins/base/animations/rengar_joke.anm"
        event_bundle_index: u32 = 8
        event_bundle_offset: u32 = 5524
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Joke"
        event_bundle_name_matches: bool = true
    }
    "Idle3" = AtomicClipData {
        index: u32 = 26
        stored_index: u32 = 26
        offset: u32 = 5704
        size: u32 = 80
        hash: hash = "0x9bd9d8e0"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 239
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 16
        animation_path: string = "characters/rengar/skins/base/animations/rengar_idle3.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
    "Spell1_Long" = AtomicClipData {
        index: u32 = 27
        stored_index: u32 = 27
        offset: u32 = 5784
        size: u32 = 84
        hash: hash = "0x7174a8a3"
        flags: u32 = 0
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 50
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 20
        animation_path: string = "characters/rengar/skins/base/animations/rengar_spell1_long.anm"
        event_bundle_index: u32 = 9
        event_bundle_offset: u32 = 5868
        event_count: u32 = 1
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 1
        track_name: string = "Actions"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
        event_bundle_clip_name: string = "Spell1_Long"
        event_bundle_name_matches: bool = true
    }
    "run1_Fast" = AtomicClipData {
        index: u32 = 28
        stored_index: u32 = 28
        offset: u32 = 6028
        size: u32 = 84
        hash: hash = "0x2f4455c0"
        flags: u32 = 2
        type_id: u32 = 1
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        frame_count: u32 = 30
        tick_duration: f32 = 0.03333333507180214
        resource_index: u32 = 23
        animation_path: string = "characters/rengar/skins/base/animations/rengar_run1_fast.anm"
        event_bundle_index: null = null
        event_bundle_offset: null = null
        event_count: u32 = 0
        mask_index: null = null
        mask_name: null = null
        track_index: u32 = 3
        track_name: string = "Default"
        tail_unknown: list[u32] = {
            0
            0
            0
            0
            0
        }
        # UNKNOWN: no strong enough evidence
        # might be: reserved record field - runtime bookkeeping metadata - type/class-specific metadata - AtomicClipData runtime/synchronization metadata - cached lookup/hash metadata - clip-specific tuning/options - reserved fields
    }
}

mMaskDataList: list[embed] = {
    MaskData {
        index: u32 = 0
        offset: u32 = 6116
        size: u32 = 1672
        name: string = "TopBody"
        hash: hash = "0xed606018"
        id: u32 = 0
        bone_count: u32 = 80
        weights: list[f32] = {
            0.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            1.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            0.0
            1.0
            1.0
            1.0
            0.0
            0.0
            0.0
            0.0
            1.0
            1.0
            0.0
            0.0
            0.0
            0.0
            0.0
            1.0
            1.0
            1.0
            0.0
            1.0
            1.0
            0.0
        }
        unknown_header_04: string = "0x4bbb4577"
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_header_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_header_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_aux_pairs: list[unknown] = {
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
            [0, 0]
        }
        # UNKNOWN: no strong enough evidence
        # might be: secondary/inverse joint remap table - per-bone auxiliary flags/metadata - reserved per-bone pair data
        joint_remap: list[embed] = {
            embed {
                mask_index: u32 = 0
                skeleton_joint_index: u32 = 0
            }
            embed {
                mask_index: u32 = 1
                skeleton_joint_index: u32 = 1
            }
            embed {
                mask_index: u32 = 2
                skeleton_joint_index: u32 = 2
            }
            embed {
                mask_index: u32 = 3
                skeleton_joint_index: u32 = 3
            }
            embed {
                mask_index: u32 = 4
                skeleton_joint_index: u32 = 4
            }
            embed {
                mask_index: u32 = 5
                skeleton_joint_index: u32 = 5
            }
            embed {
                mask_index: u32 = 6
                skeleton_joint_index: u32 = 6
            }
            embed {
                mask_index: u32 = 7
                skeleton_joint_index: u32 = 7
            }
            embed {
                mask_index: u32 = 8
                skeleton_joint_index: u32 = 8
            }
            embed {
                mask_index: u32 = 9
                skeleton_joint_index: u32 = 9
            }
            embed {
                mask_index: u32 = 10
                skeleton_joint_index: u32 = 10
            }
            embed {
                mask_index: u32 = 11
                skeleton_joint_index: u32 = 11
            }
            embed {
                mask_index: u32 = 12
                skeleton_joint_index: u32 = 12
            }
            embed {
                mask_index: u32 = 13
                skeleton_joint_index: u32 = 13
            }
            embed {
                mask_index: u32 = 14
                skeleton_joint_index: u32 = 14
            }
            embed {
                mask_index: u32 = 15
                skeleton_joint_index: u32 = 15
            }
            embed {
                mask_index: u32 = 16
                skeleton_joint_index: u32 = 16
            }
            embed {
                mask_index: u32 = 17
                skeleton_joint_index: u32 = 17
            }
            embed {
                mask_index: u32 = 18
                skeleton_joint_index: u32 = 18
            }
            embed {
                mask_index: u32 = 19
                skeleton_joint_index: u32 = 19
            }
            embed {
                mask_index: u32 = 20
                skeleton_joint_index: u32 = 20
            }
            embed {
                mask_index: u32 = 21
                skeleton_joint_index: u32 = 21
            }
            embed {
                mask_index: u32 = 22
                skeleton_joint_index: u32 = 22
            }
            embed {
                mask_index: u32 = 23
                skeleton_joint_index: u32 = 23
            }
            embed {
                mask_index: u32 = 24
                skeleton_joint_index: u32 = 24
            }
            embed {
                mask_index: u32 = 25
                skeleton_joint_index: u32 = 25
            }
            embed {
                mask_index: u32 = 26
                skeleton_joint_index: u32 = 26
            }
            embed {
                mask_index: u32 = 27
                skeleton_joint_index: u32 = 27
            }
            embed {
                mask_index: u32 = 28
                skeleton_joint_index: u32 = 28
            }
            embed {
                mask_index: u32 = 29
                skeleton_joint_index: u32 = 29
            }
            embed {
                mask_index: u32 = 30
                skeleton_joint_index: u32 = 30
            }
            embed {
                mask_index: u32 = 31
                skeleton_joint_index: u32 = 31
            }
            embed {
                mask_index: u32 = 32
                skeleton_joint_index: u32 = 32
            }
            embed {
                mask_index: u32 = 33
                skeleton_joint_index: u32 = 33
            }
            embed {
                mask_index: u32 = 34
                skeleton_joint_index: u32 = 34
            }
            embed {
                mask_index: u32 = 35
                skeleton_joint_index: u32 = 35
            }
            embed {
                mask_index: u32 = 36
                skeleton_joint_index: u32 = 36
            }
            embed {
                mask_index: u32 = 37
                skeleton_joint_index: u32 = 37
            }
            embed {
                mask_index: u32 = 38
                skeleton_joint_index: u32 = 38
            }
            embed {
                mask_index: u32 = 39
                skeleton_joint_index: u32 = 39
            }
            embed {
                mask_index: u32 = 40
                skeleton_joint_index: u32 = 40
            }
            embed {
                mask_index: u32 = 41
                skeleton_joint_index: u32 = 41
            }
            embed {
                mask_index: u32 = 42
                skeleton_joint_index: u32 = 42
            }
            embed {
                mask_index: u32 = 43
                skeleton_joint_index: u32 = 43
            }
            embed {
                mask_index: u32 = 44
                skeleton_joint_index: u32 = 44
            }
            embed {
                mask_index: u32 = 45
                skeleton_joint_index: u32 = 45
            }
            embed {
                mask_index: u32 = 46
                skeleton_joint_index: u32 = 46
            }
            embed {
                mask_index: u32 = 47
                skeleton_joint_index: u32 = 47
            }
            embed {
                mask_index: u32 = 48
                skeleton_joint_index: u32 = 48
            }
            embed {
                mask_index: u32 = 49
                skeleton_joint_index: u32 = 49
            }
            embed {
                mask_index: u32 = 50
                skeleton_joint_index: u32 = 50
            }
            embed {
                mask_index: u32 = 51
                skeleton_joint_index: u32 = 51
            }
            embed {
                mask_index: u32 = 52
                skeleton_joint_index: u32 = 52
            }
            embed {
                mask_index: u32 = 53
                skeleton_joint_index: u32 = 53
            }
            embed {
                mask_index: u32 = 54
                skeleton_joint_index: u32 = 54
            }
            embed {
                mask_index: u32 = 55
                skeleton_joint_index: u32 = 55
            }
            embed {
                mask_index: u32 = 56
                skeleton_joint_index: u32 = 56
            }
            embed {
                mask_index: u32 = 57
                skeleton_joint_index: u32 = 57
            }
            embed {
                mask_index: u32 = 58
                skeleton_joint_index: u32 = 58
            }
            embed {
                mask_index: u32 = 59
                skeleton_joint_index: u32 = 59
            }
            embed {
                mask_index: u32 = 60
                skeleton_joint_index: u32 = 60
            }
            embed {
                mask_index: u32 = 61
                skeleton_joint_index: u32 = 61
            }
            embed {
                mask_index: u32 = 62
                skeleton_joint_index: u32 = 62
            }
            embed {
                mask_index: u32 = 63
                skeleton_joint_index: u32 = 63
            }
            embed {
                mask_index: u32 = 64
                skeleton_joint_index: u32 = 64
            }
            embed {
                mask_index: u32 = 65
                skeleton_joint_index: u32 = 65
            }
            embed {
                mask_index: u32 = 66
                skeleton_joint_index: u32 = 66
            }
            embed {
                mask_index: u32 = 67
                skeleton_joint_index: u32 = 67
            }
            embed {
                mask_index: u32 = 68
                skeleton_joint_index: u32 = 68
            }
            embed {
                mask_index: u32 = 69
                skeleton_joint_index: u32 = 69
            }
            embed {
                mask_index: u32 = 70
                skeleton_joint_index: u32 = 70
            }
            embed {
                mask_index: u32 = 71
                skeleton_joint_index: u32 = 71
            }
            embed {
                mask_index: u32 = 72
                skeleton_joint_index: u32 = 72
            }
            embed {
                mask_index: u32 = 73
                skeleton_joint_index: u32 = 73
            }
            embed {
                mask_index: u32 = 74
                skeleton_joint_index: u32 = 74
            }
            embed {
                mask_index: u32 = 75
                skeleton_joint_index: u32 = 75
            }
            embed {
                mask_index: u32 = 76
                skeleton_joint_index: u32 = 76
            }
            embed {
                mask_index: u32 = 77
                skeleton_joint_index: u32 = 77
            }
            embed {
                mask_index: u32 = 78
                skeleton_joint_index: u32 = 78
            }
            embed {
                mask_index: u32 = 79
                skeleton_joint_index: u32 = 79
            }
        }
    }
}

mEventBundleList: list[embed] = {
    EventBundle {
        index: u32 = 0
        offset: u32 = 2376
        size: u32 = 156
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 0
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 132
        frame_table_rel: u32 = 140
        clip_name_rel: u32 = 148
        clip_name: string = "Crit"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 2428
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 1.0
                name: string = "Crit"
                modern_name_hash_fnv1a: hash = "0x9654058d"
                legacy_lookup_hash_fnv1: hash = "0xfa91f335"
                effect_name: string = "Rengar_Skin01_C_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0xfa91f335"
                event_name: string = "Crit"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 1.0
                event_name: string = "Crit"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 1
        offset: u32 = 2612
        size: u32 = 180
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 1
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 156
        frame_table_rel: u32 = 164
        clip_name_rel: u32 = 172
        clip_name: string = "Dance"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 2664
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 3
                start_frame: f32 = 0.0
                name: string = "AUDIO_dance"
                modern_name_hash_fnv1a: hash = "0xbc45bbc5"
                legacy_lookup_hash_fnv1: hash = "0x41947941"
                effect_name: string = "rengar_emote_dance_sound.troy"
                bone_name: string = "Invalid Joint Name"
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = true
                is_kill_event: bool = true
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x41947941"
                event_name: string = "AUDIO_dance"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 0.0
                event_name: string = "AUDIO_dance"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 2
        offset: u32 = 3112
        size: u32 = 180
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 2
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 156
        frame_table_rel: u32 = 164
        clip_name_rel: u32 = 172
        clip_name: string = "Laugh"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 3164
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 2
                start_frame: f32 = 0.0
                name: string = "AUDIO_laugh"
                modern_name_hash_fnv1a: hash = "0x0cf0606b"
                legacy_lookup_hash_fnv1: hash = "0x7ae39787"
                effect_name: string = "rengar_emote_laugh_sound.troy"
                bone_name: string = "Invalid Joint Name"
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = true
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x7ae39787"
                event_name: string = "AUDIO_laugh"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 0.0
                event_name: string = "AUDIO_laugh"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 3
        offset: u32 = 3528
        size: u32 = 152
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 3
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 128
        frame_table_rel: u32 = 136
        clip_name_rel: u32 = 144
        clip_name: string = "Spell1"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 3580
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 4.0
                name: string = "Q"
                modern_name_hash_fnv1a: hash = "0xf40c425c"
                legacy_lookup_hash_fnv1: hash = "0x050c5d6e"
                effect_name: string = "Rengar_Skin01_Q_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x050c5d6e"
                event_name: string = "Q"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 4.0
                event_name: string = "Q"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 4
        offset: u32 = 4332
        size: u32 = 180
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 4
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 156
        frame_table_rel: u32 = 164
        clip_name_rel: u32 = 172
        clip_name: string = "Taunt"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 4384
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 2
                start_frame: f32 = 0.0
                name: string = "AUDIO_taunt"
                modern_name_hash_fnv1a: hash = "0x968821ce"
                legacy_lookup_hash_fnv1: hash = "0x839d5008"
                effect_name: string = "rengar_emote_taunt_sound.troy"
                bone_name: string = "Invalid Joint Name"
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = true
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x839d5008"
                event_name: string = "AUDIO_taunt"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 0.0
                event_name: string = "AUDIO_taunt"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 5
        offset: u32 = 4780
        size: u32 = 152
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 5
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 128
        frame_table_rel: u32 = 136
        clip_name_rel: u32 = 144
        clip_name: string = "Attack1"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 4832
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 2.0
                name: string = "BA1"
                modern_name_hash_fnv1a: hash = "0xb5b7e047"
                legacy_lookup_hash_fnv1: hash = "0x1e99b663"
                effect_name: string = "Rengar_Skin01_BA1_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x1e99b663"
                event_name: string = "BA1"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 2.0
                event_name: string = "BA1"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 6
        offset: u32 = 5012
        size: u32 = 152
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 6
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 128
        frame_table_rel: u32 = 136
        clip_name_rel: u32 = 144
        clip_name: string = "Attack2"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 5064
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 2.0
                name: string = "BA2"
                modern_name_hash_fnv1a: hash = "0xb6b7e1da"
                legacy_lookup_hash_fnv1: hash = "0x1e99b660"
                effect_name: string = "Rengar_Skin01_BA2_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x1e99b660"
                event_name: string = "BA2"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 2.0
                event_name: string = "BA2"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 7
        offset: u32 = 5244
        size: u32 = 152
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 7
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 128
        frame_table_rel: u32 = 136
        clip_name_rel: u32 = 144
        clip_name: string = "Attack3"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 5296
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 2.0
                name: string = "BA3"
                modern_name_hash_fnv1a: hash = "0xb7b7e36d"
                legacy_lookup_hash_fnv1: hash = "0x1e99b661"
                effect_name: string = "Rengar_Skin01_BA3_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x1e99b661"
                event_name: string = "BA3"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 2.0
                event_name: string = "BA3"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 8
        offset: u32 = 5524
        size: u32 = 180
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 8
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 156
        frame_table_rel: u32 = 164
        clip_name_rel: u32 = 172
        clip_name: string = "Joke"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 5576
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 2
                start_frame: f32 = 0.0
                name: string = "AUDIO_joke"
                modern_name_hash_fnv1a: hash = "0xeed2417d"
                legacy_lookup_hash_fnv1: hash = "0x74ec2c21"
                effect_name: string = "rengar_emote_joke_sound.troy"
                bone_name: string = "Invalid Joint Name"
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = true
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x74ec2c21"
                event_name: string = "AUDIO_joke"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 0.0
                event_name: string = "AUDIO_joke"
                matches_event: bool = true
            }
        }
    }
    EventBundle {
        index: u32 = 9
        offset: u32 = 5868
        size: u32 = 160
        unknown_04: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        unknown_u16_0c: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved event-bundle header field - event-bundle flags/options - runtime bookkeeping/index metadata
        event_count: u32 = 1
        stored_index: u32 = 9
        event_offsets_rel: u32 = 48
        event_data_rel: u32 = 52
        hash_table_rel: u32 = 132
        frame_table_rel: u32 = 140
        clip_name_rel: u32 = 148
        clip_name: string = "Spell1_Long"
        unknown_28: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        unknown_2c: u32 = 4294967295
        # UNKNOWN: no strong enough evidence
        # might be: reserved field - runtime metadata
        events: list[embed] = {
            ParticleEventData {
                index: u32 = 0
                offset: u32 = 5920
                unknown_00: u32 = 0
                # UNKNOWN: no strong enough evidence
                # might be: reserved field - runtime metadata
                type_id: u32 = 2
                event_flags_raw: u32 = 0
                start_frame: f32 = 4.0
                name: string = "Q_Long"
                modern_name_hash_fnv1a: hash = "0x9c4b7e97"
                legacy_lookup_hash_fnv1: hash = "0x2b1e1443"
                effect_name: string = "Rengar_Skin01_Q_Cas.troy"
                bone_name: string = ""
                target_bone_name: string = ""
                end_frame: f32 = -1.0
                is_loop: bool = false
                is_kill_event: bool = false
                is_detachable: bool = false
                unknown_flag_bits: u32 = 0
                relative_offset: u32 = 52
            }
        }
        legacy_name_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                hash: hash = "0x2b1e1443"
                event_name: string = "Q_Long"
                hash_verified: bool = true
            }
        }
        start_frame_lookup: list[embed] = {
            embed {
                event_index: u32 = 0
                start_frame: f32 = 4.0
                event_name: string = "Q_Long"
                matches_event: bool = true
            }
        }
    }
}

mAnimationResourceList: list[embed] = {
    AnimationResourceData {
        index: u32 = 0
        hash: hash = "0x0acd07b4"
        path: string = "characters/rengar/skins/base/animations/rengar_channel.anm"
        hash_verified: bool = true
        offset: u32 = 7924
    }
    AnimationResourceData {
        index: u32 = 1
        hash: hash = "0x685351e5"
        path: string = "characters/rengar/skins/base/animations/rengar_channel_wndpup.anm"
        hash_verified: bool = true
        offset: u32 = 7932
    }
    AnimationResourceData {
        index: u32 = 2
        hash: hash = "0x2d2135cc"
        path: string = "characters/rengar/skins/base/animations/rengar_dance.anm"
        hash_verified: bool = true
        offset: u32 = 7940
    }
    AnimationResourceData {
        index: u32 = 3
        hash: hash = "0xdf326515"
        path: string = "characters/rengar/skins/base/animations/rengar_death.anm"
        hash_verified: bool = true
        offset: u32 = 7948
    }
    AnimationResourceData {
        index: u32 = 4
        hash: hash = "0x37e6637e"
        path: string = "characters/rengar/skins/base/animations/rengar_idle1.anm"
        hash_verified: bool = true
        offset: u32 = 7956
    }
    AnimationResourceData {
        index: u32 = 5
        hash: hash = "0xcc072253"
        path: string = "characters/rengar/skins/base/animations/rengar_idle2.anm"
        hash_verified: bool = true
        offset: u32 = 7964
    }
    AnimationResourceData {
        index: u32 = 6
        hash: hash = "0xcecf4bc6"
        path: string = "characters/rengar/skins/base/animations/rengar_laugh.anm"
        hash_verified: bool = true
        offset: u32 = 7972
    }
    AnimationResourceData {
        index: u32 = 7
        hash: hash = "0x7d8802d8"
        path: string = "characters/rengar/skins/base/animations/rengar_recall.anm"
        hash_verified: bool = true
        offset: u32 = 7980
    }
    AnimationResourceData {
        index: u32 = 8
        hash: hash = "0x6473244b"
        path: string = "characters/rengar/skins/base/animations/rengar_recall_idle.anm"
        hash_verified: bool = true
        offset: u32 = 7988
    }
    AnimationResourceData {
        index: u32 = 9
        hash: hash = "0xff2a29d1"
        path: string = "characters/rengar/skins/base/animations/rengar_run1.anm"
        hash_verified: bool = true
        offset: u32 = 7996
    }
    AnimationResourceData {
        index: u32 = 10
        hash: hash = "0x630f4030"
        path: string = "characters/rengar/skins/base/animations/rengar_run2.anm"
        hash_verified: bool = true
        offset: u32 = 8004
    }
    AnimationResourceData {
        index: u32 = 11
        hash: hash = "0x00135660"
        path: string = "characters/rengar/skins/base/animations/rengar_spell1.anm"
        hash_verified: bool = true
        offset: u32 = 8012
    }
    AnimationResourceData {
        index: u32 = 12
        hash: hash = "0x6a12a553"
        path: string = "characters/rengar/skins/base/animations/rengar_taunt.anm"
        hash_verified: bool = true
        offset: u32 = 8020
    }
    AnimationResourceData {
        index: u32 = 13
        hash: hash = "0x7d7f5ee4"
        path: string = "characters/rengar/skins/base/animations/rengar_attack1.anm"
        hash_verified: bool = true
        offset: u32 = 8028
    }
    AnimationResourceData {
        index: u32 = 14
        hash: hash = "0xb91e7ce5"
        path: string = "characters/rengar/skins/base/animations/rengar_attack2.anm"
        hash_verified: bool = true
        offset: u32 = 8036
    }
    AnimationResourceData {
        index: u32 = 15
        hash: hash = "0xa90b9cca"
        path: string = "characters/rengar/skins/base/animations/rengar_attack3.anm"
        hash_verified: bool = true
        offset: u32 = 8044
    }
    AnimationResourceData {
        index: u32 = 16
        hash: hash = "0xa4d24458"
        path: string = "characters/rengar/skins/base/animations/rengar_idle3.anm"
        hash_verified: bool = true
        offset: u32 = 8052
    }
    AnimationResourceData {
        index: u32 = 17
        hash: hash = "0xe2da8cde"
        path: string = "characters/rengar/skins/base/animations/rengar_joke.anm"
        hash_verified: bool = true
        offset: u32 = 8060
    }
    AnimationResourceData {
        index: u32 = 18
        hash: hash = "0x396f0e65"
        path: string = "characters/rengar/skins/base/animations/rengar_crit.anm"
        hash_verified: bool = true
        offset: u32 = 8068
    }
    AnimationResourceData {
        index: u32 = 19
        hash: hash = "0x88362f5c"
        path: string = "characters/rengar/skins/base/animations/rengar_dash1.anm"
        hash_verified: bool = true
        offset: u32 = 8076
    }
    AnimationResourceData {
        index: u32 = 20
        hash: hash = "0x0dff08a3"
        path: string = "characters/rengar/skins/base/animations/rengar_spell1_long.anm"
        hash_verified: bool = true
        offset: u32 = 8084
    }
    AnimationResourceData {
        index: u32 = 21
        hash: hash = "0x2d919641"
        path: string = "characters/rengar/skins/base/animations/rengar_spell2.anm"
        hash_verified: bool = true
        offset: u32 = 8092
    }
    AnimationResourceData {
        index: u32 = 22
        hash: hash = "0xe65c85e6"
        path: string = "characters/rengar/skins/base/animations/rengar_spell3.anm"
        hash_verified: bool = true
        offset: u32 = 8100
    }
    AnimationResourceData {
        index: u32 = 23
        hash: hash = "0xcf792c38"
        path: string = "characters/rengar/skins/base/animations/rengar_run1_fast.anm"
        hash_verified: bool = true
        offset: u32 = 8108
    }
}

resource_runtime_slots: list[u32] = {
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
}
# UNKNOWN: no strong enough evidence
# might be: reserved field - runtime metadata

mTimeBlendDataList: list[embed] = {
    TimeBlendData {
        source_index: u32 = 25
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 108
        source_name: string = "Joke"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13987674969366194468
        modern_u64_key_hex: string = "0xc21e344656b1e924"
    }
    TimeBlendData {
        source_index: u32 = 24
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 124
        source_name: string = "Recall"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6521702300475582756
        modern_u64_key_hex: string = "0x5a81bdb056b1e924"
    }
    TimeBlendData {
        source_index: u32 = 23
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 140
        source_name: string = "Attack3"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6391149150241679652
        modern_u64_key_hex: string = "0x58b1ec4a56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 22
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 156
        source_name: string = "Attack2"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6463208475151427876
        modern_u64_key_hex: string = "0x59b1eddd56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 21
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 172
        source_name: string = "Attack1"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6247030500422183204
        modern_u64_key_hex: string = "0x56b1e92456b1e924"
    }
    TimeBlendData {
        source_index: u32 = 20
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 188
        source_name: string = "Raw_LionGuy_recall_idle"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 7064088775117367588
        modern_u64_key_hex: string = "0x6208af5056b1e924"
    }
    TimeBlendData {
        source_index: u32 = 19
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 204
        source_name: string = "Raw_LionGuy_recall"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6929639312156911908
        modern_u64_key_hex: string = "0x602b063d56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 18
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 220
        source_name: string = "Taunt"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13590883337688443172
        modern_u64_key_hex: string = "0xbc9c846356b1e924"
    }
    TimeBlendData {
        source_index: u32 = 17
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 236
        source_name: string = "Spell6"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13399971878172485924
        modern_u64_key_hex: string = "0xb9f6436d56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 16
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 252
        source_name: string = "Spell5"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13183793903443241252
        modern_u64_key_hex: string = "0xb6f63eb456b1e924"
    }
    TimeBlendData {
        source_index: u32 = 15
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 268
        source_name: string = "Spell4_Winddown"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 5406481391727798564
        modern_u64_key_hex: string = "0x4b07ae2e56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 14
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 284
        source_name: string = "Spell4_Loop"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 12217611125825595684
        modern_u64_key_hex: string = "0xa98dac9656b1e924"
    }
    TimeBlendData {
        source_index: u32 = 13
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 300
        source_name: string = "Spell4"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13255853228352989476
        modern_u64_key_hex: string = "0xb7f6404756b1e924"
    }
    TimeBlendData {
        source_index: u32 = 12
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 316
        source_name: string = "Spell3"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13039675253623744804
        modern_u64_key_hex: string = "0xb4f63b8e56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 11
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 332
        source_name: string = "Spell2"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13111734578533493028
        modern_u64_key_hex: string = "0xb5f63d2156b1e924"
    }
    TimeBlendData {
        source_index: u32 = 10
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 348
        source_name: string = "Spell1"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 12895556603804248356
        modern_u64_key_hex: string = "0xb2f6386856b1e924"
    }
    TimeBlendData {
        source_index: u32 = 9
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 364
        source_name: string = "Run2"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 6427569502249150756
        modern_u64_key_hex: string = "0x5933506856b1e924"
    }
    TimeBlendData {
        source_index: u32 = 8
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 380
        source_name: string = "Run"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 3084207950763518244
        modern_u64_key_hex: string = "0x2acd4eca56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 7
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 396
        source_name: string = "Laugh"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13156647004303124772
        modern_u64_key_hex: string = "0xb695ccbe56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 6
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 412
        source_name: string = "Idle2"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 11302304928773564708
        modern_u64_key_hex: string = "0x9cd9da7356b1e924"
    }
    TimeBlendData {
        source_index: u32 = 5
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 428
        source_name: string = "Idle1"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 11374364253683312932
        modern_u64_key_hex: string = "0x9dd9dc0656b1e924"
    }
    TimeBlendData {
        source_index: u32 = 4
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 444
        source_name: string = "Death"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 13630352412101437732
        modern_u64_key_hex: string = "0xbd28bd4d56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 3
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 460
        source_name: string = "Dance"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 17876238947851561252
        modern_u64_key_hex: string = "0xf815289c56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 2
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 476
        source_name: string = "Crit"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 10832289108335913252
        modern_u64_key_hex: string = "0x9654058d56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 1
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 492
        source_name: string = "Channel_WNDUP"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 11831733633112205604
        modern_u64_key_hex: string = "0xa432c30d56b1e924"
    }
    TimeBlendData {
        source_index: u32 = 0
        destination_index: u32 = 21
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 508
        source_name: string = "Channel"
        destination_name: string = "Attack1"
        modern_u64_key: u64 = 2432597614516103460
        modern_u64_key_hex: string = "0x21c252a456b1e924"
    }
    TimeBlendData {
        source_index: u32 = 25
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 524
        source_name: string = "Joke"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13987674969416527325
        modern_u64_key_hex: string = "0xc21e344659b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 24
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 540
        source_name: string = "Recall"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6521702300525915613
        modern_u64_key_hex: string = "0x5a81bdb059b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 23
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 556
        source_name: string = "Attack3"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6391149150292012509
        modern_u64_key_hex: string = "0x58b1ec4a59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 22
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 572
        source_name: string = "Attack2"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6463208475201760733
        modern_u64_key_hex: string = "0x59b1eddd59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 21
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 588
        source_name: string = "Attack1"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6247030500472516061
        modern_u64_key_hex: string = "0x56b1e92459b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 20
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 604
        source_name: string = "Raw_LionGuy_recall_idle"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 7064088775167700445
        modern_u64_key_hex: string = "0x6208af5059b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 19
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 620
        source_name: string = "Raw_LionGuy_recall"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6929639312207244765
        modern_u64_key_hex: string = "0x602b063d59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 18
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 636
        source_name: string = "Taunt"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13590883337738776029
        modern_u64_key_hex: string = "0xbc9c846359b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 17
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 652
        source_name: string = "Spell6"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13399971878222818781
        modern_u64_key_hex: string = "0xb9f6436d59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 16
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 668
        source_name: string = "Spell5"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13183793903493574109
        modern_u64_key_hex: string = "0xb6f63eb459b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 15
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 684
        source_name: string = "Spell4_Winddown"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 5406481391778131421
        modern_u64_key_hex: string = "0x4b07ae2e59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 14
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 700
        source_name: string = "Spell4_Loop"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 12217611125875928541
        modern_u64_key_hex: string = "0xa98dac9659b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 13
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 716
        source_name: string = "Spell4"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13255853228403322333
        modern_u64_key_hex: string = "0xb7f6404759b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 12
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 732
        source_name: string = "Spell3"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13039675253674077661
        modern_u64_key_hex: string = "0xb4f63b8e59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 11
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 748
        source_name: string = "Spell2"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13111734578583825885
        modern_u64_key_hex: string = "0xb5f63d2159b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 10
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 764
        source_name: string = "Spell1"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 12895556603854581213
        modern_u64_key_hex: string = "0xb2f6386859b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 9
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 780
        source_name: string = "Run2"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 6427569502299483613
        modern_u64_key_hex: string = "0x5933506859b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 8
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 796
        source_name: string = "Run"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 3084207950813851101
        modern_u64_key_hex: string = "0x2acd4eca59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 7
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 812
        source_name: string = "Laugh"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13156647004353457629
        modern_u64_key_hex: string = "0xb695ccbe59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 6
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 828
        source_name: string = "Idle2"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 11302304928823897565
        modern_u64_key_hex: string = "0x9cd9da7359b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 5
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 844
        source_name: string = "Idle1"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 11374364253733645789
        modern_u64_key_hex: string = "0x9dd9dc0659b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 4
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 860
        source_name: string = "Death"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 13630352412151770589
        modern_u64_key_hex: string = "0xbd28bd4d59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 3
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 876
        source_name: string = "Dance"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 17876238947901894109
        modern_u64_key_hex: string = "0xf815289c59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 2
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 892
        source_name: string = "Crit"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 10832289108386246109
        modern_u64_key_hex: string = "0x9654058d59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 1
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 908
        source_name: string = "Channel_WNDUP"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 11831733633162538461
        modern_u64_key_hex: string = "0xa432c30d59b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 0
        destination_index: u32 = 22
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 924
        source_name: string = "Channel"
        destination_name: string = "Attack2"
        modern_u64_key: u64 = 2432597614566436317
        modern_u64_key_hex: string = "0x21c252a459b1eddd"
    }
    TimeBlendData {
        source_index: u32 = 25
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 940
        source_name: string = "Joke"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13987674969399749706
        modern_u64_key_hex: string = "0xc21e344658b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 24
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 956
        source_name: string = "Recall"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6521702300509137994
        modern_u64_key_hex: string = "0x5a81bdb058b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 23
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 972
        source_name: string = "Attack3"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6391149150275234890
        modern_u64_key_hex: string = "0x58b1ec4a58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 22
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 988
        source_name: string = "Attack2"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6463208475184983114
        modern_u64_key_hex: string = "0x59b1eddd58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 21
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1004
        source_name: string = "Attack1"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6247030500455738442
        modern_u64_key_hex: string = "0x56b1e92458b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 20
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1020
        source_name: string = "Raw_LionGuy_recall_idle"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 7064088775150922826
        modern_u64_key_hex: string = "0x6208af5058b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 19
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1036
        source_name: string = "Raw_LionGuy_recall"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6929639312190467146
        modern_u64_key_hex: string = "0x602b063d58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 18
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1052
        source_name: string = "Taunt"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13590883337721998410
        modern_u64_key_hex: string = "0xbc9c846358b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 17
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1068
        source_name: string = "Spell6"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13399971878206041162
        modern_u64_key_hex: string = "0xb9f6436d58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 16
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1084
        source_name: string = "Spell5"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13183793903476796490
        modern_u64_key_hex: string = "0xb6f63eb458b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 15
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1100
        source_name: string = "Spell4_Winddown"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 5406481391761353802
        modern_u64_key_hex: string = "0x4b07ae2e58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 14
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1116
        source_name: string = "Spell4_Loop"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 12217611125859150922
        modern_u64_key_hex: string = "0xa98dac9658b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 13
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1132
        source_name: string = "Spell4"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13255853228386544714
        modern_u64_key_hex: string = "0xb7f6404758b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 12
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1148
        source_name: string = "Spell3"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13039675253657300042
        modern_u64_key_hex: string = "0xb4f63b8e58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 11
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1164
        source_name: string = "Spell2"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13111734578567048266
        modern_u64_key_hex: string = "0xb5f63d2158b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 10
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1180
        source_name: string = "Spell1"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 12895556603837803594
        modern_u64_key_hex: string = "0xb2f6386858b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 9
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1196
        source_name: string = "Run2"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 6427569502282705994
        modern_u64_key_hex: string = "0x5933506858b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 8
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1212
        source_name: string = "Run"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 3084207950797073482
        modern_u64_key_hex: string = "0x2acd4eca58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 7
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1228
        source_name: string = "Laugh"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13156647004336680010
        modern_u64_key_hex: string = "0xb695ccbe58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 6
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1244
        source_name: string = "Idle2"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 11302304928807119946
        modern_u64_key_hex: string = "0x9cd9da7358b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 5
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1260
        source_name: string = "Idle1"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 11374364253716868170
        modern_u64_key_hex: string = "0x9dd9dc0658b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 4
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1276
        source_name: string = "Death"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 13630352412134992970
        modern_u64_key_hex: string = "0xbd28bd4d58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 3
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1292
        source_name: string = "Dance"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 17876238947885116490
        modern_u64_key_hex: string = "0xf815289c58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 2
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1308
        source_name: string = "Crit"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 10832289108369468490
        modern_u64_key_hex: string = "0x9654058d58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 1
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1324
        source_name: string = "Channel_WNDUP"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 11831733633145760842
        modern_u64_key_hex: string = "0xa432c30d58b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 0
        destination_index: u32 = 23
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.20000000298023224
        offset: u32 = 1340
        source_name: string = "Channel"
        destination_name: string = "Attack3"
        modern_u64_key: u64 = 2432597614549658698
        modern_u64_key_hex: string = "0x21c252a458b1ec4a"
    }
    TimeBlendData {
        source_index: u32 = 0
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1356
        source_name: string = "Channel"
        destination_name: string = "Death"
        modern_u64_key: u64 = 2432597616235167053
        modern_u64_key_hex: string = "0x21c252a4bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 1
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1372
        source_name: string = "Channel_WNDUP"
        destination_name: string = "Death"
        modern_u64_key: u64 = 11831733634831269197
        modern_u64_key_hex: string = "0xa432c30dbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 2
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1388
        source_name: string = "Crit"
        destination_name: string = "Death"
        modern_u64_key: u64 = 10832289110054976845
        modern_u64_key_hex: string = "0x9654058dbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 3
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1404
        source_name: string = "Dance"
        destination_name: string = "Death"
        modern_u64_key: u64 = 17876238949570624845
        modern_u64_key_hex: string = "0xf815289cbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 4
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1420
        source_name: string = "Death"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13630352413820501325
        modern_u64_key_hex: string = "0xbd28bd4dbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 5
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1436
        source_name: string = "Idle1"
        destination_name: string = "Death"
        modern_u64_key: u64 = 11374364255402376525
        modern_u64_key_hex: string = "0x9dd9dc06bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 6
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1452
        source_name: string = "Idle2"
        destination_name: string = "Death"
        modern_u64_key: u64 = 11302304930492628301
        modern_u64_key_hex: string = "0x9cd9da73bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 7
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1468
        source_name: string = "Laugh"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13156647006022188365
        modern_u64_key_hex: string = "0xb695ccbebd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 8
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1484
        source_name: string = "Run"
        destination_name: string = "Death"
        modern_u64_key: u64 = 3084207952482581837
        modern_u64_key_hex: string = "0x2acd4ecabd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 9
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1500
        source_name: string = "Run2"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6427569503968214349
        modern_u64_key_hex: string = "0x59335068bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 10
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1516
        source_name: string = "Spell1"
        destination_name: string = "Death"
        modern_u64_key: u64 = 12895556605523311949
        modern_u64_key_hex: string = "0xb2f63868bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 11
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1532
        source_name: string = "Spell2"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13111734580252556621
        modern_u64_key_hex: string = "0xb5f63d21bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 12
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1548
        source_name: string = "Spell3"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13039675255342808397
        modern_u64_key_hex: string = "0xb4f63b8ebd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 13
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1564
        source_name: string = "Spell4"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13255853230072053069
        modern_u64_key_hex: string = "0xb7f64047bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 14
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1580
        source_name: string = "Spell4_Loop"
        destination_name: string = "Death"
        modern_u64_key: u64 = 12217611127544659277
        modern_u64_key_hex: string = "0xa98dac96bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 15
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1596
        source_name: string = "Spell4_Winddown"
        destination_name: string = "Death"
        modern_u64_key: u64 = 5406481393446862157
        modern_u64_key_hex: string = "0x4b07ae2ebd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 16
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1612
        source_name: string = "Spell5"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13183793905162304845
        modern_u64_key_hex: string = "0xb6f63eb4bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 17
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1628
        source_name: string = "Spell6"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13399971879891549517
        modern_u64_key_hex: string = "0xb9f6436dbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 18
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1644
        source_name: string = "Taunt"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13590883339407506765
        modern_u64_key_hex: string = "0xbc9c8463bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 19
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1660
        source_name: string = "Raw_LionGuy_recall"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6929639313875975501
        modern_u64_key_hex: string = "0x602b063dbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 20
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1676
        source_name: string = "Raw_LionGuy_recall_idle"
        destination_name: string = "Death"
        modern_u64_key: u64 = 7064088776836431181
        modern_u64_key_hex: string = "0x6208af50bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 21
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1692
        source_name: string = "Attack1"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6247030502141246797
        modern_u64_key_hex: string = "0x56b1e924bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 22
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1708
        source_name: string = "Attack2"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6463208476870491469
        modern_u64_key_hex: string = "0x59b1edddbd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 23
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1724
        source_name: string = "Attack3"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6391149151960743245
        modern_u64_key_hex: string = "0x58b1ec4abd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 24
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1740
        source_name: string = "Recall"
        destination_name: string = "Death"
        modern_u64_key: u64 = 6521702302194646349
        modern_u64_key_hex: string = "0x5a81bdb0bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 25
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1756
        source_name: string = "Joke"
        destination_name: string = "Death"
        modern_u64_key: u64 = 13987674971085258061
        modern_u64_key_hex: string = "0xc21e3446bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 26
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1772
        source_name: string = "Idle3"
        destination_name: string = "Death"
        modern_u64_key: u64 = 11230245605582880077
        modern_u64_key_hex: string = "0x9bd9d8e0bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 27
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1788
        source_name: string = "Spell1_Long"
        destination_name: string = "Death"
        modern_u64_key: u64 = 8175344644790992205
        modern_u64_key_hex: string = "0x7174a8a3bd28bd4d"
    }
    TimeBlendData {
        source_index: u32 = 28
        destination_index: u32 = 4
        unknown_08: u32 = 0
        # UNKNOWN: no strong enough evidence
        # might be: reserved TimeBlend field - TimeBlend flags/options - additional runtime blend parameter
        m_time: f32 = 0.0
        offset: u32 = 1804
        source_name: string = "run1_Fast"
        destination_name: string = "Death"
        modern_u64_key: u64 = 3405941504494583117
        modern_u64_key_hex: string = "0x2f4455c0bd28bd4d"
    }
}

mTransitionSourceGroupList: list[embed] = {
}

transition_pair_count_total: u32 = 0
