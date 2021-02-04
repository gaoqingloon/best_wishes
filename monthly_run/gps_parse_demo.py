# coding: utf-8

# ### 1 读文件并完成解析
import gpxpy.parser as parser

gpx_file = open('./gpx1.3.2_demo.gpx', 'r')  # 读取文件
gpx_parser = parser.GPXParser(gpx_file)
gpx = gpx_parser.parse()  # 文件解析
gpx_file.close()

# ### 2 读文件并完成解析
print('======================')
print(gpx.name)
print(gpx.description)
print(gpx.author_name)
print('======================')

# ### 3 打印解析的轨迹数据
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print('Point at ({0},{1}) -> {2},{3}'.format(point.latitude, point.longitude, point.elevation,
                                                         point.geoid_height))

# ### 4 打印解析的路线
for waypoint in gpx.waypoints:
    print('waypoint {0} -> ({1},{2},{3})'.format(waypoint.name, waypoint.latitude, waypoint.longitude,
                                                 waypoint.elevation))

# ### 5 打印解析的路上各个点数据
for route in gpx.routes:
    for point in route.points:
        print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.name))

# ### 6 其他方法
print("*" * 50)
print('GPX:', gpx.to_xml())
