# Old Rengar Rebirth Changelog:

*Changes done on Renghub's mod:*

**- ANIMATIONS -**

>**- Q** animation is now way smoother and it no longer snaps Rengar onto the target if he's facing the other direction, a clean transition added, matching the Season 6 **Q**.  
**- E** animation once again plays after **Q** / **AA**.  
**- E** no longer changes Rengar's facing direction during the Leap.  
**- Q/W/E** animations no longer play during death.  
**- Leap** no longer glitches towards its animation end.  
**- Tiamat** animation once again plays during **Leap**.  
**- W** animation no longer plays on top of "*taunt*" animations (CTRL + 1/2/3/4).  
**-** Rengar is no longer sliding in **W** animation if he uses it together with **E** mid-air.  
**-** Recall animation once again plays during **Leap**.  
**-** Bush/ULT Idle Animation reverted back to S6 functionality (moved to Regular Idle animations).  
**- R** reverted to changing Rengar's Run animation only after entering stealth.  
**-** Restored Night Hunter's old "**R** Run" animation details.

**- VISUALS -** 

>**- Leap** range indicator reverted back to the old one for Night Hunter skin.  
**-** "**Q** on-hit" visuals' positioning adjusted.  
**-** "**Q** Trails" VFX no longer fails to play if **Q** is used multiple times in a same sequence.  
**-** "Emp **W** Glow" VFX duration changed to 2s to match the Empowered MS.  
**-** "**R** Heart" VFX on Base/SSW/Nighthunter skins no longer disappears.  
**-** "**R** Heart" VFX removed for Headhunter skin, as old Headhunter didn't have it.  
**-** “**R** Target Glow" VFX improved to match the old looks.  
**-** "**R** Activation" VFX on Headhunter and Night Hunter reverted to the old one.  
**-** "**R** Activation" VFX no longer keeps playing even if you cancel **R**.  
**-** "**R** Activation" VFX no longer turns Headhunter chromas into Base Headhunter for a moment.  
**-** "**R** Exclamation Mark" no longer pulsates and moves around.  
**-** The VFX surrounding the "**R** Exclamation Mark" have been removed.  
**-** Rengar is no longer transparent when jumping out of **R**.  
**-** Headhunter's "**R** Body" texture improved, matching the old one.  
**-** Increased visibility of **Leap**, **Q**, **W** and **R** visuals on Very Low settings.  
**-** Leap range no longer disappears at screen's edge.

**- SOUNDS -**

>**-** "MAX Ferocity" SFX now matches the old one, with improved quality.  
**-** "**Leap**" SFX more variations and its functionality reverted back to the old one.  
**-** "**Q** Stab" sounds significantly improved, matching the old one, with all 4 SFX variations.  
**-** "**Q** Stab" SFX timing adjusted to better match Season 6 behavior.  
**-** "**Q** Stab" SFX no longer fails to play if **E** is used right after **Q**.  
**-** "**Q** Stab" SFX no longer fails to play if **Q** is used multiple times in a same sequence.  
**-** "**Q** On-Attack" SFX restored. It once again uses the old one.  
**-** "**Q** Growl" VO reverted to playing *on-attack* rather than *on-cast*.  
**-** "Emp **Q** Activation" now has all 3 SFX variations.  
**-** "Emp **Q** Attack Speed" SFX no longer incorrectly plays on the Night Hunter skin.  
**-** "**W**" SFX improved, matching the old one and it no longer fires twice each cast.  
**-** "**E**" SFX reverted back to the old one.  
**-** "**R** Ambient" SFX reverted back to the old one on all skins (Base, HH, NH, SSW).  
**-** "**R** Activation" SFX reverted back to the old one on Base/NH/SSW skins.  
**-** **Every other sound:** higher quality + minor adjustments to match Season 6.

**- MISCELLANEOUS -**

