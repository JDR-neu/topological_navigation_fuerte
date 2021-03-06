"""autogenerated by genpy from laser_slam/LocalizedScan.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class LocalizedScan(genpy.Message):
  _md5sum = "a4d676ce9bf4274df95bd1940071f796"
  _type = "laser_slam/LocalizedScan"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# The reference frame and time point w.r.t which sensor pose is stored
# Note that header.stamp might be different from scan.header.stamp
Header header

# Original scan
sensor_msgs/LaserScan scan

# Point cloud in sensor frame at timepoint header.stamp, corrected for robot movement
sensor_msgs/PointCloud cloud

# Pose of sensor in reference frame
geometry_msgs/Pose sensor_pose

# Barycenter of cloud in ref frame
geometry_msgs/Point barycenter
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/LaserScan
# Single scan from a planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

Header header            # timestamp in the header is the acquisition time of 
                         # the first ray in the scan.
                         #
                         # in frame frame_id, angles are measured around 
                         # the positive Z axis (counterclockwise, if Z is up)
                         # with zero angle being forward along the x axis
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities    # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.

================================================================================
MSG: sensor_msgs/PointCloud
# This message holds a collection of 3d points, plus optional additional
# information about each point.

# Time of sensor data acquisition, coordinate frame ID.
Header header

# Array of 3d points. Each Point32 should be interpreted as a 3d point
# in the frame given in the header.
geometry_msgs/Point32[] points

# Each channel should have the same number of elements as points array,
# and the data in each channel should correspond 1:1 with each point.
# Channel names in common practice are listed in ChannelFloat32.msg.
ChannelFloat32[] channels

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: sensor_msgs/ChannelFloat32
# This message is used by the PointCloud message to hold optional data
# associated with each point in the cloud. The length of the values
# array should be the same as the length of the points array in the
# PointCloud, and each value should be associated with the corresponding
# point.

# Channel names in existing practice include:
#   "u", "v" - row and column (respectively) in the left stereo image.
#              This is opposite to usual conventions but remains for
#              historical reasons. The newer PointCloud2 message has no
#              such problem.
#   "rgb" - For point clouds produced by color stereo cameras. uint8
#           (R,G,B) values packed into the least significant 24 bits,
#           in order.
#   "intensity" - laser or pixel intensity.
#   "distance"

# The channel name should give semantics of the channel (e.g.
# "intensity" instead of "value").
string name

# The values array should be 1-1 with the elements of the associated
# PointCloud.
float32[] values

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['header','scan','cloud','sensor_pose','barycenter']
  _slot_types = ['std_msgs/Header','sensor_msgs/LaserScan','sensor_msgs/PointCloud','geometry_msgs/Pose','geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,scan,cloud,sensor_pose,barycenter

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LocalizedScan, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.scan is None:
        self.scan = sensor_msgs.msg.LaserScan()
      if self.cloud is None:
        self.cloud = sensor_msgs.msg.PointCloud()
      if self.sensor_pose is None:
        self.sensor_pose = geometry_msgs.msg.Pose()
      if self.barycenter is None:
        self.barycenter = geometry_msgs.msg.Point()
    else:
      self.header = std_msgs.msg.Header()
      self.scan = sensor_msgs.msg.LaserScan()
      self.cloud = sensor_msgs.msg.PointCloud()
      self.sensor_pose = geometry_msgs.msg.Pose()
      self.barycenter = geometry_msgs.msg.Point()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.scan.header.seq, _x.scan.header.stamp.secs, _x.scan.header.stamp.nsecs))
      _x = self.scan.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7f.pack(_x.scan.angle_min, _x.scan.angle_max, _x.scan.angle_increment, _x.scan.time_increment, _x.scan.scan_time, _x.scan.range_min, _x.scan.range_max))
      length = len(self.scan.ranges)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.scan.ranges))
      length = len(self.scan.intensities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.scan.intensities))
      _x = self
      buff.write(_struct_3I.pack(_x.cloud.header.seq, _x.cloud.header.stamp.secs, _x.cloud.header.stamp.nsecs))
      _x = self.cloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.cloud.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.cloud.points:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.cloud.channels)
      buff.write(_struct_I.pack(length))
      for val1 in self.cloud.channels:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.values)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.values))
      _x = self
      buff.write(_struct_10d.pack(_x.sensor_pose.position.x, _x.sensor_pose.position.y, _x.sensor_pose.position.z, _x.sensor_pose.orientation.x, _x.sensor_pose.orientation.y, _x.sensor_pose.orientation.z, _x.sensor_pose.orientation.w, _x.barycenter.x, _x.barycenter.y, _x.barycenter.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.scan is None:
        self.scan = sensor_msgs.msg.LaserScan()
      if self.cloud is None:
        self.cloud = sensor_msgs.msg.PointCloud()
      if self.sensor_pose is None:
        self.sensor_pose = geometry_msgs.msg.Pose()
      if self.barycenter is None:
        self.barycenter = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.scan.header.seq, _x.scan.header.stamp.secs, _x.scan.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scan.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scan.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.scan.angle_min, _x.scan.angle_max, _x.scan.angle_increment, _x.scan.time_increment, _x.scan.scan_time, _x.scan.range_min, _x.scan.range_max,) = _struct_7f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.scan.ranges = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.scan.intensities = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 12
      (_x.cloud.header.seq, _x.cloud.header.stamp.secs, _x.cloud.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cloud.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.cloud.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.cloud.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.cloud.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.cloud.channels = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.ChannelFloat32()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.values = struct.unpack(pattern, str[start:end])
        self.cloud.channels.append(val1)
      _x = self
      start = end
      end += 80
      (_x.sensor_pose.position.x, _x.sensor_pose.position.y, _x.sensor_pose.position.z, _x.sensor_pose.orientation.x, _x.sensor_pose.orientation.y, _x.sensor_pose.orientation.z, _x.sensor_pose.orientation.w, _x.barycenter.x, _x.barycenter.y, _x.barycenter.z,) = _struct_10d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.scan.header.seq, _x.scan.header.stamp.secs, _x.scan.header.stamp.nsecs))
      _x = self.scan.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7f.pack(_x.scan.angle_min, _x.scan.angle_max, _x.scan.angle_increment, _x.scan.time_increment, _x.scan.scan_time, _x.scan.range_min, _x.scan.range_max))
      length = len(self.scan.ranges)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.scan.ranges.tostring())
      length = len(self.scan.intensities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.scan.intensities.tostring())
      _x = self
      buff.write(_struct_3I.pack(_x.cloud.header.seq, _x.cloud.header.stamp.secs, _x.cloud.header.stamp.nsecs))
      _x = self.cloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.cloud.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.cloud.points:
        _x = val1
        buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
      length = len(self.cloud.channels)
      buff.write(_struct_I.pack(length))
      for val1 in self.cloud.channels:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.values)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.values.tostring())
      _x = self
      buff.write(_struct_10d.pack(_x.sensor_pose.position.x, _x.sensor_pose.position.y, _x.sensor_pose.position.z, _x.sensor_pose.orientation.x, _x.sensor_pose.orientation.y, _x.sensor_pose.orientation.z, _x.sensor_pose.orientation.w, _x.barycenter.x, _x.barycenter.y, _x.barycenter.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.scan is None:
        self.scan = sensor_msgs.msg.LaserScan()
      if self.cloud is None:
        self.cloud = sensor_msgs.msg.PointCloud()
      if self.sensor_pose is None:
        self.sensor_pose = geometry_msgs.msg.Pose()
      if self.barycenter is None:
        self.barycenter = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.scan.header.seq, _x.scan.header.stamp.secs, _x.scan.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scan.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scan.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.scan.angle_min, _x.scan.angle_max, _x.scan.angle_increment, _x.scan.time_increment, _x.scan.scan_time, _x.scan.range_min, _x.scan.range_max,) = _struct_7f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.scan.ranges = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.scan.intensities = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 12
      (_x.cloud.header.seq, _x.cloud.header.stamp.secs, _x.cloud.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.cloud.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.cloud.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.cloud.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point32()
        _x = val1
        start = end
        end += 12
        (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
        self.cloud.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.cloud.channels = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.ChannelFloat32()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.values = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.cloud.channels.append(val1)
      _x = self
      start = end
      end += 80
      (_x.sensor_pose.position.x, _x.sensor_pose.position.y, _x.sensor_pose.position.z, _x.sensor_pose.orientation.x, _x.sensor_pose.orientation.y, _x.sensor_pose.orientation.z, _x.sensor_pose.orientation.w, _x.barycenter.x, _x.barycenter.y, _x.barycenter.z,) = _struct_10d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_7f = struct.Struct("<7f")
_struct_3I = struct.Struct("<3I")
_struct_3f = struct.Struct("<3f")
_struct_10d = struct.Struct("<10d")
