# automatically generated by the FlatBuffers compiler, do not modify

# namespace: apemodefb

import flatbuffers

class AnimStackFb(object):
    __slots__ = ['_tab']

    # AnimStackFb
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AnimStackFb
    def Id(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # AnimStackFb
    def NameId(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreateAnimStackFb(builder, id, nameId):
    builder.Prep(4, 8)
    builder.PrependUint32(nameId)
    builder.PrependUint32(id)
    return builder.Offset()
