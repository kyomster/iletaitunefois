# S01E01 — les 48 jobs vidéo du pilote, tels que soumis à ComfyUI

Générés par `docs/scripts/build_clips_pilote.py`. Réglages : Wan2.2-I2V-A14B fp8 (high+low) + LightX2V 4 steps ; FLF2V : Wan2.2-14B-FLF2V, 1280x720, 16 im/s, 4 étapes (2+2), cfg 1, euler/simple, shift 5. Négative commune : `photorealistic rendering, skin texture, smooth gradients, cut, scene change, camera shake, morphing, text, watermark, lip sync, mouth articulation, extra characters appearing`.

| Clip | Style | Mode | s | length | Image de fin | Graine |
|---|---|---|---|---|---|---|
| P1a-1 | StyleA | i2v | 2.5 | 41 | — | 935905113 |
| P1a-2 | StyleA | i2v | 2.5 | 41 | — | 961003707 |
| P1a-3 | StyleA | i2v | 2 | 33 | — | 1978515494 |
| P1a-4 | StyleA | i2v | 2 | 33 | — | 2133379389 |
| P1b-1 | StyleA | i2v | 3 | 49 | — | 1560247387 |
| P1b-2 | StyleA | i2v | 3 | 49 | — | 1383103417 |
| P1b-3 | StyleA | i2v | 3 | 49 | — | 517634854 |
| P4a-1 | StyleA | i2v | 3 | 49 | — | 1184852763 |
| P4a-2 | StyleA | i2v | 3 | 49 | — | 1209036025 |
| P4a-3 | StyleA | i2v | 4 | 65 | — | 79326312 |
| P4b-1 | StyleA | i2v | 3.5 | 57 | — | 766038041 |
| P4b-2 | StyleA | i2v | 3.5 | 57 | — | 589813755 |
| P4b-3 | StyleA | i2v | 3 | 49 | — | 1871566692 |
| P5-1 | StyleA | i2v | 2.5 | 41 | — | 977569054 |
| P5-2 | StyleA | i2v | 3 | 49 | — | 885752574 |
| P5-3 | StyleA | i2v | 2.5 | 41 | — | 2019656289 |
| P1a-1 | StyleB | i2v | 2.5 | 41 | — | 784439010 |
| P1a-2 | StyleB | i2v | 2.5 | 41 | — | 542019842 |
| P1a-3 | StyleB | i2v | 2 | 33 | — | 1826918815 |
| P1a-4 | StyleB | i2v | 2 | 33 | — | 1713477766 |
| P1b-1 | StyleB | i2v | 3 | 49 | — | 1173761506 |
| P1b-2 | StyleB | i2v | 3 | 49 | — | 1266231810 |
| P1b-3 | StyleB | i2v | 3 | 49 | — | 131279517 |
| P4a-1 | StyleB | i2v | 3 | 49 | — | 1603680928 |
| P4a-2 | StyleB | i2v | 3 | 49 | — | 1360608580 |
| P4a-3 | StyleB | i2v | 4 | 65 | — | 498286045 |
| P4b-1 | StyleB | i2v | 3.5 | 57 | — | 882999716 |
| P4b-2 | StyleB | i2v | 3.5 | 57 | — | 976127552 |
| P4b-3 | StyleB | i2v | 3 | 49 | — | 1988396767 |
| P5-1 | StyleB | i2v | 2.5 | 41 | — | 592303271 |
| P5-2 | StyleB | i2v | 3 | 49 | — | 767742789 |
| P5-3 | StyleB | i2v | 2.5 | 41 | — | 1634259930 |
| P1a-1 | StyleC | i2v | 2.5 | 41 | — | 1506190964 |
| P1a-2 | StyleC | i2v | 2.5 | 41 | — | 1464443288 |
| P1a-3 | StyleC | i2v | 2 | 33 | — | 467902729 |
| P1a-4 | StyleC | i2v | 2 | 33 | — | 287746064 |
| P1b-1 | StyleC | i2v | 3 | 49 | — | 854662520 |
| P1b-2 | StyleC | i2v | 3 | 49 | — | 1014897300 |
| P1b-3 | StyleC | i2v | 3 | 49 | — | 1892948491 |
| P4a-1 | StyleC | i2v | 3 | 49 | — | 680593974 |
| P4a-2 | StyleC | i2v | 3 | 49 | — | 639503830 |
| P4a-3 | StyleC | i2v | 4 | 65 | — | 1790184779 |
| P4b-1 | StyleC | i2v | 3.5 | 57 | — | 1134997814 |
| P4b-2 | StyleC | i2v | 3.5 | 57 | — | 1294579414 |
| P4b-3 | StyleC | i2v | 3 | 49 | — | 25409097 |
| P5-1 | StyleC | i2v | 2.5 | 41 | — | 1414194225 |
| P5-2 | StyleC | i2v | 3 | 49 | — | 1522918355 |
| P5-3 | StyleC | i2v | 2.5 | 41 | — | 376431436 |

## Prompts de mouvement

