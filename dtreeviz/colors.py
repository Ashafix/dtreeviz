import warnings

YELLOW = '#fefecd'
GREEN = '#cfe2d4'
DARKBLUE = '#313695'
BLUE = '#4575b4'
DARKGREEN = '#006400'
LIGHTORANGE = '#fee090'
LIGHTBLUE = '#a6bddb'
GREY = '#444443'
WEDGE_COLOR = GREY

HIGHLIGHT_COLOR = '#D67C03'

color_blind_friendly_colors = {
    0: None,
    1: None,
    2: ['#FEFEBB', '#a1dab4'],
    3: ['#FEFEBB', '#D9E6F5', '#a1dab4'],
    4: ['#FEFEBB', '#D9E6F5', '#a1dab4', LIGHTORANGE],
    5: ['#FEFEBB', '#D9E6F5', '#a1dab4', '#41b6c4', LIGHTORANGE],
    6: ['#FEFEBB', '#c7e9b4', '#41b6c4', '#2c7fb8', LIGHTORANGE, '#f46d43'],
    7: ['#FEFEBB', '#c7e9b4', '#7fcdbb', '#41b6c4', '#225ea8', '#fdae61', '#f46d43'],
    8: ['#FEFEBB', '#edf8b1', '#c7e9b4', '#7fcdbb', '#1d91c0', '#225ea8', '#fdae61', '#f46d43'],
    9: ['#FEFEBB', '#c7e9b4', '#41b6c4', '#74add1', BLUE, DARKBLUE, LIGHTORANGE, '#fdae61', '#f46d43'],
    10: ['#FEFEBB', '#c7e9b4', '#41b6c4', '#74add1', BLUE, DARKBLUE, LIGHTORANGE, '#fdae61', '#f46d43', '#d73027']
}

COLORS = {'scatter_edge': GREY,
          'scatter_marker': BLUE,
          'split_line': GREY,
          'mean_line': '#f46d43',
          'axis_label': GREY,
          'title': GREY,
          'legend_title': GREY,
          'legend_edge': GREY,
          'edge': GREY,
          'color_map_min': '#c7e9b4',
          'color_map_max': '#081d58',
          'classes': color_blind_friendly_colors,
          'rect_edge': GREY,
          'text': GREY,
          'highlight': HIGHLIGHT_COLOR,
          'wedge': WEDGE_COLOR,
          'text_wedge': WEDGE_COLOR,
          'arrow': GREY,
          'tick_label': GREY,
          'leaf_label': GREY,
          'pie': GREY,
          }


def adjust_colors(colors):
    if colors is None:
        return COLORS
    return dict(COLORS, **colors)


def get_class_colors(n_colors, classes=None):
    if classes is None:
        classes = COLORS['classes']
    if n_colors in classes:
        return classes[n_colors]

    max_colors = max(classes.keys())
    warnings.warn(f'more than {max_colors} colors are used, colors are just repeated and not unique')

    new_colors = classes[max_colors]
    for i in range(n_colors - max_colors):
        new_color = classes[max_colors][i % max_colors]
        new_colors.append(new_color)

    return new_colors
