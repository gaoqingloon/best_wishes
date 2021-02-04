import tcxparser

tcx = tcxparser.TCXParser('./跑步20210131154035.tcx')

"""
<TrainingCenterDatabase xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd" xmlns:ns5="http://www.garmin.com/xmlschemas/ActivityGoals/v1" xmlns:ns3="http://www.garmin.com/xmlschemas/ActivityExtension/v2" xmlns:ns2="http://www.garmin.com/xmlschemas/UserProfile/v2" xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns4="http://www.garmin.com/xmlschemas/ProfileExtension/v1">
  <Activities>
    <Activity Sport="Running">
      <Id>2021-01-31T07:40:35Z</Id>
      <Lap StartTime="2021-01-31T07:40:35Z">
        <TotalTimeSeconds>438</TotalTimeSeconds>
        <DistanceMeters>1000</DistanceMeters>
        <Intensity>Active</Intensity>
        <TriggerMethod>Manual</TriggerMethod>
        <MaximumHeartRateBpm>
          <Value>141</Value>
        </MaximumHeartRateBpm>
        <AverageHeartRateBpm>
          <Value>130</Value>
        </AverageHeartRateBpm>
        
        <Track>
          <Trackpoint>
            <Time>2021-01-31T07:40:35Z</Time>
            <DistanceMeters>0</DistanceMeters>
          </Trackpoint>

"""
print(tcx.root)
# Duration of workout in seconds
print(tcx.duration)
# latitude/longitude at start of workout
print(tcx.latitude)
# 35.951880198
print(tcx.longitude)
# -79.0931872185
print(tcx.activity_type)
# 'running'
# ISO UTC timestamp when workout completed
print(tcx.completed_at)
# '2012-12-26T22:03:05Z'
# distance of workout in meters
print(tcx.distance)
# 4686.31103516
print(tcx.distance_units)
# 'meters'
# calories burned (as reported by device)
print(tcx.calories)
# 379