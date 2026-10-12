---
title: Lonely
date: 2026-10-11
draft: false
description: A pencil drawing from uni turned into a 3D character in Blender who walks in, sits down and lights a cigarette.
tags:
  - blog
  - drawing
  - blender
featured_image: /images/posts/making/drawing/lonely/drawing.jpg
show_cover: false
---
This one is from my sketchbook at uni: a guy with a long goat-wolf head, pointed ears with bolts in them, dreads and a big toothy grin, in a suit that's too big for him, sitting in front of a bench with guitar pedals on the shelf behind. Across the top it says LONELY. I always wanted to see him move.

![drawing.jpg](static/images/posts/making/drawing/lonely/drawing.jpg)

## First try: moving the drawing itself

The quickest way was to animate the drawing as it is. I cut the photo into layers (the page, the head, each ear, and the little shapes falling down the left margin) and moved them in Blender like a paper puppet: the head sways, the ears twitch, he blinks, and the pencil lines jitter a bit every few frames, like hand-drawn animation.

It looked like the drawing, but it was still flat. What I really wanted was him in 3D.

## Building him in 3D

He's built entirely from a Python script in Blender, with no sculpting. The head is a stack of ellipses that gets narrower towards a chin pushed forward like a goat's. The ears are flattened cones, the dreads are curves that grow from the scalp and sweep back, and the mouth is a hole cut into the snout with teeth around the edge. To stay close to the paper, the first version looked like pencil: flat grey shading, hatching in the shadows, and outlines drawn by Blender's Line Art.

![pencil.jpg](static/images/posts/making/drawing/lonely/pencil.jpg)

Most of the work was looking at him and fixing what was off. He was too chubby, so he got slimmer. The neck was a stick plugged into the jacket, the ears looked like they were about to fall off, and the belt hung so low it looked like he was wearing underwear over his trousers. The long thing hanging down his right side in the drawing isn't a tail, it's his hair. Because it's all code, each fix is a few numbers, and Blender rebuilds the scene as soon as the script is saved.

## Making him move

To walk he needed a skeleton: hips, spine, legs and arms with elbows, with the suit and trousers bending along with them. The stride is worked out from the length of his legs so his feet don't slide (mostly). When he sits down his feet stay where they are and the knees are solved from where his hips are. Once he's sitting, his hands just get targets: the breast pocket, his mouth, the lighter under the tip of the cigarette.

## Color

The pencil look was pale and hard to read, so in the end he got colors: an olive suit, a red tie, a dusk sky in the windows and LONELY as a pink neon sign. The lighter's flame lights up his face.

![walking-in.jpg](static/images/posts/making/drawing/lonely/walking-in.jpg)
![at-the-bench.jpg](static/images/posts/making/drawing/lonely/at-the-bench.jpg)

![wide|Lighting up](static/images/posts/making/drawing/lonely/lighting-up.jpg)

## The animation

He walks in, sits on the bench, takes a cigarette from his pocket, lights it and blows out the smoke.

![wide|Lonely](static/images/posts/making/drawing/lonely/lonely-animation.mp4)

Next: better hands, and maybe more scenes with him.
