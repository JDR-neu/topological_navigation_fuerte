"""autogenerated by genpy from graph_mapping_msgs/GenerateGlobalMapRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GenerateGlobalMapRequest(genpy.Message):
  _md5sum = "f4467c20d63133ab5b96ab9959a2080d"
  _type = "graph_mapping_msgs/GenerateGlobalMapRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 resolution

"""
  __slots__ = ['resolution']
  _slot_types = ['float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       resolution

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GenerateGlobalMapRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.resolution is None:
        self.resolution = 0.
    else:
      self.resolution = 0.

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
      buff.write(_struct_f.pack(self.resolution))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.resolution,) = _struct_f.unpack(str[start:end])
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
      buff.write(_struct_f.pack(self.resolution))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.resolution,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
"""autogenerated by genpy from graph_mapping_msgs/GenerateGlobalMapResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import nav_msgs.msg
import genpy
import std_msgs.msg

class GenerateGlobalMapResponse(genpy.Message):
  _md5sum = "d32df3d6aab41e07d05e6a59c207a1c0"
  _type = "graph_mapping_msgs/GenerateGlobalMapResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """nav_msgs/OccupancyGrid map
bool succeeded


================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

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
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
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
  __slots__ = ['map','succeeded']
  _slot_types = ['nav_msgs/OccupancyGrid','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       map,succeeded

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GenerateGlobalMapResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
      if self.succeeded is None:
        self.succeeded = False
    else:
      self.map = nav_msgs.msg.OccupancyGrid()
      self.succeeded = False

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
      buff.write(_struct_3I.pack(_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2If2I7d.pack(_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.map.data))
      buff.write(_struct_B.pack(self.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w,) = _struct_2If2I7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = struct.unpack(pattern, str[start:end])
      start = end
      end += 1
      (self.succeeded,) = _struct_B.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
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
      buff.write(_struct_3I.pack(_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2If2I7d.pack(_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.map.data.tostring())
      buff.write(_struct_B.pack(self.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.map is None:
        self.map = nav_msgs.msg.OccupancyGrid()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 76
      (_x.map.info.map_load_time.secs, _x.map.info.map_load_time.nsecs, _x.map.info.resolution, _x.map.info.width, _x.map.info.height, _x.map.info.origin.position.x, _x.map.info.origin.position.y, _x.map.info.origin.position.z, _x.map.info.origin.orientation.x, _x.map.info.origin.orientation.y, _x.map.info.origin.orientation.z, _x.map.info.origin.orientation.w,) = _struct_2If2I7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      start = end
      end += 1
      (self.succeeded,) = _struct_B.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2If2I7d = struct.Struct("<2If2I7d")
class GenerateGlobalMap(object):
  _type          = 'graph_mapping_msgs/GenerateGlobalMap'
  _md5sum = 'e2e166b8b209ad77352baa42f6c27607'
  _request_class  = GenerateGlobalMapRequest
  _response_class = GenerateGlobalMapResponse