### P1a-1_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-2_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon sways in the wind, the mooring ropes pull taut and slacken
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-3_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the banners snap in the wind at the crown of the balloon
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P1a-4_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd turns their heads in one movement toward the basket
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-1_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd parts into two lines, hats are lifted
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-2_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the basket is carried forward, ropes trailing on the grass
Camera : slow lateral tracking to the right, following the basket
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Characters gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-3_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : hands knot the ropes around the wicker rim
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4a-1_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon tears away from the ground, the released ropes fall back
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-2_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd rocks backwards, hats held on with both hands
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-3_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon rises and shrinks above the trees
Camera : very slow tilt upward, following the balloon
Duration : 4 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-1_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rooftops slide slowly below, chimney smoke streams sideways
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-2_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the wicker rim vibrates, the gloved hand tightens on it
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4b-3_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the haze drifts over the city, the dark patch of the crowd stays still
Camera : very slow zoom out
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P5-1_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the hand takes hold of the knife
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-2_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the blade saws the rope, fibres spring free one by one
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-3_StyleA

```
2D cartoon illustration, youtube animation style, vibrant flat design, bold thick clean outlines, simple stylized character design, exaggerated expressive face, flat cel shading with a single hard edged shadow tone, historical period characters in desaturated muted earth tones, era accurate costumes, simplified geometric background shapes less detailed than the characters, single flat shadow tone on the background too, absolutely no photorealism, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rope gives way at once, the strands whip the air
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P1a-1_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-2_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon sways in the wind, the mooring ropes pull taut and slacken
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-3_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the banners snap in the wind at the crown of the balloon
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P1a-4_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd turns their heads in one movement toward the basket
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-1_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd parts into two lines, hats are lifted
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-2_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the basket is carried forward, ropes trailing on the grass
Camera : slow lateral tracking to the right, following the basket
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Characters gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-3_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : hands knot the ropes around the wicker rim
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4a-1_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon tears away from the ground, the released ropes fall back
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-2_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd rocks backwards, hats held on with both hands
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-3_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon rises and shrinks above the trees
Camera : very slow tilt upward, following the balloon
Duration : 4 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-1_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rooftops slide slowly below, chimney smoke streams sideways
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-2_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the wicker rim vibrates, the gloved hand tightens on it
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4b-3_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the haze drifts over the city, the dark patch of the crowd stays still
Camera : very slow zoom out
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P5-1_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the hand takes hold of the knife
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-2_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the blade saws the rope, fibres spring free one by one
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-3_StyleB

```
inkman stick figure cartoon style, large round white heads with bold black ink outline, simple dot eyes and expressive mouths, thin black stick limbs, each arm ending in a simple solid black rounded mitten hand with a small thumb and no separate fingers, flat graphic character design, simplified era accurate period costumes in muted earth tones, set against a richly illustrated animation background painted with atmospheric depth and dramatic lighting, bold graphic shapes, textured light, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rope gives way at once, the strands whip the air
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P1a-1_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the mist drifts slowly across the lawns, the crowd sways gently at the foot of the balloon
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-2_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon sways in the wind, the mooring ropes pull taut and slacken
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1a-3_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the banners snap in the wind at the crown of the balloon
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P1a-4_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd turns their heads in one movement toward the basket
Camera : static
Duration : 2 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-1_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd parts into two lines, hats are lifted
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-2_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the basket is carried forward, ropes trailing on the grass
Camera : slow lateral tracking to the right, following the basket
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Characters gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P1b-3_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : hands knot the ropes around the wicker rim
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4a-1_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon tears away from the ground, the released ropes fall back
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-2_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the crowd rocks backwards, hats held on with both hands
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
The crowd keeps its back to the camera: backs, hats and shawls only, no face turns toward the viewer, no eyes. They gesture and react, they do not speak. Nobody new enters the frame, no figure appears in the foreground.
Motion starts on the first frame, no frozen start.
```

### P4a-3_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the balloon rises and shrinks above the trees
Camera : very slow tilt upward, following the balloon
Duration : 4 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-1_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rooftops slide slowly below, chimney smoke streams sideways
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P4b-2_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the wicker rim vibrates, the gloved hand tightens on it
Camera : static
Duration : 3.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P4b-3_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the haze drifts over the city, the dark patch of the crowd stays still
Camera : very slow zoom out
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```

### P5-1_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the hand takes hold of the knife
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-2_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the blade saws the rope, fibres spring free one by one
Camera : static
Duration : 3 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
Only the hands and arms already in the first frame move; no face, no head and no other person appears.
Motion starts on the first frame, no frozen start.
```

### P5-3_StyleC

```
hand drawn traditional 2D cel animation, classic 1990s action adventure cartoon series style, crisp bold black ink outlines with tapered brush weight, clean flat cel shaded color fills with exactly two tones per area and hard edged shadows, appealing shape driven character design, historical period characters with the palette shifted to muted earth tones while keeping deep teal shadows, era accurate costumes, background layout in the same crisp graphic style and less detailed than the characters, crisp and graphic not painterly, 16:9 frame:

Single continuous shot, no cut, no scene change.
Subject : the rope gives way at once, the strands whip the air
Camera : static
Duration : 2.5 seconds at 16 frames per second.
Limited animation cadence, holds on twos, not fluid interpolation.
There is no character, no person, no face and no hand anywhere in the shot, and nothing appears that is not already in the first frame.
Motion starts on the first frame, no frozen start.
```
