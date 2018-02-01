# automatically generated by the FlatBuffers compiler, do not modify

# namespace: apemodefb

import flatbuffers

class StaticVertexFb(object):
    __slots__ = ['_tab']

    # StaticVertexFb
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StaticVertexFb
    def Position(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 0)
        return obj

    # StaticVertexFb
    def Normal(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 12)
        return obj

    # StaticVertexFb
    def Tangent(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 24)
        return obj

    # StaticVertexFb
    def Uv(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 40)
        return obj


def CreateStaticVertexFb(builder, position_x, position_y, position_z, normal_x, normal_y, normal_z, tangent_x, tangent_y, tangent_z, tangent_w, uv_x, uv_y):
    builder.Prep(4, 48)
    builder.Prep(4, 8)
    builder.PrependFloat32(uv_y)
    builder.PrependFloat32(uv_x)
    builder.Prep(4, 16)
    builder.PrependFloat32(tangent_w)
    builder.PrependFloat32(tangent_z)
    builder.PrependFloat32(tangent_y)
    builder.PrependFloat32(tangent_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(normal_z)
    builder.PrependFloat32(normal_y)
    builder.PrependFloat32(normal_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(position_z)
    builder.PrependFloat32(position_y)
    builder.PrependFloat32(position_x)
    return builder.Offset()
