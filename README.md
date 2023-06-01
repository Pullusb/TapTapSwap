# TapTapSwap
Blender addon - Keymap shortcuts to swap some areas of blender

**[Download latest](https://raw.githubusercontent.com/Pullusb/TapTapSwap/master/TapTapSwap.py)**

Old blender 2.7 compatible version can be found [here](https://github.com/Pullusb/SB_blender_addons_old_2_7)

## [Demo Youtube](https://www.youtube.com/watch?v=43v5kxFkcZk)

---

### Description  

You'll stop having both outliner and the properties panels on screen when they are one "Tab" away from each other !  

Keymap **Tab** key to super quickly swap between **outliner and properties**.  
Exactly like *Shift+F7* for Property editor and *Shift+F9* for outliner but waaay faster ;)  

You can add the keymap manually the exact same way the addon does [as shown in this french forum](http://blenderlounge.fr/forum/viewtopic.php?f=5&t=1446&start=45) (which was the direct source for creating this addon)  

*But also:*  
Keymap **Z** to swap between **dopesheet and graph editor**. (Hjalti Hjalmarsson idea) 

Keymap **shift+Z** to swap between **timeline and dopesheet** (my idea, hurray !)

Keymap **Ctrl+Tab** to swap between **outliner modes**, add Shift to reverse

*bonus :*  
Keymap **ctrl+shift+alt+X** to iterate in properties panels tabs (the shortcut is way to complex but it's hard to get free left-hand-accessible shortcuts these days ^^)
  
### note
[robert-trirop](https://github.com/robert-trirop) made an addon "[editor switcher](https://github.com/robert-trirop/editor_switcher)" that call a pie menu for switching area (with all area choices), if you want a quick way to change/relocate area, it may be better for you.

---
### Changelog

#### 1.7.0 (2022/06/22)

- changed from single file mode to folder addon mode.

#### 1.6.0 (20/12/2020)

- Fix an uncorrect keymap unregister that has been there forever
- add doc url
- code cleanup

#### 2.8 update (19/02/2019)
Make it work with blender 2.8 

#### 1.4 Update (20/03/2017)
new shortcut :
**shift+Z swap timeline/dopesheet**

#### 1.2 Update (11/03/2017)
new shortcut :
**ctrl+shift+alt+X iterate swap of properties panels tabs** according to active object type and data availability of this object.
