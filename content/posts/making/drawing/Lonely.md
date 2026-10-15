---
title: Lonely
date: 2026-10-11
draft: false
description: A pencil drawing from uni turned into a 3D character in Blender who walks in, sits down and lights a cigarette.
description_es: Un dibujo a lápiz de la universidad convertido en un personaje 3D en Blender que entra, se sienta y prende un cigarrillo.
tags:
  - blog
  - drawing
  - blender
featured_image: /images/posts/making/drawing/lonely/drawing.jpg
show_cover: false
---
This one is from my sketchbook at uni: a really weird 2d dude with a cat-wolve head, pointed ears with bolts in them, dreads and a big toothy grin, in a suit that's also weirdly squared, he's standing in front of a distant entrance with stairs. The entrance is the Uni's entrance I use to study in.  

![drawing.jpg](static/images/posts/making/drawing/lonely/drawing.jpg)

## First try: moving the drawing itself

The quickest way was to animate the drawing as it is. I cut the photo into layers (the page, the head, each ear, and the little shapes falling down the left margin) and moved them in Blender like a paper puppet: the head sways, the ears twitch, he blinks, and the pencil lines jitter a bit every few frames, like hand-drawn animation.

It looked like the drawing, but it was still flat. What I really wanted was him in 3D. Although, here is where i would say i went the wrong way. From the beginning the drawing was 2D

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

<!--es-->

Este es de mi cuaderno de dibujo de la universidad: un tipo 2D bien raro con cabeza de gato-lobo, orejas puntiagudas con tornillos, dreads y una sonrisa grande llena de dientes, con un traje que también es extrañamente cuadrado, parado frente a una entrada lejana con escaleras. La entrada es la de la universidad donde estudiaba.

![drawing.jpg](static/images/posts/making/drawing/lonely/drawing.jpg)

## Primer intento: animar el dibujo tal cual

Lo más rápido era animar el dibujo así como estaba. Corté la foto en capas (la hoja, la cabeza, cada oreja y las figuritas que caen por el margen izquierdo) y las moví en Blender como un títere de papel: la cabeza se balancea, las orejas se mueven, parpadea, y las líneas de lápiz tiemblan un poco cada tantos frames, como en la animación dibujada a mano.

Se parecía al dibujo, pero seguía siendo plano. Lo que de verdad quería era tenerlo en 3D. Aunque aquí es donde diría que me fui por el camino equivocado. Desde el principio el dibujo era 2D.

## Construirlo en 3D

Está construido completamente con un script de Python en Blender, sin esculpir nada. La cabeza es una pila de elipses que se van angostando hacia una barbilla empujada hacia adelante, como la de una cabra. Las orejas son conos aplanados, los dreads son curvas que salen del cuero cabelludo y se van hacia atrás, y la boca es un hueco cortado en el hocico con dientes alrededor del borde. Para mantenerme cerca del papel, la primera versión parecía hecha a lápiz: sombreado gris plano, tramado en las sombras y contornos dibujados con el Line Art de Blender.

![pencil.jpg](static/images/posts/making/drawing/lonely/pencil.jpg)

La mayor parte del trabajo fue mirarlo y arreglar lo que no cuadraba. Estaba muy gordito, así que lo adelgacé. El cuello era un palo enchufado en la chaqueta, las orejas parecía que se le iban a caer, y el cinturón colgaba tan bajo que parecía que llevaba los calzoncillos por encima del pantalón. Eso largo que le cuelga por el lado derecho en el dibujo no es una cola, es su pelo. Como todo es código, cada arreglo es cambiar un par de números, y Blender reconstruye la escena apenas guardo el script.

## Hacerlo moverse

Para caminar necesitaba un esqueleto: cadera, columna, piernas y brazos con codos, con el traje y el pantalón doblándose junto con ellos. La zancada se calcula a partir del largo de sus piernas para que los pies no se deslicen (casi nunca). Cuando se sienta, los pies se quedan donde están y las rodillas se resuelven a partir de dónde está la cadera. Una vez sentado, las manos solo reciben objetivos: el bolsillo del pecho, la boca, el encendedor bajo la punta del cigarrillo.

## Color

El look de lápiz era pálido y difícil de leer, así que al final le puse colores: un traje verde oliva, una corbata roja, un cielo de atardecer en las ventanas y LONELY como un letrero de neón rosado. La llama del encendedor le ilumina la cara.

![walking-in.jpg](static/images/posts/making/drawing/lonely/walking-in.jpg)
![at-the-bench.jpg](static/images/posts/making/drawing/lonely/at-the-bench.jpg)

![wide|Prendiendo el cigarrillo](static/images/posts/making/drawing/lonely/lighting-up.jpg)

## La animación

Entra, se sienta en la banca, saca un cigarrillo del bolsillo, lo prende y bota el humo.

![wide|Lonely](static/images/posts/making/drawing/lonely/lonely-animation.mp4)

Lo que sigue: mejores manos, y quizás más escenas con él.
