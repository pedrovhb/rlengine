from dataclasses import dataclass

import pyglet
import typing as T
from pyglet.image import TextureRegion, gl
from pyglet.window import key

window = pyglet.window.Window()


@dataclass
class TileDimensions:
    tile_width: int = 16
    tile_height: int = 16
    sheet_border_x: int = 0
    sheet_border_y: int = 0
    tile_margin_x: int = 1
    tile_margin_y: int = 1


class TiledImageMap:

    def __init__(
            self,
            tiles_filepath: str,
            tile_dimensions: TileDimensions = None
    ):
        self.tile_dimensions = tile_dimensions or TileDimensions()
        self.tiles = pyglet.resource.image(tiles_filepath)
        self.textures: T.Dict[T.Tuple[int, int]] = {}

        for x in range(self.horizontal_tiles):
            for y in range(self.vertical_tiles):
                tex_x = (
                        x * self.tile_dimensions.tile_width
                        + x * self.tile_dimensions.tile_margin_x
                        + self.tile_dimensions.tile_margin_x
                )
                tex_y = (
                        y * self.tile_dimensions.tile_height
                        + y * self.tile_dimensions.tile_margin_y
                        + self.tile_dimensions.tile_margin_y
                )
                w = self.tile_dimensions.tile_width
                h = self.tile_dimensions.tile_height
                self.textures[x, y] = self.tiles.get_region(tex_x, tex_y, w, h)

    def __getitem__(self, item: T.Tuple[int, int]) -> TextureRegion:
        return self.textures[item]

    @property
    def horizontal_tiles(self) -> int:
        return self.tiles.width // self.tile_dimensions.tile_width

    @property
    def vertical_tiles(self) -> int:
        return self.tiles.height // self.tile_dimensions.tile_height


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')


tiles = TiledImageMap("monochrome_transparent.png")
subimage = tiles[4, 3]


@window.event
def on_draw():
    window.clear()
    for i in range(20):
        tiles[3, i].blit(i * 40, 100, 0, 32, 32)


gl.glEnable(gl.GL_TEXTURE_2D)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
pyglet.app.run()
