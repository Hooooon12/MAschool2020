# This file was automatically created by FeynRules 2.3.1
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Fri 15 May 2015 03:47:37



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
RRd1x3 = Parameter(name = 'RRd1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.9862151,
                   texname = '\\text{RRd1x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 1, 3 ])

RRd1x6 = Parameter(name = 'RRd1x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.1654681,
                   texname = '\\text{RRd1x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 1, 6 ])

RRd2x3 = Parameter(name = 'RRd2x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.1654681,
                   texname = '\\text{RRd2x3}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 2, 3 ])

RRd2x6 = Parameter(name = 'RRd2x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.9862151,
                   texname = '\\text{RRd2x6}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 2, 6 ])

RRd3x5 = Parameter(name = 'RRd3x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd3x5}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 3, 5 ])

RRd4x4 = Parameter(name = 'RRd4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd4x4}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 4, 4 ])

RRd5x2 = Parameter(name = 'RRd5x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd5x2}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 5, 2 ])

RRd6x1 = Parameter(name = 'RRd6x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRd6x1}',
                   lhablock = 'DSQMIX',
                   lhacode = [ 6, 1 ])

alp = Parameter(name = 'alp',
                nature = 'external',
                type = 'real',
                value = -0.1075727,
                texname = '\\alpha',
                lhablock = 'FRALPHA',
                lhacode = [ 1 ])

RMUH = Parameter(name = 'RMUH',
                 nature = 'external',
                 type = 'real',
                 value = 464.2435,
                 texname = '\\text{RMUH}',
                 lhablock = 'HMIX',
                 lhacode = [ 1 ])

tb = Parameter(name = 'tb',
               nature = 'external',
               type = 'real',
               value = 9.749107,
               texname = 't_b',
               lhablock = 'HMIX',
               lhacode = [ 2 ])

MA2 = Parameter(name = 'MA2',
                nature = 'external',
                type = 'real',
                value = 325121.6,
                texname = '\\text{Subsuperscript}[m,A,2]',
                lhablock = 'HMIX',
                lhacode = [ 4 ])

ICKM1x3 = Parameter(name = 'ICKM1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.003349042,
                    texname = '\\text{ICKM1x3}',
                    lhablock = 'IMVCKM',
                    lhacode = [ 1, 3 ])

ICKM2x1 = Parameter(name = 'ICKM2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.0001377152,
                    texname = '\\text{ICKM2x1}',
                    lhablock = 'IMVCKM',
                    lhacode = [ 2, 1 ])

ICKM2x2 = Parameter(name = 'ICKM2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.00003212913,
                    texname = '\\text{ICKM2x2}',
                    lhablock = 'IMVCKM',
                    lhacode = [ 2, 2 ])

ICKM3x1 = Parameter(name = 'ICKM3x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.00325855,
                    texname = '\\text{ICKM3x1}',
                    lhablock = 'IMVCKM',
                    lhacode = [ 3, 1 ])

ICKM3x2 = Parameter(name = 'ICKM3x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.0007602238,
                    texname = '\\text{ICKM3x2}',
                    lhablock = 'IMVCKM',
                    lhacode = [ 3, 2 ])

RmD21x1 = Parameter(name = 'RmD21x1',
                    nature = 'external',
                    type = 'real',
                    value = 354397.9,
                    texname = '\\text{RmD21x1}',
                    lhablock = 'MSD2',
                    lhacode = [ 1, 1 ])

RmD22x2 = Parameter(name = 'RmD22x2',
                    nature = 'external',
                    type = 'real',
                    value = 354392.9,
                    texname = '\\text{RmD22x2}',
                    lhablock = 'MSD2',
                    lhacode = [ 2, 2 ])

RmD23x3 = Parameter(name = 'RmD23x3',
                    nature = 'external',
                    type = 'real',
                    value = 346135.1,
                    texname = '\\text{RmD23x3}',
                    lhablock = 'MSD2',
                    lhacode = [ 3, 3 ])

RmE21x1 = Parameter(name = 'RmE21x1',
                    nature = 'external',
                    type = 'real',
                    value = 98195.12,
                    texname = '\\text{RmE21x1}',
                    lhablock = 'MSE2',
                    lhacode = [ 1, 1 ])

RmE22x2 = Parameter(name = 'RmE22x2',
                    nature = 'external',
                    type = 'real',
                    value = 98178.83,
                    texname = '\\text{RmE22x2}',
                    lhablock = 'MSE2',
                    lhacode = [ 2, 2 ])

RmE23x3 = Parameter(name = 'RmE23x3',
                    nature = 'external',
                    type = 'real',
                    value = 93612.93,
                    texname = '\\text{RmE23x3}',
                    lhablock = 'MSE2',
                    lhacode = [ 3, 3 ])

RmL21x1 = Parameter(name = 'RmL21x1',
                    nature = 'external',
                    type = 'real',
                    value = 117412.8,
                    texname = '\\text{RmL21x1}',
                    lhablock = 'MSL2',
                    lhacode = [ 1, 1 ])

RmL22x2 = Parameter(name = 'RmL22x2',
                    nature = 'external',
                    type = 'real',
                    value = 117404.7,
                    texname = '\\text{RmL22x2}',
                    lhablock = 'MSL2',
                    lhacode = [ 2, 2 ])

RmL23x3 = Parameter(name = 'RmL23x3',
                    nature = 'external',
                    type = 'real',
                    value = 115141.1,
                    texname = '\\text{RmL23x3}',
                    lhablock = 'MSL2',
                    lhacode = [ 3, 3 ])

RMx1 = Parameter(name = 'RMx1',
                 nature = 'external',
                 type = 'real',
                 value = 102.1024,
                 texname = '\\text{RMx1}',
                 lhablock = 'MSOFT',
                 lhacode = [ 1 ])

RMx2 = Parameter(name = 'RMx2',
                 nature = 'external',
                 type = 'real',
                 value = 192.6534,
                 texname = '\\text{RMx2}',
                 lhablock = 'MSOFT',
                 lhacode = [ 2 ])

RMx3 = Parameter(name = 'RMx3',
                 nature = 'external',
                 type = 'real',
                 value = 588.4243,
                 texname = '\\text{RMx3}',
                 lhablock = 'MSOFT',
                 lhacode = [ 3 ])

mHu2 = Parameter(name = 'mHu2',
                 nature = 'external',
                 type = 'real',
                 value = 102141.1,
                 texname = '\\text{Subsuperscript}\\left[m,H_u,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 21 ])

mHd2 = Parameter(name = 'mHd2',
                 nature = 'external',
                 type = 'real',
                 value = -215451.9,
                 texname = '\\text{Subsuperscript}\\left[m,H_d,2\\right]',
                 lhablock = 'MSOFT',
                 lhacode = [ 22 ])

RmQ21x1 = Parameter(name = 'RmQ21x1',
                    nature = 'external',
                    type = 'real',
                    value = 375246.6,
                    texname = '\\text{RmQ21x1}',
                    lhablock = 'MSQ2',
                    lhacode = [ 1, 1 ])

RmQ22x2 = Parameter(name = 'RmQ22x2',
                    nature = 'external',
                    type = 'real',
                    value = 375241.8,
                    texname = '\\text{RmQ22x2}',
                    lhablock = 'MSQ2',
                    lhacode = [ 2, 2 ])

RmQ23x3 = Parameter(name = 'RmQ23x3',
                    nature = 'external',
                    type = 'real',
                    value = 269949.8,
                    texname = '\\text{RmQ23x3}',
                    lhablock = 'MSQ2',
                    lhacode = [ 3, 3 ])

RmU21x1 = Parameter(name = 'RmU21x1',
                    nature = 'external',
                    type = 'real',
                    value = 356488.1,
                    texname = '\\text{RmU21x1}',
                    lhablock = 'MSU2',
                    lhacode = [ 1, 1 ])

RmU22x2 = Parameter(name = 'RmU22x2',
                    nature = 'external',
                    type = 'real',
                    value = 356483.5,
                    texname = '\\text{RmU22x2}',
                    lhablock = 'MSU2',
                    lhacode = [ 2, 2 ])

RmU23x3 = Parameter(name = 'RmU23x3',
                    nature = 'external',
                    type = 'real',
                    value = 149411.4,
                    texname = '\\text{RmU23x3}',
                    lhablock = 'MSU2',
                    lhacode = [ 3, 3 ])

RNN1x1 = Parameter(name = 'RNN1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.9927936,
                   texname = '\\text{RNN1x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 1 ])

RNN1x2 = Parameter(name = 'RNN1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.03701124,
                   texname = '\\text{RNN1x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 2 ])

RNN1x3 = Parameter(name = 'RNN1x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.1087277,
                   texname = '\\text{RNN1x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 3 ])

RNN1x4 = Parameter(name = 'RNN1x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.03419427,
                   texname = '\\text{RNN1x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 1, 4 ])

RNN2x1 = Parameter(name = 'RNN2x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.06145626,
                   texname = '\\text{RNN2x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 1 ])

RNN2x2 = Parameter(name = 'RNN2x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.9731574,
                   texname = '\\text{RNN2x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 2 ])

RNN2x3 = Parameter(name = 'RNN2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1992759,
                   texname = '\\text{RNN2x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 3 ])

RNN2x4 = Parameter(name = 'RNN2x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.09734984,
                   texname = '\\text{RNN2x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 2, 4 ])

RNN3x1 = Parameter(name = 'RNN3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.04928328,
                   texname = '\\text{RNN3x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 1 ])

RNN3x2 = Parameter(name = 'RNN3x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.07521552,
                   texname = '\\text{RNN3x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 2 ])

RNN3x3 = Parameter(name = 'RNN3x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.6987909,
                   texname = '\\text{RNN3x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 3 ])

RNN3x4 = Parameter(name = 'RNN3x4',
                   nature = 'external',
                   type = 'real',
                   value = -0.7096514,
                   texname = '\\text{RNN3x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 3, 4 ])

RNN4x1 = Parameter(name = 'RNN4x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.09030553,
                   texname = '\\text{RNN4x1}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 1 ])

RNN4x2 = Parameter(name = 'RNN4x2',
                   nature = 'external',
                   type = 'real',
                   value = -0.2143305,
                   texname = '\\text{RNN4x2}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 2 ])

RNN4x3 = Parameter(name = 'RNN4x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.6783499,
                   texname = '\\text{RNN4x3}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 3 ])

RNN4x4 = Parameter(name = 'RNN4x4',
                   nature = 'external',
                   type = 'real',
                   value = 0.6969568,
                   texname = '\\text{RNN4x4}',
                   lhablock = 'NMIX',
                   lhacode = [ 4, 4 ])

RLLE1x2x1 = Parameter(name = 'RLLE1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x2x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 2, 1 ])

RLLE1x2x2 = Parameter(name = 'RLLE1x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x2x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 2, 2 ])

RLLE1x2x3 = Parameter(name = 'RLLE1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x2x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 2, 3 ])

RLLE1x3x1 = Parameter(name = 'RLLE1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x3x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 3, 1 ])

RLLE1x3x2 = Parameter(name = 'RLLE1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x3x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 3, 2 ])

RLLE1x3x3 = Parameter(name = 'RLLE1x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE1x3x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 1, 3, 3 ])

RLLE2x1x1 = Parameter(name = 'RLLE2x1x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE2x1x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 1, 1 ])

RLLE2x1x2 = Parameter(name = 'RLLE2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE2x1x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 1, 2 ])

RLLE2x1x3 = Parameter(name = 'RLLE2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE2x1x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 1, 3 ])

RLLE2x3x1 = Parameter(name = 'RLLE2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE2x3x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 3, 1 ])

RLLE2x3x2 = Parameter(name = 'RLLE2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE2x3x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 3, 2 ])

RLLE2x3x3 = Parameter(name = 'RLLE2x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLLE2x3x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 2, 3, 3 ])

RLLE3x1x1 = Parameter(name = 'RLLE3x1x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x1x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 1, 1 ])

RLLE3x1x2 = Parameter(name = 'RLLE3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x1x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 1, 2 ])

RLLE3x1x3 = Parameter(name = 'RLLE3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x1x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 1, 3 ])

RLLE3x2x1 = Parameter(name = 'RLLE3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x2x1}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 2, 1 ])

RLLE3x2x2 = Parameter(name = 'RLLE3x2x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x2x2}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 2, 2 ])

RLLE3x2x3 = Parameter(name = 'RLLE3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLLE3x2x3}',
                      lhablock = 'RVLAMLLE',
                      lhacode = [ 3, 2, 3 ])

RLQD1x1x1 = Parameter(name = 'RLQD1x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x1x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 1, 1 ])

RLQD1x1x2 = Parameter(name = 'RLQD1x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x1x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 1, 2 ])

RLQD1x1x3 = Parameter(name = 'RLQD1x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x1x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 1, 3 ])

RLQD1x2x1 = Parameter(name = 'RLQD1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x2x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 2, 1 ])

RLQD1x2x2 = Parameter(name = 'RLQD1x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x2x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 2, 2 ])

RLQD1x2x3 = Parameter(name = 'RLQD1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x2x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 2, 3 ])

RLQD1x3x1 = Parameter(name = 'RLQD1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x3x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 3, 1 ])

RLQD1x3x2 = Parameter(name = 'RLQD1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x3x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 3, 2 ])

RLQD1x3x3 = Parameter(name = 'RLQD1x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD1x3x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 1, 3, 3 ])

RLQD2x1x1 = Parameter(name = 'RLQD2x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x1x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 1, 1 ])

RLQD2x1x2 = Parameter(name = 'RLQD2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x1x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 1, 2 ])

RLQD2x1x3 = Parameter(name = 'RLQD2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x1x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 1, 3 ])

RLQD2x2x1 = Parameter(name = 'RLQD2x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x2x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 2, 1 ])

RLQD2x2x2 = Parameter(name = 'RLQD2x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x2x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 2, 2 ])

RLQD2x2x3 = Parameter(name = 'RLQD2x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x2x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 2, 3 ])

RLQD2x3x1 = Parameter(name = 'RLQD2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x3x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 3, 1 ])

RLQD2x3x2 = Parameter(name = 'RLQD2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x3x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 3, 2 ])

RLQD2x3x3 = Parameter(name = 'RLQD2x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD2x3x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 2, 3, 3 ])

RLQD3x1x1 = Parameter(name = 'RLQD3x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x1x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 1, 1 ])

RLQD3x1x2 = Parameter(name = 'RLQD3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x1x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 1, 2 ])

RLQD3x1x3 = Parameter(name = 'RLQD3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x1x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 1, 3 ])

RLQD3x2x1 = Parameter(name = 'RLQD3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x2x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 2, 1 ])

RLQD3x2x2 = Parameter(name = 'RLQD3x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x2x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 2, 2 ])

RLQD3x2x3 = Parameter(name = 'RLQD3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x2x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 2, 3 ])

RLQD3x3x1 = Parameter(name = 'RLQD3x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x3x1}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 3, 1 ])

RLQD3x3x2 = Parameter(name = 'RLQD3x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x3x2}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 3, 2 ])

RLQD3x3x3 = Parameter(name = 'RLQD3x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RLQD3x3x3}',
                      lhablock = 'RVLAMLQD',
                      lhacode = [ 3, 3, 3 ])

RLDD1x1x2 = Parameter(name = 'RLDD1x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD1x1x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 1, 2 ])

RLDD1x1x3 = Parameter(name = 'RLDD1x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD1x1x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 1, 3 ])

RLDD1x2x1 = Parameter(name = 'RLDD1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD1x2x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 2, 1 ])

RLDD1x2x3 = Parameter(name = 'RLDD1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD1x2x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 2, 3 ])

RLDD1x3x1 = Parameter(name = 'RLDD1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD1x3x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 3, 1 ])

RLDD1x3x2 = Parameter(name = 'RLDD1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD1x3x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 1, 3, 2 ])

RLDD2x1x2 = Parameter(name = 'RLDD2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD2x1x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 1, 2 ])

RLDD2x1x3 = Parameter(name = 'RLDD2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD2x1x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 1, 3 ])

RLDD2x2x1 = Parameter(name = 'RLDD2x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD2x2x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 2, 1 ])

RLDD2x2x3 = Parameter(name = 'RLDD2x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD2x2x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 2, 3 ])

RLDD2x3x1 = Parameter(name = 'RLDD2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD2x3x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 3, 1 ])

RLDD2x3x2 = Parameter(name = 'RLDD2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD2x3x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 2, 3, 2 ])

RLDD3x1x2 = Parameter(name = 'RLDD3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD3x1x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 1, 2 ])

RLDD3x1x3 = Parameter(name = 'RLDD3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD3x1x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 1, 3 ])

RLDD3x2x1 = Parameter(name = 'RLDD3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD3x2x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 2, 1 ])

RLDD3x2x3 = Parameter(name = 'RLDD3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RLDD3x2x3}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 2, 3 ])

RLDD3x3x1 = Parameter(name = 'RLDD3x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD3x3x1}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 3, 1 ])

RLDD3x3x2 = Parameter(name = 'RLDD3x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RLDD3x3x2}',
                      lhablock = 'RVLAMUDD',
                      lhacode = [ 3, 3, 2 ])

RTLE1x2x1 = Parameter(name = 'RTLE1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x2x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 2, 1 ])

RTLE1x2x2 = Parameter(name = 'RTLE1x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x2x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 2, 2 ])

RTLE1x2x3 = Parameter(name = 'RTLE1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x2x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 2, 3 ])

RTLE1x3x1 = Parameter(name = 'RTLE1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x3x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 3, 1 ])

RTLE1x3x2 = Parameter(name = 'RTLE1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x3x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 3, 2 ])

RTLE1x3x3 = Parameter(name = 'RTLE1x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE1x3x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 1, 3, 3 ])

RTLE2x1x1 = Parameter(name = 'RTLE2x1x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE2x1x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 1, 1 ])

RTLE2x1x2 = Parameter(name = 'RTLE2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE2x1x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 1, 2 ])

RTLE2x1x3 = Parameter(name = 'RTLE2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE2x1x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 1, 3 ])

RTLE2x3x1 = Parameter(name = 'RTLE2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE2x3x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 3, 1 ])

RTLE2x3x2 = Parameter(name = 'RTLE2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE2x3x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 3, 2 ])

RTLE2x3x3 = Parameter(name = 'RTLE2x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTLE2x3x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 2, 3, 3 ])

RTLE3x1x1 = Parameter(name = 'RTLE3x1x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x1x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 1, 1 ])

RTLE3x1x2 = Parameter(name = 'RTLE3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x1x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 1, 2 ])

RTLE3x1x3 = Parameter(name = 'RTLE3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x1x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 1, 3 ])

RTLE3x2x1 = Parameter(name = 'RTLE3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x2x1}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 2, 1 ])

RTLE3x2x2 = Parameter(name = 'RTLE3x2x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x2x2}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 2, 2 ])

RTLE3x2x3 = Parameter(name = 'RTLE3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTLE3x2x3}',
                      lhablock = 'RVTLLE',
                      lhacode = [ 3, 2, 3 ])

RTQD1x1x1 = Parameter(name = 'RTQD1x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x1x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 1, 1 ])

RTQD1x1x2 = Parameter(name = 'RTQD1x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x1x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 1, 2 ])

RTQD1x1x3 = Parameter(name = 'RTQD1x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x1x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 1, 3 ])

RTQD1x2x1 = Parameter(name = 'RTQD1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x2x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 2, 1 ])

RTQD1x2x2 = Parameter(name = 'RTQD1x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x2x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 2, 2 ])

RTQD1x2x3 = Parameter(name = 'RTQD1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x2x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 2, 3 ])

RTQD1x3x1 = Parameter(name = 'RTQD1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x3x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 3, 1 ])

RTQD1x3x2 = Parameter(name = 'RTQD1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x3x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 3, 2 ])

RTQD1x3x3 = Parameter(name = 'RTQD1x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD1x3x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 1, 3, 3 ])

RTQD2x1x1 = Parameter(name = 'RTQD2x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x1x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 1, 1 ])

RTQD2x1x2 = Parameter(name = 'RTQD2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x1x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 1, 2 ])

RTQD2x1x3 = Parameter(name = 'RTQD2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x1x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 1, 3 ])

RTQD2x2x1 = Parameter(name = 'RTQD2x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x2x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 2, 1 ])

RTQD2x2x2 = Parameter(name = 'RTQD2x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x2x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 2, 2 ])

RTQD2x2x3 = Parameter(name = 'RTQD2x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x2x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 2, 3 ])

RTQD2x3x1 = Parameter(name = 'RTQD2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x3x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 3, 1 ])

RTQD2x3x2 = Parameter(name = 'RTQD2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x3x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 3, 2 ])

RTQD2x3x3 = Parameter(name = 'RTQD2x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD2x3x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 2, 3, 3 ])

RTQD3x1x1 = Parameter(name = 'RTQD3x1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x1x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 1, 1 ])

RTQD3x1x2 = Parameter(name = 'RTQD3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x1x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 1, 2 ])

RTQD3x1x3 = Parameter(name = 'RTQD3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x1x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 1, 3 ])

RTQD3x2x1 = Parameter(name = 'RTQD3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x2x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 2, 1 ])

RTQD3x2x2 = Parameter(name = 'RTQD3x2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x2x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 2, 2 ])

RTQD3x2x3 = Parameter(name = 'RTQD3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x2x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 2, 3 ])

RTQD3x3x1 = Parameter(name = 'RTQD3x3x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x3x1}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 3, 1 ])

RTQD3x3x2 = Parameter(name = 'RTQD3x3x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x3x2}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 3, 2 ])

RTQD3x3x3 = Parameter(name = 'RTQD3x3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{RTQD3x3x3}',
                      lhablock = 'RVTLQD',
                      lhacode = [ 3, 3, 3 ])

RTDD1x1x2 = Parameter(name = 'RTDD1x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD1x1x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 1, 2 ])

RTDD1x1x3 = Parameter(name = 'RTDD1x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD1x1x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 1, 3 ])

RTDD1x2x1 = Parameter(name = 'RTDD1x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD1x2x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 2, 1 ])

RTDD1x2x3 = Parameter(name = 'RTDD1x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD1x2x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 2, 3 ])

RTDD1x3x1 = Parameter(name = 'RTDD1x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD1x3x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 3, 1 ])

RTDD1x3x2 = Parameter(name = 'RTDD1x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD1x3x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 1, 3, 2 ])

RTDD2x1x2 = Parameter(name = 'RTDD2x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD2x1x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 1, 2 ])

RTDD2x1x3 = Parameter(name = 'RTDD2x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD2x1x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 1, 3 ])

RTDD2x2x1 = Parameter(name = 'RTDD2x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD2x2x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 2, 1 ])

RTDD2x2x3 = Parameter(name = 'RTDD2x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD2x2x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 2, 3 ])

RTDD2x3x1 = Parameter(name = 'RTDD2x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD2x3x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 3, 1 ])

RTDD2x3x2 = Parameter(name = 'RTDD2x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD2x3x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 2, 3, 2 ])

RTDD3x1x2 = Parameter(name = 'RTDD3x1x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD3x1x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 1, 2 ])

RTDD3x1x3 = Parameter(name = 'RTDD3x1x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD3x1x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 1, 3 ])

RTDD3x2x1 = Parameter(name = 'RTDD3x2x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD3x2x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 2, 1 ])

RTDD3x2x3 = Parameter(name = 'RTDD3x2x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{RTDD3x2x3}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 2, 3 ])

RTDD3x3x1 = Parameter(name = 'RTDD3x3x1',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD3x3x1}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 3, 1 ])

RTDD3x3x2 = Parameter(name = 'RTDD3x3x2',
                      nature = 'external',
                      type = 'real',
                      value = -0.2,
                      texname = '\\text{RTDD3x3x2}',
                      lhablock = 'RVTUDD',
                      lhacode = [ 3, 3, 2 ])

RRl1x3 = Parameter(name = 'RRl1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.3474325,
                   texname = '\\text{RRl1x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 1, 3 ])

RRl1x6 = Parameter(name = 'RRl1x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.937705,
                   texname = '\\text{RRl1x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 1, 6 ])

RRl2x5 = Parameter(name = 'RRl2x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl2x5}',
                   lhablock = 'SELMIX',
                   lhacode = [ 2, 5 ])

RRl3x4 = Parameter(name = 'RRl3x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl3x4}',
                   lhablock = 'SELMIX',
                   lhacode = [ 3, 4 ])

RRl4x1 = Parameter(name = 'RRl4x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl4x1}',
                   lhablock = 'SELMIX',
                   lhacode = [ 4, 1 ])

RRl5x2 = Parameter(name = 'RRl5x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRl5x2}',
                   lhablock = 'SELMIX',
                   lhacode = [ 5, 2 ])

RRl6x3 = Parameter(name = 'RRl6x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.937705,
                   texname = '\\text{RRl6x3}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 3 ])

RRl6x6 = Parameter(name = 'RRl6x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.3474325,
                   texname = '\\text{RRl6x6}',
                   lhablock = 'SELMIX',
                   lhacode = [ 6, 6 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.934,
                  texname = '\\text{Subsuperscript}[\\alpha ,w,-1]',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1176,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

RRn1x3 = Parameter(name = 'RRn1x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn1x3}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 1, 3 ])

RRn2x2 = Parameter(name = 'RRn2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn2x2}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 2, 2 ])

RRn3x1 = Parameter(name = 'RRn3x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRn3x1}',
                   lhablock = 'SNUMIX',
                   lhacode = [ 3, 1 ])

Rtd1x1 = Parameter(name = 'Rtd1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.2551888,
                   texname = '\\text{Rtd1x1}',
                   lhablock = 'TD',
                   lhacode = [ 1, 1 ])

Rtd2x2 = Parameter(name = 'Rtd2x2',
                   nature = 'external',
                   type = 'real',
                   value = -4.374642,
                   texname = '\\text{Rtd2x2}',
                   lhablock = 'TD',
                   lhacode = [ 2, 2 ])

Rtd3x3 = Parameter(name = 'Rtd3x3',
                   nature = 'external',
                   type = 'real',
                   value = -167.718,
                   texname = '\\text{Rtd3x3}',
                   lhablock = 'TD',
                   lhacode = [ 3, 3 ])

Rte1x1 = Parameter(name = 'Rte1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.02155743,
                   texname = '\\text{Rte1x1}',
                   lhablock = 'TE',
                   lhacode = [ 1, 1 ])

Rte2x2 = Parameter(name = 'Rte2x2',
                   nature = 'external',
                   type = 'real',
                   value = -4.457265,
                   texname = '\\text{Rte2x2}',
                   lhablock = 'TE',
                   lhacode = [ 2, 2 ])

Rte3x3 = Parameter(name = 'Rte3x3',
                   nature = 'external',
                   type = 'real',
                   value = -74.36274,
                   texname = '\\text{Rte3x3}',
                   lhablock = 'TE',
                   lhacode = [ 3, 3 ])

Rtu1x1 = Parameter(name = 'Rtu1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.008900702,
                   texname = '\\text{Rtu1x1}',
                   lhablock = 'TU',
                   lhacode = [ 1, 1 ])

Rtu2x2 = Parameter(name = 'Rtu2x2',
                   nature = 'external',
                   type = 'real',
                   value = -3.560256,
                   texname = '\\text{Rtu2x2}',
                   lhablock = 'TU',
                   lhacode = [ 2, 2 ])

Rtu3x3 = Parameter(name = 'Rtu3x3',
                   nature = 'external',
                   type = 'real',
                   value = -588.7617,
                   texname = '\\text{Rtu3x3}',
                   lhablock = 'TU',
                   lhacode = [ 3, 3 ])

RUU1x1 = Parameter(name = 'RUU1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.9576948,
                   texname = '\\text{RUU1x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 1 ])

RUU1x2 = Parameter(name = 'RUU1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.2877859,
                   texname = '\\text{RUU1x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 1, 2 ])

RUU2x1 = Parameter(name = 'RUU2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.2877859,
                   texname = '\\text{RUU2x1}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 1 ])

RUU2x2 = Parameter(name = 'RUU2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.9576948,
                   texname = '\\text{RUU2x2}',
                   lhablock = 'UMIX',
                   lhacode = [ 2, 2 ])

RMNS1x1 = Parameter(name = 'RMNS1x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS1x1}',
                    lhablock = 'UPMNS',
                    lhacode = [ 1, 1 ])

RMNS2x2 = Parameter(name = 'RMNS2x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS2x2}',
                    lhablock = 'UPMNS',
                    lhacode = [ 2, 2 ])

RMNS3x3 = Parameter(name = 'RMNS3x3',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{RMNS3x3}',
                    lhablock = 'UPMNS',
                    lhacode = [ 3, 3 ])

RRu1x3 = Parameter(name = 'RRu1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.5111614,
                   texname = '\\text{RRu1x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 1, 3 ])

RRu1x6 = Parameter(name = 'RRu1x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.8594848,
                   texname = '\\text{RRu1x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 1, 6 ])

RRu2x3 = Parameter(name = 'RRu2x3',
                   nature = 'external',
                   type = 'real',
                   value = -0.8594848,
                   texname = '\\text{RRu2x3}',
                   lhablock = 'USQMIX',
                   lhacode = [ 2, 3 ])

RRu2x6 = Parameter(name = 'RRu2x6',
                   nature = 'external',
                   type = 'real',
                   value = 0.5111614,
                   texname = '\\text{RRu2x6}',
                   lhablock = 'USQMIX',
                   lhacode = [ 2, 6 ])

RRu3x5 = Parameter(name = 'RRu3x5',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu3x5}',
                   lhablock = 'USQMIX',
                   lhacode = [ 3, 5 ])

RRu4x4 = Parameter(name = 'RRu4x4',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu4x4}',
                   lhablock = 'USQMIX',
                   lhacode = [ 4, 4 ])

RRu5x1 = Parameter(name = 'RRu5x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu5x1}',
                   lhablock = 'USQMIX',
                   lhacode = [ 5, 1 ])

RRu6x2 = Parameter(name = 'RRu6x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{RRu6x2}',
                   lhablock = 'USQMIX',
                   lhacode = [ 6, 2 ])

RCKM1x1 = Parameter(name = 'RCKM1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.9738404,
                    texname = '\\text{RCKM1x1}',
                    lhablock = 'VCKM',
                    lhacode = [ 1, 1 ])

RCKM1x2 = Parameter(name = 'RCKM1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.2271982,
                    texname = '\\text{RCKM1x2}',
                    lhablock = 'VCKM',
                    lhacode = [ 1, 2 ])

RCKM1x3 = Parameter(name = 'RCKM1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.002173989,
                    texname = '\\text{RCKM1x3}',
                    lhablock = 'VCKM',
                    lhacode = [ 1, 3 ])

RCKM2x1 = Parameter(name = 'RCKM2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.2270868,
                    texname = '\\text{RCKM2x1}',
                    lhablock = 'VCKM',
                    lhacode = [ 2, 1 ])

RCKM2x2 = Parameter(name = 'RCKM2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.9729587,
                    texname = '\\text{RCKM2x2}',
                    lhablock = 'VCKM',
                    lhacode = [ 2, 2 ])

RCKM2x3 = Parameter(name = 'RCKM2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.04222469,
                    texname = '\\text{RCKM2x3}',
                    lhablock = 'VCKM',
                    lhacode = [ 2, 3 ])

RCKM3x1 = Parameter(name = 'RCKM3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.007478279,
                    texname = '\\text{RCKM3x1}',
                    lhablock = 'VCKM',
                    lhacode = [ 3, 1 ])

RCKM3x2 = Parameter(name = 'RCKM3x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.04161426,
                    texname = '\\text{RCKM3x2}',
                    lhablock = 'VCKM',
                    lhacode = [ 3, 2 ])

RCKM3x3 = Parameter(name = 'RCKM3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.9991002,
                    texname = '\\text{RCKM3x3}',
                    lhablock = 'VCKM',
                    lhacode = [ 3, 3 ])

RVV1x1 = Parameter(name = 'RVV1x1',
                   nature = 'external',
                   type = 'real',
                   value = -0.9899065,
                   texname = '\\text{RVV1x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 1 ])

RVV1x2 = Parameter(name = 'RVV1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.1417221,
                   texname = '\\text{RVV1x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 1, 2 ])

RVV2x1 = Parameter(name = 'RVV2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.1417221,
                   texname = '\\text{RVV2x1}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 1 ])

RVV2x2 = Parameter(name = 'RVV2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.9899065,
                   texname = '\\text{RVV2x2}',
                   lhablock = 'VMIX',
                   lhacode = [ 2, 2 ])

Ryd1x1 = Parameter(name = 'Ryd1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.0001884671,
                   texname = '\\text{Ryd1x1}',
                   lhablock = 'YD',
                   lhacode = [ 1, 1 ])

Ryd2x2 = Parameter(name = 'Ryd2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.003230863,
                   texname = '\\text{Ryd2x2}',
                   lhablock = 'YD',
                   lhacode = [ 2, 2 ])

Ryd3x3 = Parameter(name = 'Ryd3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1360783,
                   texname = '\\text{Ryd3x3}',
                   lhablock = 'YD',
                   lhacode = [ 3, 3 ])

Rye1x1 = Parameter(name = 'Rye1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.00002882278,
                   texname = '\\text{Rye1x1}',
                   lhablock = 'YE',
                   lhacode = [ 1, 1 ])

Rye2x2 = Parameter(name = 'Rye2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.005959638,
                   texname = '\\text{Rye2x2}',
                   lhablock = 'YE',
                   lhacode = [ 2, 2 ])

Rye3x3 = Parameter(name = 'Rye3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1002358,
                   texname = '\\text{Rye3x3}',
                   lhablock = 'YE',
                   lhacode = [ 3, 3 ])

Ryu1x1 = Parameter(name = 'Ryu1x1',
                   nature = 'external',
                   type = 'real',
                   value = 8.789391e-6,
                   texname = '\\text{Ryu1x1}',
                   lhablock = 'YU',
                   lhacode = [ 1, 1 ])

Ryu2x2 = Parameter(name = 'Ryu2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.003515756,
                   texname = '\\text{Ryu2x2}',
                   lhablock = 'YU',
                   lhacode = [ 2, 2 ])

Ryu3x3 = Parameter(name = 'Ryu3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.8829349,
                   texname = '\\text{Ryu3x3}',
                   lhablock = 'YU',
                   lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 79.829013114276,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mneu1 = Parameter(name = 'Mneu1',
                  nature = 'external',
                  type = 'real',
                  value = 99.48601,
                  texname = '\\text{Mneu1}',
                  lhablock = 'MASS',
                  lhacode = [ 1000022 ])

Mneu2 = Parameter(name = 'Mneu2',
                  nature = 'external',
                  type = 'real',
                  value = 189.5047,
                  texname = '\\text{Mneu2}',
                  lhablock = 'MASS',
                  lhacode = [ 1000023 ])

Mneu3 = Parameter(name = 'Mneu3',
                  nature = 'external',
                  type = 'real',
                  value = -469.5446,
                  texname = '\\text{Mneu3}',
                  lhablock = 'MASS',
                  lhacode = [ 1000025 ])

Mneu4 = Parameter(name = 'Mneu4',
                  nature = 'external',
                  type = 'real',
                  value = 477.3438,
                  texname = '\\text{Mneu4}',
                  lhablock = 'MASS',
                  lhacode = [ 1000035 ])

Mch1 = Parameter(name = 'Mch1',
                 nature = 'external',
                 type = 'real',
                 value = 189.468,
                 texname = '\\text{Mch1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000024 ])

Mch2 = Parameter(name = 'Mch2',
                 nature = 'external',
                 type = 'real',
                 value = 480.5668,
                 texname = '\\text{Mch2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000037 ])

Mgo = Parameter(name = 'Mgo',
                nature = 'external',
                type = 'real',
                value = 616.1578,
                texname = '\\text{Mgo}',
                lhablock = 'MASS',
                lhacode = [ 1000021 ])

MH01 = Parameter(name = 'MH01',
                 nature = 'external',
                 type = 'real',
                 value = 113.9668,
                 texname = '\\text{MH01}',
                 lhablock = 'MASS',
                 lhacode = [ 25 ])

MH02 = Parameter(name = 'MH02',
                 nature = 'external',
                 type = 'real',
                 value = 564.3097,
                 texname = '\\text{MH02}',
                 lhablock = 'MASS',
                 lhacode = [ 35 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 564.6897,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 570.4586,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 37 ])

Mta = Parameter(name = 'Mta',
                nature = 'external',
                type = 'real',
                value = 1.77699,
                texname = '\\text{Mta}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.1,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.83238808,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Msn1 = Parameter(name = 'Msn1',
                 nature = 'external',
                 type = 'real',
                 value = 333.6805,
                 texname = '\\text{Msn1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000012 ])

Msn2 = Parameter(name = 'Msn2',
                 nature = 'external',
                 type = 'real',
                 value = 337.0975,
                 texname = '\\text{Msn2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000014 ])

Msn3 = Parameter(name = 'Msn3',
                 nature = 'external',
                 type = 'real',
                 value = 337.1096,
                 texname = '\\text{Msn3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000016 ])

Msl1 = Parameter(name = 'Msl1',
                 nature = 'external',
                 type = 'real',
                 value = 303.753,
                 texname = '\\text{Msl1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000011 ])

Msl2 = Parameter(name = 'Msl2',
                 nature = 'external',
                 type = 'real',
                 value = 316.8669,
                 texname = '\\text{Msl2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000013 ])

Msl3 = Parameter(name = 'Msl3',
                 nature = 'external',
                 type = 'real',
                 value = 316.9185,
                 texname = '\\text{Msl3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000015 ])

Msl4 = Parameter(name = 'Msl4',
                 nature = 'external',
                 type = 'real',
                 value = 346.4667,
                 texname = '\\text{Msl4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000011 ])

Msl5 = Parameter(name = 'Msl5',
                 nature = 'external',
                 type = 'real',
                 value = 346.478,
                 texname = '\\text{Msl5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000013 ])

Msl6 = Parameter(name = 'Msl6',
                 nature = 'external',
                 type = 'real',
                 value = 348.1667,
                 texname = '\\text{Msl6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000015 ])

Msu1 = Parameter(name = 'Msu1',
                 nature = 'external',
                 type = 'real',
                 value = 348.2026,
                 texname = '\\text{Msu1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000002 ])

Msu2 = Parameter(name = 'Msu2',
                 nature = 'external',
                 type = 'real',
                 value = 613.3992,
                 texname = '\\text{Msu2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000004 ])

Msu3 = Parameter(name = 'Msu3',
                 nature = 'external',
                 type = 'real',
                 value = 615.7041,
                 texname = '\\text{Msu3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000006 ])

Msu4 = Parameter(name = 'Msu4',
                 nature = 'external',
                 type = 'real',
                 value = 615.7276,
                 texname = '\\text{Msu4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000002 ])

Msu5 = Parameter(name = 'Msu5',
                 nature = 'external',
                 type = 'real',
                 value = 630.2198,
                 texname = '\\text{Msu5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000004 ])

Msu6 = Parameter(name = 'Msu6',
                 nature = 'external',
                 type = 'real',
                 value = 630.2357,
                 texname = '\\text{Msu6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000006 ])

Msd1 = Parameter(name = 'Msd1',
                 nature = 'external',
                 type = 'real',
                 value = 537.874,
                 texname = '\\text{Msd1}',
                 lhablock = 'MASS',
                 lhacode = [ 1000001 ])

Msd2 = Parameter(name = 'Msd2',
                 nature = 'external',
                 type = 'real',
                 value = 610.5113,
                 texname = '\\text{Msd2}',
                 lhablock = 'MASS',
                 lhacode = [ 1000003 ])

Msd3 = Parameter(name = 'Msd3',
                 nature = 'external',
                 type = 'real',
                 value = 615.5144,
                 texname = '\\text{Msd3}',
                 lhablock = 'MASS',
                 lhacode = [ 1000005 ])

Msd4 = Parameter(name = 'Msd4',
                 nature = 'external',
                 type = 'real',
                 value = 615.5223,
                 texname = '\\text{Msd4}',
                 lhablock = 'MASS',
                 lhacode = [ 2000001 ])

Msd5 = Parameter(name = 'Msd5',
                 nature = 'external',
                 type = 'real',
                 value = 634.9333,
                 texname = '\\text{Msd5}',
                 lhablock = 'MASS',
                 lhacode = [ 2000003 ])

Msd6 = Parameter(name = 'Msd6',
                 nature = 'external',
                 type = 'real',
                 value = 634.9335,
                 texname = '\\text{Msd6}',
                 lhablock = 'MASS',
                 lhacode = [ 2000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.141,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

Wneu2 = Parameter(name = 'Wneu2',
                  nature = 'external',
                  type = 'real',
                  value = 0.00004107365,
                  texname = '\\text{Wneu2}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000023 ])

Wneu3 = Parameter(name = 'Wneu3',
                  nature = 'external',
                  type = 'real',
                  value = 3.091347,
                  texname = '\\text{Wneu3}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000025 ])

Wneu4 = Parameter(name = 'Wneu4',
                  nature = 'external',
                  type = 'real',
                  value = 3.193022,
                  texname = '\\text{Wneu4}',
                  lhablock = 'DECAY',
                  lhacode = [ 1000035 ])

Wch1 = Parameter(name = 'Wch1',
                 nature = 'external',
                 type = 'real',
                 value = 0.00105656,
                 texname = '\\text{Wch1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000024 ])

Wch2 = Parameter(name = 'Wch2',
                 nature = 'external',
                 type = 'real',
                 value = 5.260644,
                 texname = '\\text{Wch2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000037 ])

Wgo = Parameter(name = 'Wgo',
                nature = 'external',
                type = 'real',
                value = 2.524968,
                texname = '\\text{Wgo}',
                lhablock = 'DECAY',
                lhacode = [ 1000021 ])

WH01 = Parameter(name = 'WH01',
                 nature = 'external',
                 type = 'real',
                 value = 0.003518961,
                 texname = '\\text{WH01}',
                 lhablock = 'DECAY',
                 lhacode = [ 25 ])

WH02 = Parameter(name = 'WH02',
                 nature = 'external',
                 type = 'real',
                 value = 1.389974,
                 texname = '\\text{WH02}',
                 lhablock = 'DECAY',
                 lhacode = [ 35 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 1.742413,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 1.176094,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 37 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.463305,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wsn1 = Parameter(name = 'Wsn1',
                 nature = 'external',
                 type = 'real',
                 value = 2.205383,
                 texname = '\\text{Wsn1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000012 ])

Wsn2 = Parameter(name = 'Wsn2',
                 nature = 'external',
                 type = 'real',
                 value = 2.263504,
                 texname = '\\text{Wsn2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000014 ])

Wsn3 = Parameter(name = 'Wsn3',
                 nature = 'external',
                 type = 'real',
                 value = 2.263504,
                 texname = '\\text{Wsn3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000016 ])

Wsl1 = Parameter(name = 'Wsl1',
                 nature = 'external',
                 type = 'real',
                 value = 1.333692,
                 texname = '\\text{Wsl1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000011 ])

Wsl2 = Parameter(name = 'Wsl2',
                 nature = 'external',
                 type = 'real',
                 value = 1.315543,
                 texname = '\\text{Wsl2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000013 ])

Wsl3 = Parameter(name = 'Wsl3',
                 nature = 'external',
                 type = 'real',
                 value = 1.315543,
                 texname = '\\text{Wsl3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000015 ])

Wsl4 = Parameter(name = 'Wsl4',
                 nature = 'external',
                 type = 'real',
                 value = 2.332189,
                 texname = '\\text{Wsl4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000011 ])

Wsl5 = Parameter(name = 'Wsl5',
                 nature = 'external',
                 type = 'real',
                 value = 2.332189,
                 texname = '\\text{Wsl5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000013 ])

Wsl6 = Parameter(name = 'Wsl6',
                 nature = 'external',
                 type = 'real',
                 value = 2.187202,
                 texname = '\\text{Wsl6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000015 ])

Wsu1 = Parameter(name = 'Wsu1',
                 nature = 'external',
                 type = 'real',
                 value = 1.34786,
                 texname = '\\text{Wsu1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000002 ])

Wsu2 = Parameter(name = 'Wsu2',
                 nature = 'external',
                 type = 'real',
                 value = 8.6374,
                 texname = '\\text{Wsu2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000004 ])

Wsu3 = Parameter(name = 'Wsu3',
                 nature = 'external',
                 type = 'real',
                 value = 1.28374,
                 texname = '\\text{Wsu3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000006 ])

Wsu4 = Parameter(name = 'Wsu4',
                 nature = 'external',
                 type = 'real',
                 value = 1.28374,
                 texname = '\\text{Wsu4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000002 ])

Wsu5 = Parameter(name = 'Wsu5',
                 nature = 'external',
                 type = 'real',
                 value = 6.37685,
                 texname = '\\text{Wsu5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000004 ])

Wsu6 = Parameter(name = 'Wsu6',
                 nature = 'external',
                 type = 'real',
                 value = 6.37685,
                 texname = '\\text{Wsu6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000006 ])

Wsd1 = Parameter(name = 'Wsd1',
                 nature = 'external',
                 type = 'real',
                 value = 7.06064,
                 texname = '\\text{Wsd1}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000001 ])

Wsd2 = Parameter(name = 'Wsd2',
                 nature = 'external',
                 type = 'real',
                 value = 0.604363,
                 texname = '\\text{Wsd2}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000003 ])

Wsd3 = Parameter(name = 'Wsd3',
                 nature = 'external',
                 type = 'real',
                 value = 0.320863,
                 texname = '\\text{Wsd3}',
                 lhablock = 'DECAY',
                 lhacode = [ 1000005 ])

Wsd4 = Parameter(name = 'Wsd4',
                 nature = 'external',
                 type = 'real',
                 value = 0.320863,
                 texname = '\\text{Wsd4}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000001 ])

Wsd5 = Parameter(name = 'Wsd5',
                 nature = 'external',
                 type = 'real',
                 value = 6.30448,
                 texname = '\\text{Wsd5}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000003 ])

Wsd6 = Parameter(name = 'Wsd6',
                 nature = 'external',
                 type = 'real',
                 value = 6.30448,
                 texname = '\\text{Wsd6}',
                 lhablock = 'DECAY',
                 lhacode = [ 2000005 ])

beta = Parameter(name = 'beta',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.atan(tb)',
                 texname = '\\beta')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'MW/MZ',
               texname = 'c_w')

mD21x1 = Parameter(name = 'mD21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD21x1',
                   texname = '\\text{mD21x1}')

mD22x2 = Parameter(name = 'mD22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD22x2',
                   texname = '\\text{mD22x2}')

mD23x3 = Parameter(name = 'mD23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmD23x3',
                   texname = '\\text{mD23x3}')

mE21x1 = Parameter(name = 'mE21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE21x1',
                   texname = '\\text{mE21x1}')

mE22x2 = Parameter(name = 'mE22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE22x2',
                   texname = '\\text{mE22x2}')

mE23x3 = Parameter(name = 'mE23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmE23x3',
                   texname = '\\text{mE23x3}')

mL21x1 = Parameter(name = 'mL21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL21x1',
                   texname = '\\text{mL21x1}')

mL22x2 = Parameter(name = 'mL22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL22x2',
                   texname = '\\text{mL22x2}')

mL23x3 = Parameter(name = 'mL23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmL23x3',
                   texname = '\\text{mL23x3}')

mQ21x1 = Parameter(name = 'mQ21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ21x1',
                   texname = '\\text{mQ21x1}')

mQ22x2 = Parameter(name = 'mQ22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ22x2',
                   texname = '\\text{mQ22x2}')

mQ23x3 = Parameter(name = 'mQ23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmQ23x3',
                   texname = '\\text{mQ23x3}')

mU21x1 = Parameter(name = 'mU21x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU21x1',
                   texname = '\\text{mU21x1}')

mU22x2 = Parameter(name = 'mU22x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU22x2',
                   texname = '\\text{mU22x2}')

mU23x3 = Parameter(name = 'mU23x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'RmU23x3',
                   texname = '\\text{mU23x3}')

MUH = Parameter(name = 'MUH',
                nature = 'internal',
                type = 'complex',
                value = 'RMUH',
                texname = '\\mu')

Mx1 = Parameter(name = 'Mx1',
                nature = 'internal',
                type = 'complex',
                value = 'RMx1',
                texname = 'M_1')

Mx2 = Parameter(name = 'Mx2',
                nature = 'internal',
                type = 'complex',
                value = 'RMx2',
                texname = 'M_2')

Mx3 = Parameter(name = 'Mx3',
                nature = 'internal',
                type = 'complex',
                value = 'RMx3',
                texname = 'M_3')

NN1x1 = Parameter(name = 'NN1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x1',
                  texname = '\\text{NN1x1}')

NN1x2 = Parameter(name = 'NN1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x2',
                  texname = '\\text{NN1x2}')

NN1x3 = Parameter(name = 'NN1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x3',
                  texname = '\\text{NN1x3}')

NN1x4 = Parameter(name = 'NN1x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN1x4',
                  texname = '\\text{NN1x4}')

NN2x1 = Parameter(name = 'NN2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x1',
                  texname = '\\text{NN2x1}')

NN2x2 = Parameter(name = 'NN2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x2',
                  texname = '\\text{NN2x2}')

NN2x3 = Parameter(name = 'NN2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x3',
                  texname = '\\text{NN2x3}')

NN2x4 = Parameter(name = 'NN2x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN2x4',
                  texname = '\\text{NN2x4}')

NN3x1 = Parameter(name = 'NN3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x1',
                  texname = '\\text{NN3x1}')

NN3x2 = Parameter(name = 'NN3x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x2',
                  texname = '\\text{NN3x2}')

NN3x3 = Parameter(name = 'NN3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x3',
                  texname = '\\text{NN3x3}')

NN3x4 = Parameter(name = 'NN3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN3x4',
                  texname = '\\text{NN3x4}')

NN4x1 = Parameter(name = 'NN4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x1',
                  texname = '\\text{NN4x1}')

NN4x2 = Parameter(name = 'NN4x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x2',
                  texname = '\\text{NN4x2}')

NN4x3 = Parameter(name = 'NN4x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x3',
                  texname = '\\text{NN4x3}')

NN4x4 = Parameter(name = 'NN4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RNN4x4',
                  texname = '\\text{NN4x4}')

Rd1x3 = Parameter(name = 'Rd1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd1x3',
                  texname = '\\text{Rd1x3}')

Rd1x6 = Parameter(name = 'Rd1x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd1x6',
                  texname = '\\text{Rd1x6}')

Rd2x3 = Parameter(name = 'Rd2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd2x3',
                  texname = '\\text{Rd2x3}')

Rd2x6 = Parameter(name = 'Rd2x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd2x6',
                  texname = '\\text{Rd2x6}')

Rd3x5 = Parameter(name = 'Rd3x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd3x5',
                  texname = '\\text{Rd3x5}')

Rd4x4 = Parameter(name = 'Rd4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd4x4',
                  texname = '\\text{Rd4x4}')

Rd5x2 = Parameter(name = 'Rd5x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd5x2',
                  texname = '\\text{Rd5x2}')

Rd6x1 = Parameter(name = 'Rd6x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRd6x1',
                  texname = '\\text{Rd6x1}')

Rl1x3 = Parameter(name = 'Rl1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl1x3',
                  texname = '\\text{Rl1x3}')

Rl1x6 = Parameter(name = 'Rl1x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl1x6',
                  texname = '\\text{Rl1x6}')

Rl2x5 = Parameter(name = 'Rl2x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl2x5',
                  texname = '\\text{Rl2x5}')

Rl3x4 = Parameter(name = 'Rl3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl3x4',
                  texname = '\\text{Rl3x4}')

Rl4x1 = Parameter(name = 'Rl4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl4x1',
                  texname = '\\text{Rl4x1}')

Rl5x2 = Parameter(name = 'Rl5x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl5x2',
                  texname = '\\text{Rl5x2}')

Rl6x3 = Parameter(name = 'Rl6x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x3',
                  texname = '\\text{Rl6x3}')

Rl6x6 = Parameter(name = 'Rl6x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRl6x6',
                  texname = '\\text{Rl6x6}')

Rn1x3 = Parameter(name = 'Rn1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn1x3',
                  texname = '\\text{Rn1x3}')

Rn2x2 = Parameter(name = 'Rn2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn2x2',
                  texname = '\\text{Rn2x2}')

Rn3x1 = Parameter(name = 'Rn3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRn3x1',
                  texname = '\\text{Rn3x1}')

Ru1x3 = Parameter(name = 'Ru1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu1x3',
                  texname = '\\text{Ru1x3}')

Ru1x6 = Parameter(name = 'Ru1x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu1x6',
                  texname = '\\text{Ru1x6}')

Ru2x3 = Parameter(name = 'Ru2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu2x3',
                  texname = '\\text{Ru2x3}')

Ru2x6 = Parameter(name = 'Ru2x6',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu2x6',
                  texname = '\\text{Ru2x6}')

Ru3x5 = Parameter(name = 'Ru3x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu3x5',
                  texname = '\\text{Ru3x5}')

Ru4x4 = Parameter(name = 'Ru4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu4x4',
                  texname = '\\text{Ru4x4}')

Ru5x1 = Parameter(name = 'Ru5x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu5x1',
                  texname = '\\text{Ru5x1}')

Ru6x2 = Parameter(name = 'Ru6x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RRu6x2',
                  texname = '\\text{Ru6x2}')

UU1x1 = Parameter(name = 'UU1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x1',
                  texname = '\\text{UU1x1}')

UU1x2 = Parameter(name = 'UU1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU1x2',
                  texname = '\\text{UU1x2}')

UU2x1 = Parameter(name = 'UU2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x1',
                  texname = '\\text{UU2x1}')

UU2x2 = Parameter(name = 'UU2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RUU2x2',
                  texname = '\\text{UU2x2}')

VV1x1 = Parameter(name = 'VV1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x1',
                  texname = '\\text{VV1x1}')

VV1x2 = Parameter(name = 'VV1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV1x2',
                  texname = '\\text{VV1x2}')

VV2x1 = Parameter(name = 'VV2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x1',
                  texname = '\\text{VV2x1}')

VV2x2 = Parameter(name = 'VV2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RVV2x2',
                  texname = '\\text{VV2x2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)',
               texname = 'e')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

LLLE1x2x1 = Parameter(name = 'LLLE1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x2x1',
                      texname = '\\text{LLLE1x2x1}')

LLLE1x2x2 = Parameter(name = 'LLLE1x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x2x2',
                      texname = '\\text{LLLE1x2x2}')

LLLE1x2x3 = Parameter(name = 'LLLE1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x2x3',
                      texname = '\\text{LLLE1x2x3}')

LLLE1x3x1 = Parameter(name = 'LLLE1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x3x1',
                      texname = '\\text{LLLE1x3x1}')

LLLE1x3x2 = Parameter(name = 'LLLE1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x3x2',
                      texname = '\\text{LLLE1x3x2}')

LLLE1x3x3 = Parameter(name = 'LLLE1x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE1x3x3',
                      texname = '\\text{LLLE1x3x3}')

LLLE2x1x1 = Parameter(name = 'LLLE2x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x1x1',
                      texname = '\\text{LLLE2x1x1}')

LLLE2x1x2 = Parameter(name = 'LLLE2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x1x2',
                      texname = '\\text{LLLE2x1x2}')

LLLE2x1x3 = Parameter(name = 'LLLE2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x1x3',
                      texname = '\\text{LLLE2x1x3}')

LLLE2x3x1 = Parameter(name = 'LLLE2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x3x1',
                      texname = '\\text{LLLE2x3x1}')

LLLE2x3x2 = Parameter(name = 'LLLE2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x3x2',
                      texname = '\\text{LLLE2x3x2}')

LLLE2x3x3 = Parameter(name = 'LLLE2x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE2x3x3',
                      texname = '\\text{LLLE2x3x3}')

LLLE3x1x1 = Parameter(name = 'LLLE3x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x1x1',
                      texname = '\\text{LLLE3x1x1}')

LLLE3x1x2 = Parameter(name = 'LLLE3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x1x2',
                      texname = '\\text{LLLE3x1x2}')

LLLE3x1x3 = Parameter(name = 'LLLE3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x1x3',
                      texname = '\\text{LLLE3x1x3}')

LLLE3x2x1 = Parameter(name = 'LLLE3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x2x1',
                      texname = '\\text{LLLE3x2x1}')

LLLE3x2x2 = Parameter(name = 'LLLE3x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x2x2',
                      texname = '\\text{LLLE3x2x2}')

LLLE3x2x3 = Parameter(name = 'LLLE3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLLE3x2x3',
                      texname = '\\text{LLLE3x2x3}')

LLQD1x1x1 = Parameter(name = 'LLQD1x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x1x1',
                      texname = '\\text{LLQD1x1x1}')

LLQD1x1x2 = Parameter(name = 'LLQD1x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x1x2',
                      texname = '\\text{LLQD1x1x2}')

LLQD1x1x3 = Parameter(name = 'LLQD1x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x1x3',
                      texname = '\\text{LLQD1x1x3}')

LLQD1x2x1 = Parameter(name = 'LLQD1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x2x1',
                      texname = '\\text{LLQD1x2x1}')

LLQD1x2x2 = Parameter(name = 'LLQD1x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x2x2',
                      texname = '\\text{LLQD1x2x2}')

LLQD1x2x3 = Parameter(name = 'LLQD1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x2x3',
                      texname = '\\text{LLQD1x2x3}')

LLQD1x3x1 = Parameter(name = 'LLQD1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x3x1',
                      texname = '\\text{LLQD1x3x1}')

LLQD1x3x2 = Parameter(name = 'LLQD1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x3x2',
                      texname = '\\text{LLQD1x3x2}')

LLQD1x3x3 = Parameter(name = 'LLQD1x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD1x3x3',
                      texname = '\\text{LLQD1x3x3}')

LLQD2x1x1 = Parameter(name = 'LLQD2x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x1x1',
                      texname = '\\text{LLQD2x1x1}')

LLQD2x1x2 = Parameter(name = 'LLQD2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x1x2',
                      texname = '\\text{LLQD2x1x2}')

LLQD2x1x3 = Parameter(name = 'LLQD2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x1x3',
                      texname = '\\text{LLQD2x1x3}')

LLQD2x2x1 = Parameter(name = 'LLQD2x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x2x1',
                      texname = '\\text{LLQD2x2x1}')

LLQD2x2x2 = Parameter(name = 'LLQD2x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x2x2',
                      texname = '\\text{LLQD2x2x2}')

LLQD2x2x3 = Parameter(name = 'LLQD2x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x2x3',
                      texname = '\\text{LLQD2x2x3}')

LLQD2x3x1 = Parameter(name = 'LLQD2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x3x1',
                      texname = '\\text{LLQD2x3x1}')

LLQD2x3x2 = Parameter(name = 'LLQD2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x3x2',
                      texname = '\\text{LLQD2x3x2}')

LLQD2x3x3 = Parameter(name = 'LLQD2x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD2x3x3',
                      texname = '\\text{LLQD2x3x3}')

LLQD3x1x1 = Parameter(name = 'LLQD3x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x1x1',
                      texname = '\\text{LLQD3x1x1}')

LLQD3x1x2 = Parameter(name = 'LLQD3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x1x2',
                      texname = '\\text{LLQD3x1x2}')

LLQD3x1x3 = Parameter(name = 'LLQD3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x1x3',
                      texname = '\\text{LLQD3x1x3}')

LLQD3x2x1 = Parameter(name = 'LLQD3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x2x1',
                      texname = '\\text{LLQD3x2x1}')

LLQD3x2x2 = Parameter(name = 'LLQD3x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x2x2',
                      texname = '\\text{LLQD3x2x2}')

LLQD3x2x3 = Parameter(name = 'LLQD3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x2x3',
                      texname = '\\text{LLQD3x2x3}')

LLQD3x3x1 = Parameter(name = 'LLQD3x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x3x1',
                      texname = '\\text{LLQD3x3x1}')

LLQD3x3x2 = Parameter(name = 'LLQD3x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x3x2',
                      texname = '\\text{LLQD3x3x2}')

LLQD3x3x3 = Parameter(name = 'LLQD3x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLQD3x3x3',
                      texname = '\\text{LLQD3x3x3}')

LUDD1x1x2 = Parameter(name = 'LUDD1x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x1x2',
                      texname = '\\text{LUDD1x1x2}')

LUDD1x1x3 = Parameter(name = 'LUDD1x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x1x3',
                      texname = '\\text{LUDD1x1x3}')

LUDD1x2x1 = Parameter(name = 'LUDD1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x2x1',
                      texname = '\\text{LUDD1x2x1}')

LUDD1x2x3 = Parameter(name = 'LUDD1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x2x3',
                      texname = '\\text{LUDD1x2x3}')

LUDD1x3x1 = Parameter(name = 'LUDD1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x3x1',
                      texname = '\\text{LUDD1x3x1}')

LUDD1x3x2 = Parameter(name = 'LUDD1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD1x3x2',
                      texname = '\\text{LUDD1x3x2}')

LUDD2x1x2 = Parameter(name = 'LUDD2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x1x2',
                      texname = '\\text{LUDD2x1x2}')

LUDD2x1x3 = Parameter(name = 'LUDD2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x1x3',
                      texname = '\\text{LUDD2x1x3}')

LUDD2x2x1 = Parameter(name = 'LUDD2x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x2x1',
                      texname = '\\text{LUDD2x2x1}')

LUDD2x2x3 = Parameter(name = 'LUDD2x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x2x3',
                      texname = '\\text{LUDD2x2x3}')

LUDD2x3x1 = Parameter(name = 'LUDD2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x3x1',
                      texname = '\\text{LUDD2x3x1}')

LUDD2x3x2 = Parameter(name = 'LUDD2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD2x3x2',
                      texname = '\\text{LUDD2x3x2}')

LUDD3x1x2 = Parameter(name = 'LUDD3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x1x2',
                      texname = '\\text{LUDD3x1x2}')

LUDD3x1x3 = Parameter(name = 'LUDD3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x1x3',
                      texname = '\\text{LUDD3x1x3}')

LUDD3x2x1 = Parameter(name = 'LUDD3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x2x1',
                      texname = '\\text{LUDD3x2x1}')

LUDD3x2x3 = Parameter(name = 'LUDD3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x2x3',
                      texname = '\\text{LUDD3x2x3}')

LUDD3x3x1 = Parameter(name = 'LUDD3x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x3x1',
                      texname = '\\text{LUDD3x3x1}')

LUDD3x3x2 = Parameter(name = 'LUDD3x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RLDD3x3x2',
                      texname = '\\text{LUDD3x3x2}')

td1x1 = Parameter(name = 'td1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtd1x1',
                  texname = '\\text{td1x1}')

td2x2 = Parameter(name = 'td2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtd2x2',
                  texname = '\\text{td2x2}')

td3x3 = Parameter(name = 'td3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtd3x3',
                  texname = '\\text{td3x3}')

te1x1 = Parameter(name = 'te1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rte1x1',
                  texname = '\\text{te1x1}')

te2x2 = Parameter(name = 'te2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rte2x2',
                  texname = '\\text{te2x2}')

te3x3 = Parameter(name = 'te3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rte3x3',
                  texname = '\\text{te3x3}')

TLLE1x2x1 = Parameter(name = 'TLLE1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x2x1',
                      texname = '\\text{TLLE1x2x1}')

TLLE1x2x2 = Parameter(name = 'TLLE1x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x2x2',
                      texname = '\\text{TLLE1x2x2}')

TLLE1x2x3 = Parameter(name = 'TLLE1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x2x3',
                      texname = '\\text{TLLE1x2x3}')

TLLE1x3x1 = Parameter(name = 'TLLE1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x3x1',
                      texname = '\\text{TLLE1x3x1}')

TLLE1x3x2 = Parameter(name = 'TLLE1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x3x2',
                      texname = '\\text{TLLE1x3x2}')

TLLE1x3x3 = Parameter(name = 'TLLE1x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE1x3x3',
                      texname = '\\text{TLLE1x3x3}')

TLLE2x1x1 = Parameter(name = 'TLLE2x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x1x1',
                      texname = '\\text{TLLE2x1x1}')

TLLE2x1x2 = Parameter(name = 'TLLE2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x1x2',
                      texname = '\\text{TLLE2x1x2}')

TLLE2x1x3 = Parameter(name = 'TLLE2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x1x3',
                      texname = '\\text{TLLE2x1x3}')

TLLE2x3x1 = Parameter(name = 'TLLE2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x3x1',
                      texname = '\\text{TLLE2x3x1}')

TLLE2x3x2 = Parameter(name = 'TLLE2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x3x2',
                      texname = '\\text{TLLE2x3x2}')

TLLE2x3x3 = Parameter(name = 'TLLE2x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE2x3x3',
                      texname = '\\text{TLLE2x3x3}')

TLLE3x1x1 = Parameter(name = 'TLLE3x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x1x1',
                      texname = '\\text{TLLE3x1x1}')

TLLE3x1x2 = Parameter(name = 'TLLE3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x1x2',
                      texname = '\\text{TLLE3x1x2}')

TLLE3x1x3 = Parameter(name = 'TLLE3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x1x3',
                      texname = '\\text{TLLE3x1x3}')

TLLE3x2x1 = Parameter(name = 'TLLE3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x2x1',
                      texname = '\\text{TLLE3x2x1}')

TLLE3x2x2 = Parameter(name = 'TLLE3x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x2x2',
                      texname = '\\text{TLLE3x2x2}')

TLLE3x2x3 = Parameter(name = 'TLLE3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTLE3x2x3',
                      texname = '\\text{TLLE3x2x3}')

TLQD1x1x1 = Parameter(name = 'TLQD1x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x1x1',
                      texname = '\\text{TLQD1x1x1}')

TLQD1x1x2 = Parameter(name = 'TLQD1x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x1x2',
                      texname = '\\text{TLQD1x1x2}')

TLQD1x1x3 = Parameter(name = 'TLQD1x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x1x3',
                      texname = '\\text{TLQD1x1x3}')

TLQD1x2x1 = Parameter(name = 'TLQD1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x2x1',
                      texname = '\\text{TLQD1x2x1}')

TLQD1x2x2 = Parameter(name = 'TLQD1x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x2x2',
                      texname = '\\text{TLQD1x2x2}')

TLQD1x2x3 = Parameter(name = 'TLQD1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x2x3',
                      texname = '\\text{TLQD1x2x3}')

TLQD1x3x1 = Parameter(name = 'TLQD1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x3x1',
                      texname = '\\text{TLQD1x3x1}')

TLQD1x3x2 = Parameter(name = 'TLQD1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x3x2',
                      texname = '\\text{TLQD1x3x2}')

TLQD1x3x3 = Parameter(name = 'TLQD1x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD1x3x3',
                      texname = '\\text{TLQD1x3x3}')

TLQD2x1x1 = Parameter(name = 'TLQD2x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x1x1',
                      texname = '\\text{TLQD2x1x1}')

TLQD2x1x2 = Parameter(name = 'TLQD2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x1x2',
                      texname = '\\text{TLQD2x1x2}')

TLQD2x1x3 = Parameter(name = 'TLQD2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x1x3',
                      texname = '\\text{TLQD2x1x3}')

TLQD2x2x1 = Parameter(name = 'TLQD2x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x2x1',
                      texname = '\\text{TLQD2x2x1}')

TLQD2x2x2 = Parameter(name = 'TLQD2x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x2x2',
                      texname = '\\text{TLQD2x2x2}')

TLQD2x2x3 = Parameter(name = 'TLQD2x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x2x3',
                      texname = '\\text{TLQD2x2x3}')

TLQD2x3x1 = Parameter(name = 'TLQD2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x3x1',
                      texname = '\\text{TLQD2x3x1}')

TLQD2x3x2 = Parameter(name = 'TLQD2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x3x2',
                      texname = '\\text{TLQD2x3x2}')

TLQD2x3x3 = Parameter(name = 'TLQD2x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD2x3x3',
                      texname = '\\text{TLQD2x3x3}')

TLQD3x1x1 = Parameter(name = 'TLQD3x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x1x1',
                      texname = '\\text{TLQD3x1x1}')

TLQD3x1x2 = Parameter(name = 'TLQD3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x1x2',
                      texname = '\\text{TLQD3x1x2}')

TLQD3x1x3 = Parameter(name = 'TLQD3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x1x3',
                      texname = '\\text{TLQD3x1x3}')

TLQD3x2x1 = Parameter(name = 'TLQD3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x2x1',
                      texname = '\\text{TLQD3x2x1}')

TLQD3x2x2 = Parameter(name = 'TLQD3x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x2x2',
                      texname = '\\text{TLQD3x2x2}')

TLQD3x2x3 = Parameter(name = 'TLQD3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x2x3',
                      texname = '\\text{TLQD3x2x3}')

TLQD3x3x1 = Parameter(name = 'TLQD3x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x3x1',
                      texname = '\\text{TLQD3x3x1}')

TLQD3x3x2 = Parameter(name = 'TLQD3x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x3x2',
                      texname = '\\text{TLQD3x3x2}')

TLQD3x3x3 = Parameter(name = 'TLQD3x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTQD3x3x3',
                      texname = '\\text{TLQD3x3x3}')

tu1x1 = Parameter(name = 'tu1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtu1x1',
                  texname = '\\text{tu1x1}')

tu2x2 = Parameter(name = 'tu2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtu2x2',
                  texname = '\\text{tu2x2}')

tu3x3 = Parameter(name = 'tu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rtu3x3',
                  texname = '\\text{tu3x3}')

TUDD1x1x2 = Parameter(name = 'TUDD1x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x1x2',
                      texname = '\\text{TUDD1x1x2}')

TUDD1x1x3 = Parameter(name = 'TUDD1x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x1x3',
                      texname = '\\text{TUDD1x1x3}')

TUDD1x2x1 = Parameter(name = 'TUDD1x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x2x1',
                      texname = '\\text{TUDD1x2x1}')

TUDD1x2x3 = Parameter(name = 'TUDD1x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x2x3',
                      texname = '\\text{TUDD1x2x3}')

TUDD1x3x1 = Parameter(name = 'TUDD1x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x3x1',
                      texname = '\\text{TUDD1x3x1}')

TUDD1x3x2 = Parameter(name = 'TUDD1x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD1x3x2',
                      texname = '\\text{TUDD1x3x2}')

TUDD2x1x2 = Parameter(name = 'TUDD2x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x1x2',
                      texname = '\\text{TUDD2x1x2}')

TUDD2x1x3 = Parameter(name = 'TUDD2x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x1x3',
                      texname = '\\text{TUDD2x1x3}')

TUDD2x2x1 = Parameter(name = 'TUDD2x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x2x1',
                      texname = '\\text{TUDD2x2x1}')

TUDD2x2x3 = Parameter(name = 'TUDD2x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x2x3',
                      texname = '\\text{TUDD2x2x3}')

TUDD2x3x1 = Parameter(name = 'TUDD2x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x3x1',
                      texname = '\\text{TUDD2x3x1}')

TUDD2x3x2 = Parameter(name = 'TUDD2x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD2x3x2',
                      texname = '\\text{TUDD2x3x2}')

TUDD3x1x2 = Parameter(name = 'TUDD3x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x1x2',
                      texname = '\\text{TUDD3x1x2}')

TUDD3x1x3 = Parameter(name = 'TUDD3x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x1x3',
                      texname = '\\text{TUDD3x1x3}')

TUDD3x2x1 = Parameter(name = 'TUDD3x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x2x1',
                      texname = '\\text{TUDD3x2x1}')

TUDD3x2x3 = Parameter(name = 'TUDD3x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x2x3',
                      texname = '\\text{TUDD3x2x3}')

TUDD3x3x1 = Parameter(name = 'TUDD3x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x3x1',
                      texname = '\\text{TUDD3x3x1}')

TUDD3x3x2 = Parameter(name = 'TUDD3x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'RTDD3x3x2',
                      texname = '\\text{TUDD3x3x2}')

yd1x1 = Parameter(name = 'yd1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryd1x1',
                  texname = '\\text{yd1x1}')

yd2x2 = Parameter(name = 'yd2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryd2x2',
                  texname = '\\text{yd2x2}')

yd3x3 = Parameter(name = 'yd3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryd3x3',
                  texname = '\\text{yd3x3}')

ye1x1 = Parameter(name = 'ye1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rye1x1',
                  texname = '\\text{ye1x1}')

ye2x2 = Parameter(name = 'ye2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rye2x2',
                  texname = '\\text{ye2x2}')

ye3x3 = Parameter(name = 'ye3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rye3x3',
                  texname = '\\text{ye3x3}')

yu1x1 = Parameter(name = 'yu1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryu1x1',
                  texname = '\\text{yu1x1}')

yu2x2 = Parameter(name = 'yu2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryu2x2',
                  texname = '\\text{yu2x2}')

yu3x3 = Parameter(name = 'yu3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Ryu3x3',
                  texname = '\\text{yu3x3}')

bb = Parameter(name = 'bb',
               nature = 'internal',
               type = 'complex',
               value = '((-mHd2 + mHu2 - MZ**2*cmath.cos(2*beta))*cmath.tan(2*beta))/2.',
               texname = 'b')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - cw**2)',
               texname = 's_w')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g\'')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*cw*MZ*sw)/ee',
                texname = 'v')

vd = Parameter(name = 'vd',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.cos(beta)',
               texname = 'v_d')

vu = Parameter(name = 'vu',
               nature = 'internal',
               type = 'real',
               value = 'vev*cmath.sin(beta)',
               texname = 'v_u')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(yu1x1)',
                  texname = '\\text{I1a11}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(yu2x2)',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(yu3x3)',
                  texname = '\\text{I1a33}')

I10a111 = Parameter(name = 'I10a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a111}')

I10a112 = Parameter(name = 'I10a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a112}')

I10a113 = Parameter(name = 'I10a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x1)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a113}')

I10a121 = Parameter(name = 'I10a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a121}')

I10a122 = Parameter(name = 'I10a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a122}')

I10a123 = Parameter(name = 'I10a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x1)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a123}')

I10a131 = Parameter(name = 'I10a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a131}')

I10a132 = Parameter(name = 'I10a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a132}')

I10a133 = Parameter(name = 'I10a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a133}')

I10a211 = Parameter(name = 'I10a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a211}')

I10a212 = Parameter(name = 'I10a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a212}')

I10a214 = Parameter(name = 'I10a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x2)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a214}')

I10a221 = Parameter(name = 'I10a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a221}')

I10a222 = Parameter(name = 'I10a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a222}')

I10a224 = Parameter(name = 'I10a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x2)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a224}')

I10a231 = Parameter(name = 'I10a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)',
                    texname = '\\text{I10a231}')

I10a232 = Parameter(name = 'I10a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)',
                    texname = '\\text{I10a232}')

I10a234 = Parameter(name = 'I10a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a234}')

I10a313 = Parameter(name = 'I10a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x3)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a313}')

I10a314 = Parameter(name = 'I10a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x3)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a314}')

I10a323 = Parameter(name = 'I10a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x3)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a323}')

I10a324 = Parameter(name = 'I10a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x3)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a324}')

I10a333 = Parameter(name = 'I10a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Rd3x5)',
                    texname = '\\text{I10a333}')

I10a334 = Parameter(name = 'I10a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Rd4x4)',
                    texname = '\\text{I10a334}')

I100a131 = Parameter(name = 'I100a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I100a131}')

I100a132 = Parameter(name = 'I100a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I100a132}')

I100a133 = Parameter(name = 'I100a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x2)',
                     texname = '\\text{I100a133}')

I100a134 = Parameter(name = 'I100a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x2)',
                     texname = '\\text{I100a134}')

I100a141 = Parameter(name = 'I100a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I100a141}')

I100a142 = Parameter(name = 'I100a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I100a142}')

I100a143 = Parameter(name = 'I100a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x1)',
                     texname = '\\text{I100a143}')

I100a144 = Parameter(name = 'I100a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x1)',
                     texname = '\\text{I100a144}')

I100a231 = Parameter(name = 'I100a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I100a231}')

I100a232 = Parameter(name = 'I100a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I100a232}')

I100a233 = Parameter(name = 'I100a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x2)',
                     texname = '\\text{I100a233}')

I100a234 = Parameter(name = 'I100a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x2)',
                     texname = '\\text{I100a234}')

I100a241 = Parameter(name = 'I100a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I100a241}')

I100a242 = Parameter(name = 'I100a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I100a242}')

I100a243 = Parameter(name = 'I100a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x1)',
                     texname = '\\text{I100a243}')

I100a244 = Parameter(name = 'I100a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x1)',
                     texname = '\\text{I100a244}')

I100a311 = Parameter(name = 'I100a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I100a311}')

I100a312 = Parameter(name = 'I100a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I100a312}')

I100a313 = Parameter(name = 'I100a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x3)',
                     texname = '\\text{I100a313}')

I100a314 = Parameter(name = 'I100a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x3)',
                     texname = '\\text{I100a314}')

I100a321 = Parameter(name = 'I100a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I100a321}')

I100a322 = Parameter(name = 'I100a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I100a322}')

I100a323 = Parameter(name = 'I100a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x3)',
                     texname = '\\text{I100a323}')

I100a324 = Parameter(name = 'I100a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x3)',
                     texname = '\\text{I100a324}')

I100a341 = Parameter(name = 'I100a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x1)',
                     texname = '\\text{I100a341}')

I100a342 = Parameter(name = 'I100a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x1)',
                     texname = '\\text{I100a342}')

I100a343 = Parameter(name = 'I100a343',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x1)',
                     texname = '\\text{I100a343}')

I100a344 = Parameter(name = 'I100a344',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x1)',
                     texname = '\\text{I100a344}')

I100a411 = Parameter(name = 'I100a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I100a411}')

I100a412 = Parameter(name = 'I100a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I100a412}')

I100a413 = Parameter(name = 'I100a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x3)',
                     texname = '\\text{I100a413}')

I100a414 = Parameter(name = 'I100a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x3)',
                     texname = '\\text{I100a414}')

I100a421 = Parameter(name = 'I100a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I100a421}')

I100a422 = Parameter(name = 'I100a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I100a422}')

I100a423 = Parameter(name = 'I100a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x3)',
                     texname = '\\text{I100a423}')

I100a424 = Parameter(name = 'I100a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x3)',
                     texname = '\\text{I100a424}')

I100a431 = Parameter(name = 'I100a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x2)',
                     texname = '\\text{I100a431}')

I100a432 = Parameter(name = 'I100a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x2)',
                     texname = '\\text{I100a432}')

I100a433 = Parameter(name = 'I100a433',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x2)',
                     texname = '\\text{I100a433}')

I100a434 = Parameter(name = 'I100a434',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x2)',
                     texname = '\\text{I100a434}')

I101a131 = Parameter(name = 'I101a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I101a131}')

I101a132 = Parameter(name = 'I101a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I101a132}')

I101a133 = Parameter(name = 'I101a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x3)',
                     texname = '\\text{I101a133}')

I101a134 = Parameter(name = 'I101a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x3)',
                     texname = '\\text{I101a134}')

I101a141 = Parameter(name = 'I101a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I101a141}')

I101a142 = Parameter(name = 'I101a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I101a142}')

I101a143 = Parameter(name = 'I101a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x3)',
                     texname = '\\text{I101a143}')

I101a144 = Parameter(name = 'I101a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x3)',
                     texname = '\\text{I101a144}')

I101a231 = Parameter(name = 'I101a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I101a231}')

I101a232 = Parameter(name = 'I101a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x3)',
                     texname = '\\text{I101a232}')

I101a233 = Parameter(name = 'I101a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x3)',
                     texname = '\\text{I101a233}')

I101a234 = Parameter(name = 'I101a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x3)',
                     texname = '\\text{I101a234}')

I101a241 = Parameter(name = 'I101a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I101a241}')

I101a242 = Parameter(name = 'I101a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x3)',
                     texname = '\\text{I101a242}')

I101a243 = Parameter(name = 'I101a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x3)',
                     texname = '\\text{I101a243}')

I101a244 = Parameter(name = 'I101a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x3)',
                     texname = '\\text{I101a244}')

I101a311 = Parameter(name = 'I101a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I101a311}')

I101a312 = Parameter(name = 'I101a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I101a312}')

I101a313 = Parameter(name = 'I101a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x2)',
                     texname = '\\text{I101a313}')

I101a314 = Parameter(name = 'I101a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x2)',
                     texname = '\\text{I101a314}')

I101a321 = Parameter(name = 'I101a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I101a321}')

I101a322 = Parameter(name = 'I101a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x2)',
                     texname = '\\text{I101a322}')

I101a323 = Parameter(name = 'I101a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x2)',
                     texname = '\\text{I101a323}')

I101a324 = Parameter(name = 'I101a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x2)',
                     texname = '\\text{I101a324}')

I101a341 = Parameter(name = 'I101a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x1x2)',
                     texname = '\\text{I101a341}')

I101a342 = Parameter(name = 'I101a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x1x2)',
                     texname = '\\text{I101a342}')

I101a343 = Parameter(name = 'I101a343',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x1x2)',
                     texname = '\\text{I101a343}')

I101a344 = Parameter(name = 'I101a344',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x1x2)',
                     texname = '\\text{I101a344}')

I101a411 = Parameter(name = 'I101a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I101a411}')

I101a412 = Parameter(name = 'I101a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I101a412}')

I101a413 = Parameter(name = 'I101a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x1)',
                     texname = '\\text{I101a413}')

I101a414 = Parameter(name = 'I101a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x1)',
                     texname = '\\text{I101a414}')

I101a421 = Parameter(name = 'I101a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I101a421}')

I101a422 = Parameter(name = 'I101a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x3x1)',
                     texname = '\\text{I101a422}')

I101a423 = Parameter(name = 'I101a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x3x1)',
                     texname = '\\text{I101a423}')

I101a424 = Parameter(name = 'I101a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x3x1)',
                     texname = '\\text{I101a424}')

I101a431 = Parameter(name = 'I101a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)*complexconjugate(TUDD3x2x1)',
                     texname = '\\text{I101a431}')

I101a432 = Parameter(name = 'I101a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)*complexconjugate(TUDD3x2x1)',
                     texname = '\\text{I101a432}')

I101a433 = Parameter(name = 'I101a433',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)*complexconjugate(TUDD2x2x1)',
                     texname = '\\text{I101a433}')

I101a434 = Parameter(name = 'I101a434',
                     nature = 'internal',
                     type = 'complex',
                     value = 'complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)*complexconjugate(TUDD1x2x1)',
                     texname = '\\text{I101a434}')

I102a151 = Parameter(name = 'I102a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a151}')

I102a152 = Parameter(name = 'I102a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a152}')

I102a153 = Parameter(name = 'I102a153',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a153}')

I102a154 = Parameter(name = 'I102a154',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a154}')

I102a161 = Parameter(name = 'I102a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a161}')

I102a162 = Parameter(name = 'I102a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a162}')

I102a163 = Parameter(name = 'I102a163',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a163}')

I102a164 = Parameter(name = 'I102a164',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a164}')

I102a251 = Parameter(name = 'I102a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a251}')

I102a252 = Parameter(name = 'I102a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a252}')

I102a253 = Parameter(name = 'I102a253',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a253}')

I102a254 = Parameter(name = 'I102a254',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a254}')

I102a261 = Parameter(name = 'I102a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a261}')

I102a262 = Parameter(name = 'I102a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a262}')

I102a263 = Parameter(name = 'I102a263',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a263}')

I102a264 = Parameter(name = 'I102a264',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a264}')

I102a311 = Parameter(name = 'I102a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a311}')

I102a312 = Parameter(name = 'I102a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a312}')

I102a313 = Parameter(name = 'I102a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a313}')

I102a314 = Parameter(name = 'I102a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a314}')

I102a321 = Parameter(name = 'I102a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a321}')

I102a322 = Parameter(name = 'I102a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a322}')

I102a323 = Parameter(name = 'I102a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a323}')

I102a324 = Parameter(name = 'I102a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a324}')

I102a361 = Parameter(name = 'I102a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a361}')

I102a362 = Parameter(name = 'I102a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a362}')

I102a363 = Parameter(name = 'I102a363',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a363}')

I102a364 = Parameter(name = 'I102a364',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a364}')

I102a411 = Parameter(name = 'I102a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a411}')

I102a412 = Parameter(name = 'I102a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a412}')

I102a413 = Parameter(name = 'I102a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a413}')

I102a414 = Parameter(name = 'I102a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a414}')

I102a421 = Parameter(name = 'I102a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a421}')

I102a422 = Parameter(name = 'I102a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a422}')

I102a423 = Parameter(name = 'I102a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a423}')

I102a424 = Parameter(name = 'I102a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a424}')

I102a451 = Parameter(name = 'I102a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I102a451}')

I102a452 = Parameter(name = 'I102a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I102a452}')

I102a453 = Parameter(name = 'I102a453',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I102a453}')

I102a454 = Parameter(name = 'I102a454',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I102a454}')

I103a131 = Parameter(name = 'I103a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a131}')

I103a132 = Parameter(name = 'I103a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a132}')

I103a133 = Parameter(name = 'I103a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a133}')

I103a134 = Parameter(name = 'I103a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a134}')

I103a141 = Parameter(name = 'I103a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a141}')

I103a142 = Parameter(name = 'I103a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a142}')

I103a143 = Parameter(name = 'I103a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a143}')

I103a144 = Parameter(name = 'I103a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a144}')

I103a231 = Parameter(name = 'I103a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a231}')

I103a232 = Parameter(name = 'I103a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a232}')

I103a233 = Parameter(name = 'I103a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a233}')

I103a234 = Parameter(name = 'I103a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a234}')

I103a241 = Parameter(name = 'I103a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a241}')

I103a242 = Parameter(name = 'I103a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a242}')

I103a243 = Parameter(name = 'I103a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a243}')

I103a244 = Parameter(name = 'I103a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a244}')

I103a511 = Parameter(name = 'I103a511',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a511}')

I103a512 = Parameter(name = 'I103a512',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a512}')

I103a513 = Parameter(name = 'I103a513',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a513}')

I103a514 = Parameter(name = 'I103a514',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a514}')

I103a521 = Parameter(name = 'I103a521',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a521}')

I103a522 = Parameter(name = 'I103a522',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a522}')

I103a523 = Parameter(name = 'I103a523',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a523}')

I103a524 = Parameter(name = 'I103a524',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a524}')

I103a541 = Parameter(name = 'I103a541',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a541}')

I103a542 = Parameter(name = 'I103a542',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a542}')

I103a543 = Parameter(name = 'I103a543',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a543}')

I103a544 = Parameter(name = 'I103a544',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x2x1)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a544}')

I103a611 = Parameter(name = 'I103a611',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a611}')

I103a612 = Parameter(name = 'I103a612',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a612}')

I103a613 = Parameter(name = 'I103a613',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a613}')

I103a614 = Parameter(name = 'I103a614',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a614}')

I103a621 = Parameter(name = 'I103a621',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a621}')

I103a622 = Parameter(name = 'I103a622',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a622}')

I103a623 = Parameter(name = 'I103a623',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a623}')

I103a624 = Parameter(name = 'I103a624',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a624}')

I103a631 = Parameter(name = 'I103a631',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I103a631}')

I103a632 = Parameter(name = 'I103a632',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I103a632}')

I103a633 = Parameter(name = 'I103a633',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I103a633}')

I103a634 = Parameter(name = 'I103a634',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I103a634}')

I104a151 = Parameter(name = 'I104a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a151}')

I104a152 = Parameter(name = 'I104a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a152}')

I104a153 = Parameter(name = 'I104a153',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a153}')

I104a154 = Parameter(name = 'I104a154',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a154}')

I104a161 = Parameter(name = 'I104a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a161}')

I104a162 = Parameter(name = 'I104a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a162}')

I104a163 = Parameter(name = 'I104a163',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a163}')

I104a164 = Parameter(name = 'I104a164',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a164}')

I104a251 = Parameter(name = 'I104a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a251}')

I104a252 = Parameter(name = 'I104a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a252}')

I104a253 = Parameter(name = 'I104a253',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a253}')

I104a254 = Parameter(name = 'I104a254',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a254}')

I104a261 = Parameter(name = 'I104a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a261}')

I104a262 = Parameter(name = 'I104a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a262}')

I104a263 = Parameter(name = 'I104a263',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a263}')

I104a264 = Parameter(name = 'I104a264',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a264}')

I104a311 = Parameter(name = 'I104a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a311}')

I104a312 = Parameter(name = 'I104a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a312}')

I104a313 = Parameter(name = 'I104a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a313}')

I104a314 = Parameter(name = 'I104a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a314}')

I104a321 = Parameter(name = 'I104a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a321}')

I104a322 = Parameter(name = 'I104a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a322}')

I104a323 = Parameter(name = 'I104a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a323}')

I104a324 = Parameter(name = 'I104a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a324}')

I104a361 = Parameter(name = 'I104a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a361}')

I104a362 = Parameter(name = 'I104a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a362}')

I104a363 = Parameter(name = 'I104a363',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a363}')

I104a364 = Parameter(name = 'I104a364',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a364}')

I104a411 = Parameter(name = 'I104a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a411}')

I104a412 = Parameter(name = 'I104a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a412}')

I104a413 = Parameter(name = 'I104a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a413}')

I104a414 = Parameter(name = 'I104a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a414}')

I104a421 = Parameter(name = 'I104a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a421}')

I104a422 = Parameter(name = 'I104a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a422}')

I104a423 = Parameter(name = 'I104a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a423}')

I104a424 = Parameter(name = 'I104a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a424}')

I104a451 = Parameter(name = 'I104a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I104a451}')

I104a452 = Parameter(name = 'I104a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I104a452}')

I104a453 = Parameter(name = 'I104a453',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I104a453}')

I104a454 = Parameter(name = 'I104a454',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I104a454}')

I105a131 = Parameter(name = 'I105a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a131}')

I105a132 = Parameter(name = 'I105a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a132}')

I105a133 = Parameter(name = 'I105a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a133}')

I105a134 = Parameter(name = 'I105a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a134}')

I105a141 = Parameter(name = 'I105a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a141}')

I105a142 = Parameter(name = 'I105a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a142}')

I105a143 = Parameter(name = 'I105a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a143}')

I105a144 = Parameter(name = 'I105a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a144}')

I105a231 = Parameter(name = 'I105a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a231}')

I105a232 = Parameter(name = 'I105a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a232}')

I105a233 = Parameter(name = 'I105a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a233}')

I105a234 = Parameter(name = 'I105a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x3)*complexconjugate(Rd3x5)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a234}')

I105a241 = Parameter(name = 'I105a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a241}')

I105a242 = Parameter(name = 'I105a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a242}')

I105a243 = Parameter(name = 'I105a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a243}')

I105a244 = Parameter(name = 'I105a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd3x3*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x3)*complexconjugate(Rd4x4)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a244}')

I105a511 = Parameter(name = 'I105a511',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a511}')

I105a512 = Parameter(name = 'I105a512',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a512}')

I105a513 = Parameter(name = 'I105a513',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a513}')

I105a514 = Parameter(name = 'I105a514',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a514}')

I105a521 = Parameter(name = 'I105a521',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a521}')

I105a522 = Parameter(name = 'I105a522',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a522}')

I105a523 = Parameter(name = 'I105a523',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a523}')

I105a524 = Parameter(name = 'I105a524',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a524}')

I105a541 = Parameter(name = 'I105a541',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a541}')

I105a542 = Parameter(name = 'I105a542',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD3x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a542}')

I105a543 = Parameter(name = 'I105a543',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD2x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a543}')

I105a544 = Parameter(name = 'I105a544',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd2x2*complexconjugate(LUDD1x1x2)*complexconjugate(Rd4x4)*complexconjugate(Rd5x2)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a544}')

I105a611 = Parameter(name = 'I105a611',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a611}')

I105a612 = Parameter(name = 'I105a612',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a612}')

I105a613 = Parameter(name = 'I105a613',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a613}')

I105a614 = Parameter(name = 'I105a614',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a614}')

I105a621 = Parameter(name = 'I105a621',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a621}')

I105a622 = Parameter(name = 'I105a622',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a622}')

I105a623 = Parameter(name = 'I105a623',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a623}')

I105a624 = Parameter(name = 'I105a624',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a624}')

I105a631 = Parameter(name = 'I105a631',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru1x6)',
                     texname = '\\text{I105a631}')

I105a632 = Parameter(name = 'I105a632',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru2x6)',
                     texname = '\\text{I105a632}')

I105a633 = Parameter(name = 'I105a633',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD2x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru3x5)',
                     texname = '\\text{I105a633}')

I105a634 = Parameter(name = 'I105a634',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yd1x1*complexconjugate(LUDD1x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd6x1)*complexconjugate(Ru4x4)',
                     texname = '\\text{I105a634}')

I106a131 = Parameter(name = 'I106a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a131}')

I106a132 = Parameter(name = 'I106a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a132}')

I106a135 = Parameter(name = 'I106a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a135}')

I106a136 = Parameter(name = 'I106a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a136}')

I106a141 = Parameter(name = 'I106a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a141}')

I106a142 = Parameter(name = 'I106a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a142}')

I106a145 = Parameter(name = 'I106a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a145}')

I106a146 = Parameter(name = 'I106a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a146}')

I106a231 = Parameter(name = 'I106a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a231}')

I106a232 = Parameter(name = 'I106a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a232}')

I106a235 = Parameter(name = 'I106a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a235}')

I106a236 = Parameter(name = 'I106a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a236}')

I106a241 = Parameter(name = 'I106a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a241}')

I106a242 = Parameter(name = 'I106a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a242}')

I106a245 = Parameter(name = 'I106a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a245}')

I106a246 = Parameter(name = 'I106a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a246}')

I106a311 = Parameter(name = 'I106a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a311}')

I106a312 = Parameter(name = 'I106a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a312}')

I106a315 = Parameter(name = 'I106a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a315}')

I106a316 = Parameter(name = 'I106a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a316}')

I106a321 = Parameter(name = 'I106a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a321}')

I106a322 = Parameter(name = 'I106a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a322}')

I106a325 = Parameter(name = 'I106a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a325}')

I106a326 = Parameter(name = 'I106a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a326}')

I106a341 = Parameter(name = 'I106a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a341}')

I106a342 = Parameter(name = 'I106a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a342}')

I106a345 = Parameter(name = 'I106a345',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a345}')

I106a346 = Parameter(name = 'I106a346',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a346}')

I106a411 = Parameter(name = 'I106a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a411}')

I106a412 = Parameter(name = 'I106a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a412}')

I106a415 = Parameter(name = 'I106a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a415}')

I106a416 = Parameter(name = 'I106a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a416}')

I106a421 = Parameter(name = 'I106a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a421}')

I106a422 = Parameter(name = 'I106a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a422}')

I106a425 = Parameter(name = 'I106a425',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a425}')

I106a426 = Parameter(name = 'I106a426',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a426}')

I106a431 = Parameter(name = 'I106a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I106a431}')

I106a432 = Parameter(name = 'I106a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I106a432}')

I106a435 = Parameter(name = 'I106a435',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I106a435}')

I106a436 = Parameter(name = 'I106a436',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I106a436}')

I107a131 = Parameter(name = 'I107a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a131}')

I107a132 = Parameter(name = 'I107a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a132}')

I107a135 = Parameter(name = 'I107a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a135}')

I107a136 = Parameter(name = 'I107a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a136}')

I107a141 = Parameter(name = 'I107a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a141}')

I107a142 = Parameter(name = 'I107a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a142}')

I107a145 = Parameter(name = 'I107a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a145}')

I107a146 = Parameter(name = 'I107a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x1)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a146}')

I107a231 = Parameter(name = 'I107a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a231}')

I107a232 = Parameter(name = 'I107a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a232}')

I107a235 = Parameter(name = 'I107a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a235}')

I107a236 = Parameter(name = 'I107a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x2)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a236}')

I107a241 = Parameter(name = 'I107a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a241}')

I107a242 = Parameter(name = 'I107a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a242}')

I107a245 = Parameter(name = 'I107a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a245}')

I107a246 = Parameter(name = 'I107a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x3x1)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a246}')

I107a311 = Parameter(name = 'I107a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a311}')

I107a312 = Parameter(name = 'I107a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a312}')

I107a315 = Parameter(name = 'I107a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a315}')

I107a316 = Parameter(name = 'I107a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a316}')

I107a321 = Parameter(name = 'I107a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a321}')

I107a322 = Parameter(name = 'I107a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a322}')

I107a325 = Parameter(name = 'I107a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a325}')

I107a326 = Parameter(name = 'I107a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x6)*complexconjugate(Rd3x5)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a326}')

I107a341 = Parameter(name = 'I107a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a341}')

I107a342 = Parameter(name = 'I107a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a342}')

I107a345 = Parameter(name = 'I107a345',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a345}')

I107a346 = Parameter(name = 'I107a346',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x2x1)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a346}')

I107a411 = Parameter(name = 'I107a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a411}')

I107a412 = Parameter(name = 'I107a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a412}')

I107a415 = Parameter(name = 'I107a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a415}')

I107a416 = Parameter(name = 'I107a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a416}')

I107a421 = Parameter(name = 'I107a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a421}')

I107a422 = Parameter(name = 'I107a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a422}')

I107a425 = Parameter(name = 'I107a425',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a425}')

I107a426 = Parameter(name = 'I107a426',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x6)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a426}')

I107a431 = Parameter(name = 'I107a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru1x3)',
                     texname = '\\text{I107a431}')

I107a432 = Parameter(name = 'I107a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu3x3*complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru2x3)',
                     texname = '\\text{I107a432}')

I107a435 = Parameter(name = 'I107a435',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu1x1*complexconjugate(LUDD1x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru5x1)',
                     texname = '\\text{I107a435}')

I107a436 = Parameter(name = 'I107a436',
                     nature = 'internal',
                     type = 'complex',
                     value = 'yu2x2*complexconjugate(LUDD2x1x2)*complexconjugate(Rd3x5)*complexconjugate(Rd4x4)*complexconjugate(Ru6x2)',
                     texname = '\\text{I107a436}')

I108a15 = Parameter(name = 'I108a15',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(yu1x1)',
                    texname = '\\text{I108a15}')

I108a26 = Parameter(name = 'I108a26',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(yu2x2)',
                    texname = '\\text{I108a26}')

I108a31 = Parameter(name = 'I108a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(yu3x3)',
                    texname = '\\text{I108a31}')

I108a32 = Parameter(name = 'I108a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(yu3x3)',
                    texname = '\\text{I108a32}')

I109a14 = Parameter(name = 'I109a14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1',
                    texname = '\\text{I109a14}')

I109a23 = Parameter(name = 'I109a23',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2',
                    texname = '\\text{I109a23}')

I109a31 = Parameter(name = 'I109a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3',
                    texname = '\\text{I109a31}')

I109a32 = Parameter(name = 'I109a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3',
                    texname = '\\text{I109a32}')

I11a111 = Parameter(name = 'I11a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a111}')

I11a112 = Parameter(name = 'I11a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a112}')

I11a113 = Parameter(name = 'I11a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a113}')

I11a121 = Parameter(name = 'I11a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a121}')

I11a122 = Parameter(name = 'I11a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a122}')

I11a123 = Parameter(name = 'I11a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a123}')

I11a131 = Parameter(name = 'I11a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a131}')

I11a132 = Parameter(name = 'I11a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a132}')

I11a133 = Parameter(name = 'I11a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a133}')

I11a211 = Parameter(name = 'I11a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a211}')

I11a212 = Parameter(name = 'I11a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a212}')

I11a214 = Parameter(name = 'I11a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a214}')

I11a221 = Parameter(name = 'I11a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a221}')

I11a222 = Parameter(name = 'I11a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a222}')

I11a224 = Parameter(name = 'I11a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a224}')

I11a231 = Parameter(name = 'I11a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I11a231}')

I11a232 = Parameter(name = 'I11a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I11a232}')

I11a234 = Parameter(name = 'I11a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a234}')

I11a313 = Parameter(name = 'I11a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a313}')

I11a314 = Parameter(name = 'I11a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a314}')

I11a323 = Parameter(name = 'I11a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a323}')

I11a324 = Parameter(name = 'I11a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a324}')

I11a333 = Parameter(name = 'I11a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I11a333}')

I11a334 = Parameter(name = 'I11a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I11a334}')

I110a15 = Parameter(name = 'I110a15',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1',
                    texname = '\\text{I110a15}')

I110a26 = Parameter(name = 'I110a26',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2',
                    texname = '\\text{I110a26}')

I110a31 = Parameter(name = 'I110a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3',
                    texname = '\\text{I110a31}')

I110a32 = Parameter(name = 'I110a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3',
                    texname = '\\text{I110a32}')

I111a15 = Parameter(name = 'I111a15',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(yd1x1)',
                    texname = '\\text{I111a15}')

I111a26 = Parameter(name = 'I111a26',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(yd2x2)',
                    texname = '\\text{I111a26}')

I111a31 = Parameter(name = 'I111a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(yd3x3)',
                    texname = '\\text{I111a31}')

I111a32 = Parameter(name = 'I111a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(yd3x3)',
                    texname = '\\text{I111a32}')

I112a14 = Parameter(name = 'I112a14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1',
                    texname = '\\text{I112a14}')

I112a23 = Parameter(name = 'I112a23',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2',
                    texname = '\\text{I112a23}')

I112a31 = Parameter(name = 'I112a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3',
                    texname = '\\text{I112a31}')

I112a32 = Parameter(name = 'I112a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3',
                    texname = '\\text{I112a32}')

I113a111 = Parameter(name = 'I113a111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD1x3x1)',
                     texname = '\\text{I113a111}')

I113a112 = Parameter(name = 'I113a112',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD1x3x1)',
                     texname = '\\text{I113a112}')

I113a115 = Parameter(name = 'I113a115',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD1x1x1)',
                     texname = '\\text{I113a115}')

I113a116 = Parameter(name = 'I113a116',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD1x2x1)',
                     texname = '\\text{I113a116}')

I113a121 = Parameter(name = 'I113a121',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD1x3x2)',
                     texname = '\\text{I113a121}')

I113a122 = Parameter(name = 'I113a122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD1x3x2)',
                     texname = '\\text{I113a122}')

I113a125 = Parameter(name = 'I113a125',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD1x1x2)',
                     texname = '\\text{I113a125}')

I113a126 = Parameter(name = 'I113a126',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD1x2x2)',
                     texname = '\\text{I113a126}')

I113a131 = Parameter(name = 'I113a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD1x3x3)',
                     texname = '\\text{I113a131}')

I113a132 = Parameter(name = 'I113a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD1x3x3)',
                     texname = '\\text{I113a132}')

I113a135 = Parameter(name = 'I113a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD1x1x3)',
                     texname = '\\text{I113a135}')

I113a136 = Parameter(name = 'I113a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD1x2x3)',
                     texname = '\\text{I113a136}')

I113a211 = Parameter(name = 'I113a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD2x3x1)',
                     texname = '\\text{I113a211}')

I113a212 = Parameter(name = 'I113a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD2x3x1)',
                     texname = '\\text{I113a212}')

I113a215 = Parameter(name = 'I113a215',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD2x1x1)',
                     texname = '\\text{I113a215}')

I113a216 = Parameter(name = 'I113a216',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD2x2x1)',
                     texname = '\\text{I113a216}')

I113a221 = Parameter(name = 'I113a221',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD2x3x2)',
                     texname = '\\text{I113a221}')

I113a222 = Parameter(name = 'I113a222',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD2x3x2)',
                     texname = '\\text{I113a222}')

I113a225 = Parameter(name = 'I113a225',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD2x1x2)',
                     texname = '\\text{I113a225}')

I113a226 = Parameter(name = 'I113a226',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD2x2x2)',
                     texname = '\\text{I113a226}')

I113a231 = Parameter(name = 'I113a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD2x3x3)',
                     texname = '\\text{I113a231}')

I113a232 = Parameter(name = 'I113a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD2x3x3)',
                     texname = '\\text{I113a232}')

I113a235 = Parameter(name = 'I113a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD2x1x3)',
                     texname = '\\text{I113a235}')

I113a236 = Parameter(name = 'I113a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD2x2x3)',
                     texname = '\\text{I113a236}')

I113a311 = Parameter(name = 'I113a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD3x3x1)',
                     texname = '\\text{I113a311}')

I113a312 = Parameter(name = 'I113a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD3x3x1)',
                     texname = '\\text{I113a312}')

I113a315 = Parameter(name = 'I113a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD3x1x1)',
                     texname = '\\text{I113a315}')

I113a316 = Parameter(name = 'I113a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD3x2x1)',
                     texname = '\\text{I113a316}')

I113a321 = Parameter(name = 'I113a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD3x3x2)',
                     texname = '\\text{I113a321}')

I113a322 = Parameter(name = 'I113a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD3x3x2)',
                     texname = '\\text{I113a322}')

I113a325 = Parameter(name = 'I113a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD3x1x2)',
                     texname = '\\text{I113a325}')

I113a326 = Parameter(name = 'I113a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD3x2x2)',
                     texname = '\\text{I113a326}')

I113a331 = Parameter(name = 'I113a331',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru1x3*complexconjugate(LLQD3x3x3)',
                     texname = '\\text{I113a331}')

I113a332 = Parameter(name = 'I113a332',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru2x3*complexconjugate(LLQD3x3x3)',
                     texname = '\\text{I113a332}')

I113a335 = Parameter(name = 'I113a335',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru5x1*complexconjugate(LLQD3x1x3)',
                     texname = '\\text{I113a335}')

I113a336 = Parameter(name = 'I113a336',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Ru6x2*complexconjugate(LLQD3x2x3)',
                     texname = '\\text{I113a336}')

I114a121 = Parameter(name = 'I114a121',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Ru1x6',
                     texname = '\\text{I114a121}')

I114a122 = Parameter(name = 'I114a122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Ru2x6',
                     texname = '\\text{I114a122}')

I114a123 = Parameter(name = 'I114a123',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Ru3x5',
                     texname = '\\text{I114a123}')

I114a124 = Parameter(name = 'I114a124',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Ru4x4',
                     texname = '\\text{I114a124}')

I114a131 = Parameter(name = 'I114a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Ru1x6',
                     texname = '\\text{I114a131}')

I114a132 = Parameter(name = 'I114a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Ru2x6',
                     texname = '\\text{I114a132}')

I114a133 = Parameter(name = 'I114a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Ru3x5',
                     texname = '\\text{I114a133}')

I114a134 = Parameter(name = 'I114a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Ru4x4',
                     texname = '\\text{I114a134}')

I114a211 = Parameter(name = 'I114a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Ru1x6',
                     texname = '\\text{I114a211}')

I114a212 = Parameter(name = 'I114a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Ru2x6',
                     texname = '\\text{I114a212}')

I114a213 = Parameter(name = 'I114a213',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Ru3x5',
                     texname = '\\text{I114a213}')

I114a214 = Parameter(name = 'I114a214',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Ru4x4',
                     texname = '\\text{I114a214}')

I114a231 = Parameter(name = 'I114a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Ru1x6',
                     texname = '\\text{I114a231}')

I114a232 = Parameter(name = 'I114a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Ru2x6',
                     texname = '\\text{I114a232}')

I114a233 = Parameter(name = 'I114a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Ru3x5',
                     texname = '\\text{I114a233}')

I114a234 = Parameter(name = 'I114a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Ru4x4',
                     texname = '\\text{I114a234}')

I114a311 = Parameter(name = 'I114a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Ru1x6',
                     texname = '\\text{I114a311}')

I114a312 = Parameter(name = 'I114a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Ru2x6',
                     texname = '\\text{I114a312}')

I114a313 = Parameter(name = 'I114a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Ru3x5',
                     texname = '\\text{I114a313}')

I114a314 = Parameter(name = 'I114a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Ru4x4',
                     texname = '\\text{I114a314}')

I114a321 = Parameter(name = 'I114a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Ru1x6',
                     texname = '\\text{I114a321}')

I114a322 = Parameter(name = 'I114a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Ru2x6',
                     texname = '\\text{I114a322}')

I114a323 = Parameter(name = 'I114a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Ru3x5',
                     texname = '\\text{I114a323}')

I114a324 = Parameter(name = 'I114a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Ru4x4',
                     texname = '\\text{I114a324}')

I115a121 = Parameter(name = 'I115a121',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Ru1x6',
                     texname = '\\text{I115a121}')

I115a122 = Parameter(name = 'I115a122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Ru2x6',
                     texname = '\\text{I115a122}')

I115a123 = Parameter(name = 'I115a123',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Ru3x5',
                     texname = '\\text{I115a123}')

I115a124 = Parameter(name = 'I115a124',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Ru4x4',
                     texname = '\\text{I115a124}')

I115a131 = Parameter(name = 'I115a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Ru1x6',
                     texname = '\\text{I115a131}')

I115a132 = Parameter(name = 'I115a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Ru2x6',
                     texname = '\\text{I115a132}')

I115a133 = Parameter(name = 'I115a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Ru3x5',
                     texname = '\\text{I115a133}')

I115a134 = Parameter(name = 'I115a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Ru4x4',
                     texname = '\\text{I115a134}')

I115a211 = Parameter(name = 'I115a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Ru1x6',
                     texname = '\\text{I115a211}')

I115a212 = Parameter(name = 'I115a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Ru2x6',
                     texname = '\\text{I115a212}')

I115a213 = Parameter(name = 'I115a213',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Ru3x5',
                     texname = '\\text{I115a213}')

I115a214 = Parameter(name = 'I115a214',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Ru4x4',
                     texname = '\\text{I115a214}')

I115a231 = Parameter(name = 'I115a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Ru1x6',
                     texname = '\\text{I115a231}')

I115a232 = Parameter(name = 'I115a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Ru2x6',
                     texname = '\\text{I115a232}')

I115a233 = Parameter(name = 'I115a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Ru3x5',
                     texname = '\\text{I115a233}')

I115a234 = Parameter(name = 'I115a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Ru4x4',
                     texname = '\\text{I115a234}')

I115a311 = Parameter(name = 'I115a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Ru1x6',
                     texname = '\\text{I115a311}')

I115a312 = Parameter(name = 'I115a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Ru2x6',
                     texname = '\\text{I115a312}')

I115a313 = Parameter(name = 'I115a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Ru3x5',
                     texname = '\\text{I115a313}')

I115a314 = Parameter(name = 'I115a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Ru4x4',
                     texname = '\\text{I115a314}')

I115a321 = Parameter(name = 'I115a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Ru1x6',
                     texname = '\\text{I115a321}')

I115a322 = Parameter(name = 'I115a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Ru2x6',
                     texname = '\\text{I115a322}')

I115a323 = Parameter(name = 'I115a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Ru3x5',
                     texname = '\\text{I115a323}')

I115a324 = Parameter(name = 'I115a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Ru4x4',
                     texname = '\\text{I115a324}')

I116a11 = Parameter(name = 'I116a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I116a11}')

I116a12 = Parameter(name = 'I116a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I116a12}')

I116a21 = Parameter(name = 'I116a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I116a21}')

I116a22 = Parameter(name = 'I116a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I116a22}')

I116a56 = Parameter(name = 'I116a56',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I116a56}')

I116a65 = Parameter(name = 'I116a65',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I116a65}')

I117a11 = Parameter(name = 'I117a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I117a11}')

I117a12 = Parameter(name = 'I117a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I117a12}')

I117a21 = Parameter(name = 'I117a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I117a21}')

I117a22 = Parameter(name = 'I117a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I117a22}')

I117a36 = Parameter(name = 'I117a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                    texname = '\\text{I117a36}')

I117a45 = Parameter(name = 'I117a45',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                    texname = '\\text{I117a45}')

I118a11 = Parameter(name = 'I118a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd1x6)*complexconjugate(td3x3)',
                    texname = '\\text{I118a11}')

I118a12 = Parameter(name = 'I118a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd1x6)*complexconjugate(td3x3)',
                    texname = '\\text{I118a12}')

I118a21 = Parameter(name = 'I118a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd2x6)*complexconjugate(td3x3)',
                    texname = '\\text{I118a21}')

I118a22 = Parameter(name = 'I118a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd2x6)*complexconjugate(td3x3)',
                    texname = '\\text{I118a22}')

I118a36 = Parameter(name = 'I118a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Rd3x5)*complexconjugate(td2x2)',
                    texname = '\\text{I118a36}')

I118a45 = Parameter(name = 'I118a45',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Rd4x4)*complexconjugate(td1x1)',
                    texname = '\\text{I118a45}')

I119a11 = Parameter(name = 'I119a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*tu3x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I119a11}')

I119a12 = Parameter(name = 'I119a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*tu3x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I119a12}')

I119a21 = Parameter(name = 'I119a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*tu3x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I119a21}')

I119a22 = Parameter(name = 'I119a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*tu3x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I119a22}')

I119a53 = Parameter(name = 'I119a53',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*tu2x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I119a53}')

I119a64 = Parameter(name = 'I119a64',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*tu1x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I119a64}')

I12a16 = Parameter(name = 'I12a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(yd1x1)',
                   texname = '\\text{I12a16}')

I12a25 = Parameter(name = 'I12a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(yd2x2)',
                   texname = '\\text{I12a25}')

I12a31 = Parameter(name = 'I12a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(yd3x3)',
                   texname = '\\text{I12a31}')

I12a32 = Parameter(name = 'I12a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(yd3x3)',
                   texname = '\\text{I12a32}')

I120a11 = Parameter(name = 'I120a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yd3x3*complexconjugate(Rd1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I120a11}')

I120a12 = Parameter(name = 'I120a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yd3x3*complexconjugate(Rd1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I120a12}')

I120a21 = Parameter(name = 'I120a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yd3x3*complexconjugate(Rd2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I120a21}')

I120a22 = Parameter(name = 'I120a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yd3x3*complexconjugate(Rd2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I120a22}')

I120a56 = Parameter(name = 'I120a56',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*yd2x2*complexconjugate(Rd5x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I120a56}')

I120a65 = Parameter(name = 'I120a65',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*yd1x1*complexconjugate(Rd6x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I120a65}')

I121a11 = Parameter(name = 'I121a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yu3x3*complexconjugate(Rd1x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I121a11}')

I121a12 = Parameter(name = 'I121a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yu3x3*complexconjugate(Rd1x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I121a12}')

I121a21 = Parameter(name = 'I121a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yu3x3*complexconjugate(Rd2x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I121a21}')

I121a22 = Parameter(name = 'I121a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yu3x3*complexconjugate(Rd2x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I121a22}')

I121a56 = Parameter(name = 'I121a56',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*yu2x2*complexconjugate(Rd5x2)*complexconjugate(yu2x2)',
                    texname = '\\text{I121a56}')

I121a65 = Parameter(name = 'I121a65',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*yu1x1*complexconjugate(Rd6x1)*complexconjugate(yu1x1)',
                    texname = '\\text{I121a65}')

I122a11 = Parameter(name = 'I122a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I122a11}')

I122a12 = Parameter(name = 'I122a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I122a12}')

I122a21 = Parameter(name = 'I122a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I122a21}')

I122a22 = Parameter(name = 'I122a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I122a22}')

I122a53 = Parameter(name = 'I122a53',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I122a53}')

I122a64 = Parameter(name = 'I122a64',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I122a64}')

I123a11 = Parameter(name = 'I123a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I123a11}')

I123a12 = Parameter(name = 'I123a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I123a12}')

I123a21 = Parameter(name = 'I123a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I123a21}')

I123a22 = Parameter(name = 'I123a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I123a22}')

I123a33 = Parameter(name = 'I123a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2*complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                    texname = '\\text{I123a33}')

I123a44 = Parameter(name = 'I123a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1*complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                    texname = '\\text{I123a44}')

I124a11 = Parameter(name = 'I124a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I124a11}')

I124a12 = Parameter(name = 'I124a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I124a12}')

I124a21 = Parameter(name = 'I124a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I124a21}')

I124a22 = Parameter(name = 'I124a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I124a22}')

I124a55 = Parameter(name = 'I124a55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I124a55}')

I124a66 = Parameter(name = 'I124a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I124a66}')

I125a11 = Parameter(name = 'I125a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*complexconjugate(Ru1x6)',
                    texname = '\\text{I125a11}')

I125a12 = Parameter(name = 'I125a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*complexconjugate(Ru1x6)',
                    texname = '\\text{I125a12}')

I125a21 = Parameter(name = 'I125a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*complexconjugate(Ru2x6)',
                    texname = '\\text{I125a21}')

I125a22 = Parameter(name = 'I125a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*complexconjugate(Ru2x6)',
                    texname = '\\text{I125a22}')

I125a33 = Parameter(name = 'I125a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*complexconjugate(Ru3x5)',
                    texname = '\\text{I125a33}')

I125a44 = Parameter(name = 'I125a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*complexconjugate(Ru4x4)',
                    texname = '\\text{I125a44}')

I126a11 = Parameter(name = 'I126a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126a11}')

I126a12 = Parameter(name = 'I126a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126a12}')

I126a21 = Parameter(name = 'I126a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126a21}')

I126a22 = Parameter(name = 'I126a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I126a22}')

I126a36 = Parameter(name = 'I126a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I126a36}')

I126a45 = Parameter(name = 'I126a45',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I126a45}')

I127a11 = Parameter(name = 'I127a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru1x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I127a11}')

I127a12 = Parameter(name = 'I127a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru1x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I127a12}')

I127a21 = Parameter(name = 'I127a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru2x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I127a21}')

I127a22 = Parameter(name = 'I127a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru2x6)*complexconjugate(tu3x3)',
                    texname = '\\text{I127a22}')

I127a36 = Parameter(name = 'I127a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Ru3x5)*complexconjugate(tu2x2)',
                    texname = '\\text{I127a36}')

I127a45 = Parameter(name = 'I127a45',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Ru4x4)*complexconjugate(tu1x1)',
                    texname = '\\text{I127a45}')

I128a11 = Parameter(name = 'I128a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*tu3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I128a11}')

I128a12 = Parameter(name = 'I128a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*tu3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I128a12}')

I128a21 = Parameter(name = 'I128a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*tu3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I128a21}')

I128a22 = Parameter(name = 'I128a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*tu3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I128a22}')

I128a54 = Parameter(name = 'I128a54',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*tu1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I128a54}')

I128a63 = Parameter(name = 'I128a63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*tu2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I128a63}')

I129a11 = Parameter(name = 'I129a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I129a11}')

I129a12 = Parameter(name = 'I129a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I129a12}')

I129a21 = Parameter(name = 'I129a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I129a21}')

I129a22 = Parameter(name = 'I129a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I129a22}')

I129a54 = Parameter(name = 'I129a54',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I129a54}')

I129a63 = Parameter(name = 'I129a63',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I129a63}')

I13a14 = Parameter(name = 'I13a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1',
                   texname = '\\text{I13a14}')

I13a23 = Parameter(name = 'I13a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2',
                   texname = '\\text{I13a23}')

I13a31 = Parameter(name = 'I13a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3',
                   texname = '\\text{I13a31}')

I13a32 = Parameter(name = 'I13a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3',
                   texname = '\\text{I13a32}')

I130a11 = Parameter(name = 'I130a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yu3x3*complexconjugate(Ru1x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I130a11}')

I130a12 = Parameter(name = 'I130a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yu3x3*complexconjugate(Ru1x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I130a12}')

I130a21 = Parameter(name = 'I130a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*yu3x3*complexconjugate(Ru2x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I130a21}')

I130a22 = Parameter(name = 'I130a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*yu3x3*complexconjugate(Ru2x3)*complexconjugate(yu3x3)',
                    texname = '\\text{I130a22}')

I130a55 = Parameter(name = 'I130a55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*yu1x1*complexconjugate(Ru5x1)*complexconjugate(yu1x1)',
                    texname = '\\text{I130a55}')

I130a66 = Parameter(name = 'I130a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*yu2x2*complexconjugate(Ru6x2)*complexconjugate(yu2x2)',
                    texname = '\\text{I130a66}')

I131a11 = Parameter(name = 'I131a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131a11}')

I131a12 = Parameter(name = 'I131a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131a12}')

I131a21 = Parameter(name = 'I131a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*yu3x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131a21}')

I131a22 = Parameter(name = 'I131a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*yu3x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I131a22}')

I131a33 = Parameter(name = 'I131a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*yu2x2*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I131a33}')

I131a44 = Parameter(name = 'I131a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*yu1x1*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I131a44}')

I132a111 = Parameter(name = 'I132a111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a111}')

I132a112 = Parameter(name = 'I132a112',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a112}')

I132a115 = Parameter(name = 'I132a115',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*complexconjugate(Rd1x6)*complexconjugate(TLQD3x1x3)',
                     texname = '\\text{I132a115}')

I132a116 = Parameter(name = 'I132a116',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*complexconjugate(Rd1x6)*complexconjugate(TLQD3x2x3)',
                     texname = '\\text{I132a116}')

I132a141 = Parameter(name = 'I132a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD1x3x3)',
                     texname = '\\text{I132a141}')

I132a142 = Parameter(name = 'I132a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*complexconjugate(Rd1x6)*complexconjugate(TLQD1x3x3)',
                     texname = '\\text{I132a142}')

I132a145 = Parameter(name = 'I132a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*complexconjugate(Rd1x6)*complexconjugate(TLQD1x1x3)',
                     texname = '\\text{I132a145}')

I132a146 = Parameter(name = 'I132a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*complexconjugate(Rd1x6)*complexconjugate(TLQD1x2x3)',
                     texname = '\\text{I132a146}')

I132a151 = Parameter(name = 'I132a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD2x3x3)',
                     texname = '\\text{I132a151}')

I132a152 = Parameter(name = 'I132a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*complexconjugate(Rd1x6)*complexconjugate(TLQD2x3x3)',
                     texname = '\\text{I132a152}')

I132a155 = Parameter(name = 'I132a155',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*complexconjugate(Rd1x6)*complexconjugate(TLQD2x1x3)',
                     texname = '\\text{I132a155}')

I132a156 = Parameter(name = 'I132a156',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*complexconjugate(Rd1x6)*complexconjugate(TLQD2x2x3)',
                     texname = '\\text{I132a156}')

I132a161 = Parameter(name = 'I132a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a161}')

I132a162 = Parameter(name = 'I132a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a162}')

I132a165 = Parameter(name = 'I132a165',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*complexconjugate(Rd1x6)*complexconjugate(TLQD3x1x3)',
                     texname = '\\text{I132a165}')

I132a166 = Parameter(name = 'I132a166',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*complexconjugate(Rd1x6)*complexconjugate(TLQD3x2x3)',
                     texname = '\\text{I132a166}')

I132a211 = Parameter(name = 'I132a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a211}')

I132a212 = Parameter(name = 'I132a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a212}')

I132a215 = Parameter(name = 'I132a215',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*complexconjugate(Rd2x6)*complexconjugate(TLQD3x1x3)',
                     texname = '\\text{I132a215}')

I132a216 = Parameter(name = 'I132a216',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*complexconjugate(Rd2x6)*complexconjugate(TLQD3x2x3)',
                     texname = '\\text{I132a216}')

I132a241 = Parameter(name = 'I132a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD1x3x3)',
                     texname = '\\text{I132a241}')

I132a242 = Parameter(name = 'I132a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*complexconjugate(Rd2x6)*complexconjugate(TLQD1x3x3)',
                     texname = '\\text{I132a242}')

I132a245 = Parameter(name = 'I132a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*complexconjugate(Rd2x6)*complexconjugate(TLQD1x1x3)',
                     texname = '\\text{I132a245}')

I132a246 = Parameter(name = 'I132a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*complexconjugate(Rd2x6)*complexconjugate(TLQD1x2x3)',
                     texname = '\\text{I132a246}')

I132a251 = Parameter(name = 'I132a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD2x3x3)',
                     texname = '\\text{I132a251}')

I132a252 = Parameter(name = 'I132a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*complexconjugate(Rd2x6)*complexconjugate(TLQD2x3x3)',
                     texname = '\\text{I132a252}')

I132a255 = Parameter(name = 'I132a255',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*complexconjugate(Rd2x6)*complexconjugate(TLQD2x1x3)',
                     texname = '\\text{I132a255}')

I132a256 = Parameter(name = 'I132a256',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*complexconjugate(Rd2x6)*complexconjugate(TLQD2x2x3)',
                     texname = '\\text{I132a256}')

I132a261 = Parameter(name = 'I132a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a261}')

I132a262 = Parameter(name = 'I132a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                     texname = '\\text{I132a262}')

I132a265 = Parameter(name = 'I132a265',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*complexconjugate(Rd2x6)*complexconjugate(TLQD3x1x3)',
                     texname = '\\text{I132a265}')

I132a266 = Parameter(name = 'I132a266',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*complexconjugate(Rd2x6)*complexconjugate(TLQD3x2x3)',
                     texname = '\\text{I132a266}')

I132a311 = Parameter(name = 'I132a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                     texname = '\\text{I132a311}')

I132a312 = Parameter(name = 'I132a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                     texname = '\\text{I132a312}')

I132a315 = Parameter(name = 'I132a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*complexconjugate(Rd3x5)*complexconjugate(TLQD3x1x2)',
                     texname = '\\text{I132a315}')

I132a316 = Parameter(name = 'I132a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*complexconjugate(Rd3x5)*complexconjugate(TLQD3x2x2)',
                     texname = '\\text{I132a316}')

I132a341 = Parameter(name = 'I132a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD1x3x2)',
                     texname = '\\text{I132a341}')

I132a342 = Parameter(name = 'I132a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*complexconjugate(Rd3x5)*complexconjugate(TLQD1x3x2)',
                     texname = '\\text{I132a342}')

I132a345 = Parameter(name = 'I132a345',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*complexconjugate(Rd3x5)*complexconjugate(TLQD1x1x2)',
                     texname = '\\text{I132a345}')

I132a346 = Parameter(name = 'I132a346',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*complexconjugate(Rd3x5)*complexconjugate(TLQD1x2x2)',
                     texname = '\\text{I132a346}')

I132a351 = Parameter(name = 'I132a351',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD2x3x2)',
                     texname = '\\text{I132a351}')

I132a352 = Parameter(name = 'I132a352',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*complexconjugate(Rd3x5)*complexconjugate(TLQD2x3x2)',
                     texname = '\\text{I132a352}')

I132a355 = Parameter(name = 'I132a355',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*complexconjugate(Rd3x5)*complexconjugate(TLQD2x1x2)',
                     texname = '\\text{I132a355}')

I132a356 = Parameter(name = 'I132a356',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*complexconjugate(Rd3x5)*complexconjugate(TLQD2x2x2)',
                     texname = '\\text{I132a356}')

I132a361 = Parameter(name = 'I132a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                     texname = '\\text{I132a361}')

I132a362 = Parameter(name = 'I132a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                     texname = '\\text{I132a362}')

I132a365 = Parameter(name = 'I132a365',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*complexconjugate(Rd3x5)*complexconjugate(TLQD3x1x2)',
                     texname = '\\text{I132a365}')

I132a366 = Parameter(name = 'I132a366',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*complexconjugate(Rd3x5)*complexconjugate(TLQD3x2x2)',
                     texname = '\\text{I132a366}')

I132a411 = Parameter(name = 'I132a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                     texname = '\\text{I132a411}')

I132a412 = Parameter(name = 'I132a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                     texname = '\\text{I132a412}')

I132a415 = Parameter(name = 'I132a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*complexconjugate(Rd4x4)*complexconjugate(TLQD3x1x1)',
                     texname = '\\text{I132a415}')

I132a416 = Parameter(name = 'I132a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*complexconjugate(Rd4x4)*complexconjugate(TLQD3x2x1)',
                     texname = '\\text{I132a416}')

I132a441 = Parameter(name = 'I132a441',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD1x3x1)',
                     texname = '\\text{I132a441}')

I132a442 = Parameter(name = 'I132a442',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*complexconjugate(Rd4x4)*complexconjugate(TLQD1x3x1)',
                     texname = '\\text{I132a442}')

I132a445 = Parameter(name = 'I132a445',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*complexconjugate(Rd4x4)*complexconjugate(TLQD1x1x1)',
                     texname = '\\text{I132a445}')

I132a446 = Parameter(name = 'I132a446',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*complexconjugate(Rd4x4)*complexconjugate(TLQD1x2x1)',
                     texname = '\\text{I132a446}')

I132a451 = Parameter(name = 'I132a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD2x3x1)',
                     texname = '\\text{I132a451}')

I132a452 = Parameter(name = 'I132a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*complexconjugate(Rd4x4)*complexconjugate(TLQD2x3x1)',
                     texname = '\\text{I132a452}')

I132a455 = Parameter(name = 'I132a455',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*complexconjugate(Rd4x4)*complexconjugate(TLQD2x1x1)',
                     texname = '\\text{I132a455}')

I132a456 = Parameter(name = 'I132a456',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*complexconjugate(Rd4x4)*complexconjugate(TLQD2x2x1)',
                     texname = '\\text{I132a456}')

I132a461 = Parameter(name = 'I132a461',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                     texname = '\\text{I132a461}')

I132a462 = Parameter(name = 'I132a462',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                     texname = '\\text{I132a462}')

I132a465 = Parameter(name = 'I132a465',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*complexconjugate(Rd4x4)*complexconjugate(TLQD3x1x1)',
                     texname = '\\text{I132a465}')

I132a466 = Parameter(name = 'I132a466',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*complexconjugate(Rd4x4)*complexconjugate(TLQD3x2x1)',
                     texname = '\\text{I132a466}')

I133a111 = Parameter(name = 'I133a111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a111}')

I133a112 = Parameter(name = 'I133a112',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a112}')

I133a115 = Parameter(name = 'I133a115',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a115}')

I133a116 = Parameter(name = 'I133a116',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a116}')

I133a141 = Parameter(name = 'I133a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a141}')

I133a142 = Parameter(name = 'I133a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a142}')

I133a145 = Parameter(name = 'I133a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*yd3x3*complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a145}')

I133a146 = Parameter(name = 'I133a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*yd3x3*complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a146}')

I133a151 = Parameter(name = 'I133a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a151}')

I133a152 = Parameter(name = 'I133a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a152}')

I133a155 = Parameter(name = 'I133a155',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*yd3x3*complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a155}')

I133a156 = Parameter(name = 'I133a156',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*yd3x3*complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a156}')

I133a161 = Parameter(name = 'I133a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a161}')

I133a162 = Parameter(name = 'I133a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a162}')

I133a165 = Parameter(name = 'I133a165',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a165}')

I133a166 = Parameter(name = 'I133a166',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x3)',
                     texname = '\\text{I133a166}')

I133a211 = Parameter(name = 'I133a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a211}')

I133a212 = Parameter(name = 'I133a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a212}')

I133a215 = Parameter(name = 'I133a215',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a215}')

I133a216 = Parameter(name = 'I133a216',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a216}')

I133a241 = Parameter(name = 'I133a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a241}')

I133a242 = Parameter(name = 'I133a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a242}')

I133a245 = Parameter(name = 'I133a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*yd3x3*complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a245}')

I133a246 = Parameter(name = 'I133a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*yd3x3*complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a246}')

I133a251 = Parameter(name = 'I133a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a251}')

I133a252 = Parameter(name = 'I133a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a252}')

I133a255 = Parameter(name = 'I133a255',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*yd3x3*complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a255}')

I133a256 = Parameter(name = 'I133a256',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*yd3x3*complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a256}')

I133a261 = Parameter(name = 'I133a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a261}')

I133a262 = Parameter(name = 'I133a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a262}')

I133a265 = Parameter(name = 'I133a265',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a265}')

I133a266 = Parameter(name = 'I133a266',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x3)',
                     texname = '\\text{I133a266}')

I133a511 = Parameter(name = 'I133a511',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a511}')

I133a512 = Parameter(name = 'I133a512',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a512}')

I133a515 = Parameter(name = 'I133a515',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*yd2x2*complexconjugate(LLQD3x1x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a515}')

I133a516 = Parameter(name = 'I133a516',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*yd2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a516}')

I133a541 = Parameter(name = 'I133a541',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*yd2x2*complexconjugate(LLQD1x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a541}')

I133a542 = Parameter(name = 'I133a542',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*yd2x2*complexconjugate(LLQD1x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a542}')

I133a545 = Parameter(name = 'I133a545',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*yd2x2*complexconjugate(LLQD1x1x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a545}')

I133a546 = Parameter(name = 'I133a546',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*yd2x2*complexconjugate(LLQD1x2x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a546}')

I133a551 = Parameter(name = 'I133a551',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*yd2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a551}')

I133a552 = Parameter(name = 'I133a552',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*yd2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a552}')

I133a555 = Parameter(name = 'I133a555',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*yd2x2*complexconjugate(LLQD2x1x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a555}')

I133a556 = Parameter(name = 'I133a556',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*yd2x2*complexconjugate(LLQD2x2x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a556}')

I133a561 = Parameter(name = 'I133a561',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a561}')

I133a562 = Parameter(name = 'I133a562',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a562}')

I133a565 = Parameter(name = 'I133a565',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*yd2x2*complexconjugate(LLQD3x1x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a565}')

I133a566 = Parameter(name = 'I133a566',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*yd2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd5x2)',
                     texname = '\\text{I133a566}')

I133a611 = Parameter(name = 'I133a611',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a611}')

I133a612 = Parameter(name = 'I133a612',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a612}')

I133a615 = Parameter(name = 'I133a615',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru5x1*yd1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a615}')

I133a616 = Parameter(name = 'I133a616',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru6x2*yd1x1*complexconjugate(LLQD3x2x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a616}')

I133a641 = Parameter(name = 'I133a641',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x3*yd1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a641}')

I133a642 = Parameter(name = 'I133a642',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x3*yd1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a642}')

I133a645 = Parameter(name = 'I133a645',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru5x1*yd1x1*complexconjugate(LLQD1x1x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a645}')

I133a646 = Parameter(name = 'I133a646',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru6x2*yd1x1*complexconjugate(LLQD1x2x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a646}')

I133a651 = Parameter(name = 'I133a651',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x3*yd1x1*complexconjugate(LLQD2x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a651}')

I133a652 = Parameter(name = 'I133a652',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x3*yd1x1*complexconjugate(LLQD2x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a652}')

I133a655 = Parameter(name = 'I133a655',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru5x1*yd1x1*complexconjugate(LLQD2x1x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a655}')

I133a656 = Parameter(name = 'I133a656',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru6x2*yd1x1*complexconjugate(LLQD2x2x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a656}')

I133a661 = Parameter(name = 'I133a661',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a661}')

I133a662 = Parameter(name = 'I133a662',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a662}')

I133a665 = Parameter(name = 'I133a665',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru5x1*yd1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a665}')

I133a666 = Parameter(name = 'I133a666',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru6x2*yd1x1*complexconjugate(LLQD3x2x1)*complexconjugate(Rd6x1)',
                     texname = '\\text{I133a666}')

I134a111 = Parameter(name = 'I134a111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a111}')

I134a112 = Parameter(name = 'I134a112',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a112}')

I134a115 = Parameter(name = 'I134a115',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a115}')

I134a116 = Parameter(name = 'I134a116',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a116}')

I134a121 = Parameter(name = 'I134a121',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru1x3*ye2x2*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a121}')

I134a122 = Parameter(name = 'I134a122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru2x3*ye2x2*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a122}')

I134a125 = Parameter(name = 'I134a125',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru5x1*ye2x2*complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a125}')

I134a126 = Parameter(name = 'I134a126',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru6x2*ye2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a126}')

I134a131 = Parameter(name = 'I134a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru1x3*ye1x1*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a131}')

I134a132 = Parameter(name = 'I134a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru2x3*ye1x1*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a132}')

I134a135 = Parameter(name = 'I134a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru5x1*ye1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a135}')

I134a136 = Parameter(name = 'I134a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru6x2*ye1x1*complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a136}')

I134a161 = Parameter(name = 'I134a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a161}')

I134a162 = Parameter(name = 'I134a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a162}')

I134a165 = Parameter(name = 'I134a165',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a165}')

I134a166 = Parameter(name = 'I134a166',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I134a166}')

I134a211 = Parameter(name = 'I134a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a211}')

I134a212 = Parameter(name = 'I134a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a212}')

I134a215 = Parameter(name = 'I134a215',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a215}')

I134a216 = Parameter(name = 'I134a216',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a216}')

I134a221 = Parameter(name = 'I134a221',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru1x3*ye2x2*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a221}')

I134a222 = Parameter(name = 'I134a222',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru2x3*ye2x2*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a222}')

I134a225 = Parameter(name = 'I134a225',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru5x1*ye2x2*complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a225}')

I134a226 = Parameter(name = 'I134a226',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru6x2*ye2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a226}')

I134a231 = Parameter(name = 'I134a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru1x3*ye1x1*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a231}')

I134a232 = Parameter(name = 'I134a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru2x3*ye1x1*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a232}')

I134a235 = Parameter(name = 'I134a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru5x1*ye1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a235}')

I134a236 = Parameter(name = 'I134a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru6x2*ye1x1*complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a236}')

I134a261 = Parameter(name = 'I134a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a261}')

I134a262 = Parameter(name = 'I134a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a262}')

I134a265 = Parameter(name = 'I134a265',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a265}')

I134a266 = Parameter(name = 'I134a266',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I134a266}')

I134a311 = Parameter(name = 'I134a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a311}')

I134a312 = Parameter(name = 'I134a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a312}')

I134a315 = Parameter(name = 'I134a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a315}')

I134a316 = Parameter(name = 'I134a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a316}')

I134a321 = Parameter(name = 'I134a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru1x3*ye2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a321}')

I134a322 = Parameter(name = 'I134a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru2x3*ye2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a322}')

I134a325 = Parameter(name = 'I134a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru5x1*ye2x2*complexconjugate(LLQD2x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a325}')

I134a326 = Parameter(name = 'I134a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru6x2*ye2x2*complexconjugate(LLQD2x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a326}')

I134a331 = Parameter(name = 'I134a331',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru1x3*ye1x1*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a331}')

I134a332 = Parameter(name = 'I134a332',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru2x3*ye1x1*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a332}')

I134a335 = Parameter(name = 'I134a335',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru5x1*ye1x1*complexconjugate(LLQD1x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a335}')

I134a336 = Parameter(name = 'I134a336',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru6x2*ye1x1*complexconjugate(LLQD1x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a336}')

I134a361 = Parameter(name = 'I134a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a361}')

I134a362 = Parameter(name = 'I134a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a362}')

I134a365 = Parameter(name = 'I134a365',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a365}')

I134a366 = Parameter(name = 'I134a366',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I134a366}')

I134a411 = Parameter(name = 'I134a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a411}')

I134a412 = Parameter(name = 'I134a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a412}')

I134a415 = Parameter(name = 'I134a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a415}')

I134a416 = Parameter(name = 'I134a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a416}')

I134a421 = Parameter(name = 'I134a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru1x3*ye2x2*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a421}')

I134a422 = Parameter(name = 'I134a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru2x3*ye2x2*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a422}')

I134a425 = Parameter(name = 'I134a425',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru5x1*ye2x2*complexconjugate(LLQD2x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a425}')

I134a426 = Parameter(name = 'I134a426',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl2x5*Ru6x2*ye2x2*complexconjugate(LLQD2x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a426}')

I134a431 = Parameter(name = 'I134a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru1x3*ye1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a431}')

I134a432 = Parameter(name = 'I134a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru2x3*ye1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a432}')

I134a435 = Parameter(name = 'I134a435',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru5x1*ye1x1*complexconjugate(LLQD1x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a435}')

I134a436 = Parameter(name = 'I134a436',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl3x4*Ru6x2*ye1x1*complexconjugate(LLQD1x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a436}')

I134a461 = Parameter(name = 'I134a461',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru1x3*ye3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a461}')

I134a462 = Parameter(name = 'I134a462',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru2x3*ye3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a462}')

I134a465 = Parameter(name = 'I134a465',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru5x1*ye3x3*complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a465}')

I134a466 = Parameter(name = 'I134a466',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x6*Ru6x2*ye3x3*complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I134a466}')

I135a111 = Parameter(name = 'I135a111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a111}')

I135a112 = Parameter(name = 'I135a112',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a112}')

I135a113 = Parameter(name = 'I135a113',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a113}')

I135a114 = Parameter(name = 'I135a114',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a114}')

I135a141 = Parameter(name = 'I135a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x6*yu3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a141}')

I135a142 = Parameter(name = 'I135a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x6*yu3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a142}')

I135a143 = Parameter(name = 'I135a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru3x5*yu2x2*complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a143}')

I135a144 = Parameter(name = 'I135a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru4x4*yu1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a144}')

I135a151 = Parameter(name = 'I135a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x6*yu3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a151}')

I135a152 = Parameter(name = 'I135a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x6*yu3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a152}')

I135a153 = Parameter(name = 'I135a153',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru3x5*yu2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a153}')

I135a154 = Parameter(name = 'I135a154',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru4x4*yu1x1*complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a154}')

I135a161 = Parameter(name = 'I135a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a161}')

I135a162 = Parameter(name = 'I135a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a162}')

I135a163 = Parameter(name = 'I135a163',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a163}')

I135a164 = Parameter(name = 'I135a164',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                     texname = '\\text{I135a164}')

I135a211 = Parameter(name = 'I135a211',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a211}')

I135a212 = Parameter(name = 'I135a212',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a212}')

I135a213 = Parameter(name = 'I135a213',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a213}')

I135a214 = Parameter(name = 'I135a214',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a214}')

I135a241 = Parameter(name = 'I135a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x6*yu3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a241}')

I135a242 = Parameter(name = 'I135a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x6*yu3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a242}')

I135a243 = Parameter(name = 'I135a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru3x5*yu2x2*complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a243}')

I135a244 = Parameter(name = 'I135a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru4x4*yu1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a244}')

I135a251 = Parameter(name = 'I135a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x6*yu3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a251}')

I135a252 = Parameter(name = 'I135a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x6*yu3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a252}')

I135a253 = Parameter(name = 'I135a253',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru3x5*yu2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a253}')

I135a254 = Parameter(name = 'I135a254',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru4x4*yu1x1*complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a254}')

I135a261 = Parameter(name = 'I135a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a261}')

I135a262 = Parameter(name = 'I135a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a262}')

I135a263 = Parameter(name = 'I135a263',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a263}')

I135a264 = Parameter(name = 'I135a264',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                     texname = '\\text{I135a264}')

I135a311 = Parameter(name = 'I135a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a311}')

I135a312 = Parameter(name = 'I135a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a312}')

I135a313 = Parameter(name = 'I135a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a313}')

I135a314 = Parameter(name = 'I135a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a314}')

I135a341 = Parameter(name = 'I135a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x6*yu3x3*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a341}')

I135a342 = Parameter(name = 'I135a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x6*yu3x3*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a342}')

I135a343 = Parameter(name = 'I135a343',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru3x5*yu2x2*complexconjugate(LLQD1x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a343}')

I135a344 = Parameter(name = 'I135a344',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru4x4*yu1x1*complexconjugate(LLQD1x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a344}')

I135a351 = Parameter(name = 'I135a351',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x6*yu3x3*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a351}')

I135a352 = Parameter(name = 'I135a352',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x6*yu3x3*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a352}')

I135a353 = Parameter(name = 'I135a353',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru3x5*yu2x2*complexconjugate(LLQD2x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a353}')

I135a354 = Parameter(name = 'I135a354',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru4x4*yu1x1*complexconjugate(LLQD2x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a354}')

I135a361 = Parameter(name = 'I135a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a361}')

I135a362 = Parameter(name = 'I135a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a362}')

I135a363 = Parameter(name = 'I135a363',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a363}')

I135a364 = Parameter(name = 'I135a364',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                     texname = '\\text{I135a364}')

I135a411 = Parameter(name = 'I135a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a411}')

I135a412 = Parameter(name = 'I135a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a412}')

I135a413 = Parameter(name = 'I135a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a413}')

I135a414 = Parameter(name = 'I135a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl1x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a414}')

I135a441 = Parameter(name = 'I135a441',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru1x6*yu3x3*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a441}')

I135a442 = Parameter(name = 'I135a442',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru2x6*yu3x3*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a442}')

I135a443 = Parameter(name = 'I135a443',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru3x5*yu2x2*complexconjugate(LLQD1x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a443}')

I135a444 = Parameter(name = 'I135a444',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl4x1*Ru4x4*yu1x1*complexconjugate(LLQD1x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a444}')

I135a451 = Parameter(name = 'I135a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru1x6*yu3x3*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a451}')

I135a452 = Parameter(name = 'I135a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru2x6*yu3x3*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a452}')

I135a453 = Parameter(name = 'I135a453',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru3x5*yu2x2*complexconjugate(LLQD2x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a453}')

I135a454 = Parameter(name = 'I135a454',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl5x2*Ru4x4*yu1x1*complexconjugate(LLQD2x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a454}')

I135a461 = Parameter(name = 'I135a461',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru1x6*yu3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a461}')

I135a462 = Parameter(name = 'I135a462',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru2x6*yu3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a462}')

I135a463 = Parameter(name = 'I135a463',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru3x5*yu2x2*complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a463}')

I135a464 = Parameter(name = 'I135a464',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rl6x3*Ru4x4*yu1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                     texname = '\\text{I135a464}')

I136a131 = Parameter(name = 'I136a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a131}')

I136a132 = Parameter(name = 'I136a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a132}')

I136a135 = Parameter(name = 'I136a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a135}')

I136a136 = Parameter(name = 'I136a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a136}')

I136a141 = Parameter(name = 'I136a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a141}')

I136a142 = Parameter(name = 'I136a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a142}')

I136a145 = Parameter(name = 'I136a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a145}')

I136a146 = Parameter(name = 'I136a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a146}')

I136a231 = Parameter(name = 'I136a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a231}')

I136a232 = Parameter(name = 'I136a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a232}')

I136a235 = Parameter(name = 'I136a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a235}')

I136a236 = Parameter(name = 'I136a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a236}')

I136a241 = Parameter(name = 'I136a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a241}')

I136a242 = Parameter(name = 'I136a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a242}')

I136a245 = Parameter(name = 'I136a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a245}')

I136a246 = Parameter(name = 'I136a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a246}')

I136a311 = Parameter(name = 'I136a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a311}')

I136a312 = Parameter(name = 'I136a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a312}')

I136a315 = Parameter(name = 'I136a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a315}')

I136a316 = Parameter(name = 'I136a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a316}')

I136a321 = Parameter(name = 'I136a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a321}')

I136a322 = Parameter(name = 'I136a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a322}')

I136a325 = Parameter(name = 'I136a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a325}')

I136a326 = Parameter(name = 'I136a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a326}')

I136a341 = Parameter(name = 'I136a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a341}')

I136a342 = Parameter(name = 'I136a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a342}')

I136a345 = Parameter(name = 'I136a345',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd3x5*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a345}')

I136a346 = Parameter(name = 'I136a346',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd3x5*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a346}')

I136a411 = Parameter(name = 'I136a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a411}')

I136a412 = Parameter(name = 'I136a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a412}')

I136a415 = Parameter(name = 'I136a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a415}')

I136a416 = Parameter(name = 'I136a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a416}')

I136a421 = Parameter(name = 'I136a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a421}')

I136a422 = Parameter(name = 'I136a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a422}')

I136a425 = Parameter(name = 'I136a425',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a425}')

I136a426 = Parameter(name = 'I136a426',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a426}')

I136a431 = Parameter(name = 'I136a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a431}')

I136a432 = Parameter(name = 'I136a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I136a432}')

I136a435 = Parameter(name = 'I136a435',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd3x5*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I136a435}')

I136a436 = Parameter(name = 'I136a436',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd3x5*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I136a436}')

I137a131 = Parameter(name = 'I137a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a131}')

I137a132 = Parameter(name = 'I137a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a132}')

I137a135 = Parameter(name = 'I137a135',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a135}')

I137a136 = Parameter(name = 'I137a136',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a136}')

I137a141 = Parameter(name = 'I137a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a141}')

I137a142 = Parameter(name = 'I137a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a142}')

I137a145 = Parameter(name = 'I137a145',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a145}')

I137a146 = Parameter(name = 'I137a146',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a146}')

I137a231 = Parameter(name = 'I137a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a231}')

I137a232 = Parameter(name = 'I137a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a232}')

I137a235 = Parameter(name = 'I137a235',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a235}')

I137a236 = Parameter(name = 'I137a236',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a236}')

I137a241 = Parameter(name = 'I137a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a241}')

I137a242 = Parameter(name = 'I137a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a242}')

I137a245 = Parameter(name = 'I137a245',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a245}')

I137a246 = Parameter(name = 'I137a246',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a246}')

I137a311 = Parameter(name = 'I137a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a311}')

I137a312 = Parameter(name = 'I137a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a312}')

I137a315 = Parameter(name = 'I137a315',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a315}')

I137a316 = Parameter(name = 'I137a316',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a316}')

I137a321 = Parameter(name = 'I137a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd3x5*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a321}')

I137a322 = Parameter(name = 'I137a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd3x5*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a322}')

I137a325 = Parameter(name = 'I137a325',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x6*Rd3x5*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a325}')

I137a326 = Parameter(name = 'I137a326',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x6*Rd3x5*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a326}')

I137a341 = Parameter(name = 'I137a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a341}')

I137a342 = Parameter(name = 'I137a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a342}')

I137a345 = Parameter(name = 'I137a345',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd3x5*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a345}')

I137a346 = Parameter(name = 'I137a346',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd3x5*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a346}')

I137a411 = Parameter(name = 'I137a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a411}')

I137a412 = Parameter(name = 'I137a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a412}')

I137a415 = Parameter(name = 'I137a415',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a415}')

I137a416 = Parameter(name = 'I137a416',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a416}')

I137a421 = Parameter(name = 'I137a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a421}')

I137a422 = Parameter(name = 'I137a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a422}')

I137a425 = Parameter(name = 'I137a425',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x6*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a425}')

I137a426 = Parameter(name = 'I137a426',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x6*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a426}')

I137a431 = Parameter(name = 'I137a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd4x4*Ru1x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a431}')

I137a432 = Parameter(name = 'I137a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd4x4*Ru2x3*complexconjugate(yu3x3)',
                     texname = '\\text{I137a432}')

I137a435 = Parameter(name = 'I137a435',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd3x5*Rd4x4*Ru5x1*complexconjugate(yu1x1)',
                     texname = '\\text{I137a435}')

I137a436 = Parameter(name = 'I137a436',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd3x5*Rd4x4*Ru6x2*complexconjugate(yu2x2)',
                     texname = '\\text{I137a436}')

I138a151 = Parameter(name = 'I138a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a151}')

I138a152 = Parameter(name = 'I138a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a152}')

I138a153 = Parameter(name = 'I138a153',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I138a153}')

I138a154 = Parameter(name = 'I138a154',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I138a154}')

I138a161 = Parameter(name = 'I138a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a161}')

I138a162 = Parameter(name = 'I138a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a162}')

I138a163 = Parameter(name = 'I138a163',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I138a163}')

I138a164 = Parameter(name = 'I138a164',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I138a164}')

I138a251 = Parameter(name = 'I138a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a251}')

I138a252 = Parameter(name = 'I138a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a252}')

I138a253 = Parameter(name = 'I138a253',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I138a253}')

I138a254 = Parameter(name = 'I138a254',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I138a254}')

I138a261 = Parameter(name = 'I138a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a261}')

I138a262 = Parameter(name = 'I138a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a262}')

I138a263 = Parameter(name = 'I138a263',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I138a263}')

I138a264 = Parameter(name = 'I138a264',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I138a264}')

I138a311 = Parameter(name = 'I138a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a311}')

I138a312 = Parameter(name = 'I138a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a312}')

I138a313 = Parameter(name = 'I138a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I138a313}')

I138a314 = Parameter(name = 'I138a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I138a314}')

I138a321 = Parameter(name = 'I138a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a321}')

I138a322 = Parameter(name = 'I138a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a322}')

I138a323 = Parameter(name = 'I138a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I138a323}')

I138a324 = Parameter(name = 'I138a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I138a324}')

I138a361 = Parameter(name = 'I138a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a361}')

I138a362 = Parameter(name = 'I138a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I138a362}')

I138a363 = Parameter(name = 'I138a363',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd3x5*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I138a363}')

I138a364 = Parameter(name = 'I138a364',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd3x5*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I138a364}')

I138a411 = Parameter(name = 'I138a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a411}')

I138a412 = Parameter(name = 'I138a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a412}')

I138a413 = Parameter(name = 'I138a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I138a413}')

I138a414 = Parameter(name = 'I138a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I138a414}')

I138a421 = Parameter(name = 'I138a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a421}')

I138a422 = Parameter(name = 'I138a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I138a422}')

I138a423 = Parameter(name = 'I138a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I138a423}')

I138a424 = Parameter(name = 'I138a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I138a424}')

I138a451 = Parameter(name = 'I138a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd4x4*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a451}')

I138a452 = Parameter(name = 'I138a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd4x4*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I138a452}')

I138a453 = Parameter(name = 'I138a453',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd4x4*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I138a453}')

I138a454 = Parameter(name = 'I138a454',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd4x4*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I138a454}')

I139a151 = Parameter(name = 'I139a151',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a151}')

I139a152 = Parameter(name = 'I139a152',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a152}')

I139a153 = Parameter(name = 'I139a153',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I139a153}')

I139a154 = Parameter(name = 'I139a154',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I139a154}')

I139a161 = Parameter(name = 'I139a161',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a161}')

I139a162 = Parameter(name = 'I139a162',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a162}')

I139a163 = Parameter(name = 'I139a163',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I139a163}')

I139a164 = Parameter(name = 'I139a164',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I139a164}')

I139a251 = Parameter(name = 'I139a251',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a251}')

I139a252 = Parameter(name = 'I139a252',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a252}')

I139a253 = Parameter(name = 'I139a253',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I139a253}')

I139a254 = Parameter(name = 'I139a254',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I139a254}')

I139a261 = Parameter(name = 'I139a261',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a261}')

I139a262 = Parameter(name = 'I139a262',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a262}')

I139a263 = Parameter(name = 'I139a263',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I139a263}')

I139a264 = Parameter(name = 'I139a264',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I139a264}')

I139a311 = Parameter(name = 'I139a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a311}')

I139a312 = Parameter(name = 'I139a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a312}')

I139a313 = Parameter(name = 'I139a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I139a313}')

I139a314 = Parameter(name = 'I139a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I139a314}')

I139a321 = Parameter(name = 'I139a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a321}')

I139a322 = Parameter(name = 'I139a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a322}')

I139a323 = Parameter(name = 'I139a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I139a323}')

I139a324 = Parameter(name = 'I139a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I139a324}')

I139a361 = Parameter(name = 'I139a361',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a361}')

I139a362 = Parameter(name = 'I139a362',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I139a362}')

I139a363 = Parameter(name = 'I139a363',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd3x5*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I139a363}')

I139a364 = Parameter(name = 'I139a364',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd3x5*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I139a364}')

I139a411 = Parameter(name = 'I139a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a411}')

I139a412 = Parameter(name = 'I139a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a412}')

I139a413 = Parameter(name = 'I139a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I139a413}')

I139a414 = Parameter(name = 'I139a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I139a414}')

I139a421 = Parameter(name = 'I139a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a421}')

I139a422 = Parameter(name = 'I139a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I139a422}')

I139a423 = Parameter(name = 'I139a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I139a423}')

I139a424 = Parameter(name = 'I139a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I139a424}')

I139a451 = Parameter(name = 'I139a451',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd4x4*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a451}')

I139a452 = Parameter(name = 'I139a452',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd4x4*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I139a452}')

I139a453 = Parameter(name = 'I139a453',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd4x4*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I139a453}')

I139a454 = Parameter(name = 'I139a454',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd4x4*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I139a454}')

I14a16 = Parameter(name = 'I14a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1',
                   texname = '\\text{I14a16}')

I14a25 = Parameter(name = 'I14a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2',
                   texname = '\\text{I14a25}')

I14a31 = Parameter(name = 'I14a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3',
                   texname = '\\text{I14a31}')

I14a32 = Parameter(name = 'I14a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3',
                   texname = '\\text{I14a32}')

I140a131 = Parameter(name = 'I140a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a131}')

I140a132 = Parameter(name = 'I140a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a132}')

I140a133 = Parameter(name = 'I140a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I140a133}')

I140a134 = Parameter(name = 'I140a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I140a134}')

I140a141 = Parameter(name = 'I140a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a141}')

I140a142 = Parameter(name = 'I140a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a142}')

I140a143 = Parameter(name = 'I140a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I140a143}')

I140a144 = Parameter(name = 'I140a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I140a144}')

I140a231 = Parameter(name = 'I140a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a231}')

I140a232 = Parameter(name = 'I140a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a232}')

I140a233 = Parameter(name = 'I140a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I140a233}')

I140a234 = Parameter(name = 'I140a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I140a234}')

I140a241 = Parameter(name = 'I140a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a241}')

I140a242 = Parameter(name = 'I140a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I140a242}')

I140a243 = Parameter(name = 'I140a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I140a243}')

I140a244 = Parameter(name = 'I140a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I140a244}')

I140a511 = Parameter(name = 'I140a511',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a511}')

I140a512 = Parameter(name = 'I140a512',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a512}')

I140a513 = Parameter(name = 'I140a513',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I140a513}')

I140a514 = Parameter(name = 'I140a514',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I140a514}')

I140a521 = Parameter(name = 'I140a521',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a521}')

I140a522 = Parameter(name = 'I140a522',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a522}')

I140a523 = Parameter(name = 'I140a523',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I140a523}')

I140a524 = Parameter(name = 'I140a524',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I140a524}')

I140a541 = Parameter(name = 'I140a541',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd4x4*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a541}')

I140a542 = Parameter(name = 'I140a542',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd4x4*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I140a542}')

I140a543 = Parameter(name = 'I140a543',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd4x4*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I140a543}')

I140a544 = Parameter(name = 'I140a544',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd4x4*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I140a544}')

I140a611 = Parameter(name = 'I140a611',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a611}')

I140a612 = Parameter(name = 'I140a612',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a612}')

I140a613 = Parameter(name = 'I140a613',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I140a613}')

I140a614 = Parameter(name = 'I140a614',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I140a614}')

I140a621 = Parameter(name = 'I140a621',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a621}')

I140a622 = Parameter(name = 'I140a622',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a622}')

I140a623 = Parameter(name = 'I140a623',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I140a623}')

I140a624 = Parameter(name = 'I140a624',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I140a624}')

I140a631 = Parameter(name = 'I140a631',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a631}')

I140a632 = Parameter(name = 'I140a632',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd3x5*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I140a632}')

I140a633 = Parameter(name = 'I140a633',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd3x5*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I140a633}')

I140a634 = Parameter(name = 'I140a634',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd3x5*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I140a634}')

I141a131 = Parameter(name = 'I141a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a131}')

I141a132 = Parameter(name = 'I141a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd1x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a132}')

I141a133 = Parameter(name = 'I141a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd1x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I141a133}')

I141a134 = Parameter(name = 'I141a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd1x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I141a134}')

I141a141 = Parameter(name = 'I141a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a141}')

I141a142 = Parameter(name = 'I141a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd1x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a142}')

I141a143 = Parameter(name = 'I141a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd1x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I141a143}')

I141a144 = Parameter(name = 'I141a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd1x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I141a144}')

I141a231 = Parameter(name = 'I141a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x3*Rd3x5*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a231}')

I141a232 = Parameter(name = 'I141a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x3*Rd2x3*Rd3x5*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a232}')

I141a233 = Parameter(name = 'I141a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x3*Rd2x3*Rd3x5*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I141a233}')

I141a234 = Parameter(name = 'I141a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x3*Rd2x3*Rd3x5*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I141a234}')

I141a241 = Parameter(name = 'I141a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x3*Rd4x4*Ru1x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a241}')

I141a242 = Parameter(name = 'I141a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x3*Rd2x3*Rd4x4*Ru2x6*complexconjugate(yd3x3)',
                     texname = '\\text{I141a242}')

I141a243 = Parameter(name = 'I141a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x3*Rd2x3*Rd4x4*Ru3x5*complexconjugate(yd3x3)',
                     texname = '\\text{I141a243}')

I141a244 = Parameter(name = 'I141a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x3*Rd2x3*Rd4x4*Ru4x4*complexconjugate(yd3x3)',
                     texname = '\\text{I141a244}')

I141a511 = Parameter(name = 'I141a511',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a511}')

I141a512 = Parameter(name = 'I141a512',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd1x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a512}')

I141a513 = Parameter(name = 'I141a513',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd1x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I141a513}')

I141a514 = Parameter(name = 'I141a514',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd1x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I141a514}')

I141a521 = Parameter(name = 'I141a521',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a521}')

I141a522 = Parameter(name = 'I141a522',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x2*Rd2x6*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a522}')

I141a523 = Parameter(name = 'I141a523',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x2*Rd2x6*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I141a523}')

I141a524 = Parameter(name = 'I141a524',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x2*Rd2x6*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I141a524}')

I141a541 = Parameter(name = 'I141a541',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd4x4*Rd5x2*Ru1x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a541}')

I141a542 = Parameter(name = 'I141a542',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x1x2*Rd4x4*Rd5x2*Ru2x6*complexconjugate(yd2x2)',
                     texname = '\\text{I141a542}')

I141a543 = Parameter(name = 'I141a543',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x1x2*Rd4x4*Rd5x2*Ru3x5*complexconjugate(yd2x2)',
                     texname = '\\text{I141a543}')

I141a544 = Parameter(name = 'I141a544',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x1x2*Rd4x4*Rd5x2*Ru4x4*complexconjugate(yd2x2)',
                     texname = '\\text{I141a544}')

I141a611 = Parameter(name = 'I141a611',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a611}')

I141a612 = Parameter(name = 'I141a612',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd1x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a612}')

I141a613 = Parameter(name = 'I141a613',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd1x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I141a613}')

I141a614 = Parameter(name = 'I141a614',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd1x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I141a614}')

I141a621 = Parameter(name = 'I141a621',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a621}')

I141a622 = Parameter(name = 'I141a622',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x3x1*Rd2x6*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a622}')

I141a623 = Parameter(name = 'I141a623',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x3x1*Rd2x6*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I141a623}')

I141a624 = Parameter(name = 'I141a624',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x3x1*Rd2x6*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I141a624}')

I141a631 = Parameter(name = 'I141a631',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd6x1*Ru1x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a631}')

I141a632 = Parameter(name = 'I141a632',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD3x2x1*Rd3x5*Rd6x1*Ru2x6*complexconjugate(yd1x1)',
                     texname = '\\text{I141a632}')

I141a633 = Parameter(name = 'I141a633',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD2x2x1*Rd3x5*Rd6x1*Ru3x5*complexconjugate(yd1x1)',
                     texname = '\\text{I141a633}')

I141a634 = Parameter(name = 'I141a634',
                     nature = 'internal',
                     type = 'complex',
                     value = 'LUDD1x2x1*Rd3x5*Rd6x1*Ru4x4*complexconjugate(yd1x1)',
                     texname = '\\text{I141a634}')

I142a131 = Parameter(name = 'I142a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru1x6*TUDD3x3x2',
                     texname = '\\text{I142a131}')

I142a132 = Parameter(name = 'I142a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru2x6*TUDD3x3x2',
                     texname = '\\text{I142a132}')

I142a133 = Parameter(name = 'I142a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru3x5*TUDD2x3x2',
                     texname = '\\text{I142a133}')

I142a134 = Parameter(name = 'I142a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru4x4*TUDD1x3x2',
                     texname = '\\text{I142a134}')

I142a141 = Parameter(name = 'I142a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru1x6*TUDD3x3x1',
                     texname = '\\text{I142a141}')

I142a142 = Parameter(name = 'I142a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru2x6*TUDD3x3x1',
                     texname = '\\text{I142a142}')

I142a143 = Parameter(name = 'I142a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru3x5*TUDD2x3x1',
                     texname = '\\text{I142a143}')

I142a144 = Parameter(name = 'I142a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru4x4*TUDD1x3x1',
                     texname = '\\text{I142a144}')

I142a231 = Parameter(name = 'I142a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru1x6*TUDD3x3x2',
                     texname = '\\text{I142a231}')

I142a232 = Parameter(name = 'I142a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru2x6*TUDD3x3x2',
                     texname = '\\text{I142a232}')

I142a233 = Parameter(name = 'I142a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru3x5*TUDD2x3x2',
                     texname = '\\text{I142a233}')

I142a234 = Parameter(name = 'I142a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru4x4*TUDD1x3x2',
                     texname = '\\text{I142a234}')

I142a241 = Parameter(name = 'I142a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru1x6*TUDD3x3x1',
                     texname = '\\text{I142a241}')

I142a242 = Parameter(name = 'I142a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru2x6*TUDD3x3x1',
                     texname = '\\text{I142a242}')

I142a243 = Parameter(name = 'I142a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru3x5*TUDD2x3x1',
                     texname = '\\text{I142a243}')

I142a244 = Parameter(name = 'I142a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru4x4*TUDD1x3x1',
                     texname = '\\text{I142a244}')

I142a311 = Parameter(name = 'I142a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru1x6*TUDD3x2x3',
                     texname = '\\text{I142a311}')

I142a312 = Parameter(name = 'I142a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru2x6*TUDD3x2x3',
                     texname = '\\text{I142a312}')

I142a313 = Parameter(name = 'I142a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru3x5*TUDD2x2x3',
                     texname = '\\text{I142a313}')

I142a314 = Parameter(name = 'I142a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru4x4*TUDD1x2x3',
                     texname = '\\text{I142a314}')

I142a321 = Parameter(name = 'I142a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru1x6*TUDD3x2x3',
                     texname = '\\text{I142a321}')

I142a322 = Parameter(name = 'I142a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru2x6*TUDD3x2x3',
                     texname = '\\text{I142a322}')

I142a323 = Parameter(name = 'I142a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru3x5*TUDD2x2x3',
                     texname = '\\text{I142a323}')

I142a324 = Parameter(name = 'I142a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru4x4*TUDD1x2x3',
                     texname = '\\text{I142a324}')

I142a341 = Parameter(name = 'I142a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru1x6*TUDD3x2x1',
                     texname = '\\text{I142a341}')

I142a342 = Parameter(name = 'I142a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru2x6*TUDD3x2x1',
                     texname = '\\text{I142a342}')

I142a343 = Parameter(name = 'I142a343',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru3x5*TUDD2x2x1',
                     texname = '\\text{I142a343}')

I142a344 = Parameter(name = 'I142a344',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru4x4*TUDD1x2x1',
                     texname = '\\text{I142a344}')

I142a411 = Parameter(name = 'I142a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru1x6*TUDD3x1x3',
                     texname = '\\text{I142a411}')

I142a412 = Parameter(name = 'I142a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru2x6*TUDD3x1x3',
                     texname = '\\text{I142a412}')

I142a413 = Parameter(name = 'I142a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru3x5*TUDD2x1x3',
                     texname = '\\text{I142a413}')

I142a414 = Parameter(name = 'I142a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru4x4*TUDD1x1x3',
                     texname = '\\text{I142a414}')

I142a421 = Parameter(name = 'I142a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru1x6*TUDD3x1x3',
                     texname = '\\text{I142a421}')

I142a422 = Parameter(name = 'I142a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru2x6*TUDD3x1x3',
                     texname = '\\text{I142a422}')

I142a423 = Parameter(name = 'I142a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru3x5*TUDD2x1x3',
                     texname = '\\text{I142a423}')

I142a424 = Parameter(name = 'I142a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru4x4*TUDD1x1x3',
                     texname = '\\text{I142a424}')

I142a431 = Parameter(name = 'I142a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru1x6*TUDD3x1x2',
                     texname = '\\text{I142a431}')

I142a432 = Parameter(name = 'I142a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru2x6*TUDD3x1x2',
                     texname = '\\text{I142a432}')

I142a433 = Parameter(name = 'I142a433',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru3x5*TUDD2x1x2',
                     texname = '\\text{I142a433}')

I142a434 = Parameter(name = 'I142a434',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru4x4*TUDD1x1x2',
                     texname = '\\text{I142a434}')

I143a131 = Parameter(name = 'I143a131',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru1x6*TUDD3x2x3',
                     texname = '\\text{I143a131}')

I143a132 = Parameter(name = 'I143a132',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru2x6*TUDD3x2x3',
                     texname = '\\text{I143a132}')

I143a133 = Parameter(name = 'I143a133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru3x5*TUDD2x2x3',
                     texname = '\\text{I143a133}')

I143a134 = Parameter(name = 'I143a134',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru4x4*TUDD1x2x3',
                     texname = '\\text{I143a134}')

I143a141 = Parameter(name = 'I143a141',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru1x6*TUDD3x1x3',
                     texname = '\\text{I143a141}')

I143a142 = Parameter(name = 'I143a142',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru2x6*TUDD3x1x3',
                     texname = '\\text{I143a142}')

I143a143 = Parameter(name = 'I143a143',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru3x5*TUDD2x1x3',
                     texname = '\\text{I143a143}')

I143a144 = Parameter(name = 'I143a144',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru4x4*TUDD1x1x3',
                     texname = '\\text{I143a144}')

I143a231 = Parameter(name = 'I143a231',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru1x6*TUDD3x2x3',
                     texname = '\\text{I143a231}')

I143a232 = Parameter(name = 'I143a232',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru2x6*TUDD3x2x3',
                     texname = '\\text{I143a232}')

I143a233 = Parameter(name = 'I143a233',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru3x5*TUDD2x2x3',
                     texname = '\\text{I143a233}')

I143a234 = Parameter(name = 'I143a234',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru4x4*TUDD1x2x3',
                     texname = '\\text{I143a234}')

I143a241 = Parameter(name = 'I143a241',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru1x6*TUDD3x1x3',
                     texname = '\\text{I143a241}')

I143a242 = Parameter(name = 'I143a242',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru2x6*TUDD3x1x3',
                     texname = '\\text{I143a242}')

I143a243 = Parameter(name = 'I143a243',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru3x5*TUDD2x1x3',
                     texname = '\\text{I143a243}')

I143a244 = Parameter(name = 'I143a244',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru4x4*TUDD1x1x3',
                     texname = '\\text{I143a244}')

I143a311 = Parameter(name = 'I143a311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru1x6*TUDD3x3x2',
                     texname = '\\text{I143a311}')

I143a312 = Parameter(name = 'I143a312',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru2x6*TUDD3x3x2',
                     texname = '\\text{I143a312}')

I143a313 = Parameter(name = 'I143a313',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru3x5*TUDD2x3x2',
                     texname = '\\text{I143a313}')

I143a314 = Parameter(name = 'I143a314',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd3x5*Ru4x4*TUDD1x3x2',
                     texname = '\\text{I143a314}')

I143a321 = Parameter(name = 'I143a321',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru1x6*TUDD3x3x2',
                     texname = '\\text{I143a321}')

I143a322 = Parameter(name = 'I143a322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru2x6*TUDD3x3x2',
                     texname = '\\text{I143a322}')

I143a323 = Parameter(name = 'I143a323',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru3x5*TUDD2x3x2',
                     texname = '\\text{I143a323}')

I143a324 = Parameter(name = 'I143a324',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd3x5*Ru4x4*TUDD1x3x2',
                     texname = '\\text{I143a324}')

I143a341 = Parameter(name = 'I143a341',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru1x6*TUDD3x1x2',
                     texname = '\\text{I143a341}')

I143a342 = Parameter(name = 'I143a342',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru2x6*TUDD3x1x2',
                     texname = '\\text{I143a342}')

I143a343 = Parameter(name = 'I143a343',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru3x5*TUDD2x1x2',
                     texname = '\\text{I143a343}')

I143a344 = Parameter(name = 'I143a344',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru4x4*TUDD1x1x2',
                     texname = '\\text{I143a344}')

I143a411 = Parameter(name = 'I143a411',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru1x6*TUDD3x3x1',
                     texname = '\\text{I143a411}')

I143a412 = Parameter(name = 'I143a412',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru2x6*TUDD3x3x1',
                     texname = '\\text{I143a412}')

I143a413 = Parameter(name = 'I143a413',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru3x5*TUDD2x3x1',
                     texname = '\\text{I143a413}')

I143a414 = Parameter(name = 'I143a414',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd1x6*Rd4x4*Ru4x4*TUDD1x3x1',
                     texname = '\\text{I143a414}')

I143a421 = Parameter(name = 'I143a421',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru1x6*TUDD3x3x1',
                     texname = '\\text{I143a421}')

I143a422 = Parameter(name = 'I143a422',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru2x6*TUDD3x3x1',
                     texname = '\\text{I143a422}')

I143a423 = Parameter(name = 'I143a423',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru3x5*TUDD2x3x1',
                     texname = '\\text{I143a423}')

I143a424 = Parameter(name = 'I143a424',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd2x6*Rd4x4*Ru4x4*TUDD1x3x1',
                     texname = '\\text{I143a424}')

I143a431 = Parameter(name = 'I143a431',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru1x6*TUDD3x2x1',
                     texname = '\\text{I143a431}')

I143a432 = Parameter(name = 'I143a432',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru2x6*TUDD3x2x1',
                     texname = '\\text{I143a432}')

I143a433 = Parameter(name = 'I143a433',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru3x5*TUDD2x2x1',
                     texname = '\\text{I143a433}')

I143a434 = Parameter(name = 'I143a434',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Rd3x5*Rd4x4*Ru4x4*TUDD1x2x1',
                     texname = '\\text{I143a434}')

I144a16 = Parameter(name = 'I144a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd6x1)',
                    texname = '\\text{I144a16}')

I144a25 = Parameter(name = 'I144a25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd5x2)',
                    texname = '\\text{I144a25}')

I144a31 = Parameter(name = 'I144a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd1x3)',
                    texname = '\\text{I144a31}')

I144a32 = Parameter(name = 'I144a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd2x3)',
                    texname = '\\text{I144a32}')

I145a14 = Parameter(name = 'I145a14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                    texname = '\\text{I145a14}')

I145a23 = Parameter(name = 'I145a23',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                    texname = '\\text{I145a23}')

I145a31 = Parameter(name = 'I145a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I145a31}')

I145a32 = Parameter(name = 'I145a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                    texname = '\\text{I145a32}')

I146a16 = Parameter(name = 'I146a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu1x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I146a16}')

I146a25 = Parameter(name = 'I146a25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu2x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I146a25}')

I146a31 = Parameter(name = 'I146a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu3x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I146a31}')

I146a32 = Parameter(name = 'I146a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yu3x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I146a32}')

I147a14 = Parameter(name = 'I147a14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl4x1)',
                    texname = '\\text{I147a14}')

I147a25 = Parameter(name = 'I147a25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl5x2)',
                    texname = '\\text{I147a25}')

I147a31 = Parameter(name = 'I147a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl1x3)',
                    texname = '\\text{I147a31}')

I147a36 = Parameter(name = 'I147a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x3)',
                    texname = '\\text{I147a36}')

I148a13 = Parameter(name = 'I148a13',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl3x4)*complexconjugate(ye1x1)',
                    texname = '\\text{I148a13}')

I148a22 = Parameter(name = 'I148a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl2x5)*complexconjugate(ye2x2)',
                    texname = '\\text{I148a22}')

I148a31 = Parameter(name = 'I148a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I148a31}')

I148a36 = Parameter(name = 'I148a36',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                    texname = '\\text{I148a36}')

I149a13 = Parameter(name = 'I149a13',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn3x1)',
                    texname = '\\text{I149a13}')

I149a22 = Parameter(name = 'I149a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn2x2)',
                    texname = '\\text{I149a22}')

I149a31 = Parameter(name = 'I149a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Rn1x3)',
                    texname = '\\text{I149a31}')

I15a16 = Parameter(name = 'I15a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(yu1x1)',
                   texname = '\\text{I15a16}')

I15a25 = Parameter(name = 'I15a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(yu2x2)',
                   texname = '\\text{I15a25}')

I15a31 = Parameter(name = 'I15a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(yu3x3)',
                   texname = '\\text{I15a31}')

I15a32 = Parameter(name = 'I15a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(yu3x3)',
                   texname = '\\text{I15a32}')

I150a13 = Parameter(name = 'I150a13',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye1x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I150a13}')

I150a22 = Parameter(name = 'I150a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye2x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I150a22}')

I150a31 = Parameter(name = 'I150a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I150a31}')

I151a15 = Parameter(name = 'I151a15',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru5x1)',
                    texname = '\\text{I151a15}')

I151a26 = Parameter(name = 'I151a26',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru6x2)',
                    texname = '\\text{I151a26}')

I151a31 = Parameter(name = 'I151a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru1x3)',
                    texname = '\\text{I151a31}')

I151a32 = Parameter(name = 'I151a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru2x3)',
                    texname = '\\text{I151a32}')

I152a14 = Parameter(name = 'I152a14',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I152a14}')

I152a23 = Parameter(name = 'I152a23',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I152a23}')

I152a31 = Parameter(name = 'I152a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I152a31}')

I152a32 = Parameter(name = 'I152a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I152a32}')

I153a15 = Parameter(name = 'I153a15',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I153a15}')

I153a26 = Parameter(name = 'I153a26',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I153a26}')

I153a31 = Parameter(name = 'I153a31',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I153a31}')

I153a32 = Parameter(name = 'I153a32',
                    nature = 'internal',
                    type = 'complex',
                    value = 'yd3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I153a32}')

I154a11 = Parameter(name = 'I154a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I154a11}')

I154a12 = Parameter(name = 'I154a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I154a12}')

I154a21 = Parameter(name = 'I154a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I154a21}')

I154a22 = Parameter(name = 'I154a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I154a22}')

I154a56 = Parameter(name = 'I154a56',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I154a56}')

I154a65 = Parameter(name = 'I154a65',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I154a65}')

I155a11 = Parameter(name = 'I155a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I155a11}')

I155a16 = Parameter(name = 'I155a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I155a16}')

I155a25 = Parameter(name = 'I155a25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I155a25}')

I155a34 = Parameter(name = 'I155a34',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I155a34}')

I156a11 = Parameter(name = 'I156a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I156a11}')

I156a12 = Parameter(name = 'I156a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I156a12}')

I156a21 = Parameter(name = 'I156a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I156a21}')

I156a22 = Parameter(name = 'I156a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I156a22}')

I156a56 = Parameter(name = 'I156a56',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I156a56}')

I156a65 = Parameter(name = 'I156a65',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I156a65}')

I157a11 = Parameter(name = 'I157a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I157a11}')

I157a16 = Parameter(name = 'I157a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I157a16}')

I157a25 = Parameter(name = 'I157a25',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I157a25}')

I157a34 = Parameter(name = 'I157a34',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I157a34}')

I158a11 = Parameter(name = 'I158a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I158a11}')

I158a12 = Parameter(name = 'I158a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(Rd1x3)',
                    texname = '\\text{I158a12}')

I158a21 = Parameter(name = 'I158a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I158a21}')

I158a22 = Parameter(name = 'I158a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(Rd2x3)',
                    texname = '\\text{I158a22}')

I158a55 = Parameter(name = 'I158a55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(Rd5x2)',
                    texname = '\\text{I158a55}')

I158a66 = Parameter(name = 'I158a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(Rd6x1)',
                    texname = '\\text{I158a66}')

I159a11 = Parameter(name = 'I159a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I159a11}')

I159a16 = Parameter(name = 'I159a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I159a16}')

I159a44 = Parameter(name = 'I159a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I159a44}')

I159a55 = Parameter(name = 'I159a55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I159a55}')

I159a61 = Parameter(name = 'I159a61',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I159a61}')

I159a66 = Parameter(name = 'I159a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I159a66}')

I16a14 = Parameter(name = 'I16a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1',
                   texname = '\\text{I16a14}')

I16a23 = Parameter(name = 'I16a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2',
                   texname = '\\text{I16a23}')

I16a31 = Parameter(name = 'I16a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3',
                   texname = '\\text{I16a31}')

I16a32 = Parameter(name = 'I16a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3',
                   texname = '\\text{I16a32}')

I160a11 = Parameter(name = 'I160a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I160a11}')

I160a12 = Parameter(name = 'I160a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I160a12}')

I160a21 = Parameter(name = 'I160a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I160a21}')

I160a22 = Parameter(name = 'I160a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I160a22}')

I160a55 = Parameter(name = 'I160a55',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru5x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I160a55}')

I160a66 = Parameter(name = 'I160a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru6x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I160a66}')

I161a11 = Parameter(name = 'I161a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye1x1',
                    texname = '\\text{I161a11}')

I161a22 = Parameter(name = 'I161a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye2x2',
                    texname = '\\text{I161a22}')

I161a33 = Parameter(name = 'I161a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'ye3x3',
                    texname = '\\text{I161a33}')

I162a11 = Parameter(name = 'I162a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*complexconjugate(Rd1x6)',
                    texname = '\\text{I162a11}')

I162a12 = Parameter(name = 'I162a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*complexconjugate(Rd1x6)',
                    texname = '\\text{I162a12}')

I162a21 = Parameter(name = 'I162a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*complexconjugate(Rd2x6)',
                    texname = '\\text{I162a21}')

I162a22 = Parameter(name = 'I162a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*complexconjugate(Rd2x6)',
                    texname = '\\text{I162a22}')

I162a33 = Parameter(name = 'I162a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*complexconjugate(Rd3x5)',
                    texname = '\\text{I162a33}')

I162a44 = Parameter(name = 'I162a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*complexconjugate(Rd4x4)',
                    texname = '\\text{I162a44}')

I163a11 = Parameter(name = 'I163a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*complexconjugate(Rl1x6)',
                    texname = '\\text{I163a11}')

I163a16 = Parameter(name = 'I163a16',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl1x6)',
                    texname = '\\text{I163a16}')

I163a22 = Parameter(name = 'I163a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*complexconjugate(Rl2x5)',
                    texname = '\\text{I163a22}')

I163a33 = Parameter(name = 'I163a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*complexconjugate(Rl3x4)',
                    texname = '\\text{I163a33}')

I163a61 = Parameter(name = 'I163a61',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I163a61}')

I163a66 = Parameter(name = 'I163a66',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*complexconjugate(Rl6x6)',
                    texname = '\\text{I163a66}')

I164a11 = Parameter(name = 'I164a11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*complexconjugate(Ru1x6)',
                    texname = '\\text{I164a11}')

I164a12 = Parameter(name = 'I164a12',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*complexconjugate(Ru1x6)',
                    texname = '\\text{I164a12}')

I164a21 = Parameter(name = 'I164a21',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru1x6*complexconjugate(Ru2x6)',
                    texname = '\\text{I164a21}')

I164a22 = Parameter(name = 'I164a22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru2x6*complexconjugate(Ru2x6)',
                    texname = '\\text{I164a22}')

I164a33 = Parameter(name = 'I164a33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru3x5*complexconjugate(Ru3x5)',
                    texname = '\\text{I164a33}')

I164a44 = Parameter(name = 'I164a44',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Ru4x4*complexconjugate(Ru4x4)',
                    texname = '\\text{I164a44}')

I17a111 = Parameter(name = 'I17a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD1x3x1)',
                    texname = '\\text{I17a111}')

I17a112 = Parameter(name = 'I17a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD1x3x1)',
                    texname = '\\text{I17a112}')

I17a115 = Parameter(name = 'I17a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD1x2x1)',
                    texname = '\\text{I17a115}')

I17a116 = Parameter(name = 'I17a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD1x1x1)',
                    texname = '\\text{I17a116}')

I17a121 = Parameter(name = 'I17a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD1x3x2)',
                    texname = '\\text{I17a121}')

I17a122 = Parameter(name = 'I17a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD1x3x2)',
                    texname = '\\text{I17a122}')

I17a125 = Parameter(name = 'I17a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD1x2x2)',
                    texname = '\\text{I17a125}')

I17a126 = Parameter(name = 'I17a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD1x1x2)',
                    texname = '\\text{I17a126}')

I17a131 = Parameter(name = 'I17a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD1x3x3)',
                    texname = '\\text{I17a131}')

I17a132 = Parameter(name = 'I17a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD1x3x3)',
                    texname = '\\text{I17a132}')

I17a135 = Parameter(name = 'I17a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD1x2x3)',
                    texname = '\\text{I17a135}')

I17a136 = Parameter(name = 'I17a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD1x1x3)',
                    texname = '\\text{I17a136}')

I17a211 = Parameter(name = 'I17a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD2x3x1)',
                    texname = '\\text{I17a211}')

I17a212 = Parameter(name = 'I17a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD2x3x1)',
                    texname = '\\text{I17a212}')

I17a215 = Parameter(name = 'I17a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD2x2x1)',
                    texname = '\\text{I17a215}')

I17a216 = Parameter(name = 'I17a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD2x1x1)',
                    texname = '\\text{I17a216}')

I17a221 = Parameter(name = 'I17a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD2x3x2)',
                    texname = '\\text{I17a221}')

I17a222 = Parameter(name = 'I17a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD2x3x2)',
                    texname = '\\text{I17a222}')

I17a225 = Parameter(name = 'I17a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD2x2x2)',
                    texname = '\\text{I17a225}')

I17a226 = Parameter(name = 'I17a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD2x1x2)',
                    texname = '\\text{I17a226}')

I17a231 = Parameter(name = 'I17a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD2x3x3)',
                    texname = '\\text{I17a231}')

I17a232 = Parameter(name = 'I17a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD2x3x3)',
                    texname = '\\text{I17a232}')

I17a235 = Parameter(name = 'I17a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD2x2x3)',
                    texname = '\\text{I17a235}')

I17a236 = Parameter(name = 'I17a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD2x1x3)',
                    texname = '\\text{I17a236}')

I17a311 = Parameter(name = 'I17a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD3x3x1)',
                    texname = '\\text{I17a311}')

I17a312 = Parameter(name = 'I17a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD3x3x1)',
                    texname = '\\text{I17a312}')

I17a315 = Parameter(name = 'I17a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD3x2x1)',
                    texname = '\\text{I17a315}')

I17a316 = Parameter(name = 'I17a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD3x1x1)',
                    texname = '\\text{I17a316}')

I17a321 = Parameter(name = 'I17a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD3x3x2)',
                    texname = '\\text{I17a321}')

I17a322 = Parameter(name = 'I17a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD3x3x2)',
                    texname = '\\text{I17a322}')

I17a325 = Parameter(name = 'I17a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD3x2x2)',
                    texname = '\\text{I17a325}')

I17a326 = Parameter(name = 'I17a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD3x1x2)',
                    texname = '\\text{I17a326}')

I17a331 = Parameter(name = 'I17a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*complexconjugate(LLQD3x3x3)',
                    texname = '\\text{I17a331}')

I17a332 = Parameter(name = 'I17a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*complexconjugate(LLQD3x3x3)',
                    texname = '\\text{I17a332}')

I17a335 = Parameter(name = 'I17a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*complexconjugate(LLQD3x2x3)',
                    texname = '\\text{I17a335}')

I17a336 = Parameter(name = 'I17a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*complexconjugate(LLQD3x1x3)',
                    texname = '\\text{I17a336}')

I18a111 = Parameter(name = 'I18a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x6',
                    texname = '\\text{I18a111}')

I18a112 = Parameter(name = 'I18a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x6',
                    texname = '\\text{I18a112}')

I18a113 = Parameter(name = 'I18a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd3x5',
                    texname = '\\text{I18a113}')

I18a114 = Parameter(name = 'I18a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd4x4',
                    texname = '\\text{I18a114}')

I18a121 = Parameter(name = 'I18a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x6',
                    texname = '\\text{I18a121}')

I18a122 = Parameter(name = 'I18a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x6',
                    texname = '\\text{I18a122}')

I18a123 = Parameter(name = 'I18a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd3x5',
                    texname = '\\text{I18a123}')

I18a124 = Parameter(name = 'I18a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd4x4',
                    texname = '\\text{I18a124}')

I18a131 = Parameter(name = 'I18a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6',
                    texname = '\\text{I18a131}')

I18a132 = Parameter(name = 'I18a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6',
                    texname = '\\text{I18a132}')

I18a133 = Parameter(name = 'I18a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5',
                    texname = '\\text{I18a133}')

I18a134 = Parameter(name = 'I18a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4',
                    texname = '\\text{I18a134}')

I18a211 = Parameter(name = 'I18a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x6',
                    texname = '\\text{I18a211}')

I18a212 = Parameter(name = 'I18a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x6',
                    texname = '\\text{I18a212}')

I18a213 = Parameter(name = 'I18a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd3x5',
                    texname = '\\text{I18a213}')

I18a214 = Parameter(name = 'I18a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd4x4',
                    texname = '\\text{I18a214}')

I18a221 = Parameter(name = 'I18a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x6',
                    texname = '\\text{I18a221}')

I18a222 = Parameter(name = 'I18a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x6',
                    texname = '\\text{I18a222}')

I18a223 = Parameter(name = 'I18a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd3x5',
                    texname = '\\text{I18a223}')

I18a224 = Parameter(name = 'I18a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd4x4',
                    texname = '\\text{I18a224}')

I18a231 = Parameter(name = 'I18a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6',
                    texname = '\\text{I18a231}')

I18a232 = Parameter(name = 'I18a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6',
                    texname = '\\text{I18a232}')

I18a233 = Parameter(name = 'I18a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5',
                    texname = '\\text{I18a233}')

I18a234 = Parameter(name = 'I18a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4',
                    texname = '\\text{I18a234}')

I18a311 = Parameter(name = 'I18a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6',
                    texname = '\\text{I18a311}')

I18a312 = Parameter(name = 'I18a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6',
                    texname = '\\text{I18a312}')

I18a313 = Parameter(name = 'I18a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5',
                    texname = '\\text{I18a313}')

I18a314 = Parameter(name = 'I18a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4',
                    texname = '\\text{I18a314}')

I18a321 = Parameter(name = 'I18a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6',
                    texname = '\\text{I18a321}')

I18a322 = Parameter(name = 'I18a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6',
                    texname = '\\text{I18a322}')

I18a323 = Parameter(name = 'I18a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5',
                    texname = '\\text{I18a323}')

I18a324 = Parameter(name = 'I18a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4',
                    texname = '\\text{I18a324}')

I18a331 = Parameter(name = 'I18a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6',
                    texname = '\\text{I18a331}')

I18a332 = Parameter(name = 'I18a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6',
                    texname = '\\text{I18a332}')

I18a333 = Parameter(name = 'I18a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5',
                    texname = '\\text{I18a333}')

I18a334 = Parameter(name = 'I18a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4',
                    texname = '\\text{I18a334}')

I19a111 = Parameter(name = 'I19a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x6',
                    texname = '\\text{I19a111}')

I19a112 = Parameter(name = 'I19a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x6',
                    texname = '\\text{I19a112}')

I19a113 = Parameter(name = 'I19a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd3x5',
                    texname = '\\text{I19a113}')

I19a114 = Parameter(name = 'I19a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd4x4',
                    texname = '\\text{I19a114}')

I19a121 = Parameter(name = 'I19a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x6',
                    texname = '\\text{I19a121}')

I19a122 = Parameter(name = 'I19a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x6',
                    texname = '\\text{I19a122}')

I19a123 = Parameter(name = 'I19a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd3x5',
                    texname = '\\text{I19a123}')

I19a124 = Parameter(name = 'I19a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd4x4',
                    texname = '\\text{I19a124}')

I19a131 = Parameter(name = 'I19a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6',
                    texname = '\\text{I19a131}')

I19a132 = Parameter(name = 'I19a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6',
                    texname = '\\text{I19a132}')

I19a133 = Parameter(name = 'I19a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5',
                    texname = '\\text{I19a133}')

I19a134 = Parameter(name = 'I19a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4',
                    texname = '\\text{I19a134}')

I19a211 = Parameter(name = 'I19a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x6',
                    texname = '\\text{I19a211}')

I19a212 = Parameter(name = 'I19a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x6',
                    texname = '\\text{I19a212}')

I19a213 = Parameter(name = 'I19a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd3x5',
                    texname = '\\text{I19a213}')

I19a214 = Parameter(name = 'I19a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd4x4',
                    texname = '\\text{I19a214}')

I19a221 = Parameter(name = 'I19a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x6',
                    texname = '\\text{I19a221}')

I19a222 = Parameter(name = 'I19a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x6',
                    texname = '\\text{I19a222}')

I19a223 = Parameter(name = 'I19a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd3x5',
                    texname = '\\text{I19a223}')

I19a224 = Parameter(name = 'I19a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd4x4',
                    texname = '\\text{I19a224}')

I19a231 = Parameter(name = 'I19a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6',
                    texname = '\\text{I19a231}')

I19a232 = Parameter(name = 'I19a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6',
                    texname = '\\text{I19a232}')

I19a233 = Parameter(name = 'I19a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5',
                    texname = '\\text{I19a233}')

I19a234 = Parameter(name = 'I19a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4',
                    texname = '\\text{I19a234}')

I19a311 = Parameter(name = 'I19a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6',
                    texname = '\\text{I19a311}')

I19a312 = Parameter(name = 'I19a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6',
                    texname = '\\text{I19a312}')

I19a313 = Parameter(name = 'I19a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5',
                    texname = '\\text{I19a313}')

I19a314 = Parameter(name = 'I19a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4',
                    texname = '\\text{I19a314}')

I19a321 = Parameter(name = 'I19a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6',
                    texname = '\\text{I19a321}')

I19a322 = Parameter(name = 'I19a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6',
                    texname = '\\text{I19a322}')

I19a323 = Parameter(name = 'I19a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5',
                    texname = '\\text{I19a323}')

I19a324 = Parameter(name = 'I19a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4',
                    texname = '\\text{I19a324}')

I19a331 = Parameter(name = 'I19a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6',
                    texname = '\\text{I19a331}')

I19a332 = Parameter(name = 'I19a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6',
                    texname = '\\text{I19a332}')

I19a333 = Parameter(name = 'I19a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5',
                    texname = '\\text{I19a333}')

I19a334 = Parameter(name = 'I19a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4',
                    texname = '\\text{I19a334}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1x1',
                  texname = '\\text{I2a11}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2x2',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3',
                  texname = '\\text{I2a33}')

I20a111 = Parameter(name = 'I20a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x1*Rd1x6',
                    texname = '\\text{I20a111}')

I20a112 = Parameter(name = 'I20a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x1*Rd2x6',
                    texname = '\\text{I20a112}')

I20a113 = Parameter(name = 'I20a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x2x1*Rd3x5',
                    texname = '\\text{I20a113}')

I20a121 = Parameter(name = 'I20a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x1*Rd1x6',
                    texname = '\\text{I20a121}')

I20a122 = Parameter(name = 'I20a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x1*Rd2x6',
                    texname = '\\text{I20a122}')

I20a123 = Parameter(name = 'I20a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x2x1*Rd3x5',
                    texname = '\\text{I20a123}')

I20a131 = Parameter(name = 'I20a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x1*Rd1x6',
                    texname = '\\text{I20a131}')

I20a132 = Parameter(name = 'I20a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x1*Rd2x6',
                    texname = '\\text{I20a132}')

I20a133 = Parameter(name = 'I20a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x2x1*Rd3x5',
                    texname = '\\text{I20a133}')

I20a211 = Parameter(name = 'I20a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x2*Rd1x6',
                    texname = '\\text{I20a211}')

I20a212 = Parameter(name = 'I20a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x2*Rd2x6',
                    texname = '\\text{I20a212}')

I20a214 = Parameter(name = 'I20a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x1x2*Rd4x4',
                    texname = '\\text{I20a214}')

I20a221 = Parameter(name = 'I20a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x2*Rd1x6',
                    texname = '\\text{I20a221}')

I20a222 = Parameter(name = 'I20a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x2*Rd2x6',
                    texname = '\\text{I20a222}')

I20a224 = Parameter(name = 'I20a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x1x2*Rd4x4',
                    texname = '\\text{I20a224}')

I20a231 = Parameter(name = 'I20a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x2*Rd1x6',
                    texname = '\\text{I20a231}')

I20a232 = Parameter(name = 'I20a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x2*Rd2x6',
                    texname = '\\text{I20a232}')

I20a234 = Parameter(name = 'I20a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x1x2*Rd4x4',
                    texname = '\\text{I20a234}')

I20a313 = Parameter(name = 'I20a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x2x3*Rd3x5',
                    texname = '\\text{I20a313}')

I20a314 = Parameter(name = 'I20a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x1x3*Rd4x4',
                    texname = '\\text{I20a314}')

I20a323 = Parameter(name = 'I20a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x2x3*Rd3x5',
                    texname = '\\text{I20a323}')

I20a324 = Parameter(name = 'I20a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x1x3*Rd4x4',
                    texname = '\\text{I20a324}')

I20a333 = Parameter(name = 'I20a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x2x3*Rd3x5',
                    texname = '\\text{I20a333}')

I20a334 = Parameter(name = 'I20a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x1x3*Rd4x4',
                    texname = '\\text{I20a334}')

I21a111 = Parameter(name = 'I21a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x1x3*Rd1x6',
                    texname = '\\text{I21a111}')

I21a112 = Parameter(name = 'I21a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x1x3*Rd2x6',
                    texname = '\\text{I21a112}')

I21a113 = Parameter(name = 'I21a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x1x2*Rd3x5',
                    texname = '\\text{I21a113}')

I21a121 = Parameter(name = 'I21a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x1x3*Rd1x6',
                    texname = '\\text{I21a121}')

I21a122 = Parameter(name = 'I21a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x1x3*Rd2x6',
                    texname = '\\text{I21a122}')

I21a123 = Parameter(name = 'I21a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x1x2*Rd3x5',
                    texname = '\\text{I21a123}')

I21a131 = Parameter(name = 'I21a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x1x3*Rd1x6',
                    texname = '\\text{I21a131}')

I21a132 = Parameter(name = 'I21a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x1x3*Rd2x6',
                    texname = '\\text{I21a132}')

I21a133 = Parameter(name = 'I21a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x1x2*Rd3x5',
                    texname = '\\text{I21a133}')

I21a211 = Parameter(name = 'I21a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x2x3*Rd1x6',
                    texname = '\\text{I21a211}')

I21a212 = Parameter(name = 'I21a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x2x3*Rd2x6',
                    texname = '\\text{I21a212}')

I21a214 = Parameter(name = 'I21a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x2x1*Rd4x4',
                    texname = '\\text{I21a214}')

I21a221 = Parameter(name = 'I21a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x2x3*Rd1x6',
                    texname = '\\text{I21a221}')

I21a222 = Parameter(name = 'I21a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x2x3*Rd2x6',
                    texname = '\\text{I21a222}')

I21a224 = Parameter(name = 'I21a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x2x1*Rd4x4',
                    texname = '\\text{I21a224}')

I21a231 = Parameter(name = 'I21a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x2x3*Rd1x6',
                    texname = '\\text{I21a231}')

I21a232 = Parameter(name = 'I21a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x2x3*Rd2x6',
                    texname = '\\text{I21a232}')

I21a234 = Parameter(name = 'I21a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x2x1*Rd4x4',
                    texname = '\\text{I21a234}')

I21a313 = Parameter(name = 'I21a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x2*Rd3x5',
                    texname = '\\text{I21a313}')

I21a314 = Parameter(name = 'I21a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD1x3x1*Rd4x4',
                    texname = '\\text{I21a314}')

I21a323 = Parameter(name = 'I21a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x2*Rd3x5',
                    texname = '\\text{I21a323}')

I21a324 = Parameter(name = 'I21a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD2x3x1*Rd4x4',
                    texname = '\\text{I21a324}')

I21a333 = Parameter(name = 'I21a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x2*Rd3x5',
                    texname = '\\text{I21a333}')

I21a334 = Parameter(name = 'I21a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LUDD3x3x1*Rd4x4',
                    texname = '\\text{I21a334}')

I22a11 = Parameter(name = 'I22a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I22a11}')

I22a12 = Parameter(name = 'I22a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I22a12}')

I22a21 = Parameter(name = 'I22a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I22a21}')

I22a22 = Parameter(name = 'I22a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I22a22}')

I22a55 = Parameter(name = 'I22a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I22a55}')

I22a66 = Parameter(name = 'I22a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I22a66}')

I23a11 = Parameter(name = 'I23a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*complexconjugate(Rd1x6)',
                   texname = '\\text{I23a11}')

I23a12 = Parameter(name = 'I23a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*complexconjugate(Rd1x6)',
                   texname = '\\text{I23a12}')

I23a21 = Parameter(name = 'I23a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*complexconjugate(Rd2x6)',
                   texname = '\\text{I23a21}')

I23a22 = Parameter(name = 'I23a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*complexconjugate(Rd2x6)',
                   texname = '\\text{I23a22}')

I23a33 = Parameter(name = 'I23a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*complexconjugate(Rd3x5)',
                   texname = '\\text{I23a33}')

I23a44 = Parameter(name = 'I23a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*complexconjugate(Rd4x4)',
                   texname = '\\text{I23a44}')

I24a11 = Parameter(name = 'I24a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd1x6)*complexconjugate(td3x3)',
                   texname = '\\text{I24a11}')

I24a12 = Parameter(name = 'I24a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd1x6)*complexconjugate(td3x3)',
                   texname = '\\text{I24a12}')

I24a21 = Parameter(name = 'I24a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd2x6)*complexconjugate(td3x3)',
                   texname = '\\text{I24a21}')

I24a22 = Parameter(name = 'I24a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd2x6)*complexconjugate(td3x3)',
                   texname = '\\text{I24a22}')

I24a35 = Parameter(name = 'I24a35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Rd3x5)*complexconjugate(td2x2)',
                   texname = '\\text{I24a35}')

I24a46 = Parameter(name = 'I24a46',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Rd4x4)*complexconjugate(td1x1)',
                   texname = '\\text{I24a46}')

I25a11 = Parameter(name = 'I25a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I25a11}')

I25a12 = Parameter(name = 'I25a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I25a12}')

I25a21 = Parameter(name = 'I25a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I25a21}')

I25a22 = Parameter(name = 'I25a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I25a22}')

I25a35 = Parameter(name = 'I25a35',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                   texname = '\\text{I25a35}')

I25a46 = Parameter(name = 'I25a46',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                   texname = '\\text{I25a46}')

I26a11 = Parameter(name = 'I26a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*td3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I26a11}')

I26a12 = Parameter(name = 'I26a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*td3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I26a12}')

I26a21 = Parameter(name = 'I26a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*td3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I26a21}')

I26a22 = Parameter(name = 'I26a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*td3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I26a22}')

I26a53 = Parameter(name = 'I26a53',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*td2x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I26a53}')

I26a64 = Parameter(name = 'I26a64',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*td1x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I26a64}')

I27a11 = Parameter(name = 'I27a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yd3x3*complexconjugate(Rd1x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I27a11}')

I27a12 = Parameter(name = 'I27a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yd3x3*complexconjugate(Rd1x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I27a12}')

I27a21 = Parameter(name = 'I27a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yd3x3*complexconjugate(Rd2x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I27a21}')

I27a22 = Parameter(name = 'I27a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yd3x3*complexconjugate(Rd2x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I27a22}')

I27a55 = Parameter(name = 'I27a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*yd2x2*complexconjugate(Rd5x2)*complexconjugate(yd2x2)',
                   texname = '\\text{I27a55}')

I27a66 = Parameter(name = 'I27a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*yd1x1*complexconjugate(Rd6x1)*complexconjugate(yd1x1)',
                   texname = '\\text{I27a66}')

I28a11 = Parameter(name = 'I28a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I28a11}')

I28a12 = Parameter(name = 'I28a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I28a12}')

I28a21 = Parameter(name = 'I28a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I28a21}')

I28a22 = Parameter(name = 'I28a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I28a22}')

I28a53 = Parameter(name = 'I28a53',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I28a53}')

I28a64 = Parameter(name = 'I28a64',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I28a64}')

I29a11 = Parameter(name = 'I29a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I29a11}')

I29a12 = Parameter(name = 'I29a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I29a12}')

I29a21 = Parameter(name = 'I29a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I29a21}')

I29a22 = Parameter(name = 'I29a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                   texname = '\\text{I29a22}')

I29a33 = Parameter(name = 'I29a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2*complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                   texname = '\\text{I29a33}')

I29a44 = Parameter(name = 'I29a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1*complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                   texname = '\\text{I29a44}')

I3a14 = Parameter(name = 'I3a14',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd4x4)*complexconjugate(yd1x1)',
                  texname = '\\text{I3a14}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd3x5)*complexconjugate(yd2x2)',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd1x6)*complexconjugate(yd3x3)',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(Rd2x6)*complexconjugate(yd3x3)',
                  texname = '\\text{I3a32}')

I30a11 = Parameter(name = 'I30a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(yd1x1)',
                   texname = '\\text{I30a11}')

I30a22 = Parameter(name = 'I30a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(yd2x2)',
                   texname = '\\text{I30a22}')

I30a33 = Parameter(name = 'I30a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(yd3x3)',
                   texname = '\\text{I30a33}')

I31a11 = Parameter(name = 'I31a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1',
                   texname = '\\text{I31a11}')

I31a22 = Parameter(name = 'I31a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2',
                   texname = '\\text{I31a22}')

I31a33 = Parameter(name = 'I31a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3',
                   texname = '\\text{I31a33}')

I32a11 = Parameter(name = 'I32a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye1x1)',
                   texname = '\\text{I32a11}')

I32a22 = Parameter(name = 'I32a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye2x2)',
                   texname = '\\text{I32a22}')

I32a33 = Parameter(name = 'I32a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(ye3x3)',
                   texname = '\\text{I32a33}')

I33a13 = Parameter(name = 'I33a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl3x4)*complexconjugate(ye1x1)',
                   texname = '\\text{I33a13}')

I33a22 = Parameter(name = 'I33a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl2x5)*complexconjugate(ye2x2)',
                   texname = '\\text{I33a22}')

I33a31 = Parameter(name = 'I33a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I33a31}')

I33a36 = Parameter(name = 'I33a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I33a36}')

I34a14 = Parameter(name = 'I34a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye1x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I34a14}')

I34a25 = Parameter(name = 'I34a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye2x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I34a25}')

I34a31 = Parameter(name = 'I34a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I34a31}')

I34a36 = Parameter(name = 'I34a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I34a36}')

I35a111 = Parameter(name = 'I35a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a111}')

I35a115 = Parameter(name = 'I35a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x1*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a115}')

I35a116 = Parameter(name = 'I35a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a116}')

I35a121 = Parameter(name = 'I35a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a121}')

I35a124 = Parameter(name = 'I35a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a124}')

I35a126 = Parameter(name = 'I35a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a126}')

I35a134 = Parameter(name = 'I35a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a134}')

I35a135 = Parameter(name = 'I35a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x1*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a135}')

I35a211 = Parameter(name = 'I35a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a211}')

I35a215 = Parameter(name = 'I35a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a215}')

I35a216 = Parameter(name = 'I35a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a216}')

I35a221 = Parameter(name = 'I35a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a221}')

I35a224 = Parameter(name = 'I35a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x2*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a224}')

I35a226 = Parameter(name = 'I35a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a226}')

I35a234 = Parameter(name = 'I35a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x2*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a234}')

I35a235 = Parameter(name = 'I35a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a235}')

I35a311 = Parameter(name = 'I35a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a311}')

I35a315 = Parameter(name = 'I35a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a315}')

I35a316 = Parameter(name = 'I35a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a316}')

I35a321 = Parameter(name = 'I35a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I35a321}')

I35a324 = Parameter(name = 'I35a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a324}')

I35a326 = Parameter(name = 'I35a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I35a326}')

I35a334 = Parameter(name = 'I35a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*complexconjugate(Rl4x1)',
                    texname = '\\text{I35a334}')

I35a335 = Parameter(name = 'I35a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*complexconjugate(Rl5x2)',
                    texname = '\\text{I35a335}')

I36a111 = Parameter(name = 'I36a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a111}')

I36a114 = Parameter(name = 'I36a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a114}')

I36a115 = Parameter(name = 'I36a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a115}')

I36a116 = Parameter(name = 'I36a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a116}')

I36a121 = Parameter(name = 'I36a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a121}')

I36a124 = Parameter(name = 'I36a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a124}')

I36a125 = Parameter(name = 'I36a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a125}')

I36a126 = Parameter(name = 'I36a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a126}')

I36a131 = Parameter(name = 'I36a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a131}')

I36a134 = Parameter(name = 'I36a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a134}')

I36a135 = Parameter(name = 'I36a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a135}')

I36a136 = Parameter(name = 'I36a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a136}')

I36a211 = Parameter(name = 'I36a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a211}')

I36a214 = Parameter(name = 'I36a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a214}')

I36a215 = Parameter(name = 'I36a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a215}')

I36a216 = Parameter(name = 'I36a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a216}')

I36a221 = Parameter(name = 'I36a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a221}')

I36a224 = Parameter(name = 'I36a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a224}')

I36a225 = Parameter(name = 'I36a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a225}')

I36a226 = Parameter(name = 'I36a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a226}')

I36a231 = Parameter(name = 'I36a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a231}')

I36a234 = Parameter(name = 'I36a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a234}')

I36a235 = Parameter(name = 'I36a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a235}')

I36a236 = Parameter(name = 'I36a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a236}')

I36a311 = Parameter(name = 'I36a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a311}')

I36a314 = Parameter(name = 'I36a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a314}')

I36a315 = Parameter(name = 'I36a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a315}')

I36a316 = Parameter(name = 'I36a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a316}')

I36a321 = Parameter(name = 'I36a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a321}')

I36a324 = Parameter(name = 'I36a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a324}')

I36a325 = Parameter(name = 'I36a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a325}')

I36a326 = Parameter(name = 'I36a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a326}')

I36a331 = Parameter(name = 'I36a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*complexconjugate(Rl1x3)',
                    texname = '\\text{I36a331}')

I36a334 = Parameter(name = 'I36a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*complexconjugate(Rl4x1)',
                    texname = '\\text{I36a334}')

I36a335 = Parameter(name = 'I36a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*complexconjugate(Rl5x2)',
                    texname = '\\text{I36a335}')

I36a336 = Parameter(name = 'I36a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*complexconjugate(Rl6x3)',
                    texname = '\\text{I36a336}')

I37a121 = Parameter(name = 'I37a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x1x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a121}')

I37a122 = Parameter(name = 'I37a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x1x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a122}')

I37a123 = Parameter(name = 'I37a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x1x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a123}')

I37a126 = Parameter(name = 'I37a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x1x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a126}')

I37a131 = Parameter(name = 'I37a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x1x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a131}')

I37a132 = Parameter(name = 'I37a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x1x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a132}')

I37a133 = Parameter(name = 'I37a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x1x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a133}')

I37a136 = Parameter(name = 'I37a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x1x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a136}')

I37a211 = Parameter(name = 'I37a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x2x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a211}')

I37a212 = Parameter(name = 'I37a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x2x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a212}')

I37a213 = Parameter(name = 'I37a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x2x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a213}')

I37a216 = Parameter(name = 'I37a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x2x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a216}')

I37a231 = Parameter(name = 'I37a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x2x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a231}')

I37a232 = Parameter(name = 'I37a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x2x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a232}')

I37a233 = Parameter(name = 'I37a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x2x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a233}')

I37a236 = Parameter(name = 'I37a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE3x2x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a236}')

I37a311 = Parameter(name = 'I37a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a311}')

I37a312 = Parameter(name = 'I37a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a312}')

I37a313 = Parameter(name = 'I37a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a313}')

I37a316 = Parameter(name = 'I37a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE1x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a316}')

I37a321 = Parameter(name = 'I37a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I37a321}')

I37a322 = Parameter(name = 'I37a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I37a322}')

I37a323 = Parameter(name = 'I37a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I37a323}')

I37a326 = Parameter(name = 'I37a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LLLE2x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I37a326}')

I38a11 = Parameter(name = 'I38a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I38a11}')

I38a16 = Parameter(name = 'I38a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I38a16}')

I38a44 = Parameter(name = 'I38a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I38a44}')

I38a55 = Parameter(name = 'I38a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I38a55}')

I38a61 = Parameter(name = 'I38a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I38a61}')

I38a66 = Parameter(name = 'I38a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I38a66}')

I39a11 = Parameter(name = 'I39a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*complexconjugate(Rl1x6)',
                   texname = '\\text{I39a11}')

I39a16 = Parameter(name = 'I39a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl1x6)',
                   texname = '\\text{I39a16}')

I39a22 = Parameter(name = 'I39a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*complexconjugate(Rl2x5)',
                   texname = '\\text{I39a22}')

I39a33 = Parameter(name = 'I39a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*complexconjugate(Rl3x4)',
                   texname = '\\text{I39a33}')

I39a61 = Parameter(name = 'I39a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I39a61}')

I39a66 = Parameter(name = 'I39a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I39a66}')

I4a16 = Parameter(name = 'I4a16',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd1x1*complexconjugate(Rd6x1)',
                  texname = '\\text{I4a16}')

I4a25 = Parameter(name = 'I4a25',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd2x2*complexconjugate(Rd5x2)',
                  texname = '\\text{I4a25}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3*complexconjugate(Rd1x3)',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yd3x3*complexconjugate(Rd2x3)',
                  texname = '\\text{I4a32}')

I40a14 = Parameter(name = 'I40a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(ye1x1)',
                   texname = '\\text{I40a14}')

I40a25 = Parameter(name = 'I40a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(ye2x2)',
                   texname = '\\text{I40a25}')

I40a31 = Parameter(name = 'I40a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(ye3x3)',
                   texname = '\\text{I40a31}')

I40a36 = Parameter(name = 'I40a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(ye3x3)',
                   texname = '\\text{I40a36}')

I41a13 = Parameter(name = 'I41a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*ye1x1',
                   texname = '\\text{I41a13}')

I41a22 = Parameter(name = 'I41a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*ye2x2',
                   texname = '\\text{I41a22}')

I41a31 = Parameter(name = 'I41a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3',
                   texname = '\\text{I41a31}')

I41a36 = Parameter(name = 'I41a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I41a36}')

I42a14 = Parameter(name = 'I42a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1',
                   texname = '\\text{I42a14}')

I42a25 = Parameter(name = 'I42a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2',
                   texname = '\\text{I42a25}')

I42a31 = Parameter(name = 'I42a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3',
                   texname = '\\text{I42a31}')

I42a36 = Parameter(name = 'I42a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3',
                   texname = '\\text{I42a36}')

I43a13 = Parameter(name = 'I43a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*ye1x1',
                   texname = '\\text{I43a13}')

I43a22 = Parameter(name = 'I43a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*ye2x2',
                   texname = '\\text{I43a22}')

I43a31 = Parameter(name = 'I43a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3',
                   texname = '\\text{I43a31}')

I43a36 = Parameter(name = 'I43a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3',
                   texname = '\\text{I43a36}')

I44a111 = Parameter(name = 'I44a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE1x3x1)',
                    texname = '\\text{I44a111}')

I44a115 = Parameter(name = 'I44a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE1x2x1)',
                    texname = '\\text{I44a115}')

I44a116 = Parameter(name = 'I44a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE1x3x1)',
                    texname = '\\text{I44a116}')

I44a121 = Parameter(name = 'I44a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE1x3x2)',
                    texname = '\\text{I44a121}')

I44a125 = Parameter(name = 'I44a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE1x2x2)',
                    texname = '\\text{I44a125}')

I44a126 = Parameter(name = 'I44a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE1x3x2)',
                    texname = '\\text{I44a126}')

I44a131 = Parameter(name = 'I44a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE1x3x3)',
                    texname = '\\text{I44a131}')

I44a135 = Parameter(name = 'I44a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE1x2x3)',
                    texname = '\\text{I44a135}')

I44a136 = Parameter(name = 'I44a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE1x3x3)',
                    texname = '\\text{I44a136}')

I44a211 = Parameter(name = 'I44a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE2x3x1)',
                    texname = '\\text{I44a211}')

I44a214 = Parameter(name = 'I44a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE2x1x1)',
                    texname = '\\text{I44a214}')

I44a216 = Parameter(name = 'I44a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE2x3x1)',
                    texname = '\\text{I44a216}')

I44a221 = Parameter(name = 'I44a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE2x3x2)',
                    texname = '\\text{I44a221}')

I44a224 = Parameter(name = 'I44a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE2x1x2)',
                    texname = '\\text{I44a224}')

I44a226 = Parameter(name = 'I44a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE2x3x2)',
                    texname = '\\text{I44a226}')

I44a231 = Parameter(name = 'I44a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLLE2x3x3)',
                    texname = '\\text{I44a231}')

I44a234 = Parameter(name = 'I44a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE2x1x3)',
                    texname = '\\text{I44a234}')

I44a236 = Parameter(name = 'I44a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLLE2x3x3)',
                    texname = '\\text{I44a236}')

I44a314 = Parameter(name = 'I44a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE3x1x1)',
                    texname = '\\text{I44a314}')

I44a315 = Parameter(name = 'I44a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE3x2x1)',
                    texname = '\\text{I44a315}')

I44a324 = Parameter(name = 'I44a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE3x1x2)',
                    texname = '\\text{I44a324}')

I44a325 = Parameter(name = 'I44a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE3x2x2)',
                    texname = '\\text{I44a325}')

I44a334 = Parameter(name = 'I44a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLLE3x1x3)',
                    texname = '\\text{I44a334}')

I44a335 = Parameter(name = 'I44a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLLE3x2x3)',
                    texname = '\\text{I44a335}')

I45a111 = Parameter(name = 'I45a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x1x1)',
                    texname = '\\text{I45a111}')

I45a114 = Parameter(name = 'I45a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x1x1)',
                    texname = '\\text{I45a114}')

I45a115 = Parameter(name = 'I45a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x1x1)',
                    texname = '\\text{I45a115}')

I45a116 = Parameter(name = 'I45a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x1x1)',
                    texname = '\\text{I45a116}')

I45a121 = Parameter(name = 'I45a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x1x2)',
                    texname = '\\text{I45a121}')

I45a124 = Parameter(name = 'I45a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x1x2)',
                    texname = '\\text{I45a124}')

I45a125 = Parameter(name = 'I45a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x1x2)',
                    texname = '\\text{I45a125}')

I45a126 = Parameter(name = 'I45a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x1x2)',
                    texname = '\\text{I45a126}')

I45a131 = Parameter(name = 'I45a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x1x3)',
                    texname = '\\text{I45a131}')

I45a134 = Parameter(name = 'I45a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x1x3)',
                    texname = '\\text{I45a134}')

I45a135 = Parameter(name = 'I45a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x1x3)',
                    texname = '\\text{I45a135}')

I45a136 = Parameter(name = 'I45a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x1x3)',
                    texname = '\\text{I45a136}')

I45a211 = Parameter(name = 'I45a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x2x1)',
                    texname = '\\text{I45a211}')

I45a214 = Parameter(name = 'I45a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x2x1)',
                    texname = '\\text{I45a214}')

I45a215 = Parameter(name = 'I45a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x2x1)',
                    texname = '\\text{I45a215}')

I45a216 = Parameter(name = 'I45a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x2x1)',
                    texname = '\\text{I45a216}')

I45a221 = Parameter(name = 'I45a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x2x2)',
                    texname = '\\text{I45a221}')

I45a224 = Parameter(name = 'I45a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x2x2)',
                    texname = '\\text{I45a224}')

I45a225 = Parameter(name = 'I45a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x2x2)',
                    texname = '\\text{I45a225}')

I45a226 = Parameter(name = 'I45a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x2x2)',
                    texname = '\\text{I45a226}')

I45a231 = Parameter(name = 'I45a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x2x3)',
                    texname = '\\text{I45a231}')

I45a234 = Parameter(name = 'I45a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x2x3)',
                    texname = '\\text{I45a234}')

I45a235 = Parameter(name = 'I45a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x2x3)',
                    texname = '\\text{I45a235}')

I45a236 = Parameter(name = 'I45a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x2x3)',
                    texname = '\\text{I45a236}')

I45a311 = Parameter(name = 'I45a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x3x1)',
                    texname = '\\text{I45a311}')

I45a314 = Parameter(name = 'I45a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x3x1)',
                    texname = '\\text{I45a314}')

I45a315 = Parameter(name = 'I45a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x3x1)',
                    texname = '\\text{I45a315}')

I45a316 = Parameter(name = 'I45a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x3x1)',
                    texname = '\\text{I45a316}')

I45a321 = Parameter(name = 'I45a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x3x2)',
                    texname = '\\text{I45a321}')

I45a324 = Parameter(name = 'I45a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x3x2)',
                    texname = '\\text{I45a324}')

I45a325 = Parameter(name = 'I45a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x3x2)',
                    texname = '\\text{I45a325}')

I45a326 = Parameter(name = 'I45a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x3x2)',
                    texname = '\\text{I45a326}')

I45a331 = Parameter(name = 'I45a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*complexconjugate(LLQD3x3x3)',
                    texname = '\\text{I45a331}')

I45a334 = Parameter(name = 'I45a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*complexconjugate(LLQD1x3x3)',
                    texname = '\\text{I45a334}')

I45a335 = Parameter(name = 'I45a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*complexconjugate(LLQD2x3x3)',
                    texname = '\\text{I45a335}')

I45a336 = Parameter(name = 'I45a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*complexconjugate(LLQD3x3x3)',
                    texname = '\\text{I45a336}')

I46a121 = Parameter(name = 'I46a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl1x6',
                    texname = '\\text{I46a121}')

I46a122 = Parameter(name = 'I46a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x2*Rl2x5',
                    texname = '\\text{I46a122}')

I46a123 = Parameter(name = 'I46a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x1*Rl3x4',
                    texname = '\\text{I46a123}')

I46a126 = Parameter(name = 'I46a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl6x6',
                    texname = '\\text{I46a126}')

I46a131 = Parameter(name = 'I46a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl1x6',
                    texname = '\\text{I46a131}')

I46a132 = Parameter(name = 'I46a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x2*Rl2x5',
                    texname = '\\text{I46a132}')

I46a133 = Parameter(name = 'I46a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x1*Rl3x4',
                    texname = '\\text{I46a133}')

I46a136 = Parameter(name = 'I46a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl6x6',
                    texname = '\\text{I46a136}')

I46a211 = Parameter(name = 'I46a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl1x6',
                    texname = '\\text{I46a211}')

I46a212 = Parameter(name = 'I46a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x2*Rl2x5',
                    texname = '\\text{I46a212}')

I46a213 = Parameter(name = 'I46a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x1*Rl3x4',
                    texname = '\\text{I46a213}')

I46a216 = Parameter(name = 'I46a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl6x6',
                    texname = '\\text{I46a216}')

I46a231 = Parameter(name = 'I46a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl1x6',
                    texname = '\\text{I46a231}')

I46a232 = Parameter(name = 'I46a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x2*Rl2x5',
                    texname = '\\text{I46a232}')

I46a233 = Parameter(name = 'I46a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x1*Rl3x4',
                    texname = '\\text{I46a233}')

I46a236 = Parameter(name = 'I46a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl6x6',
                    texname = '\\text{I46a236}')

I46a311 = Parameter(name = 'I46a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl1x6',
                    texname = '\\text{I46a311}')

I46a312 = Parameter(name = 'I46a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*Rl2x5',
                    texname = '\\text{I46a312}')

I46a313 = Parameter(name = 'I46a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*Rl3x4',
                    texname = '\\text{I46a313}')

I46a316 = Parameter(name = 'I46a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl6x6',
                    texname = '\\text{I46a316}')

I46a321 = Parameter(name = 'I46a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl1x6',
                    texname = '\\text{I46a321}')

I46a322 = Parameter(name = 'I46a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*Rl2x5',
                    texname = '\\text{I46a322}')

I46a323 = Parameter(name = 'I46a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*Rl3x4',
                    texname = '\\text{I46a323}')

I46a326 = Parameter(name = 'I46a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl6x6',
                    texname = '\\text{I46a326}')

I47a11 = Parameter(name = 'I47a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I47a11}')

I47a16 = Parameter(name = 'I47a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I47a16}')

I47a44 = Parameter(name = 'I47a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I47a44}')

I47a55 = Parameter(name = 'I47a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I47a55}')

I47a61 = Parameter(name = 'I47a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I47a61}')

I47a66 = Parameter(name = 'I47a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I47a66}')

I48a11 = Parameter(name = 'I48a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*complexconjugate(Rl1x6)',
                   texname = '\\text{I48a11}')

I48a16 = Parameter(name = 'I48a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl1x6)',
                   texname = '\\text{I48a16}')

I48a22 = Parameter(name = 'I48a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*complexconjugate(Rl2x5)',
                   texname = '\\text{I48a22}')

I48a33 = Parameter(name = 'I48a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*complexconjugate(Rl3x4)',
                   texname = '\\text{I48a33}')

I48a61 = Parameter(name = 'I48a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I48a61}')

I48a66 = Parameter(name = 'I48a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*complexconjugate(Rl6x6)',
                   texname = '\\text{I48a66}')

I49a11 = Parameter(name = 'I49a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl1x6)*complexconjugate(te3x3)',
                   texname = '\\text{I49a11}')

I49a16 = Parameter(name = 'I49a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl1x6)*complexconjugate(te3x3)',
                   texname = '\\text{I49a16}')

I49a25 = Parameter(name = 'I49a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(Rl2x5)*complexconjugate(te2x2)',
                   texname = '\\text{I49a25}')

I49a34 = Parameter(name = 'I49a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(Rl3x4)*complexconjugate(te1x1)',
                   texname = '\\text{I49a34}')

I49a61 = Parameter(name = 'I49a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I49a61}')

I49a66 = Parameter(name = 'I49a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I49a66}')

I5a111 = Parameter(name = 'I5a111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x1*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a111}')

I5a112 = Parameter(name = 'I5a112',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x1*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a112}')

I5a115 = Parameter(name = 'I5a115',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x2x1*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a115}')

I5a116 = Parameter(name = 'I5a116',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x1x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a116}')

I5a121 = Parameter(name = 'I5a121',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x1*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a121}')

I5a122 = Parameter(name = 'I5a122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x1*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a122}')

I5a125 = Parameter(name = 'I5a125',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x2x1*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a125}')

I5a126 = Parameter(name = 'I5a126',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x1x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a126}')

I5a131 = Parameter(name = 'I5a131',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x1*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a131}')

I5a132 = Parameter(name = 'I5a132',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x1*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a132}')

I5a135 = Parameter(name = 'I5a135',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x2x1*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a135}')

I5a136 = Parameter(name = 'I5a136',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x1x1*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a136}')

I5a211 = Parameter(name = 'I5a211',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x2*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a211}')

I5a212 = Parameter(name = 'I5a212',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x2*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a212}')

I5a215 = Parameter(name = 'I5a215',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x2x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a215}')

I5a216 = Parameter(name = 'I5a216',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x1x2*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a216}')

I5a221 = Parameter(name = 'I5a221',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x2*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a221}')

I5a222 = Parameter(name = 'I5a222',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x2*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a222}')

I5a225 = Parameter(name = 'I5a225',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x2x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a225}')

I5a226 = Parameter(name = 'I5a226',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x1x2*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a226}')

I5a231 = Parameter(name = 'I5a231',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x2*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a231}')

I5a232 = Parameter(name = 'I5a232',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x2*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a232}')

I5a235 = Parameter(name = 'I5a235',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x2x2*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a235}')

I5a236 = Parameter(name = 'I5a236',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x1x2*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a236}')

I5a311 = Parameter(name = 'I5a311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a311}')

I5a312 = Parameter(name = 'I5a312',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a312}')

I5a315 = Parameter(name = 'I5a315',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x2x3*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a315}')

I5a316 = Parameter(name = 'I5a316',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD1x1x3*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a316}')

I5a321 = Parameter(name = 'I5a321',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a321}')

I5a322 = Parameter(name = 'I5a322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a322}')

I5a325 = Parameter(name = 'I5a325',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x2x3*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a325}')

I5a326 = Parameter(name = 'I5a326',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD2x1x3*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a326}')

I5a331 = Parameter(name = 'I5a331',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x3*complexconjugate(Rd1x3)',
                   texname = '\\text{I5a331}')

I5a332 = Parameter(name = 'I5a332',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x3x3*complexconjugate(Rd2x3)',
                   texname = '\\text{I5a332}')

I5a335 = Parameter(name = 'I5a335',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x2x3*complexconjugate(Rd5x2)',
                   texname = '\\text{I5a335}')

I5a336 = Parameter(name = 'I5a336',
                   nature = 'internal',
                   type = 'complex',
                   value = 'LLQD3x1x3*complexconjugate(Rd6x1)',
                   texname = '\\text{I5a336}')

I50a11 = Parameter(name = 'I50a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I50a11}')

I50a16 = Parameter(name = 'I50a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I50a16}')

I50a25 = Parameter(name = 'I50a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(Rl2x5)*complexconjugate(ye2x2)',
                   texname = '\\text{I50a25}')

I50a34 = Parameter(name = 'I50a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(Rl3x4)*complexconjugate(ye1x1)',
                   texname = '\\text{I50a34}')

I50a61 = Parameter(name = 'I50a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I50a61}')

I50a66 = Parameter(name = 'I50a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I50a66}')

I51a11 = Parameter(name = 'I51a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*te3x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I51a11}')

I51a16 = Parameter(name = 'I51a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I51a16}')

I51a43 = Parameter(name = 'I51a43',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*te1x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I51a43}')

I51a52 = Parameter(name = 'I51a52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*te2x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I51a52}')

I51a61 = Parameter(name = 'I51a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I51a61}')

I51a66 = Parameter(name = 'I51a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I51a66}')

I52a11 = Parameter(name = 'I52a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*ye3x3*complexconjugate(Rl1x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I52a11}')

I52a16 = Parameter(name = 'I52a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl1x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I52a16}')

I52a44 = Parameter(name = 'I52a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*ye1x1*complexconjugate(Rl4x1)*complexconjugate(ye1x1)',
                   texname = '\\text{I52a44}')

I52a55 = Parameter(name = 'I52a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*ye2x2*complexconjugate(Rl5x2)*complexconjugate(ye2x2)',
                   texname = '\\text{I52a55}')

I52a61 = Parameter(name = 'I52a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I52a61}')

I52a66 = Parameter(name = 'I52a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I52a66}')

I53a11 = Parameter(name = 'I53a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I53a11}')

I53a16 = Parameter(name = 'I53a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I53a16}')

I53a43 = Parameter(name = 'I53a43',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*ye1x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I53a43}')

I53a52 = Parameter(name = 'I53a52',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*ye2x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I53a52}')

I53a61 = Parameter(name = 'I53a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I53a61}')

I53a66 = Parameter(name = 'I53a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I53a66}')

I54a11 = Parameter(name = 'I54a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3*complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I54a11}')

I54a16 = Parameter(name = 'I54a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I54a16}')

I54a22 = Parameter(name = 'I54a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*ye2x2*complexconjugate(Rl2x5)*complexconjugate(ye2x2)',
                   texname = '\\text{I54a22}')

I54a33 = Parameter(name = 'I54a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*ye1x1*complexconjugate(Rl3x4)*complexconjugate(ye1x1)',
                   texname = '\\text{I54a33}')

I54a61 = Parameter(name = 'I54a61',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I54a61}')

I54a66 = Parameter(name = 'I54a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I54a66}')

I55a111 = Parameter(name = 'I55a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x1*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a111}')

I55a112 = Parameter(name = 'I55a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x1*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a112}')

I55a121 = Parameter(name = 'I55a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x1*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a121}')

I55a123 = Parameter(name = 'I55a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a123}')

I55a132 = Parameter(name = 'I55a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a132}')

I55a133 = Parameter(name = 'I55a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a133}')

I55a211 = Parameter(name = 'I55a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x2*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a211}')

I55a212 = Parameter(name = 'I55a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a212}')

I55a221 = Parameter(name = 'I55a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x2*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a221}')

I55a223 = Parameter(name = 'I55a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x2*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a223}')

I55a232 = Parameter(name = 'I55a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a232}')

I55a233 = Parameter(name = 'I55a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a233}')

I55a311 = Parameter(name = 'I55a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a311}')

I55a312 = Parameter(name = 'I55a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a312}')

I55a321 = Parameter(name = 'I55a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I55a321}')

I55a323 = Parameter(name = 'I55a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a323}')

I55a332 = Parameter(name = 'I55a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*complexconjugate(Rn2x2)',
                    texname = '\\text{I55a332}')

I55a333 = Parameter(name = 'I55a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*complexconjugate(Rn3x1)',
                    texname = '\\text{I55a333}')

I56a111 = Parameter(name = 'I56a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a111}')

I56a112 = Parameter(name = 'I56a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a112}')

I56a113 = Parameter(name = 'I56a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a113}')

I56a121 = Parameter(name = 'I56a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a121}')

I56a122 = Parameter(name = 'I56a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a122}')

I56a123 = Parameter(name = 'I56a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a123}')

I56a131 = Parameter(name = 'I56a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a131}')

I56a132 = Parameter(name = 'I56a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a132}')

I56a133 = Parameter(name = 'I56a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a133}')

I56a211 = Parameter(name = 'I56a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a211}')

I56a212 = Parameter(name = 'I56a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a212}')

I56a213 = Parameter(name = 'I56a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a213}')

I56a221 = Parameter(name = 'I56a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a221}')

I56a222 = Parameter(name = 'I56a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a222}')

I56a223 = Parameter(name = 'I56a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a223}')

I56a231 = Parameter(name = 'I56a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a231}')

I56a232 = Parameter(name = 'I56a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a232}')

I56a233 = Parameter(name = 'I56a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a233}')

I56a311 = Parameter(name = 'I56a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a311}')

I56a312 = Parameter(name = 'I56a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a312}')

I56a313 = Parameter(name = 'I56a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a313}')

I56a321 = Parameter(name = 'I56a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a321}')

I56a322 = Parameter(name = 'I56a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a322}')

I56a323 = Parameter(name = 'I56a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a323}')

I56a331 = Parameter(name = 'I56a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*complexconjugate(Rn1x3)',
                    texname = '\\text{I56a331}')

I56a332 = Parameter(name = 'I56a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*complexconjugate(Rn2x2)',
                    texname = '\\text{I56a332}')

I56a333 = Parameter(name = 'I56a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*complexconjugate(Rn3x1)',
                    texname = '\\text{I56a333}')

I57a11 = Parameter(name = 'I57a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I57a11}')

I57a16 = Parameter(name = 'I57a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I57a16}')

I57a25 = Parameter(name = 'I57a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I57a25}')

I57a34 = Parameter(name = 'I57a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*complexconjugate(Rn3x1)',
                   texname = '\\text{I57a34}')

I58a11 = Parameter(name = 'I58a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*te3x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I58a11}')

I58a16 = Parameter(name = 'I58a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*te3x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I58a16}')

I58a22 = Parameter(name = 'I58a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*te2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I58a22}')

I58a33 = Parameter(name = 'I58a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*te1x1*complexconjugate(Rn3x1)',
                   texname = '\\text{I58a33}')

I59a11 = Parameter(name = 'I59a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x3*ye3x3*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I59a11}')

I59a16 = Parameter(name = 'I59a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x3*ye3x3*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I59a16}')

I59a25 = Parameter(name = 'I59a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl5x2*ye2x2*complexconjugate(Rn2x2)*complexconjugate(ye2x2)',
                   texname = '\\text{I59a25}')

I59a34 = Parameter(name = 'I59a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl4x1*ye1x1*complexconjugate(Rn3x1)*complexconjugate(ye1x1)',
                   texname = '\\text{I59a34}')

I6a111 = Parameter(name = 'I6a111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a111}')

I6a112 = Parameter(name = 'I6a112',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a112}')

I6a113 = Parameter(name = 'I6a113',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a113}')

I6a114 = Parameter(name = 'I6a114',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a114}')

I6a121 = Parameter(name = 'I6a121',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a121}')

I6a122 = Parameter(name = 'I6a122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a122}')

I6a123 = Parameter(name = 'I6a123',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a123}')

I6a124 = Parameter(name = 'I6a124',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a124}')

I6a131 = Parameter(name = 'I6a131',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a131}')

I6a132 = Parameter(name = 'I6a132',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a132}')

I6a133 = Parameter(name = 'I6a133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a133}')

I6a134 = Parameter(name = 'I6a134',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a134}')

I6a211 = Parameter(name = 'I6a211',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a211}')

I6a212 = Parameter(name = 'I6a212',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a212}')

I6a213 = Parameter(name = 'I6a213',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a213}')

I6a214 = Parameter(name = 'I6a214',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a214}')

I6a221 = Parameter(name = 'I6a221',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a221}')

I6a222 = Parameter(name = 'I6a222',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a222}')

I6a223 = Parameter(name = 'I6a223',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a223}')

I6a224 = Parameter(name = 'I6a224',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a224}')

I6a231 = Parameter(name = 'I6a231',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a231}')

I6a232 = Parameter(name = 'I6a232',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a232}')

I6a233 = Parameter(name = 'I6a233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a233}')

I6a234 = Parameter(name = 'I6a234',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a234}')

I6a311 = Parameter(name = 'I6a311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a311}')

I6a312 = Parameter(name = 'I6a312',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a312}')

I6a313 = Parameter(name = 'I6a313',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a313}')

I6a314 = Parameter(name = 'I6a314',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a314}')

I6a321 = Parameter(name = 'I6a321',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a321}')

I6a322 = Parameter(name = 'I6a322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a322}')

I6a323 = Parameter(name = 'I6a323',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a323}')

I6a324 = Parameter(name = 'I6a324',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a324}')

I6a331 = Parameter(name = 'I6a331',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I6a331}')

I6a332 = Parameter(name = 'I6a332',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I6a332}')

I6a333 = Parameter(name = 'I6a333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I6a333}')

I6a334 = Parameter(name = 'I6a334',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I6a334}')

I60a11 = Parameter(name = 'I60a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl1x6*ye3x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I60a11}')

I60a16 = Parameter(name = 'I60a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl6x6*ye3x3*complexconjugate(Rn1x3)',
                   texname = '\\text{I60a16}')

I60a22 = Parameter(name = 'I60a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl2x5*ye2x2*complexconjugate(Rn2x2)',
                   texname = '\\text{I60a22}')

I60a33 = Parameter(name = 'I60a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rl3x4*ye1x1*complexconjugate(Rn3x1)',
                   texname = '\\text{I60a33}')

I61a111 = Parameter(name = 'I61a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a111}')

I61a112 = Parameter(name = 'I61a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a112}')

I61a115 = Parameter(name = 'I61a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a115}')

I61a116 = Parameter(name = 'I61a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a116}')

I61a121 = Parameter(name = 'I61a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a121}')

I61a122 = Parameter(name = 'I61a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a122}')

I61a125 = Parameter(name = 'I61a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a125}')

I61a126 = Parameter(name = 'I61a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a126}')

I61a151 = Parameter(name = 'I61a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x3*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a151}')

I61a152 = Parameter(name = 'I61a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x3*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a152}')

I61a155 = Parameter(name = 'I61a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd5x2*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a155}')

I61a156 = Parameter(name = 'I61a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd6x1*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a156}')

I61a161 = Parameter(name = 'I61a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x3*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a161}')

I61a162 = Parameter(name = 'I61a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x3*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a162}')

I61a165 = Parameter(name = 'I61a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd5x2*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a165}')

I61a166 = Parameter(name = 'I61a166',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd6x1*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a166}')

I61a211 = Parameter(name = 'I61a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x3*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a211}')

I61a212 = Parameter(name = 'I61a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x3*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a212}')

I61a215 = Parameter(name = 'I61a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd5x2*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a215}')

I61a216 = Parameter(name = 'I61a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd6x1*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a216}')

I61a221 = Parameter(name = 'I61a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x3*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a221}')

I61a222 = Parameter(name = 'I61a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x3*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a222}')

I61a225 = Parameter(name = 'I61a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd5x2*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a225}')

I61a226 = Parameter(name = 'I61a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd6x1*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a226}')

I61a251 = Parameter(name = 'I61a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x3*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a251}')

I61a252 = Parameter(name = 'I61a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x3*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a252}')

I61a255 = Parameter(name = 'I61a255',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd5x2*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a255}')

I61a256 = Parameter(name = 'I61a256',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd6x1*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a256}')

I61a261 = Parameter(name = 'I61a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x3*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a261}')

I61a262 = Parameter(name = 'I61a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x3*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a262}')

I61a265 = Parameter(name = 'I61a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd5x2*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a265}')

I61a266 = Parameter(name = 'I61a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd6x1*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a266}')

I61a311 = Parameter(name = 'I61a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x3*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a311}')

I61a312 = Parameter(name = 'I61a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x3*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a312}')

I61a315 = Parameter(name = 'I61a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd5x2*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a315}')

I61a316 = Parameter(name = 'I61a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd6x1*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a316}')

I61a321 = Parameter(name = 'I61a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x3*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a321}')

I61a322 = Parameter(name = 'I61a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x3*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a322}')

I61a325 = Parameter(name = 'I61a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd5x2*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a325}')

I61a326 = Parameter(name = 'I61a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd6x1*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a326}')

I61a351 = Parameter(name = 'I61a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x3*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a351}')

I61a352 = Parameter(name = 'I61a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x3*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a352}')

I61a355 = Parameter(name = 'I61a355',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd5x2*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a355}')

I61a356 = Parameter(name = 'I61a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd6x1*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a356}')

I61a361 = Parameter(name = 'I61a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x3*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a361}')

I61a362 = Parameter(name = 'I61a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x3*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I61a362}')

I61a365 = Parameter(name = 'I61a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd5x2*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I61a365}')

I61a366 = Parameter(name = 'I61a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd6x1*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I61a366}')

I62a111 = Parameter(name = 'I62a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rd1x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a111}')

I62a112 = Parameter(name = 'I62a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rd1x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a112}')

I62a113 = Parameter(name = 'I62a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rd1x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a113}')

I62a114 = Parameter(name = 'I62a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rd1x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a114}')

I62a121 = Parameter(name = 'I62a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rd2x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a121}')

I62a122 = Parameter(name = 'I62a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rd2x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a122}')

I62a123 = Parameter(name = 'I62a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rd2x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a123}')

I62a124 = Parameter(name = 'I62a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rd2x6)*complexconjugate(Rn1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a124}')

I62a131 = Parameter(name = 'I62a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6*complexconjugate(Rd3x5)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a131}')

I62a132 = Parameter(name = 'I62a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6*complexconjugate(Rd3x5)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a132}')

I62a133 = Parameter(name = 'I62a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5*complexconjugate(Rd3x5)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a133}')

I62a134 = Parameter(name = 'I62a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4*complexconjugate(Rd3x5)*complexconjugate(Rn1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a134}')

I62a141 = Parameter(name = 'I62a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6*complexconjugate(Rd4x4)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a141}')

I62a142 = Parameter(name = 'I62a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6*complexconjugate(Rd4x4)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a142}')

I62a143 = Parameter(name = 'I62a143',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5*complexconjugate(Rd4x4)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a143}')

I62a144 = Parameter(name = 'I62a144',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4*complexconjugate(Rd4x4)*complexconjugate(Rn1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a144}')

I62a211 = Parameter(name = 'I62a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rd1x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a211}')

I62a212 = Parameter(name = 'I62a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rd1x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a212}')

I62a213 = Parameter(name = 'I62a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rd1x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a213}')

I62a214 = Parameter(name = 'I62a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rd1x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a214}')

I62a221 = Parameter(name = 'I62a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rd2x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a221}')

I62a222 = Parameter(name = 'I62a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rd2x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a222}')

I62a223 = Parameter(name = 'I62a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rd2x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a223}')

I62a224 = Parameter(name = 'I62a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rd2x6)*complexconjugate(Rn2x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a224}')

I62a231 = Parameter(name = 'I62a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x6*complexconjugate(Rd3x5)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a231}')

I62a232 = Parameter(name = 'I62a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x6*complexconjugate(Rd3x5)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a232}')

I62a233 = Parameter(name = 'I62a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd3x5*complexconjugate(Rd3x5)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a233}')

I62a234 = Parameter(name = 'I62a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd4x4*complexconjugate(Rd3x5)*complexconjugate(Rn2x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a234}')

I62a241 = Parameter(name = 'I62a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x6*complexconjugate(Rd4x4)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a241}')

I62a242 = Parameter(name = 'I62a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x6*complexconjugate(Rd4x4)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a242}')

I62a243 = Parameter(name = 'I62a243',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd3x5*complexconjugate(Rd4x4)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a243}')

I62a244 = Parameter(name = 'I62a244',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd4x4*complexconjugate(Rd4x4)*complexconjugate(Rn2x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a244}')

I62a311 = Parameter(name = 'I62a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rd1x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a311}')

I62a312 = Parameter(name = 'I62a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rd1x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a312}')

I62a313 = Parameter(name = 'I62a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rd1x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a313}')

I62a314 = Parameter(name = 'I62a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rd1x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a314}')

I62a321 = Parameter(name = 'I62a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rd2x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a321}')

I62a322 = Parameter(name = 'I62a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rd2x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a322}')

I62a323 = Parameter(name = 'I62a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rd2x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a323}')

I62a324 = Parameter(name = 'I62a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rd2x6)*complexconjugate(Rn3x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I62a324}')

I62a331 = Parameter(name = 'I62a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x6*complexconjugate(Rd3x5)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a331}')

I62a332 = Parameter(name = 'I62a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x6*complexconjugate(Rd3x5)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a332}')

I62a333 = Parameter(name = 'I62a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd3x5*complexconjugate(Rd3x5)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a333}')

I62a334 = Parameter(name = 'I62a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd4x4*complexconjugate(Rd3x5)*complexconjugate(Rn3x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I62a334}')

I62a341 = Parameter(name = 'I62a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x6*complexconjugate(Rd4x4)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a341}')

I62a342 = Parameter(name = 'I62a342',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x6*complexconjugate(Rd4x4)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a342}')

I62a343 = Parameter(name = 'I62a343',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd3x5*complexconjugate(Rd4x4)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a343}')

I62a344 = Parameter(name = 'I62a344',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd4x4*complexconjugate(Rd4x4)*complexconjugate(Rn3x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I62a344}')

I63a111 = Parameter(name = 'I63a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a111}')

I63a112 = Parameter(name = 'I63a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a112}')

I63a113 = Parameter(name = 'I63a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a113}')

I63a114 = Parameter(name = 'I63a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rd1x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a114}')

I63a121 = Parameter(name = 'I63a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a121}')

I63a122 = Parameter(name = 'I63a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a122}')

I63a123 = Parameter(name = 'I63a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a123}')

I63a124 = Parameter(name = 'I63a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rd2x3)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a124}')

I63a151 = Parameter(name = 'I63a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a151}')

I63a152 = Parameter(name = 'I63a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a152}')

I63a153 = Parameter(name = 'I63a153',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x2x2*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a153}')

I63a154 = Parameter(name = 'I63a154',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x2x1*complexconjugate(Rd5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a154}')

I63a161 = Parameter(name = 'I63a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a161}')

I63a162 = Parameter(name = 'I63a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a162}')

I63a163 = Parameter(name = 'I63a163',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x1x2*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a163}')

I63a164 = Parameter(name = 'I63a164',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x1x1*complexconjugate(Rd6x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I63a164}')

I63a211 = Parameter(name = 'I63a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a211}')

I63a212 = Parameter(name = 'I63a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a212}')

I63a213 = Parameter(name = 'I63a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x3x2*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a213}')

I63a214 = Parameter(name = 'I63a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x3x1*complexconjugate(Rd1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a214}')

I63a221 = Parameter(name = 'I63a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a221}')

I63a222 = Parameter(name = 'I63a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a222}')

I63a223 = Parameter(name = 'I63a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x3x2*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a223}')

I63a224 = Parameter(name = 'I63a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x3x1*complexconjugate(Rd2x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a224}')

I63a251 = Parameter(name = 'I63a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a251}')

I63a252 = Parameter(name = 'I63a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a252}')

I63a253 = Parameter(name = 'I63a253',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x2x2*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a253}')

I63a254 = Parameter(name = 'I63a254',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x2x1*complexconjugate(Rd5x2)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a254}')

I63a261 = Parameter(name = 'I63a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a261}')

I63a262 = Parameter(name = 'I63a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a262}')

I63a263 = Parameter(name = 'I63a263',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x1x2*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a263}')

I63a264 = Parameter(name = 'I63a264',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x1x1*complexconjugate(Rd6x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I63a264}')

I63a311 = Parameter(name = 'I63a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a311}')

I63a312 = Parameter(name = 'I63a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x3x3*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a312}')

I63a313 = Parameter(name = 'I63a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x3x2*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a313}')

I63a314 = Parameter(name = 'I63a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x3x1*complexconjugate(Rd1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a314}')

I63a321 = Parameter(name = 'I63a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a321}')

I63a322 = Parameter(name = 'I63a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x3x3*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a322}')

I63a323 = Parameter(name = 'I63a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x3x2*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a323}')

I63a324 = Parameter(name = 'I63a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x3x1*complexconjugate(Rd2x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a324}')

I63a351 = Parameter(name = 'I63a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a351}')

I63a352 = Parameter(name = 'I63a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x2x3*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a352}')

I63a353 = Parameter(name = 'I63a353',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x2x2*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a353}')

I63a354 = Parameter(name = 'I63a354',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x2x1*complexconjugate(Rd5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a354}')

I63a361 = Parameter(name = 'I63a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a361}')

I63a362 = Parameter(name = 'I63a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x1x3*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a362}')

I63a363 = Parameter(name = 'I63a363',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x1x2*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a363}')

I63a364 = Parameter(name = 'I63a364',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x1x1*complexconjugate(Rd6x1)*complexconjugate(Rn3x1)',
                    texname = '\\text{I63a364}')

I64a141 = Parameter(name = 'I64a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl1x3*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a141}')

I64a144 = Parameter(name = 'I64a144',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x1*Rl4x1*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a144}')

I64a145 = Parameter(name = 'I64a145',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x2*Rl5x2*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a145}')

I64a146 = Parameter(name = 'I64a146',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl6x3*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a146}')

I64a151 = Parameter(name = 'I64a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl1x3*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a151}')

I64a154 = Parameter(name = 'I64a154',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x1*Rl4x1*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a154}')

I64a155 = Parameter(name = 'I64a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x2*Rl5x2*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a155}')

I64a156 = Parameter(name = 'I64a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl6x3*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a156}')

I64a211 = Parameter(name = 'I64a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl1x3*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a211}')

I64a214 = Parameter(name = 'I64a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*Rl4x1*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a214}')

I64a215 = Parameter(name = 'I64a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*Rl5x2*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a215}')

I64a216 = Parameter(name = 'I64a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl6x3*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a216}')

I64a241 = Parameter(name = 'I64a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl1x3*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a241}')

I64a244 = Parameter(name = 'I64a244',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x1*Rl4x1*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a244}')

I64a245 = Parameter(name = 'I64a245',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x2*Rl5x2*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a245}')

I64a246 = Parameter(name = 'I64a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl6x3*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a246}')

I64a261 = Parameter(name = 'I64a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl1x3*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a261}')

I64a264 = Parameter(name = 'I64a264',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*Rl4x1*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a264}')

I64a265 = Parameter(name = 'I64a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*Rl5x2*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a265}')

I64a266 = Parameter(name = 'I64a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl6x3*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a266}')

I64a311 = Parameter(name = 'I64a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl1x3*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a311}')

I64a314 = Parameter(name = 'I64a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*Rl4x1*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a314}')

I64a315 = Parameter(name = 'I64a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*Rl5x2*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a315}')

I64a316 = Parameter(name = 'I64a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl6x3*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a316}')

I64a351 = Parameter(name = 'I64a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl1x3*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a351}')

I64a354 = Parameter(name = 'I64a354',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x1*Rl4x1*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a354}')

I64a355 = Parameter(name = 'I64a355',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x2*Rl5x2*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a355}')

I64a356 = Parameter(name = 'I64a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl6x3*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a356}')

I64a361 = Parameter(name = 'I64a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl1x3*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a361}')

I64a364 = Parameter(name = 'I64a364',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*Rl4x1*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I64a364}')

I64a365 = Parameter(name = 'I64a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*Rl5x2*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I64a365}')

I64a366 = Parameter(name = 'I64a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl6x3*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I64a366}')

I65a121 = Parameter(name = 'I65a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl1x6*complexconjugate(Rl2x5)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a121}')

I65a122 = Parameter(name = 'I65a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x2*Rl2x5*complexconjugate(Rl2x5)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a122}')

I65a123 = Parameter(name = 'I65a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x1*Rl3x4*complexconjugate(Rl2x5)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a123}')

I65a126 = Parameter(name = 'I65a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x2x3*Rl6x6*complexconjugate(Rl2x5)*complexconjugate(Rn1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a126}')

I65a131 = Parameter(name = 'I65a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl1x6*complexconjugate(Rl3x4)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a131}')

I65a132 = Parameter(name = 'I65a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x2*Rl2x5*complexconjugate(Rl3x4)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a132}')

I65a133 = Parameter(name = 'I65a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x1*Rl3x4*complexconjugate(Rl3x4)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a133}')

I65a136 = Parameter(name = 'I65a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE3x1x3*Rl6x6*complexconjugate(Rl3x4)*complexconjugate(Rn1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a136}')

I65a211 = Parameter(name = 'I65a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl1x6*complexconjugate(Rl1x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a211}')

I65a212 = Parameter(name = 'I65a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*Rl2x5*complexconjugate(Rl1x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a212}')

I65a213 = Parameter(name = 'I65a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*Rl3x4*complexconjugate(Rl1x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a213}')

I65a216 = Parameter(name = 'I65a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl6x6*complexconjugate(Rl1x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a216}')

I65a231 = Parameter(name = 'I65a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl1x6*complexconjugate(Rl3x4)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a231}')

I65a232 = Parameter(name = 'I65a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x2*Rl2x5*complexconjugate(Rl3x4)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a232}')

I65a233 = Parameter(name = 'I65a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x1*Rl3x4*complexconjugate(Rl3x4)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a233}')

I65a236 = Parameter(name = 'I65a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x1x3*Rl6x6*complexconjugate(Rl3x4)*complexconjugate(Rn2x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I65a236}')

I65a261 = Parameter(name = 'I65a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl1x6*complexconjugate(Rl6x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a261}')

I65a262 = Parameter(name = 'I65a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x2*Rl2x5*complexconjugate(Rl6x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a262}')

I65a263 = Parameter(name = 'I65a263',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x1*Rl3x4*complexconjugate(Rl6x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a263}')

I65a266 = Parameter(name = 'I65a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE2x3x3*Rl6x6*complexconjugate(Rl6x6)*complexconjugate(Rn2x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a266}')

I65a311 = Parameter(name = 'I65a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl1x6*complexconjugate(Rl1x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a311}')

I65a312 = Parameter(name = 'I65a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*Rl2x5*complexconjugate(Rl1x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a312}')

I65a313 = Parameter(name = 'I65a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*Rl3x4*complexconjugate(Rl1x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a313}')

I65a316 = Parameter(name = 'I65a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl6x6*complexconjugate(Rl1x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a316}')

I65a321 = Parameter(name = 'I65a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl1x6*complexconjugate(Rl2x5)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a321}')

I65a322 = Parameter(name = 'I65a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x2*Rl2x5*complexconjugate(Rl2x5)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a322}')

I65a323 = Parameter(name = 'I65a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x1*Rl3x4*complexconjugate(Rl2x5)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a323}')

I65a326 = Parameter(name = 'I65a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x2x3*Rl6x6*complexconjugate(Rl2x5)*complexconjugate(Rn3x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I65a326}')

I65a361 = Parameter(name = 'I65a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl1x6*complexconjugate(Rl6x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a361}')

I65a362 = Parameter(name = 'I65a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x2*Rl2x5*complexconjugate(Rl6x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a362}')

I65a363 = Parameter(name = 'I65a363',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x1*Rl3x4*complexconjugate(Rl6x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a363}')

I65a366 = Parameter(name = 'I65a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLLE1x3x3*Rl6x6*complexconjugate(Rl6x6)*complexconjugate(Rn3x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I65a366}')

I66a141 = Parameter(name = 'I66a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE3x1x3*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a141}')

I66a142 = Parameter(name = 'I66a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE3x1x2*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a142}')

I66a143 = Parameter(name = 'I66a143',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE3x1x1*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a143}')

I66a146 = Parameter(name = 'I66a146',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE3x1x3*complexconjugate(Rl4x1)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a146}')

I66a151 = Parameter(name = 'I66a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE3x2x3*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a151}')

I66a152 = Parameter(name = 'I66a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE3x2x2*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a152}')

I66a153 = Parameter(name = 'I66a153',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE3x2x1*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a153}')

I66a156 = Parameter(name = 'I66a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE3x2x3*complexconjugate(Rl5x2)*complexconjugate(Rn1x3)',
                    texname = '\\text{I66a156}')

I66a211 = Parameter(name = 'I66a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE2x3x3*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a211}')

I66a212 = Parameter(name = 'I66a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE2x3x2*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a212}')

I66a213 = Parameter(name = 'I66a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE2x3x1*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a213}')

I66a216 = Parameter(name = 'I66a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE2x3x3*complexconjugate(Rl1x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a216}')

I66a241 = Parameter(name = 'I66a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE2x1x3*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a241}')

I66a242 = Parameter(name = 'I66a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE2x1x2*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a242}')

I66a243 = Parameter(name = 'I66a243',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE2x1x1*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a243}')

I66a246 = Parameter(name = 'I66a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE2x1x3*complexconjugate(Rl4x1)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a246}')

I66a261 = Parameter(name = 'I66a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE2x3x3*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a261}')

I66a262 = Parameter(name = 'I66a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE2x3x2*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a262}')

I66a263 = Parameter(name = 'I66a263',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE2x3x1*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a263}')

I66a266 = Parameter(name = 'I66a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE2x3x3*complexconjugate(Rl6x3)*complexconjugate(Rn2x2)',
                    texname = '\\text{I66a266}')

I66a311 = Parameter(name = 'I66a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE1x3x3*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a311}')

I66a312 = Parameter(name = 'I66a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE1x3x2*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a312}')

I66a313 = Parameter(name = 'I66a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE1x3x1*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a313}')

I66a316 = Parameter(name = 'I66a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE1x3x3*complexconjugate(Rl1x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a316}')

I66a351 = Parameter(name = 'I66a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE1x2x3*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a351}')

I66a352 = Parameter(name = 'I66a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE1x2x2*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a352}')

I66a353 = Parameter(name = 'I66a353',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE1x2x1*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a353}')

I66a356 = Parameter(name = 'I66a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE1x2x3*complexconjugate(Rl5x2)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a356}')

I66a361 = Parameter(name = 'I66a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*TLLE1x3x3*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a361}')

I66a362 = Parameter(name = 'I66a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*TLLE1x3x2*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a362}')

I66a363 = Parameter(name = 'I66a363',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*TLLE1x3x1*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a363}')

I66a366 = Parameter(name = 'I66a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*TLLE1x3x3*complexconjugate(Rl6x3)*complexconjugate(Rn3x1)',
                    texname = '\\text{I66a366}')

I67a13 = Parameter(name = 'I67a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1',
                   texname = '\\text{I67a13}')

I67a22 = Parameter(name = 'I67a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2',
                   texname = '\\text{I67a22}')

I67a31 = Parameter(name = 'I67a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3',
                   texname = '\\text{I67a31}')

I68a13 = Parameter(name = 'I68a13',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1*complexconjugate(ye1x1)',
                   texname = '\\text{I68a13}')

I68a22 = Parameter(name = 'I68a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(ye2x2)',
                   texname = '\\text{I68a22}')

I68a31 = Parameter(name = 'I68a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(ye3x3)',
                   texname = '\\text{I68a31}')

I69a11 = Parameter(name = 'I69a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl1x3)',
                   texname = '\\text{I69a11}')

I69a16 = Parameter(name = 'I69a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl6x3)',
                   texname = '\\text{I69a16}')

I69a25 = Parameter(name = 'I69a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl5x2)',
                   texname = '\\text{I69a25}')

I69a34 = Parameter(name = 'I69a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1*complexconjugate(Rl4x1)',
                   texname = '\\text{I69a34}')

I7a111 = Parameter(name = 'I7a111',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a111}')

I7a112 = Parameter(name = 'I7a112',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a112}')

I7a113 = Parameter(name = 'I7a113',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a113}')

I7a114 = Parameter(name = 'I7a114',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a114}')

I7a121 = Parameter(name = 'I7a121',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a121}')

I7a122 = Parameter(name = 'I7a122',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a122}')

I7a123 = Parameter(name = 'I7a123',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a123}')

I7a124 = Parameter(name = 'I7a124',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a124}')

I7a131 = Parameter(name = 'I7a131',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a131}')

I7a132 = Parameter(name = 'I7a132',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a132}')

I7a133 = Parameter(name = 'I7a133',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a133}')

I7a134 = Parameter(name = 'I7a134',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a134}')

I7a211 = Parameter(name = 'I7a211',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a211}')

I7a212 = Parameter(name = 'I7a212',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a212}')

I7a213 = Parameter(name = 'I7a213',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a213}')

I7a214 = Parameter(name = 'I7a214',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a214}')

I7a221 = Parameter(name = 'I7a221',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a221}')

I7a222 = Parameter(name = 'I7a222',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a222}')

I7a223 = Parameter(name = 'I7a223',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a223}')

I7a224 = Parameter(name = 'I7a224',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a224}')

I7a231 = Parameter(name = 'I7a231',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a231}')

I7a232 = Parameter(name = 'I7a232',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a232}')

I7a233 = Parameter(name = 'I7a233',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a233}')

I7a234 = Parameter(name = 'I7a234',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a234}')

I7a311 = Parameter(name = 'I7a311',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a311}')

I7a312 = Parameter(name = 'I7a312',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a312}')

I7a313 = Parameter(name = 'I7a313',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a313}')

I7a314 = Parameter(name = 'I7a314',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a314}')

I7a321 = Parameter(name = 'I7a321',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a321}')

I7a322 = Parameter(name = 'I7a322',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a322}')

I7a323 = Parameter(name = 'I7a323',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a323}')

I7a324 = Parameter(name = 'I7a324',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a324}')

I7a331 = Parameter(name = 'I7a331',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                   texname = '\\text{I7a331}')

I7a332 = Parameter(name = 'I7a332',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                   texname = '\\text{I7a332}')

I7a333 = Parameter(name = 'I7a333',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                   texname = '\\text{I7a333}')

I7a334 = Parameter(name = 'I7a334',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                   texname = '\\text{I7a334}')

I70a11 = Parameter(name = 'I70a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl1x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I70a11}')

I70a16 = Parameter(name = 'I70a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl6x6)*complexconjugate(ye3x3)',
                   texname = '\\text{I70a16}')

I70a22 = Parameter(name = 'I70a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl2x5)*complexconjugate(ye2x2)',
                   texname = '\\text{I70a22}')

I70a33 = Parameter(name = 'I70a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1*complexconjugate(Rl3x4)*complexconjugate(ye1x1)',
                   texname = '\\text{I70a33}')

I71a11 = Parameter(name = 'I71a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl1x6)*complexconjugate(te3x3)',
                   texname = '\\text{I71a11}')

I71a16 = Parameter(name = 'I71a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*complexconjugate(Rl6x6)*complexconjugate(te3x3)',
                   texname = '\\text{I71a16}')

I71a22 = Parameter(name = 'I71a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*complexconjugate(Rl2x5)*complexconjugate(te2x2)',
                   texname = '\\text{I71a22}')

I71a33 = Parameter(name = 'I71a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1*complexconjugate(Rl3x4)*complexconjugate(te1x1)',
                   texname = '\\text{I71a33}')

I72a11 = Parameter(name = 'I72a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*ye3x3*complexconjugate(Rl1x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I72a11}')

I72a16 = Parameter(name = 'I72a16',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn1x3*ye3x3*complexconjugate(Rl6x3)*complexconjugate(ye3x3)',
                   texname = '\\text{I72a16}')

I72a25 = Parameter(name = 'I72a25',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn2x2*ye2x2*complexconjugate(Rl5x2)*complexconjugate(ye2x2)',
                   texname = '\\text{I72a25}')

I72a34 = Parameter(name = 'I72a34',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rn3x1*ye1x1*complexconjugate(Rl4x1)*complexconjugate(ye1x1)',
                   texname = '\\text{I72a34}')

I73a111 = Parameter(name = 'I73a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x1x1)',
                    texname = '\\text{I73a111}')

I73a112 = Parameter(name = 'I73a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x1x1)',
                    texname = '\\text{I73a112}')

I73a113 = Parameter(name = 'I73a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x1x1)',
                    texname = '\\text{I73a113}')

I73a121 = Parameter(name = 'I73a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x1x2)',
                    texname = '\\text{I73a121}')

I73a122 = Parameter(name = 'I73a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x1x2)',
                    texname = '\\text{I73a122}')

I73a123 = Parameter(name = 'I73a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x1x2)',
                    texname = '\\text{I73a123}')

I73a131 = Parameter(name = 'I73a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x1x3)',
                    texname = '\\text{I73a131}')

I73a132 = Parameter(name = 'I73a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x1x3)',
                    texname = '\\text{I73a132}')

I73a133 = Parameter(name = 'I73a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x1x3)',
                    texname = '\\text{I73a133}')

I73a211 = Parameter(name = 'I73a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x2x1)',
                    texname = '\\text{I73a211}')

I73a212 = Parameter(name = 'I73a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x2x1)',
                    texname = '\\text{I73a212}')

I73a213 = Parameter(name = 'I73a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x2x1)',
                    texname = '\\text{I73a213}')

I73a221 = Parameter(name = 'I73a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x2x2)',
                    texname = '\\text{I73a221}')

I73a222 = Parameter(name = 'I73a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x2x2)',
                    texname = '\\text{I73a222}')

I73a223 = Parameter(name = 'I73a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x2x2)',
                    texname = '\\text{I73a223}')

I73a231 = Parameter(name = 'I73a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x2x3)',
                    texname = '\\text{I73a231}')

I73a232 = Parameter(name = 'I73a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x2x3)',
                    texname = '\\text{I73a232}')

I73a233 = Parameter(name = 'I73a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x2x3)',
                    texname = '\\text{I73a233}')

I73a311 = Parameter(name = 'I73a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x3x1)',
                    texname = '\\text{I73a311}')

I73a312 = Parameter(name = 'I73a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x3x1)',
                    texname = '\\text{I73a312}')

I73a313 = Parameter(name = 'I73a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x3x1)',
                    texname = '\\text{I73a313}')

I73a321 = Parameter(name = 'I73a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x3x2)',
                    texname = '\\text{I73a321}')

I73a322 = Parameter(name = 'I73a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x3x2)',
                    texname = '\\text{I73a322}')

I73a323 = Parameter(name = 'I73a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x3x2)',
                    texname = '\\text{I73a323}')

I73a331 = Parameter(name = 'I73a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLQD3x3x3)',
                    texname = '\\text{I73a331}')

I73a332 = Parameter(name = 'I73a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLQD2x3x3)',
                    texname = '\\text{I73a332}')

I73a333 = Parameter(name = 'I73a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLQD1x3x3)',
                    texname = '\\text{I73a333}')

I74a111 = Parameter(name = 'I74a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x1x1)',
                    texname = '\\text{I74a111}')

I74a112 = Parameter(name = 'I74a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x1x1)',
                    texname = '\\text{I74a112}')

I74a121 = Parameter(name = 'I74a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x1x2)',
                    texname = '\\text{I74a121}')

I74a122 = Parameter(name = 'I74a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x1x2)',
                    texname = '\\text{I74a122}')

I74a131 = Parameter(name = 'I74a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x1x3)',
                    texname = '\\text{I74a131}')

I74a132 = Parameter(name = 'I74a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x1x3)',
                    texname = '\\text{I74a132}')

I74a211 = Parameter(name = 'I74a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x2x1)',
                    texname = '\\text{I74a211}')

I74a213 = Parameter(name = 'I74a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x2x1)',
                    texname = '\\text{I74a213}')

I74a221 = Parameter(name = 'I74a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x2x2)',
                    texname = '\\text{I74a221}')

I74a223 = Parameter(name = 'I74a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x2x2)',
                    texname = '\\text{I74a223}')

I74a231 = Parameter(name = 'I74a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn1x3*complexconjugate(LLLE3x2x3)',
                    texname = '\\text{I74a231}')

I74a233 = Parameter(name = 'I74a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x2x3)',
                    texname = '\\text{I74a233}')

I74a312 = Parameter(name = 'I74a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x3x1)',
                    texname = '\\text{I74a312}')

I74a313 = Parameter(name = 'I74a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x3x1)',
                    texname = '\\text{I74a313}')

I74a322 = Parameter(name = 'I74a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x3x2)',
                    texname = '\\text{I74a322}')

I74a323 = Parameter(name = 'I74a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x3x2)',
                    texname = '\\text{I74a323}')

I74a332 = Parameter(name = 'I74a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn2x2*complexconjugate(LLLE2x3x3)',
                    texname = '\\text{I74a332}')

I74a333 = Parameter(name = 'I74a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rn3x1*complexconjugate(LLLE1x3x3)',
                    texname = '\\text{I74a333}')

I75a111 = Parameter(name = 'I75a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                    texname = '\\text{I75a111}')

I75a112 = Parameter(name = 'I75a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x3x3)',
                    texname = '\\text{I75a112}')

I75a115 = Parameter(name = 'I75a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x2x3)',
                    texname = '\\text{I75a115}')

I75a116 = Parameter(name = 'I75a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*complexconjugate(Rd1x6)*complexconjugate(TLQD3x1x3)',
                    texname = '\\text{I75a116}')

I75a121 = Parameter(name = 'I75a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                    texname = '\\text{I75a121}')

I75a122 = Parameter(name = 'I75a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x3x3)',
                    texname = '\\text{I75a122}')

I75a125 = Parameter(name = 'I75a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x2x3)',
                    texname = '\\text{I75a125}')

I75a126 = Parameter(name = 'I75a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*complexconjugate(Rd2x6)*complexconjugate(TLQD3x1x3)',
                    texname = '\\text{I75a126}')

I75a131 = Parameter(name = 'I75a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                    texname = '\\text{I75a131}')

I75a132 = Parameter(name = 'I75a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x3x2)',
                    texname = '\\text{I75a132}')

I75a135 = Parameter(name = 'I75a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x2x2)',
                    texname = '\\text{I75a135}')

I75a136 = Parameter(name = 'I75a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*complexconjugate(Rd3x5)*complexconjugate(TLQD3x1x2)',
                    texname = '\\text{I75a136}')

I75a141 = Parameter(name = 'I75a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                    texname = '\\text{I75a141}')

I75a142 = Parameter(name = 'I75a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x3x1)',
                    texname = '\\text{I75a142}')

I75a145 = Parameter(name = 'I75a145',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x2x1)',
                    texname = '\\text{I75a145}')

I75a146 = Parameter(name = 'I75a146',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*complexconjugate(Rd4x4)*complexconjugate(TLQD3x1x1)',
                    texname = '\\text{I75a146}')

I75a211 = Parameter(name = 'I75a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*complexconjugate(Rd1x6)*complexconjugate(TLQD2x3x3)',
                    texname = '\\text{I75a211}')

I75a212 = Parameter(name = 'I75a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*complexconjugate(Rd1x6)*complexconjugate(TLQD2x3x3)',
                    texname = '\\text{I75a212}')

I75a215 = Parameter(name = 'I75a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*complexconjugate(Rd1x6)*complexconjugate(TLQD2x2x3)',
                    texname = '\\text{I75a215}')

I75a216 = Parameter(name = 'I75a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*complexconjugate(Rd1x6)*complexconjugate(TLQD2x1x3)',
                    texname = '\\text{I75a216}')

I75a221 = Parameter(name = 'I75a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*complexconjugate(Rd2x6)*complexconjugate(TLQD2x3x3)',
                    texname = '\\text{I75a221}')

I75a222 = Parameter(name = 'I75a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*complexconjugate(Rd2x6)*complexconjugate(TLQD2x3x3)',
                    texname = '\\text{I75a222}')

I75a225 = Parameter(name = 'I75a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*complexconjugate(Rd2x6)*complexconjugate(TLQD2x2x3)',
                    texname = '\\text{I75a225}')

I75a226 = Parameter(name = 'I75a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*complexconjugate(Rd2x6)*complexconjugate(TLQD2x1x3)',
                    texname = '\\text{I75a226}')

I75a231 = Parameter(name = 'I75a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*complexconjugate(Rd3x5)*complexconjugate(TLQD2x3x2)',
                    texname = '\\text{I75a231}')

I75a232 = Parameter(name = 'I75a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*complexconjugate(Rd3x5)*complexconjugate(TLQD2x3x2)',
                    texname = '\\text{I75a232}')

I75a235 = Parameter(name = 'I75a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*complexconjugate(Rd3x5)*complexconjugate(TLQD2x2x2)',
                    texname = '\\text{I75a235}')

I75a236 = Parameter(name = 'I75a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*complexconjugate(Rd3x5)*complexconjugate(TLQD2x1x2)',
                    texname = '\\text{I75a236}')

I75a241 = Parameter(name = 'I75a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*complexconjugate(Rd4x4)*complexconjugate(TLQD2x3x1)',
                    texname = '\\text{I75a241}')

I75a242 = Parameter(name = 'I75a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*complexconjugate(Rd4x4)*complexconjugate(TLQD2x3x1)',
                    texname = '\\text{I75a242}')

I75a245 = Parameter(name = 'I75a245',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*complexconjugate(Rd4x4)*complexconjugate(TLQD2x2x1)',
                    texname = '\\text{I75a245}')

I75a246 = Parameter(name = 'I75a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*complexconjugate(Rd4x4)*complexconjugate(TLQD2x1x1)',
                    texname = '\\text{I75a246}')

I75a311 = Parameter(name = 'I75a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*complexconjugate(Rd1x6)*complexconjugate(TLQD1x3x3)',
                    texname = '\\text{I75a311}')

I75a312 = Parameter(name = 'I75a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*complexconjugate(Rd1x6)*complexconjugate(TLQD1x3x3)',
                    texname = '\\text{I75a312}')

I75a315 = Parameter(name = 'I75a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*complexconjugate(Rd1x6)*complexconjugate(TLQD1x2x3)',
                    texname = '\\text{I75a315}')

I75a316 = Parameter(name = 'I75a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*complexconjugate(Rd1x6)*complexconjugate(TLQD1x1x3)',
                    texname = '\\text{I75a316}')

I75a321 = Parameter(name = 'I75a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*complexconjugate(Rd2x6)*complexconjugate(TLQD1x3x3)',
                    texname = '\\text{I75a321}')

I75a322 = Parameter(name = 'I75a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*complexconjugate(Rd2x6)*complexconjugate(TLQD1x3x3)',
                    texname = '\\text{I75a322}')

I75a325 = Parameter(name = 'I75a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*complexconjugate(Rd2x6)*complexconjugate(TLQD1x2x3)',
                    texname = '\\text{I75a325}')

I75a326 = Parameter(name = 'I75a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*complexconjugate(Rd2x6)*complexconjugate(TLQD1x1x3)',
                    texname = '\\text{I75a326}')

I75a331 = Parameter(name = 'I75a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*complexconjugate(Rd3x5)*complexconjugate(TLQD1x3x2)',
                    texname = '\\text{I75a331}')

I75a332 = Parameter(name = 'I75a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*complexconjugate(Rd3x5)*complexconjugate(TLQD1x3x2)',
                    texname = '\\text{I75a332}')

I75a335 = Parameter(name = 'I75a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*complexconjugate(Rd3x5)*complexconjugate(TLQD1x2x2)',
                    texname = '\\text{I75a335}')

I75a336 = Parameter(name = 'I75a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*complexconjugate(Rd3x5)*complexconjugate(TLQD1x1x2)',
                    texname = '\\text{I75a336}')

I75a341 = Parameter(name = 'I75a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*complexconjugate(Rd4x4)*complexconjugate(TLQD1x3x1)',
                    texname = '\\text{I75a341}')

I75a342 = Parameter(name = 'I75a342',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*complexconjugate(Rd4x4)*complexconjugate(TLQD1x3x1)',
                    texname = '\\text{I75a342}')

I75a345 = Parameter(name = 'I75a345',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*complexconjugate(Rd4x4)*complexconjugate(TLQD1x2x1)',
                    texname = '\\text{I75a345}')

I75a346 = Parameter(name = 'I75a346',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*complexconjugate(Rd4x4)*complexconjugate(TLQD1x1x1)',
                    texname = '\\text{I75a346}')

I76a111 = Parameter(name = 'I76a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a111}')

I76a112 = Parameter(name = 'I76a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a112}')

I76a115 = Parameter(name = 'I76a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a115}')

I76a116 = Parameter(name = 'I76a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a116}')

I76a121 = Parameter(name = 'I76a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a121}')

I76a122 = Parameter(name = 'I76a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a122}')

I76a125 = Parameter(name = 'I76a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*yd3x3*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a125}')

I76a126 = Parameter(name = 'I76a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*yd3x3*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a126}')

I76a151 = Parameter(name = 'I76a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a151}')

I76a152 = Parameter(name = 'I76a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*yd2x2*complexconjugate(LLQD3x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a152}')

I76a155 = Parameter(name = 'I76a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*yd2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a155}')

I76a156 = Parameter(name = 'I76a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*yd2x2*complexconjugate(LLQD3x1x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a156}')

I76a161 = Parameter(name = 'I76a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn1x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a161}')

I76a162 = Parameter(name = 'I76a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn1x3*yd1x1*complexconjugate(LLQD3x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a162}')

I76a165 = Parameter(name = 'I76a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn1x3*yd1x1*complexconjugate(LLQD3x2x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a165}')

I76a166 = Parameter(name = 'I76a166',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn1x3*yd1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a166}')

I76a211 = Parameter(name = 'I76a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a211}')

I76a212 = Parameter(name = 'I76a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a212}')

I76a215 = Parameter(name = 'I76a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*yd3x3*complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a215}')

I76a216 = Parameter(name = 'I76a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*yd3x3*complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a216}')

I76a221 = Parameter(name = 'I76a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a221}')

I76a222 = Parameter(name = 'I76a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a222}')

I76a225 = Parameter(name = 'I76a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*yd3x3*complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a225}')

I76a226 = Parameter(name = 'I76a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*yd3x3*complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a226}')

I76a251 = Parameter(name = 'I76a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*yd2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a251}')

I76a252 = Parameter(name = 'I76a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*yd2x2*complexconjugate(LLQD2x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a252}')

I76a255 = Parameter(name = 'I76a255',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*yd2x2*complexconjugate(LLQD2x2x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a255}')

I76a256 = Parameter(name = 'I76a256',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*yd2x2*complexconjugate(LLQD2x1x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a256}')

I76a261 = Parameter(name = 'I76a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn2x2*yd1x1*complexconjugate(LLQD2x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a261}')

I76a262 = Parameter(name = 'I76a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn2x2*yd1x1*complexconjugate(LLQD2x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a262}')

I76a265 = Parameter(name = 'I76a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn2x2*yd1x1*complexconjugate(LLQD2x2x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a265}')

I76a266 = Parameter(name = 'I76a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn2x2*yd1x1*complexconjugate(LLQD2x1x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a266}')

I76a311 = Parameter(name = 'I76a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a311}')

I76a312 = Parameter(name = 'I76a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a312}')

I76a315 = Parameter(name = 'I76a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*yd3x3*complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a315}')

I76a316 = Parameter(name = 'I76a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*yd3x3*complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x3)',
                    texname = '\\text{I76a316}')

I76a321 = Parameter(name = 'I76a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a321}')

I76a322 = Parameter(name = 'I76a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a322}')

I76a325 = Parameter(name = 'I76a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*yd3x3*complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a325}')

I76a326 = Parameter(name = 'I76a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*yd3x3*complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x3)',
                    texname = '\\text{I76a326}')

I76a351 = Parameter(name = 'I76a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*yd2x2*complexconjugate(LLQD1x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a351}')

I76a352 = Parameter(name = 'I76a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*yd2x2*complexconjugate(LLQD1x3x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a352}')

I76a355 = Parameter(name = 'I76a355',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*yd2x2*complexconjugate(LLQD1x2x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a355}')

I76a356 = Parameter(name = 'I76a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*yd2x2*complexconjugate(LLQD1x1x2)*complexconjugate(Rd5x2)',
                    texname = '\\text{I76a356}')

I76a361 = Parameter(name = 'I76a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x3*Rn3x1*yd1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a361}')

I76a362 = Parameter(name = 'I76a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x3*Rn3x1*yd1x1*complexconjugate(LLQD1x3x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a362}')

I76a365 = Parameter(name = 'I76a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd5x2*Rn3x1*yd1x1*complexconjugate(LLQD1x2x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a365}')

I76a366 = Parameter(name = 'I76a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd6x1*Rn3x1*yd1x1*complexconjugate(LLQD1x1x1)*complexconjugate(Rd6x1)',
                    texname = '\\text{I76a366}')

I77a111 = Parameter(name = 'I77a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a111}')

I77a112 = Parameter(name = 'I77a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a112}')

I77a113 = Parameter(name = 'I77a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn1x3*yd2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a113}')

I77a114 = Parameter(name = 'I77a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn1x3*yd1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a114}')

I77a121 = Parameter(name = 'I77a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a121}')

I77a122 = Parameter(name = 'I77a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a122}')

I77a123 = Parameter(name = 'I77a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn1x3*yd2x2*complexconjugate(LLQD3x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a123}')

I77a124 = Parameter(name = 'I77a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn1x3*yd1x1*complexconjugate(LLQD3x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a124}')

I77a131 = Parameter(name = 'I77a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a131}')

I77a132 = Parameter(name = 'I77a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a132}')

I77a133 = Parameter(name = 'I77a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn1x3*yd2x2*complexconjugate(LLQD3x2x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a133}')

I77a134 = Parameter(name = 'I77a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn1x3*yd1x1*complexconjugate(LLQD3x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a134}')

I77a141 = Parameter(name = 'I77a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a141}')

I77a142 = Parameter(name = 'I77a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn1x3*yd3x3*complexconjugate(LLQD3x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a142}')

I77a143 = Parameter(name = 'I77a143',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn1x3*yd2x2*complexconjugate(LLQD3x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a143}')

I77a144 = Parameter(name = 'I77a144',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn1x3*yd1x1*complexconjugate(LLQD3x1x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a144}')

I77a211 = Parameter(name = 'I77a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a211}')

I77a212 = Parameter(name = 'I77a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a212}')

I77a213 = Parameter(name = 'I77a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn2x2*yd2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a213}')

I77a214 = Parameter(name = 'I77a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn2x2*yd1x1*complexconjugate(LLQD2x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a214}')

I77a221 = Parameter(name = 'I77a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a221}')

I77a222 = Parameter(name = 'I77a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a222}')

I77a223 = Parameter(name = 'I77a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn2x2*yd2x2*complexconjugate(LLQD2x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a223}')

I77a224 = Parameter(name = 'I77a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn2x2*yd1x1*complexconjugate(LLQD2x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a224}')

I77a231 = Parameter(name = 'I77a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a231}')

I77a232 = Parameter(name = 'I77a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a232}')

I77a233 = Parameter(name = 'I77a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn2x2*yd2x2*complexconjugate(LLQD2x2x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a233}')

I77a234 = Parameter(name = 'I77a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn2x2*yd1x1*complexconjugate(LLQD2x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a234}')

I77a241 = Parameter(name = 'I77a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a241}')

I77a242 = Parameter(name = 'I77a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn2x2*yd3x3*complexconjugate(LLQD2x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a242}')

I77a243 = Parameter(name = 'I77a243',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn2x2*yd2x2*complexconjugate(LLQD2x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a243}')

I77a244 = Parameter(name = 'I77a244',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn2x2*yd1x1*complexconjugate(LLQD2x1x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a244}')

I77a311 = Parameter(name = 'I77a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a311}')

I77a312 = Parameter(name = 'I77a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a312}')

I77a313 = Parameter(name = 'I77a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn3x1*yd2x2*complexconjugate(LLQD1x2x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a313}')

I77a314 = Parameter(name = 'I77a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn3x1*yd1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd1x6)',
                    texname = '\\text{I77a314}')

I77a321 = Parameter(name = 'I77a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a321}')

I77a322 = Parameter(name = 'I77a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a322}')

I77a323 = Parameter(name = 'I77a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn3x1*yd2x2*complexconjugate(LLQD1x2x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a323}')

I77a324 = Parameter(name = 'I77a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn3x1*yd1x1*complexconjugate(LLQD1x1x3)*complexconjugate(Rd2x6)',
                    texname = '\\text{I77a324}')

I77a331 = Parameter(name = 'I77a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a331}')

I77a332 = Parameter(name = 'I77a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a332}')

I77a333 = Parameter(name = 'I77a333',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn3x1*yd2x2*complexconjugate(LLQD1x2x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a333}')

I77a334 = Parameter(name = 'I77a334',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn3x1*yd1x1*complexconjugate(LLQD1x1x2)*complexconjugate(Rd3x5)',
                    texname = '\\text{I77a334}')

I77a341 = Parameter(name = 'I77a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a341}')

I77a342 = Parameter(name = 'I77a342',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*Rn3x1*yd3x3*complexconjugate(LLQD1x3x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a342}')

I77a343 = Parameter(name = 'I77a343',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*Rn3x1*yd2x2*complexconjugate(LLQD1x2x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a343}')

I77a344 = Parameter(name = 'I77a344',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*Rn3x1*yd1x1*complexconjugate(LLQD1x1x1)*complexconjugate(Rd4x4)',
                    texname = '\\text{I77a344}')

I78a114 = Parameter(name = 'I78a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*complexconjugate(Rl1x6)*complexconjugate(TLLE3x1x3)',
                    texname = '\\text{I78a114}')

I78a115 = Parameter(name = 'I78a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*complexconjugate(Rl1x6)*complexconjugate(TLLE3x2x3)',
                    texname = '\\text{I78a115}')

I78a124 = Parameter(name = 'I78a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*complexconjugate(Rl2x5)*complexconjugate(TLLE3x1x2)',
                    texname = '\\text{I78a124}')

I78a125 = Parameter(name = 'I78a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*complexconjugate(Rl2x5)*complexconjugate(TLLE3x2x2)',
                    texname = '\\text{I78a125}')

I78a134 = Parameter(name = 'I78a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*complexconjugate(Rl3x4)*complexconjugate(TLLE3x1x1)',
                    texname = '\\text{I78a134}')

I78a135 = Parameter(name = 'I78a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*complexconjugate(Rl3x4)*complexconjugate(TLLE3x2x1)',
                    texname = '\\text{I78a135}')

I78a164 = Parameter(name = 'I78a164',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*complexconjugate(Rl6x6)*complexconjugate(TLLE3x1x3)',
                    texname = '\\text{I78a164}')

I78a165 = Parameter(name = 'I78a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*complexconjugate(Rl6x6)*complexconjugate(TLLE3x2x3)',
                    texname = '\\text{I78a165}')

I78a211 = Parameter(name = 'I78a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*complexconjugate(Rl1x6)*complexconjugate(TLLE2x3x3)',
                    texname = '\\text{I78a211}')

I78a214 = Parameter(name = 'I78a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*complexconjugate(Rl1x6)*complexconjugate(TLLE2x1x3)',
                    texname = '\\text{I78a214}')

I78a216 = Parameter(name = 'I78a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*complexconjugate(Rl1x6)*complexconjugate(TLLE2x3x3)',
                    texname = '\\text{I78a216}')

I78a221 = Parameter(name = 'I78a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*complexconjugate(Rl2x5)*complexconjugate(TLLE2x3x2)',
                    texname = '\\text{I78a221}')

I78a224 = Parameter(name = 'I78a224',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*complexconjugate(Rl2x5)*complexconjugate(TLLE2x1x2)',
                    texname = '\\text{I78a224}')

I78a226 = Parameter(name = 'I78a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*complexconjugate(Rl2x5)*complexconjugate(TLLE2x3x2)',
                    texname = '\\text{I78a226}')

I78a231 = Parameter(name = 'I78a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*complexconjugate(Rl3x4)*complexconjugate(TLLE2x3x1)',
                    texname = '\\text{I78a231}')

I78a234 = Parameter(name = 'I78a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*complexconjugate(Rl3x4)*complexconjugate(TLLE2x1x1)',
                    texname = '\\text{I78a234}')

I78a236 = Parameter(name = 'I78a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*complexconjugate(Rl3x4)*complexconjugate(TLLE2x3x1)',
                    texname = '\\text{I78a236}')

I78a261 = Parameter(name = 'I78a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*complexconjugate(Rl6x6)*complexconjugate(TLLE2x3x3)',
                    texname = '\\text{I78a261}')

I78a264 = Parameter(name = 'I78a264',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*complexconjugate(Rl6x6)*complexconjugate(TLLE2x1x3)',
                    texname = '\\text{I78a264}')

I78a266 = Parameter(name = 'I78a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*complexconjugate(Rl6x6)*complexconjugate(TLLE2x3x3)',
                    texname = '\\text{I78a266}')

I78a311 = Parameter(name = 'I78a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*complexconjugate(Rl1x6)*complexconjugate(TLLE1x3x3)',
                    texname = '\\text{I78a311}')

I78a315 = Parameter(name = 'I78a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*complexconjugate(Rl1x6)*complexconjugate(TLLE1x2x3)',
                    texname = '\\text{I78a315}')

I78a316 = Parameter(name = 'I78a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*complexconjugate(Rl1x6)*complexconjugate(TLLE1x3x3)',
                    texname = '\\text{I78a316}')

I78a321 = Parameter(name = 'I78a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*complexconjugate(Rl2x5)*complexconjugate(TLLE1x3x2)',
                    texname = '\\text{I78a321}')

I78a325 = Parameter(name = 'I78a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*complexconjugate(Rl2x5)*complexconjugate(TLLE1x2x2)',
                    texname = '\\text{I78a325}')

I78a326 = Parameter(name = 'I78a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*complexconjugate(Rl2x5)*complexconjugate(TLLE1x3x2)',
                    texname = '\\text{I78a326}')

I78a331 = Parameter(name = 'I78a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*complexconjugate(Rl3x4)*complexconjugate(TLLE1x3x1)',
                    texname = '\\text{I78a331}')

I78a335 = Parameter(name = 'I78a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*complexconjugate(Rl3x4)*complexconjugate(TLLE1x2x1)',
                    texname = '\\text{I78a335}')

I78a336 = Parameter(name = 'I78a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*complexconjugate(Rl3x4)*complexconjugate(TLLE1x3x1)',
                    texname = '\\text{I78a336}')

I78a361 = Parameter(name = 'I78a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*complexconjugate(Rl6x6)*complexconjugate(TLLE1x3x3)',
                    texname = '\\text{I78a361}')

I78a365 = Parameter(name = 'I78a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*complexconjugate(Rl6x6)*complexconjugate(TLLE1x2x3)',
                    texname = '\\text{I78a365}')

I78a366 = Parameter(name = 'I78a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*complexconjugate(Rl6x6)*complexconjugate(TLLE1x3x3)',
                    texname = '\\text{I78a366}')

I79a114 = Parameter(name = 'I79a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*ye3x3*complexconjugate(LLLE3x1x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a114}')

I79a115 = Parameter(name = 'I79a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*ye3x3*complexconjugate(LLLE3x2x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a115}')

I79a144 = Parameter(name = 'I79a144',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*ye1x1*complexconjugate(LLLE3x1x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a144}')

I79a145 = Parameter(name = 'I79a145',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*ye1x1*complexconjugate(LLLE3x2x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a145}')

I79a154 = Parameter(name = 'I79a154',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*ye2x2*complexconjugate(LLLE3x1x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a154}')

I79a155 = Parameter(name = 'I79a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*ye2x2*complexconjugate(LLLE3x2x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a155}')

I79a164 = Parameter(name = 'I79a164',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn1x3*ye3x3*complexconjugate(LLLE3x1x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a164}')

I79a165 = Parameter(name = 'I79a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn1x3*ye3x3*complexconjugate(LLLE3x2x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a165}')

I79a211 = Parameter(name = 'I79a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a211}')

I79a214 = Parameter(name = 'I79a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*ye3x3*complexconjugate(LLLE2x1x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a214}')

I79a216 = Parameter(name = 'I79a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a216}')

I79a241 = Parameter(name = 'I79a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*ye1x1*complexconjugate(LLLE2x3x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a241}')

I79a244 = Parameter(name = 'I79a244',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*ye1x1*complexconjugate(LLLE2x1x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a244}')

I79a246 = Parameter(name = 'I79a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*ye1x1*complexconjugate(LLLE2x3x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a246}')

I79a251 = Parameter(name = 'I79a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*ye2x2*complexconjugate(LLLE2x3x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a251}')

I79a254 = Parameter(name = 'I79a254',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*ye2x2*complexconjugate(LLLE2x1x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a254}')

I79a256 = Parameter(name = 'I79a256',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*ye2x2*complexconjugate(LLLE2x3x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a256}')

I79a261 = Parameter(name = 'I79a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a261}')

I79a264 = Parameter(name = 'I79a264',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl4x1*Rn2x2*ye3x3*complexconjugate(LLLE2x1x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a264}')

I79a266 = Parameter(name = 'I79a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a266}')

I79a311 = Parameter(name = 'I79a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a311}')

I79a315 = Parameter(name = 'I79a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*ye3x3*complexconjugate(LLLE1x2x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a315}')

I79a316 = Parameter(name = 'I79a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl1x3)',
                    texname = '\\text{I79a316}')

I79a341 = Parameter(name = 'I79a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*ye1x1*complexconjugate(LLLE1x3x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a341}')

I79a345 = Parameter(name = 'I79a345',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*ye1x1*complexconjugate(LLLE1x2x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a345}')

I79a346 = Parameter(name = 'I79a346',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*ye1x1*complexconjugate(LLLE1x3x1)*complexconjugate(Rl4x1)',
                    texname = '\\text{I79a346}')

I79a351 = Parameter(name = 'I79a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*ye2x2*complexconjugate(LLLE1x3x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a351}')

I79a355 = Parameter(name = 'I79a355',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*ye2x2*complexconjugate(LLLE1x2x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a355}')

I79a356 = Parameter(name = 'I79a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*ye2x2*complexconjugate(LLLE1x3x2)*complexconjugate(Rl5x2)',
                    texname = '\\text{I79a356}')

I79a361 = Parameter(name = 'I79a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x3*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a361}')

I79a365 = Parameter(name = 'I79a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl5x2*Rn3x1*ye3x3*complexconjugate(LLLE1x2x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a365}')

I79a366 = Parameter(name = 'I79a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x3*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl6x3)',
                    texname = '\\text{I79a366}')

I8a11 = Parameter(name = 'I8a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x3*complexconjugate(Rd1x3)',
                  texname = '\\text{I8a11}')

I8a12 = Parameter(name = 'I8a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x3*complexconjugate(Rd1x3)',
                  texname = '\\text{I8a12}')

I8a21 = Parameter(name = 'I8a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x3*complexconjugate(Rd2x3)',
                  texname = '\\text{I8a21}')

I8a22 = Parameter(name = 'I8a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x3*complexconjugate(Rd2x3)',
                  texname = '\\text{I8a22}')

I8a55 = Parameter(name = 'I8a55',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd5x2*complexconjugate(Rd5x2)',
                  texname = '\\text{I8a55}')

I8a66 = Parameter(name = 'I8a66',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd6x1*complexconjugate(Rd6x1)',
                  texname = '\\text{I8a66}')

I80a112 = Parameter(name = 'I80a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn1x3*ye2x2*complexconjugate(LLLE3x2x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a112}')

I80a113 = Parameter(name = 'I80a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn1x3*ye1x1*complexconjugate(LLLE3x1x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a113}')

I80a122 = Parameter(name = 'I80a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn1x3*ye2x2*complexconjugate(LLLE3x2x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a122}')

I80a123 = Parameter(name = 'I80a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn1x3*ye1x1*complexconjugate(LLLE3x1x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a123}')

I80a132 = Parameter(name = 'I80a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn1x3*ye2x2*complexconjugate(LLLE3x2x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a132}')

I80a133 = Parameter(name = 'I80a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn1x3*ye1x1*complexconjugate(LLLE3x1x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a133}')

I80a162 = Parameter(name = 'I80a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn1x3*ye2x2*complexconjugate(LLLE3x2x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a162}')

I80a163 = Parameter(name = 'I80a163',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn1x3*ye1x1*complexconjugate(LLLE3x1x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a163}')

I80a211 = Parameter(name = 'I80a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a211}')

I80a213 = Parameter(name = 'I80a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn2x2*ye1x1*complexconjugate(LLLE2x1x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a213}')

I80a216 = Parameter(name = 'I80a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a216}')

I80a221 = Parameter(name = 'I80a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a221}')

I80a223 = Parameter(name = 'I80a223',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn2x2*ye1x1*complexconjugate(LLLE2x1x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a223}')

I80a226 = Parameter(name = 'I80a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a226}')

I80a231 = Parameter(name = 'I80a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a231}')

I80a233 = Parameter(name = 'I80a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn2x2*ye1x1*complexconjugate(LLLE2x1x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a233}')

I80a236 = Parameter(name = 'I80a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a236}')

I80a261 = Parameter(name = 'I80a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a261}')

I80a263 = Parameter(name = 'I80a263',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl3x4*Rn2x2*ye1x1*complexconjugate(LLLE2x1x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a263}')

I80a266 = Parameter(name = 'I80a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn2x2*ye3x3*complexconjugate(LLLE2x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a266}')

I80a311 = Parameter(name = 'I80a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a311}')

I80a312 = Parameter(name = 'I80a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn3x1*ye2x2*complexconjugate(LLLE1x2x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a312}')

I80a316 = Parameter(name = 'I80a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl1x6)',
                    texname = '\\text{I80a316}')

I80a321 = Parameter(name = 'I80a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a321}')

I80a322 = Parameter(name = 'I80a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn3x1*ye2x2*complexconjugate(LLLE1x2x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a322}')

I80a326 = Parameter(name = 'I80a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x2)*complexconjugate(Rl2x5)',
                    texname = '\\text{I80a326}')

I80a331 = Parameter(name = 'I80a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a331}')

I80a332 = Parameter(name = 'I80a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn3x1*ye2x2*complexconjugate(LLLE1x2x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a332}')

I80a336 = Parameter(name = 'I80a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x1)*complexconjugate(Rl3x4)',
                    texname = '\\text{I80a336}')

I80a361 = Parameter(name = 'I80a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl1x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a361}')

I80a362 = Parameter(name = 'I80a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl2x5*Rn3x1*ye2x2*complexconjugate(LLLE1x2x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a362}')

I80a366 = Parameter(name = 'I80a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rl6x6*Rn3x1*ye3x3*complexconjugate(LLLE1x3x3)*complexconjugate(Rl6x6)',
                    texname = '\\text{I80a366}')

I81a14 = Parameter(name = 'I81a14',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                   texname = '\\text{I81a14}')

I81a23 = Parameter(name = 'I81a23',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                   texname = '\\text{I81a23}')

I81a31 = Parameter(name = 'I81a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81a31}')

I81a32 = Parameter(name = 'I81a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I81a32}')

I82a15 = Parameter(name = 'I82a15',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu1x1*complexconjugate(Ru5x1)',
                   texname = '\\text{I82a15}')

I82a26 = Parameter(name = 'I82a26',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu2x2*complexconjugate(Ru6x2)',
                   texname = '\\text{I82a26}')

I82a31 = Parameter(name = 'I82a31',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I82a31}')

I82a32 = Parameter(name = 'I82a32',
                   nature = 'internal',
                   type = 'complex',
                   value = 'yu3x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I82a32}')

I83a111 = Parameter(name = 'I83a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a111}')

I83a112 = Parameter(name = 'I83a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a112}')

I83a115 = Parameter(name = 'I83a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a115}')

I83a116 = Parameter(name = 'I83a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a116}')

I83a121 = Parameter(name = 'I83a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a121}')

I83a122 = Parameter(name = 'I83a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a122}')

I83a125 = Parameter(name = 'I83a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a125}')

I83a126 = Parameter(name = 'I83a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a126}')

I83a131 = Parameter(name = 'I83a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a131}')

I83a132 = Parameter(name = 'I83a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a132}')

I83a135 = Parameter(name = 'I83a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a135}')

I83a136 = Parameter(name = 'I83a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a136}')

I83a211 = Parameter(name = 'I83a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a211}')

I83a212 = Parameter(name = 'I83a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a212}')

I83a215 = Parameter(name = 'I83a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a215}')

I83a216 = Parameter(name = 'I83a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a216}')

I83a221 = Parameter(name = 'I83a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a221}')

I83a222 = Parameter(name = 'I83a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a222}')

I83a225 = Parameter(name = 'I83a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a225}')

I83a226 = Parameter(name = 'I83a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a226}')

I83a231 = Parameter(name = 'I83a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a231}')

I83a232 = Parameter(name = 'I83a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a232}')

I83a235 = Parameter(name = 'I83a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a235}')

I83a236 = Parameter(name = 'I83a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a236}')

I83a311 = Parameter(name = 'I83a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a311}')

I83a312 = Parameter(name = 'I83a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a312}')

I83a315 = Parameter(name = 'I83a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a315}')

I83a316 = Parameter(name = 'I83a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a316}')

I83a321 = Parameter(name = 'I83a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a321}')

I83a322 = Parameter(name = 'I83a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a322}')

I83a325 = Parameter(name = 'I83a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a325}')

I83a326 = Parameter(name = 'I83a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a326}')

I83a331 = Parameter(name = 'I83a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*complexconjugate(Ru1x3)',
                    texname = '\\text{I83a331}')

I83a332 = Parameter(name = 'I83a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*complexconjugate(Ru2x3)',
                    texname = '\\text{I83a332}')

I83a335 = Parameter(name = 'I83a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*complexconjugate(Ru5x1)',
                    texname = '\\text{I83a335}')

I83a336 = Parameter(name = 'I83a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*complexconjugate(Ru6x2)',
                    texname = '\\text{I83a336}')

I84a11 = Parameter(name = 'I84a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I84a11}')

I84a12 = Parameter(name = 'I84a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I84a12}')

I84a21 = Parameter(name = 'I84a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I84a21}')

I84a22 = Parameter(name = 'I84a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I84a22}')

I84a55 = Parameter(name = 'I84a55',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru5x1*complexconjugate(Ru5x1)',
                   texname = '\\text{I84a55}')

I84a66 = Parameter(name = 'I84a66',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru6x2*complexconjugate(Ru6x2)',
                   texname = '\\text{I84a66}')

I85a11 = Parameter(name = 'I85a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x6*complexconjugate(Ru1x6)',
                   texname = '\\text{I85a11}')

I85a12 = Parameter(name = 'I85a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x6*complexconjugate(Ru1x6)',
                   texname = '\\text{I85a12}')

I85a21 = Parameter(name = 'I85a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru1x6*complexconjugate(Ru2x6)',
                   texname = '\\text{I85a21}')

I85a22 = Parameter(name = 'I85a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru2x6*complexconjugate(Ru2x6)',
                   texname = '\\text{I85a22}')

I85a33 = Parameter(name = 'I85a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru3x5*complexconjugate(Ru3x5)',
                   texname = '\\text{I85a33}')

I85a44 = Parameter(name = 'I85a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Ru4x4*complexconjugate(Ru4x4)',
                   texname = '\\text{I85a44}')

I86a11 = Parameter(name = 'I86a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I86a11}')

I86a12 = Parameter(name = 'I86a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I86a12}')

I86a21 = Parameter(name = 'I86a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I86a21}')

I86a22 = Parameter(name = 'I86a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I86a22}')

I86a56 = Parameter(name = 'I86a56',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Ru6x2)',
                   texname = '\\text{I86a56}')

I86a65 = Parameter(name = 'I86a65',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Ru5x1)',
                   texname = '\\text{I86a65}')

I87a11 = Parameter(name = 'I87a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru1x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I87a11}')

I87a12 = Parameter(name = 'I87a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru2x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I87a12}')

I87a21 = Parameter(name = 'I87a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru1x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I87a21}')

I87a22 = Parameter(name = 'I87a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru2x6)*complexconjugate(tu3x3)',
                   texname = '\\text{I87a22}')

I87a53 = Parameter(name = 'I87a53',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Ru3x5)*complexconjugate(tu2x2)',
                   texname = '\\text{I87a53}')

I87a64 = Parameter(name = 'I87a64',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Ru4x4)*complexconjugate(tu1x1)',
                   texname = '\\text{I87a64}')

I88a11 = Parameter(name = 'I88a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I88a11}')

I88a12 = Parameter(name = 'I88a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I88a12}')

I88a21 = Parameter(name = 'I88a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I88a21}')

I88a22 = Parameter(name = 'I88a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I88a22}')

I88a53 = Parameter(name = 'I88a53',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                   texname = '\\text{I88a53}')

I88a64 = Parameter(name = 'I88a64',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                   texname = '\\text{I88a64}')

I89a11 = Parameter(name = 'I89a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*td3x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I89a11}')

I89a12 = Parameter(name = 'I89a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*td3x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I89a12}')

I89a21 = Parameter(name = 'I89a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*td3x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I89a21}')

I89a22 = Parameter(name = 'I89a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*td3x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I89a22}')

I89a36 = Parameter(name = 'I89a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*td2x2*complexconjugate(Ru6x2)',
                   texname = '\\text{I89a36}')

I89a45 = Parameter(name = 'I89a45',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*td1x1*complexconjugate(Ru5x1)',
                   texname = '\\text{I89a45}')

I9a11 = Parameter(name = 'I9a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x6*complexconjugate(Rd1x6)',
                  texname = '\\text{I9a11}')

I9a12 = Parameter(name = 'I9a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x6*complexconjugate(Rd1x6)',
                  texname = '\\text{I9a12}')

I9a21 = Parameter(name = 'I9a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd1x6*complexconjugate(Rd2x6)',
                  texname = '\\text{I9a21}')

I9a22 = Parameter(name = 'I9a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd2x6*complexconjugate(Rd2x6)',
                  texname = '\\text{I9a22}')

I9a33 = Parameter(name = 'I9a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd3x5*complexconjugate(Rd3x5)',
                  texname = '\\text{I9a33}')

I9a44 = Parameter(name = 'I9a44',
                  nature = 'internal',
                  type = 'complex',
                  value = 'Rd4x4*complexconjugate(Rd4x4)',
                  texname = '\\text{I9a44}')

I90a11 = Parameter(name = 'I90a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I90a11}')

I90a12 = Parameter(name = 'I90a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I90a12}')

I90a21 = Parameter(name = 'I90a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Ru1x3)',
                   texname = '\\text{I90a21}')

I90a22 = Parameter(name = 'I90a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Ru2x3)',
                   texname = '\\text{I90a22}')

I90a36 = Parameter(name = 'I90a36',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2*complexconjugate(Ru6x2)',
                   texname = '\\text{I90a36}')

I90a45 = Parameter(name = 'I90a45',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1*complexconjugate(Ru5x1)',
                   texname = '\\text{I90a45}')

I91a11 = Parameter(name = 'I91a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yd3x3*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I91a11}')

I91a12 = Parameter(name = 'I91a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yd3x3*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I91a12}')

I91a21 = Parameter(name = 'I91a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yd3x3*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I91a21}')

I91a22 = Parameter(name = 'I91a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yd3x3*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                   texname = '\\text{I91a22}')

I91a56 = Parameter(name = 'I91a56',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*yd2x2*complexconjugate(Ru6x2)*complexconjugate(yd2x2)',
                   texname = '\\text{I91a56}')

I91a65 = Parameter(name = 'I91a65',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*yd1x1*complexconjugate(Ru5x1)*complexconjugate(yd1x1)',
                   texname = '\\text{I91a65}')

I92a11 = Parameter(name = 'I92a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I92a11}')

I92a12 = Parameter(name = 'I92a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x6*yd3x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I92a12}')

I92a21 = Parameter(name = 'I92a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I92a21}')

I92a22 = Parameter(name = 'I92a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x6*yd3x3*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                   texname = '\\text{I92a22}')

I92a33 = Parameter(name = 'I92a33',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd3x5*yd2x2*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                   texname = '\\text{I92a33}')

I92a44 = Parameter(name = 'I92a44',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd4x4*yd1x1*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                   texname = '\\text{I92a44}')

I93a11 = Parameter(name = 'I93a11',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yu3x3*complexconjugate(Ru1x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I93a11}')

I93a12 = Parameter(name = 'I93a12',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd1x3*yu3x3*complexconjugate(Ru2x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I93a12}')

I93a21 = Parameter(name = 'I93a21',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yu3x3*complexconjugate(Ru1x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I93a21}')

I93a22 = Parameter(name = 'I93a22',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd2x3*yu3x3*complexconjugate(Ru2x3)*complexconjugate(yu3x3)',
                   texname = '\\text{I93a22}')

I93a56 = Parameter(name = 'I93a56',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd5x2*yu2x2*complexconjugate(Ru6x2)*complexconjugate(yu2x2)',
                   texname = '\\text{I93a56}')

I93a65 = Parameter(name = 'I93a65',
                   nature = 'internal',
                   type = 'complex',
                   value = 'Rd6x1*yu1x1*complexconjugate(Ru5x1)*complexconjugate(yu1x1)',
                   texname = '\\text{I93a65}')

I94a121 = Parameter(name = 'I94a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a121}')

I94a122 = Parameter(name = 'I94a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a122}')

I94a123 = Parameter(name = 'I94a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x2)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a123}')

I94a124 = Parameter(name = 'I94a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x2)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a124}')

I94a131 = Parameter(name = 'I94a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a131}')

I94a132 = Parameter(name = 'I94a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a132}')

I94a133 = Parameter(name = 'I94a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x3)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a133}')

I94a134 = Parameter(name = 'I94a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x3)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a134}')

I94a211 = Parameter(name = 'I94a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a211}')

I94a212 = Parameter(name = 'I94a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a212}')

I94a213 = Parameter(name = 'I94a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x1)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a213}')

I94a214 = Parameter(name = 'I94a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x1)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a214}')

I94a231 = Parameter(name = 'I94a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a231}')

I94a232 = Parameter(name = 'I94a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a232}')

I94a233 = Parameter(name = 'I94a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x3)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a233}')

I94a234 = Parameter(name = 'I94a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x3)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a234}')

I94a311 = Parameter(name = 'I94a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a311}')

I94a312 = Parameter(name = 'I94a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a312}')

I94a313 = Parameter(name = 'I94a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x1)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a313}')

I94a314 = Parameter(name = 'I94a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x1)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a314}')

I94a321 = Parameter(name = 'I94a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Ru1x6)',
                    texname = '\\text{I94a321}')

I94a322 = Parameter(name = 'I94a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Ru2x6)',
                    texname = '\\text{I94a322}')

I94a323 = Parameter(name = 'I94a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x2)*complexconjugate(Ru3x5)',
                    texname = '\\text{I94a323}')

I94a324 = Parameter(name = 'I94a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x2)*complexconjugate(Ru4x4)',
                    texname = '\\text{I94a324}')

I95a121 = Parameter(name = 'I95a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a121}')

I95a122 = Parameter(name = 'I95a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x1)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a122}')

I95a123 = Parameter(name = 'I95a123',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x1)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a123}')

I95a124 = Parameter(name = 'I95a124',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x1)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a124}')

I95a131 = Parameter(name = 'I95a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a131}')

I95a132 = Parameter(name = 'I95a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x1)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a132}')

I95a133 = Parameter(name = 'I95a133',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x1)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a133}')

I95a134 = Parameter(name = 'I95a134',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x1)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a134}')

I95a211 = Parameter(name = 'I95a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a211}')

I95a212 = Parameter(name = 'I95a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x2)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a212}')

I95a213 = Parameter(name = 'I95a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x2)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a213}')

I95a214 = Parameter(name = 'I95a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x2)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a214}')

I95a231 = Parameter(name = 'I95a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a231}')

I95a232 = Parameter(name = 'I95a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x3x2)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a232}')

I95a233 = Parameter(name = 'I95a233',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x3x2)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a233}')

I95a234 = Parameter(name = 'I95a234',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x3x2)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a234}')

I95a311 = Parameter(name = 'I95a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a311}')

I95a312 = Parameter(name = 'I95a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x1x3)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a312}')

I95a313 = Parameter(name = 'I95a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x1x3)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a313}')

I95a314 = Parameter(name = 'I95a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x1x3)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a314}')

I95a321 = Parameter(name = 'I95a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Ru1x6)',
                    texname = '\\text{I95a321}')

I95a322 = Parameter(name = 'I95a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD3x2x3)*complexconjugate(Ru2x6)',
                    texname = '\\text{I95a322}')

I95a323 = Parameter(name = 'I95a323',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD2x2x3)*complexconjugate(Ru3x5)',
                    texname = '\\text{I95a323}')

I95a324 = Parameter(name = 'I95a324',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complexconjugate(LUDD1x2x3)*complexconjugate(Ru4x4)',
                    texname = '\\text{I95a324}')

I96a111 = Parameter(name = 'I96a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a111}')

I96a112 = Parameter(name = 'I96a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a112}')

I96a115 = Parameter(name = 'I96a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x3*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a115}')

I96a116 = Parameter(name = 'I96a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x3*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a116}')

I96a141 = Parameter(name = 'I96a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x3*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a141}')

I96a142 = Parameter(name = 'I96a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x3*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a142}')

I96a145 = Parameter(name = 'I96a145',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x3*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a145}')

I96a146 = Parameter(name = 'I96a146',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x3*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a146}')

I96a151 = Parameter(name = 'I96a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x3*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a151}')

I96a152 = Parameter(name = 'I96a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x3*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a152}')

I96a155 = Parameter(name = 'I96a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x3*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a155}')

I96a156 = Parameter(name = 'I96a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x3*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a156}')

I96a161 = Parameter(name = 'I96a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a161}')

I96a162 = Parameter(name = 'I96a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x3*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a162}')

I96a165 = Parameter(name = 'I96a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x3*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a165}')

I96a166 = Parameter(name = 'I96a166',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x3*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a166}')

I96a211 = Parameter(name = 'I96a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a211}')

I96a212 = Parameter(name = 'I96a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a212}')

I96a215 = Parameter(name = 'I96a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x3*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a215}')

I96a216 = Parameter(name = 'I96a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x3*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a216}')

I96a241 = Parameter(name = 'I96a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x3*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a241}')

I96a242 = Parameter(name = 'I96a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x3*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a242}')

I96a245 = Parameter(name = 'I96a245',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x3*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a245}')

I96a246 = Parameter(name = 'I96a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x3*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a246}')

I96a251 = Parameter(name = 'I96a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x3*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a251}')

I96a252 = Parameter(name = 'I96a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x3*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a252}')

I96a255 = Parameter(name = 'I96a255',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x3*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a255}')

I96a256 = Parameter(name = 'I96a256',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x3*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a256}')

I96a261 = Parameter(name = 'I96a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a261}')

I96a262 = Parameter(name = 'I96a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x3*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a262}')

I96a265 = Parameter(name = 'I96a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x3*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a265}')

I96a266 = Parameter(name = 'I96a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x3*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)*complexconjugate(yd3x3)',
                    texname = '\\text{I96a266}')

I96a511 = Parameter(name = 'I96a511',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a511}')

I96a512 = Parameter(name = 'I96a512',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a512}')

I96a515 = Parameter(name = 'I96a515',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd5x2*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a515}')

I96a516 = Parameter(name = 'I96a516',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd5x2*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a516}')

I96a541 = Parameter(name = 'I96a541',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd5x2*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a541}')

I96a542 = Parameter(name = 'I96a542',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd5x2*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a542}')

I96a545 = Parameter(name = 'I96a545',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd5x2*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a545}')

I96a546 = Parameter(name = 'I96a546',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd5x2*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a546}')

I96a551 = Parameter(name = 'I96a551',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd5x2*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a551}')

I96a552 = Parameter(name = 'I96a552',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd5x2*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a552}')

I96a555 = Parameter(name = 'I96a555',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd5x2*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a555}')

I96a556 = Parameter(name = 'I96a556',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd5x2*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a556}')

I96a561 = Parameter(name = 'I96a561',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a561}')

I96a562 = Parameter(name = 'I96a562',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd5x2*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a562}')

I96a565 = Parameter(name = 'I96a565',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd5x2*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a565}')

I96a566 = Parameter(name = 'I96a566',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd5x2*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)*complexconjugate(yd2x2)',
                    texname = '\\text{I96a566}')

I96a611 = Parameter(name = 'I96a611',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a611}')

I96a612 = Parameter(name = 'I96a612',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a612}')

I96a615 = Parameter(name = 'I96a615',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd6x1*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a615}')

I96a616 = Parameter(name = 'I96a616',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd6x1*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a616}')

I96a641 = Parameter(name = 'I96a641',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd6x1*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a641}')

I96a642 = Parameter(name = 'I96a642',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd6x1*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a642}')

I96a645 = Parameter(name = 'I96a645',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd6x1*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a645}')

I96a646 = Parameter(name = 'I96a646',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd6x1*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a646}')

I96a651 = Parameter(name = 'I96a651',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd6x1*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a651}')

I96a652 = Parameter(name = 'I96a652',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd6x1*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a652}')

I96a655 = Parameter(name = 'I96a655',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd6x1*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a655}')

I96a656 = Parameter(name = 'I96a656',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd6x1*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a656}')

I96a661 = Parameter(name = 'I96a661',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a661}')

I96a662 = Parameter(name = 'I96a662',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd6x1*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a662}')

I96a665 = Parameter(name = 'I96a665',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd6x1*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a665}')

I96a666 = Parameter(name = 'I96a666',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd6x1*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)*complexconjugate(yd1x1)',
                    texname = '\\text{I96a666}')

I97a111 = Parameter(name = 'I97a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl1x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a111}')

I97a112 = Parameter(name = 'I97a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl1x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a112}')

I97a115 = Parameter(name = 'I97a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6*complexconjugate(Rl1x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a115}')

I97a116 = Parameter(name = 'I97a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6*complexconjugate(Rl1x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a116}')

I97a121 = Parameter(name = 'I97a121',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rl2x5)*complexconjugate(Ru1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a121}')

I97a122 = Parameter(name = 'I97a122',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rl2x5)*complexconjugate(Ru2x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a122}')

I97a125 = Parameter(name = 'I97a125',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x6*complexconjugate(Rl2x5)*complexconjugate(Ru5x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a125}')

I97a126 = Parameter(name = 'I97a126',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x6*complexconjugate(Rl2x5)*complexconjugate(Ru6x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a126}')

I97a131 = Parameter(name = 'I97a131',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rl3x4)*complexconjugate(Ru1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a131}')

I97a132 = Parameter(name = 'I97a132',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rl3x4)*complexconjugate(Ru2x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a132}')

I97a135 = Parameter(name = 'I97a135',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x6*complexconjugate(Rl3x4)*complexconjugate(Ru5x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a135}')

I97a136 = Parameter(name = 'I97a136',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x6*complexconjugate(Rl3x4)*complexconjugate(Ru6x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a136}')

I97a161 = Parameter(name = 'I97a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl6x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a161}')

I97a162 = Parameter(name = 'I97a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl6x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a162}')

I97a165 = Parameter(name = 'I97a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6*complexconjugate(Rl6x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a165}')

I97a166 = Parameter(name = 'I97a166',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6*complexconjugate(Rl6x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a166}')

I97a211 = Parameter(name = 'I97a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl1x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a211}')

I97a212 = Parameter(name = 'I97a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl1x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a212}')

I97a215 = Parameter(name = 'I97a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6*complexconjugate(Rl1x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a215}')

I97a216 = Parameter(name = 'I97a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6*complexconjugate(Rl1x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a216}')

I97a221 = Parameter(name = 'I97a221',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rl2x5)*complexconjugate(Ru1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a221}')

I97a222 = Parameter(name = 'I97a222',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rl2x5)*complexconjugate(Ru2x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a222}')

I97a225 = Parameter(name = 'I97a225',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x6*complexconjugate(Rl2x5)*complexconjugate(Ru5x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a225}')

I97a226 = Parameter(name = 'I97a226',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x6*complexconjugate(Rl2x5)*complexconjugate(Ru6x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a226}')

I97a231 = Parameter(name = 'I97a231',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rl3x4)*complexconjugate(Ru1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a231}')

I97a232 = Parameter(name = 'I97a232',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rl3x4)*complexconjugate(Ru2x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a232}')

I97a235 = Parameter(name = 'I97a235',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x6*complexconjugate(Rl3x4)*complexconjugate(Ru5x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a235}')

I97a236 = Parameter(name = 'I97a236',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x6*complexconjugate(Rl3x4)*complexconjugate(Ru6x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a236}')

I97a261 = Parameter(name = 'I97a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl6x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a261}')

I97a262 = Parameter(name = 'I97a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl6x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a262}')

I97a265 = Parameter(name = 'I97a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6*complexconjugate(Rl6x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a265}')

I97a266 = Parameter(name = 'I97a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6*complexconjugate(Rl6x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a266}')

I97a311 = Parameter(name = 'I97a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl1x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a311}')

I97a312 = Parameter(name = 'I97a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl1x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a312}')

I97a315 = Parameter(name = 'I97a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5*complexconjugate(Rl1x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a315}')

I97a316 = Parameter(name = 'I97a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5*complexconjugate(Rl1x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a316}')

I97a321 = Parameter(name = 'I97a321',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rl2x5)*complexconjugate(Ru1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a321}')

I97a322 = Parameter(name = 'I97a322',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rl2x5)*complexconjugate(Ru2x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a322}')

I97a325 = Parameter(name = 'I97a325',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd3x5*complexconjugate(Rl2x5)*complexconjugate(Ru5x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a325}')

I97a326 = Parameter(name = 'I97a326',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd3x5*complexconjugate(Rl2x5)*complexconjugate(Ru6x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a326}')

I97a331 = Parameter(name = 'I97a331',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rl3x4)*complexconjugate(Ru1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a331}')

I97a332 = Parameter(name = 'I97a332',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rl3x4)*complexconjugate(Ru2x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a332}')

I97a335 = Parameter(name = 'I97a335',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd3x5*complexconjugate(Rl3x4)*complexconjugate(Ru5x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a335}')

I97a336 = Parameter(name = 'I97a336',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd3x5*complexconjugate(Rl3x4)*complexconjugate(Ru6x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a336}')

I97a361 = Parameter(name = 'I97a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl6x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a361}')

I97a362 = Parameter(name = 'I97a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl6x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a362}')

I97a365 = Parameter(name = 'I97a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5*complexconjugate(Rl6x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a365}')

I97a366 = Parameter(name = 'I97a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5*complexconjugate(Rl6x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a366}')

I97a411 = Parameter(name = 'I97a411',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl1x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a411}')

I97a412 = Parameter(name = 'I97a412',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl1x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a412}')

I97a415 = Parameter(name = 'I97a415',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4*complexconjugate(Rl1x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a415}')

I97a416 = Parameter(name = 'I97a416',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4*complexconjugate(Rl1x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a416}')

I97a421 = Parameter(name = 'I97a421',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rl2x5)*complexconjugate(Ru1x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a421}')

I97a422 = Parameter(name = 'I97a422',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rl2x5)*complexconjugate(Ru2x3)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a422}')

I97a425 = Parameter(name = 'I97a425',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd4x4*complexconjugate(Rl2x5)*complexconjugate(Ru5x1)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a425}')

I97a426 = Parameter(name = 'I97a426',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd4x4*complexconjugate(Rl2x5)*complexconjugate(Ru6x2)*complexconjugate(ye2x2)',
                    texname = '\\text{I97a426}')

I97a431 = Parameter(name = 'I97a431',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rl3x4)*complexconjugate(Ru1x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a431}')

I97a432 = Parameter(name = 'I97a432',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rl3x4)*complexconjugate(Ru2x3)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a432}')

I97a435 = Parameter(name = 'I97a435',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd4x4*complexconjugate(Rl3x4)*complexconjugate(Ru5x1)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a435}')

I97a436 = Parameter(name = 'I97a436',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd4x4*complexconjugate(Rl3x4)*complexconjugate(Ru6x2)*complexconjugate(ye1x1)',
                    texname = '\\text{I97a436}')

I97a461 = Parameter(name = 'I97a461',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl6x6)*complexconjugate(Ru1x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a461}')

I97a462 = Parameter(name = 'I97a462',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl6x6)*complexconjugate(Ru2x3)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a462}')

I97a465 = Parameter(name = 'I97a465',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4*complexconjugate(Rl6x6)*complexconjugate(Ru5x1)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a465}')

I97a466 = Parameter(name = 'I97a466',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4*complexconjugate(Rl6x6)*complexconjugate(Ru6x2)*complexconjugate(ye3x3)',
                    texname = '\\text{I97a466}')

I98a111 = Parameter(name = 'I98a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl1x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a111}')

I98a112 = Parameter(name = 'I98a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl1x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a112}')

I98a113 = Parameter(name = 'I98a113',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6*complexconjugate(Rl1x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a113}')

I98a114 = Parameter(name = 'I98a114',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6*complexconjugate(Rl1x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a114}')

I98a141 = Parameter(name = 'I98a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rl4x1)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a141}')

I98a142 = Parameter(name = 'I98a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd1x6*complexconjugate(Rl4x1)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a142}')

I98a143 = Parameter(name = 'I98a143',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd1x6*complexconjugate(Rl4x1)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a143}')

I98a144 = Parameter(name = 'I98a144',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd1x6*complexconjugate(Rl4x1)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a144}')

I98a151 = Parameter(name = 'I98a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rl5x2)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a151}')

I98a152 = Parameter(name = 'I98a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd1x6*complexconjugate(Rl5x2)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a152}')

I98a153 = Parameter(name = 'I98a153',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd1x6*complexconjugate(Rl5x2)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a153}')

I98a154 = Parameter(name = 'I98a154',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd1x6*complexconjugate(Rl5x2)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a154}')

I98a161 = Parameter(name = 'I98a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl6x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a161}')

I98a162 = Parameter(name = 'I98a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd1x6*complexconjugate(Rl6x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a162}')

I98a163 = Parameter(name = 'I98a163',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd1x6*complexconjugate(Rl6x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a163}')

I98a164 = Parameter(name = 'I98a164',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd1x6*complexconjugate(Rl6x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a164}')

I98a211 = Parameter(name = 'I98a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl1x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a211}')

I98a212 = Parameter(name = 'I98a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl1x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a212}')

I98a213 = Parameter(name = 'I98a213',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6*complexconjugate(Rl1x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a213}')

I98a214 = Parameter(name = 'I98a214',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6*complexconjugate(Rl1x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a214}')

I98a241 = Parameter(name = 'I98a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rl4x1)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a241}')

I98a242 = Parameter(name = 'I98a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x3*Rd2x6*complexconjugate(Rl4x1)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a242}')

I98a243 = Parameter(name = 'I98a243',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x3*Rd2x6*complexconjugate(Rl4x1)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a243}')

I98a244 = Parameter(name = 'I98a244',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x3*Rd2x6*complexconjugate(Rl4x1)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a244}')

I98a251 = Parameter(name = 'I98a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rl5x2)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a251}')

I98a252 = Parameter(name = 'I98a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x3*Rd2x6*complexconjugate(Rl5x2)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a252}')

I98a253 = Parameter(name = 'I98a253',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x3*Rd2x6*complexconjugate(Rl5x2)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a253}')

I98a254 = Parameter(name = 'I98a254',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x3*Rd2x6*complexconjugate(Rl5x2)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a254}')

I98a261 = Parameter(name = 'I98a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl6x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a261}')

I98a262 = Parameter(name = 'I98a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x3*Rd2x6*complexconjugate(Rl6x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a262}')

I98a263 = Parameter(name = 'I98a263',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x3*Rd2x6*complexconjugate(Rl6x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a263}')

I98a264 = Parameter(name = 'I98a264',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x3*Rd2x6*complexconjugate(Rl6x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a264}')

I98a311 = Parameter(name = 'I98a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl1x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a311}')

I98a312 = Parameter(name = 'I98a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl1x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a312}')

I98a313 = Parameter(name = 'I98a313',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5*complexconjugate(Rl1x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a313}')

I98a314 = Parameter(name = 'I98a314',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5*complexconjugate(Rl1x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a314}')

I98a341 = Parameter(name = 'I98a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rl4x1)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a341}')

I98a342 = Parameter(name = 'I98a342',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x2*Rd3x5*complexconjugate(Rl4x1)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a342}')

I98a343 = Parameter(name = 'I98a343',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x2*Rd3x5*complexconjugate(Rl4x1)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a343}')

I98a344 = Parameter(name = 'I98a344',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x2*Rd3x5*complexconjugate(Rl4x1)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a344}')

I98a351 = Parameter(name = 'I98a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rl5x2)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a351}')

I98a352 = Parameter(name = 'I98a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x2*Rd3x5*complexconjugate(Rl5x2)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a352}')

I98a353 = Parameter(name = 'I98a353',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x2*Rd3x5*complexconjugate(Rl5x2)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a353}')

I98a354 = Parameter(name = 'I98a354',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x2*Rd3x5*complexconjugate(Rl5x2)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a354}')

I98a361 = Parameter(name = 'I98a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl6x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a361}')

I98a362 = Parameter(name = 'I98a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x2*Rd3x5*complexconjugate(Rl6x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a362}')

I98a363 = Parameter(name = 'I98a363',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x2*Rd3x5*complexconjugate(Rl6x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a363}')

I98a364 = Parameter(name = 'I98a364',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x2*Rd3x5*complexconjugate(Rl6x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a364}')

I98a411 = Parameter(name = 'I98a411',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl1x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a411}')

I98a412 = Parameter(name = 'I98a412',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl1x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a412}')

I98a413 = Parameter(name = 'I98a413',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4*complexconjugate(Rl1x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a413}')

I98a414 = Parameter(name = 'I98a414',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4*complexconjugate(Rl1x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a414}')

I98a441 = Parameter(name = 'I98a441',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rl4x1)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a441}')

I98a442 = Parameter(name = 'I98a442',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x3x1*Rd4x4*complexconjugate(Rl4x1)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a442}')

I98a443 = Parameter(name = 'I98a443',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x2x1*Rd4x4*complexconjugate(Rl4x1)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a443}')

I98a444 = Parameter(name = 'I98a444',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD1x1x1*Rd4x4*complexconjugate(Rl4x1)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a444}')

I98a451 = Parameter(name = 'I98a451',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rl5x2)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a451}')

I98a452 = Parameter(name = 'I98a452',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x3x1*Rd4x4*complexconjugate(Rl5x2)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a452}')

I98a453 = Parameter(name = 'I98a453',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x2x1*Rd4x4*complexconjugate(Rl5x2)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a453}')

I98a454 = Parameter(name = 'I98a454',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD2x1x1*Rd4x4*complexconjugate(Rl5x2)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a454}')

I98a461 = Parameter(name = 'I98a461',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl6x3)*complexconjugate(Ru1x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a461}')

I98a462 = Parameter(name = 'I98a462',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x3x1*Rd4x4*complexconjugate(Rl6x3)*complexconjugate(Ru2x6)*complexconjugate(yu3x3)',
                    texname = '\\text{I98a462}')

I98a463 = Parameter(name = 'I98a463',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x2x1*Rd4x4*complexconjugate(Rl6x3)*complexconjugate(Ru3x5)*complexconjugate(yu2x2)',
                    texname = '\\text{I98a463}')

I98a464 = Parameter(name = 'I98a464',
                    nature = 'internal',
                    type = 'complex',
                    value = 'LLQD3x1x1*Rd4x4*complexconjugate(Rl6x3)*complexconjugate(Ru4x4)*complexconjugate(yu1x1)',
                    texname = '\\text{I98a464}')

I99a111 = Parameter(name = 'I99a111',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a111}')

I99a112 = Parameter(name = 'I99a112',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a112}')

I99a115 = Parameter(name = 'I99a115',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x1x3*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a115}')

I99a116 = Parameter(name = 'I99a116',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x2x3*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a116}')

I99a141 = Parameter(name = 'I99a141',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x3x3*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a141}')

I99a142 = Parameter(name = 'I99a142',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x3x3*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a142}')

I99a145 = Parameter(name = 'I99a145',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x1x3*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a145}')

I99a146 = Parameter(name = 'I99a146',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD1x2x3*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a146}')

I99a151 = Parameter(name = 'I99a151',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x3x3*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a151}')

I99a152 = Parameter(name = 'I99a152',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x3x3*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a152}')

I99a155 = Parameter(name = 'I99a155',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x1x3*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a155}')

I99a156 = Parameter(name = 'I99a156',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD2x2x3*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a156}')

I99a161 = Parameter(name = 'I99a161',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a161}')

I99a162 = Parameter(name = 'I99a162',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x3x3*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a162}')

I99a165 = Parameter(name = 'I99a165',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x1x3*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a165}')

I99a166 = Parameter(name = 'I99a166',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd1x6*TLQD3x2x3*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a166}')

I99a211 = Parameter(name = 'I99a211',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a211}')

I99a212 = Parameter(name = 'I99a212',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a212}')

I99a215 = Parameter(name = 'I99a215',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x1x3*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a215}')

I99a216 = Parameter(name = 'I99a216',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x2x3*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a216}')

I99a241 = Parameter(name = 'I99a241',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x3x3*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a241}')

I99a242 = Parameter(name = 'I99a242',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x3x3*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a242}')

I99a245 = Parameter(name = 'I99a245',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x1x3*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a245}')

I99a246 = Parameter(name = 'I99a246',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD1x2x3*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a246}')

I99a251 = Parameter(name = 'I99a251',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x3x3*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a251}')

I99a252 = Parameter(name = 'I99a252',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x3x3*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a252}')

I99a255 = Parameter(name = 'I99a255',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x1x3*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a255}')

I99a256 = Parameter(name = 'I99a256',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD2x2x3*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a256}')

I99a261 = Parameter(name = 'I99a261',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a261}')

I99a262 = Parameter(name = 'I99a262',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x3x3*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a262}')

I99a265 = Parameter(name = 'I99a265',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x1x3*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a265}')

I99a266 = Parameter(name = 'I99a266',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd2x6*TLQD3x2x3*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a266}')

I99a311 = Parameter(name = 'I99a311',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a311}')

I99a312 = Parameter(name = 'I99a312',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a312}')

I99a315 = Parameter(name = 'I99a315',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x1x2*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a315}')

I99a316 = Parameter(name = 'I99a316',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x2x2*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a316}')

I99a341 = Parameter(name = 'I99a341',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x3x2*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a341}')

I99a342 = Parameter(name = 'I99a342',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x3x2*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a342}')

I99a345 = Parameter(name = 'I99a345',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x1x2*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a345}')

I99a346 = Parameter(name = 'I99a346',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD1x2x2*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a346}')

I99a351 = Parameter(name = 'I99a351',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x3x2*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a351}')

I99a352 = Parameter(name = 'I99a352',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x3x2*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a352}')

I99a355 = Parameter(name = 'I99a355',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x1x2*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a355}')

I99a356 = Parameter(name = 'I99a356',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD2x2x2*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a356}')

I99a361 = Parameter(name = 'I99a361',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a361}')

I99a362 = Parameter(name = 'I99a362',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x3x2*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a362}')

I99a365 = Parameter(name = 'I99a365',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x1x2*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a365}')

I99a366 = Parameter(name = 'I99a366',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd3x5*TLQD3x2x2*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a366}')

I99a411 = Parameter(name = 'I99a411',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rl1x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a411}')

I99a412 = Parameter(name = 'I99a412',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rl1x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a412}')

I99a415 = Parameter(name = 'I99a415',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x1x1*complexconjugate(Rl1x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a415}')

I99a416 = Parameter(name = 'I99a416',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x2x1*complexconjugate(Rl1x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a416}')

I99a441 = Parameter(name = 'I99a441',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x3x1*complexconjugate(Rl4x1)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a441}')

I99a442 = Parameter(name = 'I99a442',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x3x1*complexconjugate(Rl4x1)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a442}')

I99a445 = Parameter(name = 'I99a445',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x1x1*complexconjugate(Rl4x1)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a445}')

I99a446 = Parameter(name = 'I99a446',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD1x2x1*complexconjugate(Rl4x1)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a446}')

I99a451 = Parameter(name = 'I99a451',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x3x1*complexconjugate(Rl5x2)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a451}')

I99a452 = Parameter(name = 'I99a452',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x3x1*complexconjugate(Rl5x2)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a452}')

I99a455 = Parameter(name = 'I99a455',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x1x1*complexconjugate(Rl5x2)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a455}')

I99a456 = Parameter(name = 'I99a456',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD2x2x1*complexconjugate(Rl5x2)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a456}')

I99a461 = Parameter(name = 'I99a461',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rl6x3)*complexconjugate(Ru1x3)',
                    texname = '\\text{I99a461}')

I99a462 = Parameter(name = 'I99a462',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x3x1*complexconjugate(Rl6x3)*complexconjugate(Ru2x3)',
                    texname = '\\text{I99a462}')

I99a465 = Parameter(name = 'I99a465',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x1x1*complexconjugate(Rl6x3)*complexconjugate(Ru5x1)',
                    texname = '\\text{I99a465}')

I99a466 = Parameter(name = 'I99a466',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Rd4x4*TLQD3x2x1*complexconjugate(Rl6x3)*complexconjugate(Ru6x2)',
                    texname = '\\text{I99a466}')

