def track_image(filepath_track, img_width=500, img_length=800, zoom=12):
    '''
    Эта функция создаёт изображение, включающее в себя участок карты,
    где проходит текущий трек и сам трек с точками старта и финиша.
    '''

    import gpxpy
    import staticmaps
    import requests

    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)
    context.set_zoom(zoom)

    with open(filepath_track, "r") as file:
        gpx = gpxpy.parse(file)

    for track in gpx.tracks:
        for segment in track.segments:
            line = [staticmaps.create_latlng(
                p.latitude, p.longitude) for p in segment.points]
            context.add_object(staticmaps.Line(line, width=3))

    for point in gpx.walk(only_points=True):
        start = staticmaps.create_latlng(point.latitude, point.longitude)
        marker = staticmaps.ImageMarker(
            start, "start.png", origin_x=27, origin_y=5)
        context.add_object(marker)
        break

    for point in gpx.walk(only_points=True):
        finish = staticmaps.create_latlng(point.latitude, point.longitude)
    marker = staticmaps.ImageMarker(
        finish, "finish.png", origin_x=5, origin_y=35)
    context.add_object(marker)

    try:

        image = context.render_cairo(img_width, img_length)
        image.write_to_png("map.png")

    except requests.exceptions.ConnectionError:
        print('Ошибка подключения к OpenStreetMap')


if __name__ == '__main__':
    track_image('day_2.gpx')