>**-** Other skins are no longer affected by the mod, only the 4 OG ones (Base, HH, NH and SSW).  
**-** Skins no longer use Classic skin's icon in the HUD.  
**-** Enforced changes to make sure the mod stays working long-term.  
**-** Mod fully debloated.  
**-** File count reduced from 417 to 186.  
**-** All .DDS converted to .TEX (modern format).  
**-** All .SCO converted to .SCB (modern format).  
**-** Rewritten a lot of code to modern Riot standards.  
**-** More compact code (16.000+ lines thinner).  
**-** Many flags corrected from 8-bit to 16-bit.  
**-** Mod thumbnail added for supported mod-loaders.  
**-** Disabled skin-hacking.

‎

*The mod fixes a total of* ***20 live bugs*** *from the* [***RENGAR BUGS LIST***](https://www.reddit.com/r/Rengarmains/comments/1loa2ad/megapost_all_rengar_bugs/) *as well:‎*

>**- E** and **W** animations [play during the **Leap**](https://youtu.be/8d1e-Zh8EWo?t=32).  
**- W** animation [not lingering](https://youtu.be/8d1e-Zh8EWo?t=9) if Rengar casts **W** together with other actions.  
**- "*****Q\_Cas*****"** VFX [goes ahead](https://www.youtube.com/watch?v=d3vy5_FHiEg) of **Q** anim if his attack speed is low enough, its speed remains the same  
**- "*****Q\_Cas*****"** VFX [plays at the start of **Leap**](https://youtu.be/K3Hemjh_w28) if **Q** is activated prior to the jump.  
**- "*****Q\_Cas*****"** VFX [plays twice for Emp **Q**](https://youtu.be/r7EMeKskaC0).  
**-** Emp **Q** “*ASBuff*” SFX plays inside the target instead of the Rengar itself – Creating [issues like this](https://youtu.be/app4V5Ormvg).  
**-** Right as Rengar casts **R** while he’s walking, his "*Run*" animation [glitches out for a second](https://youtu.be/UnL2MhJQ-Vs).  
**- Q** VO playing [oncast](https://youtu.be/etlfp2TVz1c) instead of onattack fixed  
**-** "*Bush Idle*" anim [breaks](https://youtu.be/tQv62w5tHZ8) if **R** cancels while in bush.  
**- Q** "*on-hit*" SFX [doesn't play](https://youtu.be/NxUbzXnZtO8) for Regular **Q** if he: activates it > gets 4 Ferocity and jumps with it.  
**-** When casting **E** mid-air, its animation [keeps playing](https://youtu.be/XLNeLf9QgVg) even when he starts walking,  
**- Q** [has no onhit visuals](https://imgur.com/a/oIGdi0J) that **AA**s play, e.g [Blood](https://imgur.com/a/plJMCHi).  
**-** **E** [sometimes cancels](https://youtu.be/2S6KiaDo0Vc) **Q**'s "onhit" sound event.  
**- Tiamat** [not copying **Q**](https://github.com/ArdaSenyurek/Rengar-Bugs/issues/32) animation, fixed.  
**- Q** onHit SFX [playing twice](https://github.com/ArdaSenyurek/Rengar-Bugs/issues/20), fixed  
**-** "***Q\_Cas***" VFX [playing twice](https://github.com/ArdaSenyurek/Rengar-Bugs/issues/36) on Night Hunter, fixed  
***- "Q\_Cas"*** VFX [not playing](https://github.com/ArdaSenyurek/Rengar-Bugs/issues/110) while in bush/ult, fixed  
**‎- E** VFX [clipping into the ground](https://github.com/ArdaSenyurek/Rengar-Bugs/issues/118) after a flash, fixed  
**-** Some parts of Headhunter's "***R body***" texture [being transparent](https://imgur.com/a/23PmHmc), fixed.  
**-** Leap Range [disappearing](https://youtu.be/xXbHYecIK3Q) at the edge of the screen, fixed.

*More changes on the Runeforge* [***releases***](https://runeforge.dev/mods/b397d88f-d6da-47a7-821e-9acd2109fa89/releases) *page.*
