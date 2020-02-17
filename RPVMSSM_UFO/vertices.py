# This file was automatically created by FeynRules 2.3.1
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Fri 15 May 2015 03:47:37


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.h01, P.h01, P.h02 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2400})

V_2 = Vertex(name = 'V_2',
             particles = [ P.h02, P.h02, P.h02 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2401})

V_3 = Vertex(name = 'V_3',
             particles = [ P.h01, P.h01, P.h01 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2399})

V_4 = Vertex(name = 'V_4',
             particles = [ P.h01, P.h02, P.h02 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2398})

V_5 = Vertex(name = 'V_5',
             particles = [ P.a, P.a, P.H__minus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVSS1 ],
             couplings = {(0,0):C.GC_2541})

V_6 = Vertex(name = 'V_6',
             particles = [ P.A0, P.A0, P.h02 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2554})

V_7 = Vertex(name = 'V_7',
             particles = [ P.H__minus__, P.h02, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2555})

V_8 = Vertex(name = 'V_8',
             particles = [ P.A0, P.A0, P.h01 ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2552})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H__minus__, P.h01, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2553})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_2540})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_6})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_9,(0,0):C.GC_9,(2,2):C.GC_9})

V_13 = Vertex(name = 'V_13',
              particles = [ P.x1__minus__, P.x1__plus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2390,(0,1):C.GC_2344})

V_14 = Vertex(name = 'V_14',
              particles = [ P.x2__minus__, P.x1__plus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2394,(0,1):C.GC_2345})

V_15 = Vertex(name = 'V_15',
              particles = [ P.x1__minus__, P.x2__plus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2391,(0,1):C.GC_2348})

V_16 = Vertex(name = 'V_16',
              particles = [ P.x2__minus__, P.x2__plus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2395,(0,1):C.GC_2349})

V_17 = Vertex(name = 'V_17',
              particles = [ P.x1__minus__, P.x1__plus__, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2388,(0,1):C.GC_2342})

V_18 = Vertex(name = 'V_18',
              particles = [ P.x2__minus__, P.x1__plus__, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2392,(0,1):C.GC_2343})

V_19 = Vertex(name = 'V_19',
              particles = [ P.x1__minus__, P.x2__plus__, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2389,(0,1):C.GC_2346})

V_20 = Vertex(name = 'V_20',
              particles = [ P.x2__minus__, P.x2__plus__, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2393,(0,1):C.GC_2347})

V_21 = Vertex(name = 'V_21',
              particles = [ P.x1__minus__, P.x1__plus__, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2528,(0,1):C.GC_2494})

V_22 = Vertex(name = 'V_22',
              particles = [ P.x2__minus__, P.x1__plus__, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2530,(0,1):C.GC_2495})

V_23 = Vertex(name = 'V_23',
              particles = [ P.x1__minus__, P.x2__plus__, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2529,(0,1):C.GC_2496})

V_24 = Vertex(name = 'V_24',
              particles = [ P.x2__minus__, P.x2__plus__, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2531,(0,1):C.GC_2497})

V_25 = Vertex(name = 'V_25',
              particles = [ P.x1__minus__, P.n1, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2236,(0,1):C.GC_2464})

V_26 = Vertex(name = 'V_26',
              particles = [ P.x2__minus__, P.n1, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2240,(0,1):C.GC_2468})

V_27 = Vertex(name = 'V_27',
              particles = [ P.x1__minus__, P.n2, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2237,(0,1):C.GC_2465})

V_28 = Vertex(name = 'V_28',
              particles = [ P.x2__minus__, P.n2, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2241,(0,1):C.GC_2469})

V_29 = Vertex(name = 'V_29',
              particles = [ P.x1__minus__, P.n3, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2238,(0,1):C.GC_2466})

V_30 = Vertex(name = 'V_30',
              particles = [ P.x2__minus__, P.n3, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2242,(0,1):C.GC_2470})

V_31 = Vertex(name = 'V_31',
              particles = [ P.x1__minus__, P.n4, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2239,(0,1):C.GC_2467})

V_32 = Vertex(name = 'V_32',
              particles = [ P.x2__minus__, P.n4, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2243,(0,1):C.GC_2471})

V_33 = Vertex(name = 'V_33',
              particles = [ P.n1, P.n1, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2369,(0,1):C.GC_2263})

V_34 = Vertex(name = 'V_34',
              particles = [ P.n2, P.n1, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2372,(0,1):C.GC_2266})

V_35 = Vertex(name = 'V_35',
              particles = [ P.n3, P.n1, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2377,(0,1):C.GC_2271})

V_36 = Vertex(name = 'V_36',
              particles = [ P.n4, P.n1, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2384,(0,1):C.GC_2278})

V_37 = Vertex(name = 'V_37',
              particles = [ P.n2, P.n2, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2373,(0,1):C.GC_2267})

V_38 = Vertex(name = 'V_38',
              particles = [ P.n3, P.n2, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2378,(0,1):C.GC_2272})

V_39 = Vertex(name = 'V_39',
              particles = [ P.n4, P.n2, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2385,(0,1):C.GC_2279})

V_40 = Vertex(name = 'V_40',
              particles = [ P.n3, P.n3, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2379,(0,1):C.GC_2273})

V_41 = Vertex(name = 'V_41',
              particles = [ P.n4, P.n3, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2386,(0,1):C.GC_2280})

V_42 = Vertex(name = 'V_42',
              particles = [ P.n4, P.n4, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2387,(0,1):C.GC_2281})

V_43 = Vertex(name = 'V_43',
              particles = [ P.n1, P.n1, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2368,(0,1):C.GC_2262})

V_44 = Vertex(name = 'V_44',
              particles = [ P.n2, P.n1, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2370,(0,1):C.GC_2264})

V_45 = Vertex(name = 'V_45',
              particles = [ P.n3, P.n1, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2374,(0,1):C.GC_2268})

V_46 = Vertex(name = 'V_46',
              particles = [ P.n4, P.n1, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2380,(0,1):C.GC_2274})

V_47 = Vertex(name = 'V_47',
              particles = [ P.n2, P.n2, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2371,(0,1):C.GC_2265})

V_48 = Vertex(name = 'V_48',
              particles = [ P.n3, P.n2, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2375,(0,1):C.GC_2269})

V_49 = Vertex(name = 'V_49',
              particles = [ P.n4, P.n2, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2381,(0,1):C.GC_2275})

V_50 = Vertex(name = 'V_50',
              particles = [ P.n3, P.n3, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2376,(0,1):C.GC_2270})

V_51 = Vertex(name = 'V_51',
              particles = [ P.n4, P.n3, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2382,(0,1):C.GC_2276})

V_52 = Vertex(name = 'V_52',
              particles = [ P.n4, P.n4, P.h01 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2383,(0,1):C.GC_2277})

V_53 = Vertex(name = 'V_53',
              particles = [ P.n1, P.n1, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2510,(0,1):C.GC_2454})

V_54 = Vertex(name = 'V_54',
              particles = [ P.n2, P.n1, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2511,(0,1):C.GC_2455})

V_55 = Vertex(name = 'V_55',
              particles = [ P.n3, P.n1, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2513,(0,1):C.GC_2457})

V_56 = Vertex(name = 'V_56',
              particles = [ P.n4, P.n1, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2516,(0,1):C.GC_2460})

V_57 = Vertex(name = 'V_57',
              particles = [ P.n2, P.n2, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2512,(0,1):C.GC_2456})

V_58 = Vertex(name = 'V_58',
              particles = [ P.n3, P.n2, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2514,(0,1):C.GC_2458})

V_59 = Vertex(name = 'V_59',
              particles = [ P.n4, P.n2, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2517,(0,1):C.GC_2461})

V_60 = Vertex(name = 'V_60',
              particles = [ P.n3, P.n3, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2515,(0,1):C.GC_2459})

V_61 = Vertex(name = 'V_61',
              particles = [ P.n4, P.n3, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2518,(0,1):C.GC_2462})

V_62 = Vertex(name = 'V_62',
              particles = [ P.n4, P.n4, P.A0 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2519,(0,1):C.GC_2463})

V_63 = Vertex(name = 'V_63',
              particles = [ P.d__tilde__, P.d, P.h02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2198,(0,1):C.GC_2207})

V_64 = Vertex(name = 'V_64',
              particles = [ P.s__tilde__, P.s, P.h02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2199,(0,1):C.GC_2208})

V_65 = Vertex(name = 'V_65',
              particles = [ P.b__tilde__, P.b, P.h02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2200,(0,1):C.GC_2209})

V_66 = Vertex(name = 'V_66',
              particles = [ P.u__tilde__, P.d, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_2216,(0,0):C.GC_2405})

V_67 = Vertex(name = 'V_67',
              particles = [ P.c__tilde__, P.s, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_2217,(0,0):C.GC_2406})

V_68 = Vertex(name = 'V_68',
              particles = [ P.t__tilde__, P.b, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_2218,(0,0):C.GC_2407})

V_69 = Vertex(name = 'V_69',
              particles = [ P.e__plus__, P.e__minus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2201,(0,1):C.GC_2210})

V_70 = Vertex(name = 'V_70',
              particles = [ P.mu__plus__, P.mu__minus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2202,(0,1):C.GC_2211})

V_71 = Vertex(name = 'V_71',
              particles = [ P.tau__plus__, P.tau__minus__, P.h02 ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2203,(0,1):C.GC_2212})

V_72 = Vertex(name = 'V_72',
              particles = [ P.u__tilde__, P.u, P.h01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2204,(0,1):C.GC_2213})

V_73 = Vertex(name = 'V_73',
              particles = [ P.c__tilde__, P.c, P.h01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2205,(0,1):C.GC_2214})

V_74 = Vertex(name = 'V_74',
              particles = [ P.t__tilde__, P.t, P.h01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2206,(0,1):C.GC_2215})

V_75 = Vertex(name = 'V_75',
              particles = [ P.u__tilde__, P.u, P.A0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2222,(0,1):C.GC_2225})

V_76 = Vertex(name = 'V_76',
              particles = [ P.c__tilde__, P.c, P.A0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2223,(0,1):C.GC_2226})

V_77 = Vertex(name = 'V_77',
              particles = [ P.t__tilde__, P.t, P.A0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_2224,(0,1):C.GC_2227})

V_78 = Vertex(name = 'V_78',
              particles = [ P.n1, P.d, P.sd4__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1020,(0,0):C.GC_2004})

V_79 = Vertex(name = 'V_79',
              particles = [ P.n1, P.d, P.sd6__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1857,(0,1):C.GC_2014})

V_80 = Vertex(name = 'V_80',
              particles = [ P.n2, P.d, P.sd4__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1038,(0,0):C.GC_2005})

V_81 = Vertex(name = 'V_81',
              particles = [ P.n2, P.d, P.sd6__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1892,(0,1):C.GC_2015})

V_82 = Vertex(name = 'V_82',
              particles = [ P.n3, P.d, P.sd4__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1056,(0,0):C.GC_2006})

V_83 = Vertex(name = 'V_83',
              particles = [ P.n3, P.d, P.sd6__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1927,(0,1):C.GC_2016})

V_84 = Vertex(name = 'V_84',
              particles = [ P.n4, P.d, P.sd4__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1074,(0,0):C.GC_2007})

V_85 = Vertex(name = 'V_85',
              particles = [ P.n4, P.d, P.sd6__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1962,(0,1):C.GC_2017})

V_86 = Vertex(name = 'V_86',
              particles = [ P.n1, P.s, P.sd3__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1021,(0,0):C.GC_1999})

V_87 = Vertex(name = 'V_87',
              particles = [ P.n1, P.s, P.sd5__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1858,(0,1):C.GC_2009})

V_88 = Vertex(name = 'V_88',
              particles = [ P.n2, P.s, P.sd3__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1039,(0,0):C.GC_2000})

V_89 = Vertex(name = 'V_89',
              particles = [ P.n2, P.s, P.sd5__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1893,(0,1):C.GC_2010})

V_90 = Vertex(name = 'V_90',
              particles = [ P.n3, P.s, P.sd3__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1057,(0,0):C.GC_2001})

V_91 = Vertex(name = 'V_91',
              particles = [ P.n3, P.s, P.sd5__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1928,(0,1):C.GC_2011})

V_92 = Vertex(name = 'V_92',
              particles = [ P.n4, P.s, P.sd3__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,1):C.GC_1075,(0,0):C.GC_2002})

V_93 = Vertex(name = 'V_93',
              particles = [ P.n4, P.s, P.sd5__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1963,(0,1):C.GC_2012})

V_94 = Vertex(name = 'V_94',
              particles = [ P.n1, P.b, P.sd1__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1984,(0,1):C.GC_1979})

V_95 = Vertex(name = 'V_95',
              particles = [ P.n1, P.b, P.sd2__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1994,(0,1):C.GC_1989})

V_96 = Vertex(name = 'V_96',
              particles = [ P.n2, P.b, P.sd1__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1985,(0,1):C.GC_1980})

V_97 = Vertex(name = 'V_97',
              particles = [ P.n2, P.b, P.sd2__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1995,(0,1):C.GC_1990})

V_98 = Vertex(name = 'V_98',
              particles = [ P.n3, P.b, P.sd1__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1986,(0,1):C.GC_1981})

V_99 = Vertex(name = 'V_99',
              particles = [ P.n3, P.b, P.sd2__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_1996,(0,1):C.GC_1991})

V_100 = Vertex(name = 'V_100',
               particles = [ P.n4, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1987,(0,1):C.GC_1982})

V_101 = Vertex(name = 'V_101',
               particles = [ P.n4, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1997,(0,1):C.GC_1992})

V_102 = Vertex(name = 'V_102',
               particles = [ P.ve__tilde__, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_503})

V_103 = Vertex(name = 'V_103',
               particles = [ P.ve__tilde__, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_504})

V_104 = Vertex(name = 'V_104',
               particles = [ P.ve__tilde__, P.d, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_505})

V_105 = Vertex(name = 'V_105',
               particles = [ P.ve__tilde__, P.d, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_506})

V_106 = Vertex(name = 'V_106',
               particles = [ P.vm__tilde__, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_507})

V_107 = Vertex(name = 'V_107',
               particles = [ P.vm__tilde__, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_508})

V_108 = Vertex(name = 'V_108',
               particles = [ P.vm__tilde__, P.d, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_509})

V_109 = Vertex(name = 'V_109',
               particles = [ P.vm__tilde__, P.d, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_510})

V_110 = Vertex(name = 'V_110',
               particles = [ P.vt__tilde__, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_511})

V_111 = Vertex(name = 'V_111',
               particles = [ P.vt__tilde__, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_512})

V_112 = Vertex(name = 'V_112',
               particles = [ P.vt__tilde__, P.d, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_513})

V_113 = Vertex(name = 'V_113',
               particles = [ P.vt__tilde__, P.d, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_514})

V_114 = Vertex(name = 'V_114',
               particles = [ P.ve__tilde__, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_515})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ve__tilde__, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_516})

V_116 = Vertex(name = 'V_116',
               particles = [ P.ve__tilde__, P.s, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_517})

V_117 = Vertex(name = 'V_117',
               particles = [ P.ve__tilde__, P.s, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_518})

V_118 = Vertex(name = 'V_118',
               particles = [ P.vm__tilde__, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_519})

V_119 = Vertex(name = 'V_119',
               particles = [ P.vm__tilde__, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_520})

V_120 = Vertex(name = 'V_120',
               particles = [ P.vm__tilde__, P.s, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_521})

V_121 = Vertex(name = 'V_121',
               particles = [ P.vm__tilde__, P.s, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_522})

V_122 = Vertex(name = 'V_122',
               particles = [ P.vt__tilde__, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_523})

V_123 = Vertex(name = 'V_123',
               particles = [ P.vt__tilde__, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_524})

V_124 = Vertex(name = 'V_124',
               particles = [ P.vt__tilde__, P.s, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_525})

V_125 = Vertex(name = 'V_125',
               particles = [ P.vt__tilde__, P.s, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_526})

V_126 = Vertex(name = 'V_126',
               particles = [ P.ve__tilde__, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_527})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ve__tilde__, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_528})

V_128 = Vertex(name = 'V_128',
               particles = [ P.ve__tilde__, P.b, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_529})

V_129 = Vertex(name = 'V_129',
               particles = [ P.ve__tilde__, P.b, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_530})

V_130 = Vertex(name = 'V_130',
               particles = [ P.vm__tilde__, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_531})

V_131 = Vertex(name = 'V_131',
               particles = [ P.vm__tilde__, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_532})

V_132 = Vertex(name = 'V_132',
               particles = [ P.vm__tilde__, P.b, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_533})

V_133 = Vertex(name = 'V_133',
               particles = [ P.vm__tilde__, P.b, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_534})

V_134 = Vertex(name = 'V_134',
               particles = [ P.vt__tilde__, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_535})

V_135 = Vertex(name = 'V_135',
               particles = [ P.vt__tilde__, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_536})

V_136 = Vertex(name = 'V_136',
               particles = [ P.vt__tilde__, P.b, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_537})

V_137 = Vertex(name = 'V_137',
               particles = [ P.vt__tilde__, P.b, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_538})

V_138 = Vertex(name = 'V_138',
               particles = [ P.ve, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_559})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ve, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_560})

V_140 = Vertex(name = 'V_140',
               particles = [ P.ve, P.d, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_561})

V_141 = Vertex(name = 'V_141',
               particles = [ P.ve, P.d, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_562})

V_142 = Vertex(name = 'V_142',
               particles = [ P.vm, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_563})

V_143 = Vertex(name = 'V_143',
               particles = [ P.vm, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_564})

V_144 = Vertex(name = 'V_144',
               particles = [ P.vm, P.d, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_565})

V_145 = Vertex(name = 'V_145',
               particles = [ P.vm, P.d, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_566})

V_146 = Vertex(name = 'V_146',
               particles = [ P.vt, P.d, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_567})

V_147 = Vertex(name = 'V_147',
               particles = [ P.vt, P.d, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_568})

V_148 = Vertex(name = 'V_148',
               particles = [ P.vt, P.d, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_569})

V_149 = Vertex(name = 'V_149',
               particles = [ P.vt, P.d, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_570})

V_150 = Vertex(name = 'V_150',
               particles = [ P.ve, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_571})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ve, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_572})

V_152 = Vertex(name = 'V_152',
               particles = [ P.ve, P.s, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_573})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ve, P.s, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_574})

V_154 = Vertex(name = 'V_154',
               particles = [ P.vm, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_575})

V_155 = Vertex(name = 'V_155',
               particles = [ P.vm, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_576})

V_156 = Vertex(name = 'V_156',
               particles = [ P.vm, P.s, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_577})

V_157 = Vertex(name = 'V_157',
               particles = [ P.vm, P.s, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_578})

V_158 = Vertex(name = 'V_158',
               particles = [ P.vt, P.s, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_579})

V_159 = Vertex(name = 'V_159',
               particles = [ P.vt, P.s, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_580})

V_160 = Vertex(name = 'V_160',
               particles = [ P.vt, P.s, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_581})

V_161 = Vertex(name = 'V_161',
               particles = [ P.vt, P.s, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_582})

V_162 = Vertex(name = 'V_162',
               particles = [ P.ve, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_583})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ve, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_584})

V_164 = Vertex(name = 'V_164',
               particles = [ P.ve, P.b, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_585})

V_165 = Vertex(name = 'V_165',
               particles = [ P.ve, P.b, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_586})

V_166 = Vertex(name = 'V_166',
               particles = [ P.vm, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_587})

V_167 = Vertex(name = 'V_167',
               particles = [ P.vm, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_588})

V_168 = Vertex(name = 'V_168',
               particles = [ P.vm, P.b, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_589})

V_169 = Vertex(name = 'V_169',
               particles = [ P.vm, P.b, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_590})

V_170 = Vertex(name = 'V_170',
               particles = [ P.vt, P.b, P.sd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_591})

V_171 = Vertex(name = 'V_171',
               particles = [ P.vt, P.b, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_592})

V_172 = Vertex(name = 'V_172',
               particles = [ P.vt, P.b, P.sd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_593})

V_173 = Vertex(name = 'V_173',
               particles = [ P.vt, P.b, P.sd4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_594})

V_174 = Vertex(name = 'V_174',
               particles = [ P.u, P.e__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_660})

V_175 = Vertex(name = 'V_175',
               particles = [ P.u, P.e__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_661})

V_176 = Vertex(name = 'V_176',
               particles = [ P.u, P.e__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_662})

V_177 = Vertex(name = 'V_177',
               particles = [ P.u, P.e__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_663})

V_178 = Vertex(name = 'V_178',
               particles = [ P.c, P.e__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_664})

V_179 = Vertex(name = 'V_179',
               particles = [ P.c, P.e__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_665})

V_180 = Vertex(name = 'V_180',
               particles = [ P.c, P.e__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_666})

V_181 = Vertex(name = 'V_181',
               particles = [ P.c, P.e__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_667})

V_182 = Vertex(name = 'V_182',
               particles = [ P.t, P.e__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_668})

V_183 = Vertex(name = 'V_183',
               particles = [ P.t, P.e__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_669})

V_184 = Vertex(name = 'V_184',
               particles = [ P.t, P.e__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_670})

V_185 = Vertex(name = 'V_185',
               particles = [ P.t, P.e__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_671})

V_186 = Vertex(name = 'V_186',
               particles = [ P.u, P.mu__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_672})

V_187 = Vertex(name = 'V_187',
               particles = [ P.u, P.mu__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_673})

V_188 = Vertex(name = 'V_188',
               particles = [ P.u, P.mu__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_674})

V_189 = Vertex(name = 'V_189',
               particles = [ P.u, P.mu__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_675})

V_190 = Vertex(name = 'V_190',
               particles = [ P.c, P.mu__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_676})

V_191 = Vertex(name = 'V_191',
               particles = [ P.c, P.mu__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_677})

V_192 = Vertex(name = 'V_192',
               particles = [ P.c, P.mu__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_678})

V_193 = Vertex(name = 'V_193',
               particles = [ P.c, P.mu__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_679})

V_194 = Vertex(name = 'V_194',
               particles = [ P.t, P.mu__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_680})

V_195 = Vertex(name = 'V_195',
               particles = [ P.t, P.mu__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_681})

V_196 = Vertex(name = 'V_196',
               particles = [ P.t, P.mu__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_682})

V_197 = Vertex(name = 'V_197',
               particles = [ P.t, P.mu__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_683})

V_198 = Vertex(name = 'V_198',
               particles = [ P.u, P.tau__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_684})

V_199 = Vertex(name = 'V_199',
               particles = [ P.u, P.tau__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_685})

V_200 = Vertex(name = 'V_200',
               particles = [ P.u, P.tau__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_686})

V_201 = Vertex(name = 'V_201',
               particles = [ P.u, P.tau__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_687})

V_202 = Vertex(name = 'V_202',
               particles = [ P.c, P.tau__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_688})

V_203 = Vertex(name = 'V_203',
               particles = [ P.c, P.tau__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_689})

V_204 = Vertex(name = 'V_204',
               particles = [ P.c, P.tau__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_690})

V_205 = Vertex(name = 'V_205',
               particles = [ P.c, P.tau__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_691})

V_206 = Vertex(name = 'V_206',
               particles = [ P.t, P.tau__minus__, P.sd1__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_692})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t, P.tau__minus__, P.sd2__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_693})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t, P.tau__minus__, P.sd3__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_694})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t, P.tau__minus__, P.sd4__tilde__ ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_695})

V_210 = Vertex(name = 'V_210',
               particles = [ P.a, P.sd1__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_772})

V_211 = Vertex(name = 'V_211',
               particles = [ P.a, P.sd1__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_774})

V_212 = Vertex(name = 'V_212',
               particles = [ P.a, P.sd1, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_776})

V_213 = Vertex(name = 'V_213',
               particles = [ P.a, P.sd2__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_778})

V_214 = Vertex(name = 'V_214',
               particles = [ P.a, P.sd3__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_780})

V_215 = Vertex(name = 'V_215',
               particles = [ P.a, P.sd4__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_782})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.sd5__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_748})

V_217 = Vertex(name = 'V_217',
               particles = [ P.a, P.sd6__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_750})

V_218 = Vertex(name = 'V_218',
               particles = [ P.u__tilde__, P.d__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_60})

V_219 = Vertex(name = 'V_219',
               particles = [ P.u__tilde__, P.d__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_61})

V_220 = Vertex(name = 'V_220',
               particles = [ P.u__tilde__, P.d__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_62})

V_221 = Vertex(name = 'V_221',
               particles = [ P.c__tilde__, P.d__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_63})

V_222 = Vertex(name = 'V_222',
               particles = [ P.c__tilde__, P.d__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_64})

V_223 = Vertex(name = 'V_223',
               particles = [ P.c__tilde__, P.d__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_65})

V_224 = Vertex(name = 'V_224',
               particles = [ P.t__tilde__, P.d__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_66})

V_225 = Vertex(name = 'V_225',
               particles = [ P.t__tilde__, P.d__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_67})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.d__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_68})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.s__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_69})

V_228 = Vertex(name = 'V_228',
               particles = [ P.u__tilde__, P.s__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_70})

V_229 = Vertex(name = 'V_229',
               particles = [ P.u__tilde__, P.s__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_71})

V_230 = Vertex(name = 'V_230',
               particles = [ P.c__tilde__, P.s__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_72})

V_231 = Vertex(name = 'V_231',
               particles = [ P.c__tilde__, P.s__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_73})

V_232 = Vertex(name = 'V_232',
               particles = [ P.c__tilde__, P.s__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_74})

V_233 = Vertex(name = 'V_233',
               particles = [ P.t__tilde__, P.s__tilde__, P.sd1__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_75})

V_234 = Vertex(name = 'V_234',
               particles = [ P.t__tilde__, P.s__tilde__, P.sd2__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_76})

V_235 = Vertex(name = 'V_235',
               particles = [ P.t__tilde__, P.s__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_77})

V_236 = Vertex(name = 'V_236',
               particles = [ P.u__tilde__, P.b__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_78})

V_237 = Vertex(name = 'V_237',
               particles = [ P.u__tilde__, P.b__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_79})

V_238 = Vertex(name = 'V_238',
               particles = [ P.c__tilde__, P.b__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_80})

V_239 = Vertex(name = 'V_239',
               particles = [ P.c__tilde__, P.b__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_81})

V_240 = Vertex(name = 'V_240',
               particles = [ P.t__tilde__, P.b__tilde__, P.sd3__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_82})

V_241 = Vertex(name = 'V_241',
               particles = [ P.t__tilde__, P.b__tilde__, P.sd4__tilde__ ],
               color = [ 'EpsilonBar(1,2,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_83})

V_242 = Vertex(name = 'V_242',
               particles = [ P.d__tilde__, P.n1, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1847,(0,1):C.GC_900})

V_243 = Vertex(name = 'V_243',
               particles = [ P.d__tilde__, P.n1, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1014,(0,0):C.GC_1839})

V_244 = Vertex(name = 'V_244',
               particles = [ P.s__tilde__, P.n1, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1848,(0,1):C.GC_896})

V_245 = Vertex(name = 'V_245',
               particles = [ P.s__tilde__, P.n1, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1015,(0,0):C.GC_1838})

V_246 = Vertex(name = 'V_246',
               particles = [ P.b__tilde__, P.n1, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1849,(0,1):C.GC_1016})

V_247 = Vertex(name = 'V_247',
               particles = [ P.b__tilde__, P.n1, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1850,(0,1):C.GC_1017})

V_248 = Vertex(name = 'V_248',
               particles = [ P.d__tilde__, P.n2, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1882,(0,1):C.GC_901})

V_249 = Vertex(name = 'V_249',
               particles = [ P.d__tilde__, P.n2, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1032,(0,0):C.GC_1874})

V_250 = Vertex(name = 'V_250',
               particles = [ P.s__tilde__, P.n2, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1883,(0,1):C.GC_897})

V_251 = Vertex(name = 'V_251',
               particles = [ P.s__tilde__, P.n2, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1033,(0,0):C.GC_1873})

V_252 = Vertex(name = 'V_252',
               particles = [ P.b__tilde__, P.n2, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1884,(0,1):C.GC_1034})

V_253 = Vertex(name = 'V_253',
               particles = [ P.b__tilde__, P.n2, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1885,(0,1):C.GC_1035})

V_254 = Vertex(name = 'V_254',
               particles = [ P.d__tilde__, P.n3, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1917,(0,1):C.GC_902})

V_255 = Vertex(name = 'V_255',
               particles = [ P.d__tilde__, P.n3, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1050,(0,0):C.GC_1909})

V_256 = Vertex(name = 'V_256',
               particles = [ P.s__tilde__, P.n3, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1918,(0,1):C.GC_898})

V_257 = Vertex(name = 'V_257',
               particles = [ P.s__tilde__, P.n3, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1051,(0,0):C.GC_1908})

V_258 = Vertex(name = 'V_258',
               particles = [ P.b__tilde__, P.n3, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1919,(0,1):C.GC_1052})

V_259 = Vertex(name = 'V_259',
               particles = [ P.b__tilde__, P.n3, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1920,(0,1):C.GC_1053})

V_260 = Vertex(name = 'V_260',
               particles = [ P.d__tilde__, P.n4, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1952,(0,1):C.GC_903})

V_261 = Vertex(name = 'V_261',
               particles = [ P.d__tilde__, P.n4, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1068,(0,0):C.GC_1944})

V_262 = Vertex(name = 'V_262',
               particles = [ P.s__tilde__, P.n4, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1953,(0,1):C.GC_899})

V_263 = Vertex(name = 'V_263',
               particles = [ P.s__tilde__, P.n4, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1069,(0,0):C.GC_1943})

V_264 = Vertex(name = 'V_264',
               particles = [ P.b__tilde__, P.n4, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1954,(0,1):C.GC_1070})

V_265 = Vertex(name = 'V_265',
               particles = [ P.b__tilde__, P.n4, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1955,(0,1):C.GC_1071})

V_266 = Vertex(name = 'V_266',
               particles = [ P.u__tilde__, P.x1__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2113})

V_267 = Vertex(name = 'V_267',
               particles = [ P.u__tilde__, P.x1__plus__, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2102,(0,1):C.GC_1819})

V_268 = Vertex(name = 'V_268',
               particles = [ P.c__tilde__, P.x1__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2114})

V_269 = Vertex(name = 'V_269',
               particles = [ P.c__tilde__, P.x1__plus__, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2103,(0,1):C.GC_1820})

V_270 = Vertex(name = 'V_270',
               particles = [ P.t__tilde__, P.x1__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2117,(0,1):C.GC_1821})

V_271 = Vertex(name = 'V_271',
               particles = [ P.t__tilde__, P.x1__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2118,(0,1):C.GC_1822})

V_272 = Vertex(name = 'V_272',
               particles = [ P.u__tilde__, P.x2__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2140})

V_273 = Vertex(name = 'V_273',
               particles = [ P.u__tilde__, P.x2__plus__, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2129,(0,1):C.GC_1832})

V_274 = Vertex(name = 'V_274',
               particles = [ P.c__tilde__, P.x2__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2141})

V_275 = Vertex(name = 'V_275',
               particles = [ P.c__tilde__, P.x2__plus__, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2130,(0,1):C.GC_1833})

V_276 = Vertex(name = 'V_276',
               particles = [ P.t__tilde__, P.x2__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2144,(0,1):C.GC_1834})

V_277 = Vertex(name = 'V_277',
               particles = [ P.t__tilde__, P.x2__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2145,(0,1):C.GC_1835})

V_278 = Vertex(name = 'V_278',
               particles = [ P.d__tilde__, P.ve, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_118})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.ve, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_119})

V_280 = Vertex(name = 'V_280',
               particles = [ P.d__tilde__, P.ve, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_120})

V_281 = Vertex(name = 'V_281',
               particles = [ P.d__tilde__, P.ve, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_121})

V_282 = Vertex(name = 'V_282',
               particles = [ P.s__tilde__, P.ve, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_122})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.ve, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_123})

V_284 = Vertex(name = 'V_284',
               particles = [ P.s__tilde__, P.ve, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_124})

V_285 = Vertex(name = 'V_285',
               particles = [ P.s__tilde__, P.ve, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_125})

V_286 = Vertex(name = 'V_286',
               particles = [ P.b__tilde__, P.ve, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_126})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.ve, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_127})

V_288 = Vertex(name = 'V_288',
               particles = [ P.b__tilde__, P.ve, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_128})

V_289 = Vertex(name = 'V_289',
               particles = [ P.b__tilde__, P.ve, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_129})

V_290 = Vertex(name = 'V_290',
               particles = [ P.d__tilde__, P.vm, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_130})

V_291 = Vertex(name = 'V_291',
               particles = [ P.d__tilde__, P.vm, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_131})

V_292 = Vertex(name = 'V_292',
               particles = [ P.d__tilde__, P.vm, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_132})

V_293 = Vertex(name = 'V_293',
               particles = [ P.d__tilde__, P.vm, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_133})

V_294 = Vertex(name = 'V_294',
               particles = [ P.s__tilde__, P.vm, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_134})

V_295 = Vertex(name = 'V_295',
               particles = [ P.s__tilde__, P.vm, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_135})

V_296 = Vertex(name = 'V_296',
               particles = [ P.s__tilde__, P.vm, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_136})

V_297 = Vertex(name = 'V_297',
               particles = [ P.s__tilde__, P.vm, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_137})

V_298 = Vertex(name = 'V_298',
               particles = [ P.b__tilde__, P.vm, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_138})

V_299 = Vertex(name = 'V_299',
               particles = [ P.b__tilde__, P.vm, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_139})

V_300 = Vertex(name = 'V_300',
               particles = [ P.b__tilde__, P.vm, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_140})

V_301 = Vertex(name = 'V_301',
               particles = [ P.b__tilde__, P.vm, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_141})

V_302 = Vertex(name = 'V_302',
               particles = [ P.d__tilde__, P.vt, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_142})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.vt, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_143})

V_304 = Vertex(name = 'V_304',
               particles = [ P.d__tilde__, P.vt, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_144})

V_305 = Vertex(name = 'V_305',
               particles = [ P.d__tilde__, P.vt, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_145})

V_306 = Vertex(name = 'V_306',
               particles = [ P.s__tilde__, P.vt, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_146})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.vt, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_147})

V_308 = Vertex(name = 'V_308',
               particles = [ P.s__tilde__, P.vt, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_148})

V_309 = Vertex(name = 'V_309',
               particles = [ P.s__tilde__, P.vt, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_149})

V_310 = Vertex(name = 'V_310',
               particles = [ P.b__tilde__, P.vt, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_150})

V_311 = Vertex(name = 'V_311',
               particles = [ P.b__tilde__, P.vt, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_151})

V_312 = Vertex(name = 'V_312',
               particles = [ P.b__tilde__, P.vt, P.sd5 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_152})

V_313 = Vertex(name = 'V_313',
               particles = [ P.b__tilde__, P.vt, P.sd6 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_153})

V_314 = Vertex(name = 'V_314',
               particles = [ P.ve__tilde__, P.d__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_154})

V_315 = Vertex(name = 'V_315',
               particles = [ P.ve__tilde__, P.d__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_155})

V_316 = Vertex(name = 'V_316',
               particles = [ P.ve__tilde__, P.d__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_156})

V_317 = Vertex(name = 'V_317',
               particles = [ P.ve__tilde__, P.d__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_157})

V_318 = Vertex(name = 'V_318',
               particles = [ P.vm__tilde__, P.d__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_158})

V_319 = Vertex(name = 'V_319',
               particles = [ P.vm__tilde__, P.d__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_159})

V_320 = Vertex(name = 'V_320',
               particles = [ P.vm__tilde__, P.d__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_160})

V_321 = Vertex(name = 'V_321',
               particles = [ P.vm__tilde__, P.d__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_161})

V_322 = Vertex(name = 'V_322',
               particles = [ P.vt__tilde__, P.d__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_162})

V_323 = Vertex(name = 'V_323',
               particles = [ P.vt__tilde__, P.d__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_163})

V_324 = Vertex(name = 'V_324',
               particles = [ P.vt__tilde__, P.d__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_164})

V_325 = Vertex(name = 'V_325',
               particles = [ P.vt__tilde__, P.d__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_165})

V_326 = Vertex(name = 'V_326',
               particles = [ P.ve__tilde__, P.s__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_166})

V_327 = Vertex(name = 'V_327',
               particles = [ P.ve__tilde__, P.s__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_167})

V_328 = Vertex(name = 'V_328',
               particles = [ P.ve__tilde__, P.s__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_168})

V_329 = Vertex(name = 'V_329',
               particles = [ P.ve__tilde__, P.s__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_169})

V_330 = Vertex(name = 'V_330',
               particles = [ P.vm__tilde__, P.s__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_170})

V_331 = Vertex(name = 'V_331',
               particles = [ P.vm__tilde__, P.s__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_171})

V_332 = Vertex(name = 'V_332',
               particles = [ P.vm__tilde__, P.s__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_172})

V_333 = Vertex(name = 'V_333',
               particles = [ P.vm__tilde__, P.s__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_173})

V_334 = Vertex(name = 'V_334',
               particles = [ P.vt__tilde__, P.s__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_174})

V_335 = Vertex(name = 'V_335',
               particles = [ P.vt__tilde__, P.s__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_175})

V_336 = Vertex(name = 'V_336',
               particles = [ P.vt__tilde__, P.s__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_176})

V_337 = Vertex(name = 'V_337',
               particles = [ P.vt__tilde__, P.s__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_177})

V_338 = Vertex(name = 'V_338',
               particles = [ P.ve__tilde__, P.b__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_178})

V_339 = Vertex(name = 'V_339',
               particles = [ P.ve__tilde__, P.b__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_179})

V_340 = Vertex(name = 'V_340',
               particles = [ P.ve__tilde__, P.b__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_180})

V_341 = Vertex(name = 'V_341',
               particles = [ P.ve__tilde__, P.b__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_181})

V_342 = Vertex(name = 'V_342',
               particles = [ P.vm__tilde__, P.b__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_182})

V_343 = Vertex(name = 'V_343',
               particles = [ P.vm__tilde__, P.b__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_183})

V_344 = Vertex(name = 'V_344',
               particles = [ P.vm__tilde__, P.b__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_184})

V_345 = Vertex(name = 'V_345',
               particles = [ P.vm__tilde__, P.b__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_185})

V_346 = Vertex(name = 'V_346',
               particles = [ P.vt__tilde__, P.b__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_186})

V_347 = Vertex(name = 'V_347',
               particles = [ P.vt__tilde__, P.b__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_187})

V_348 = Vertex(name = 'V_348',
               particles = [ P.vt__tilde__, P.b__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_188})

V_349 = Vertex(name = 'V_349',
               particles = [ P.vt__tilde__, P.b__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_189})

V_350 = Vertex(name = 'V_350',
               particles = [ P.u__tilde__, P.e__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_190})

V_351 = Vertex(name = 'V_351',
               particles = [ P.u__tilde__, P.e__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_191})

V_352 = Vertex(name = 'V_352',
               particles = [ P.u__tilde__, P.e__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_192})

V_353 = Vertex(name = 'V_353',
               particles = [ P.u__tilde__, P.e__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_193})

V_354 = Vertex(name = 'V_354',
               particles = [ P.c__tilde__, P.e__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_194})

V_355 = Vertex(name = 'V_355',
               particles = [ P.c__tilde__, P.e__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_195})

V_356 = Vertex(name = 'V_356',
               particles = [ P.c__tilde__, P.e__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_196})

V_357 = Vertex(name = 'V_357',
               particles = [ P.c__tilde__, P.e__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_197})

V_358 = Vertex(name = 'V_358',
               particles = [ P.t__tilde__, P.e__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_198})

V_359 = Vertex(name = 'V_359',
               particles = [ P.t__tilde__, P.e__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_199})

V_360 = Vertex(name = 'V_360',
               particles = [ P.t__tilde__, P.e__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_200})

V_361 = Vertex(name = 'V_361',
               particles = [ P.t__tilde__, P.e__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_201})

V_362 = Vertex(name = 'V_362',
               particles = [ P.u__tilde__, P.mu__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_202})

V_363 = Vertex(name = 'V_363',
               particles = [ P.u__tilde__, P.mu__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_203})

V_364 = Vertex(name = 'V_364',
               particles = [ P.u__tilde__, P.mu__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_204})

V_365 = Vertex(name = 'V_365',
               particles = [ P.u__tilde__, P.mu__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_205})

V_366 = Vertex(name = 'V_366',
               particles = [ P.c__tilde__, P.mu__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_206})

V_367 = Vertex(name = 'V_367',
               particles = [ P.c__tilde__, P.mu__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_207})

V_368 = Vertex(name = 'V_368',
               particles = [ P.c__tilde__, P.mu__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_208})

V_369 = Vertex(name = 'V_369',
               particles = [ P.c__tilde__, P.mu__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_209})

V_370 = Vertex(name = 'V_370',
               particles = [ P.t__tilde__, P.mu__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_210})

V_371 = Vertex(name = 'V_371',
               particles = [ P.t__tilde__, P.mu__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_211})

V_372 = Vertex(name = 'V_372',
               particles = [ P.t__tilde__, P.mu__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_212})

V_373 = Vertex(name = 'V_373',
               particles = [ P.t__tilde__, P.mu__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_213})

V_374 = Vertex(name = 'V_374',
               particles = [ P.u__tilde__, P.tau__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_214})

V_375 = Vertex(name = 'V_375',
               particles = [ P.u__tilde__, P.tau__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_215})

V_376 = Vertex(name = 'V_376',
               particles = [ P.u__tilde__, P.tau__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_216})

V_377 = Vertex(name = 'V_377',
               particles = [ P.u__tilde__, P.tau__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_217})

V_378 = Vertex(name = 'V_378',
               particles = [ P.c__tilde__, P.tau__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_218})

V_379 = Vertex(name = 'V_379',
               particles = [ P.c__tilde__, P.tau__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_219})

V_380 = Vertex(name = 'V_380',
               particles = [ P.c__tilde__, P.tau__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_220})

V_381 = Vertex(name = 'V_381',
               particles = [ P.c__tilde__, P.tau__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_221})

V_382 = Vertex(name = 'V_382',
               particles = [ P.t__tilde__, P.tau__plus__, P.sd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_222})

V_383 = Vertex(name = 'V_383',
               particles = [ P.t__tilde__, P.tau__plus__, P.sd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_223})

V_384 = Vertex(name = 'V_384',
               particles = [ P.t__tilde__, P.tau__plus__, P.sd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_224})

V_385 = Vertex(name = 'V_385',
               particles = [ P.t__tilde__, P.tau__plus__, P.sd4 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_225})

V_386 = Vertex(name = 'V_386',
               particles = [ P.u, P.d, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_226})

V_387 = Vertex(name = 'V_387',
               particles = [ P.u, P.d, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_227})

V_388 = Vertex(name = 'V_388',
               particles = [ P.u, P.d, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_228})

V_389 = Vertex(name = 'V_389',
               particles = [ P.c, P.d, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_229})

V_390 = Vertex(name = 'V_390',
               particles = [ P.c, P.d, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_230})

V_391 = Vertex(name = 'V_391',
               particles = [ P.c, P.d, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_231})

V_392 = Vertex(name = 'V_392',
               particles = [ P.t, P.d, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_232})

V_393 = Vertex(name = 'V_393',
               particles = [ P.t, P.d, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_233})

V_394 = Vertex(name = 'V_394',
               particles = [ P.t, P.d, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_234})

V_395 = Vertex(name = 'V_395',
               particles = [ P.u, P.s, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_235})

V_396 = Vertex(name = 'V_396',
               particles = [ P.u, P.s, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_236})

V_397 = Vertex(name = 'V_397',
               particles = [ P.u, P.s, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_237})

V_398 = Vertex(name = 'V_398',
               particles = [ P.c, P.s, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_238})

V_399 = Vertex(name = 'V_399',
               particles = [ P.c, P.s, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_239})

V_400 = Vertex(name = 'V_400',
               particles = [ P.c, P.s, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_240})

V_401 = Vertex(name = 'V_401',
               particles = [ P.t, P.s, P.sd1 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_241})

V_402 = Vertex(name = 'V_402',
               particles = [ P.t, P.s, P.sd2 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_242})

V_403 = Vertex(name = 'V_403',
               particles = [ P.t, P.s, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_243})

V_404 = Vertex(name = 'V_404',
               particles = [ P.u, P.b, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_244})

V_405 = Vertex(name = 'V_405',
               particles = [ P.u, P.b, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_245})

V_406 = Vertex(name = 'V_406',
               particles = [ P.c, P.b, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_246})

V_407 = Vertex(name = 'V_407',
               particles = [ P.c, P.b, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_247})

V_408 = Vertex(name = 'V_408',
               particles = [ P.t, P.b, P.sd3 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_248})

V_409 = Vertex(name = 'V_409',
               particles = [ P.t, P.b, P.sd4 ],
               color = [ 'Epsilon(1,2,3)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_249})

V_410 = Vertex(name = 'V_410',
               particles = [ P.a, P.a, P.sd1__tilde__, P.sd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_256})

V_411 = Vertex(name = 'V_411',
               particles = [ P.a, P.a, P.sd1__tilde__, P.sd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_259})

V_412 = Vertex(name = 'V_412',
               particles = [ P.a, P.a, P.sd1, P.sd2__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_262})

V_413 = Vertex(name = 'V_413',
               particles = [ P.a, P.a, P.sd2__tilde__, P.sd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_265})

V_414 = Vertex(name = 'V_414',
               particles = [ P.a, P.a, P.sd3__tilde__, P.sd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_268})

V_415 = Vertex(name = 'V_415',
               particles = [ P.a, P.a, P.sd4__tilde__, P.sd4 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_271})

V_416 = Vertex(name = 'V_416',
               particles = [ P.a, P.a, P.sd5__tilde__, P.sd5 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_250})

V_417 = Vertex(name = 'V_417',
               particles = [ P.a, P.a, P.sd6__tilde__, P.sd6 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_253})

V_418 = Vertex(name = 'V_418',
               particles = [ P.h02, P.sd1__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2356})

V_419 = Vertex(name = 'V_419',
               particles = [ P.h02, P.sd1__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2357})

V_420 = Vertex(name = 'V_420',
               particles = [ P.h02, P.sd1, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2358})

V_421 = Vertex(name = 'V_421',
               particles = [ P.h02, P.sd2__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2359})

V_422 = Vertex(name = 'V_422',
               particles = [ P.h02, P.sd3__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2326})

V_423 = Vertex(name = 'V_423',
               particles = [ P.h02, P.sd3__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2296})

V_424 = Vertex(name = 'V_424',
               particles = [ P.h02, P.sd4__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2327})

V_425 = Vertex(name = 'V_425',
               particles = [ P.h02, P.sd4__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2297})

V_426 = Vertex(name = 'V_426',
               particles = [ P.h02, P.sd3, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2360})

V_427 = Vertex(name = 'V_427',
               particles = [ P.h02, P.sd5__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2332})

V_428 = Vertex(name = 'V_428',
               particles = [ P.h02, P.sd4, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2361})

V_429 = Vertex(name = 'V_429',
               particles = [ P.h02, P.sd6__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2333})

V_430 = Vertex(name = 'V_430',
               particles = [ P.h01, P.sd1__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2309})

V_431 = Vertex(name = 'V_431',
               particles = [ P.h01, P.sd1__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2310})

V_432 = Vertex(name = 'V_432',
               particles = [ P.h01, P.sd1, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2311})

V_433 = Vertex(name = 'V_433',
               particles = [ P.h01, P.sd2__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2312})

V_434 = Vertex(name = 'V_434',
               particles = [ P.h01, P.sd3__tilde__, P.sd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2313})

V_435 = Vertex(name = 'V_435',
               particles = [ P.h01, P.sd3__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2286})

V_436 = Vertex(name = 'V_436',
               particles = [ P.h01, P.sd4__tilde__, P.sd4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2314})

V_437 = Vertex(name = 'V_437',
               particles = [ P.h01, P.sd4__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2287})

V_438 = Vertex(name = 'V_438',
               particles = [ P.h01, P.sd3, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2288})

V_439 = Vertex(name = 'V_439',
               particles = [ P.h01, P.sd5__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2307})

V_440 = Vertex(name = 'V_440',
               particles = [ P.h01, P.sd4, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2289})

V_441 = Vertex(name = 'V_441',
               particles = [ P.h01, P.sd6__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2308})

V_442 = Vertex(name = 'V_442',
               particles = [ P.A0, P.sd1__tilde__, P.sd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2430})

V_443 = Vertex(name = 'V_443',
               particles = [ P.A0, P.sd1__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2431})

V_444 = Vertex(name = 'V_444',
               particles = [ P.A0, P.sd1, P.sd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2432})

V_445 = Vertex(name = 'V_445',
               particles = [ P.A0, P.sd2__tilde__, P.sd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2433})

V_446 = Vertex(name = 'V_446',
               particles = [ P.A0, P.sd3__tilde__, P.sd5 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2428})

V_447 = Vertex(name = 'V_447',
               particles = [ P.A0, P.sd4__tilde__, P.sd6 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2429})

V_448 = Vertex(name = 'V_448',
               particles = [ P.A0, P.sd3, P.sd5__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2434})

V_449 = Vertex(name = 'V_449',
               particles = [ P.A0, P.sd4, P.sd6__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2435})

V_450 = Vertex(name = 'V_450',
               particles = [ P.d__tilde__, P.d, P.h01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2244,(0,1):C.GC_2253})

V_451 = Vertex(name = 'V_451',
               particles = [ P.s__tilde__, P.s, P.h01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2245,(0,1):C.GC_2254})

V_452 = Vertex(name = 'V_452',
               particles = [ P.b__tilde__, P.b, P.h01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2246,(0,1):C.GC_2255})

V_453 = Vertex(name = 'V_453',
               particles = [ P.e__plus__, P.e__minus__, P.h01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2247,(0,1):C.GC_2256})

V_454 = Vertex(name = 'V_454',
               particles = [ P.mu__plus__, P.mu__minus__, P.h01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2248,(0,1):C.GC_2257})

V_455 = Vertex(name = 'V_455',
               particles = [ P.tau__plus__, P.tau__minus__, P.h01 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2249,(0,1):C.GC_2258})

V_456 = Vertex(name = 'V_456',
               particles = [ P.u__tilde__, P.u, P.h02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2250,(0,1):C.GC_2259})

V_457 = Vertex(name = 'V_457',
               particles = [ P.c__tilde__, P.c, P.h02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2251,(0,1):C.GC_2260})

V_458 = Vertex(name = 'V_458',
               particles = [ P.t__tilde__, P.t, P.h02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2252,(0,1):C.GC_2261})

V_459 = Vertex(name = 'V_459',
               particles = [ P.n1, P.x1__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2228,(0,0):C.GC_2520})

V_460 = Vertex(name = 'V_460',
               particles = [ P.n2, P.x1__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2229,(0,0):C.GC_2521})

V_461 = Vertex(name = 'V_461',
               particles = [ P.n3, P.x1__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2230,(0,0):C.GC_2522})

V_462 = Vertex(name = 'V_462',
               particles = [ P.n4, P.x1__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2231,(0,0):C.GC_2523})

V_463 = Vertex(name = 'V_463',
               particles = [ P.n1, P.x2__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2232,(0,0):C.GC_2524})

V_464 = Vertex(name = 'V_464',
               particles = [ P.n2, P.x2__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2233,(0,0):C.GC_2525})

V_465 = Vertex(name = 'V_465',
               particles = [ P.n3, P.x2__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2234,(0,0):C.GC_2526})

V_466 = Vertex(name = 'V_466',
               particles = [ P.n4, P.x2__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_2235,(0,0):C.GC_2527})

V_467 = Vertex(name = 'V_467',
               particles = [ P.d__tilde__, P.d, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2414,(0,1):C.GC_2420})

V_468 = Vertex(name = 'V_468',
               particles = [ P.s__tilde__, P.s, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2415,(0,1):C.GC_2421})

V_469 = Vertex(name = 'V_469',
               particles = [ P.b__tilde__, P.b, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2416,(0,1):C.GC_2422})

V_470 = Vertex(name = 'V_470',
               particles = [ P.e__plus__, P.e__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2417,(0,1):C.GC_2423})

V_471 = Vertex(name = 'V_471',
               particles = [ P.mu__plus__, P.mu__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2418,(0,1):C.GC_2424})

V_472 = Vertex(name = 'V_472',
               particles = [ P.tau__plus__, P.tau__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2419,(0,1):C.GC_2425})

V_473 = Vertex(name = 'V_473',
               particles = [ P.d__tilde__, P.u, P.H__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2219,(0,1):C.GC_2408})

V_474 = Vertex(name = 'V_474',
               particles = [ P.s__tilde__, P.c, P.H__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2220,(0,1):C.GC_2409})

V_475 = Vertex(name = 'V_475',
               particles = [ P.b__tilde__, P.t, P.H__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2221,(0,1):C.GC_2410})

V_476 = Vertex(name = 'V_476',
               particles = [ P.e__plus__, P.ve, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2411})

V_477 = Vertex(name = 'V_477',
               particles = [ P.mu__plus__, P.vm, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2412})

V_478 = Vertex(name = 'V_478',
               particles = [ P.tau__plus__, P.vt, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2413})

V_479 = Vertex(name = 'V_479',
               particles = [ P.n1, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1018,(0,0):C.GC_2030})

V_480 = Vertex(name = 'V_480',
               particles = [ P.n1, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1851,(0,1):C.GC_2034})

V_481 = Vertex(name = 'V_481',
               particles = [ P.n2, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1036,(0,0):C.GC_2031})

V_482 = Vertex(name = 'V_482',
               particles = [ P.n2, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1886,(0,1):C.GC_2035})

V_483 = Vertex(name = 'V_483',
               particles = [ P.n3, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1054,(0,0):C.GC_2032})

V_484 = Vertex(name = 'V_484',
               particles = [ P.n3, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1921,(0,1):C.GC_2036})

V_485 = Vertex(name = 'V_485',
               particles = [ P.n4, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1072,(0,0):C.GC_2033})

V_486 = Vertex(name = 'V_486',
               particles = [ P.n4, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1956,(0,1):C.GC_2037})

V_487 = Vertex(name = 'V_487',
               particles = [ P.n1, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1019,(0,0):C.GC_2026})

V_488 = Vertex(name = 'V_488',
               particles = [ P.n1, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1852,(0,1):C.GC_2038})

V_489 = Vertex(name = 'V_489',
               particles = [ P.n2, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1037,(0,0):C.GC_2027})

V_490 = Vertex(name = 'V_490',
               particles = [ P.n2, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1887,(0,1):C.GC_2039})

V_491 = Vertex(name = 'V_491',
               particles = [ P.n3, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1055,(0,0):C.GC_2028})

V_492 = Vertex(name = 'V_492',
               particles = [ P.n3, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1922,(0,1):C.GC_2040})

V_493 = Vertex(name = 'V_493',
               particles = [ P.n4, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1073,(0,0):C.GC_2029})

V_494 = Vertex(name = 'V_494',
               particles = [ P.n4, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1957,(0,1):C.GC_2041})

V_495 = Vertex(name = 'V_495',
               particles = [ P.n1, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2022,(0,1):C.GC_2018})

V_496 = Vertex(name = 'V_496',
               particles = [ P.n1, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2046,(0,1):C.GC_2042})

V_497 = Vertex(name = 'V_497',
               particles = [ P.n2, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2023,(0,1):C.GC_2019})

V_498 = Vertex(name = 'V_498',
               particles = [ P.n2, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2047,(0,1):C.GC_2043})

V_499 = Vertex(name = 'V_499',
               particles = [ P.n3, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2024,(0,1):C.GC_2020})

V_500 = Vertex(name = 'V_500',
               particles = [ P.n3, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2048,(0,1):C.GC_2044})

V_501 = Vertex(name = 'V_501',
               particles = [ P.n4, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2025,(0,1):C.GC_2021})

V_502 = Vertex(name = 'V_502',
               particles = [ P.n4, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2049,(0,1):C.GC_2045})

V_503 = Vertex(name = 'V_503',
               particles = [ P.ve__tilde__, P.e__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_274})

V_504 = Vertex(name = 'V_504',
               particles = [ P.ve__tilde__, P.e__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_275})

V_505 = Vertex(name = 'V_505',
               particles = [ P.ve__tilde__, P.e__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_276})

V_506 = Vertex(name = 'V_506',
               particles = [ P.vm__tilde__, P.e__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_277})

V_507 = Vertex(name = 'V_507',
               particles = [ P.vm__tilde__, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_278})

V_508 = Vertex(name = 'V_508',
               particles = [ P.vm__tilde__, P.e__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_279})

V_509 = Vertex(name = 'V_509',
               particles = [ P.vt__tilde__, P.e__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_280})

V_510 = Vertex(name = 'V_510',
               particles = [ P.vt__tilde__, P.e__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_281})

V_511 = Vertex(name = 'V_511',
               particles = [ P.ve__tilde__, P.mu__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_282})

V_512 = Vertex(name = 'V_512',
               particles = [ P.ve__tilde__, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_283})

V_513 = Vertex(name = 'V_513',
               particles = [ P.ve__tilde__, P.mu__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_284})

V_514 = Vertex(name = 'V_514',
               particles = [ P.vm__tilde__, P.mu__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_285})

V_515 = Vertex(name = 'V_515',
               particles = [ P.vm__tilde__, P.mu__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_286})

V_516 = Vertex(name = 'V_516',
               particles = [ P.vm__tilde__, P.mu__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_287})

V_517 = Vertex(name = 'V_517',
               particles = [ P.vt__tilde__, P.mu__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_288})

V_518 = Vertex(name = 'V_518',
               particles = [ P.vt__tilde__, P.mu__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_289})

V_519 = Vertex(name = 'V_519',
               particles = [ P.ve__tilde__, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_290})

V_520 = Vertex(name = 'V_520',
               particles = [ P.ve__tilde__, P.tau__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_291})

V_521 = Vertex(name = 'V_521',
               particles = [ P.ve__tilde__, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_292})

V_522 = Vertex(name = 'V_522',
               particles = [ P.vm__tilde__, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_293})

V_523 = Vertex(name = 'V_523',
               particles = [ P.vm__tilde__, P.tau__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_294})

V_524 = Vertex(name = 'V_524',
               particles = [ P.vm__tilde__, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_295})

V_525 = Vertex(name = 'V_525',
               particles = [ P.vt__tilde__, P.tau__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_296})

V_526 = Vertex(name = 'V_526',
               particles = [ P.vt__tilde__, P.tau__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_297})

V_527 = Vertex(name = 'V_527',
               particles = [ P.u__tilde__, P.d, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_298})

V_528 = Vertex(name = 'V_528',
               particles = [ P.u__tilde__, P.d, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_299})

V_529 = Vertex(name = 'V_529',
               particles = [ P.u__tilde__, P.d, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_300})

V_530 = Vertex(name = 'V_530',
               particles = [ P.u__tilde__, P.d, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_301})

V_531 = Vertex(name = 'V_531',
               particles = [ P.c__tilde__, P.d, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_302})

V_532 = Vertex(name = 'V_532',
               particles = [ P.c__tilde__, P.d, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_303})

V_533 = Vertex(name = 'V_533',
               particles = [ P.c__tilde__, P.d, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_304})

V_534 = Vertex(name = 'V_534',
               particles = [ P.c__tilde__, P.d, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_305})

V_535 = Vertex(name = 'V_535',
               particles = [ P.t__tilde__, P.d, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_306})

V_536 = Vertex(name = 'V_536',
               particles = [ P.t__tilde__, P.d, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_307})

V_537 = Vertex(name = 'V_537',
               particles = [ P.t__tilde__, P.d, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_308})

V_538 = Vertex(name = 'V_538',
               particles = [ P.t__tilde__, P.d, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_309})

V_539 = Vertex(name = 'V_539',
               particles = [ P.u__tilde__, P.s, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_310})

V_540 = Vertex(name = 'V_540',
               particles = [ P.u__tilde__, P.s, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_311})

V_541 = Vertex(name = 'V_541',
               particles = [ P.u__tilde__, P.s, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_312})

V_542 = Vertex(name = 'V_542',
               particles = [ P.u__tilde__, P.s, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_313})

V_543 = Vertex(name = 'V_543',
               particles = [ P.c__tilde__, P.s, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_314})

V_544 = Vertex(name = 'V_544',
               particles = [ P.c__tilde__, P.s, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_315})

V_545 = Vertex(name = 'V_545',
               particles = [ P.c__tilde__, P.s, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_316})

V_546 = Vertex(name = 'V_546',
               particles = [ P.c__tilde__, P.s, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_317})

V_547 = Vertex(name = 'V_547',
               particles = [ P.t__tilde__, P.s, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_318})

V_548 = Vertex(name = 'V_548',
               particles = [ P.t__tilde__, P.s, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_319})

V_549 = Vertex(name = 'V_549',
               particles = [ P.t__tilde__, P.s, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_320})

V_550 = Vertex(name = 'V_550',
               particles = [ P.t__tilde__, P.s, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_321})

V_551 = Vertex(name = 'V_551',
               particles = [ P.u__tilde__, P.b, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_322})

V_552 = Vertex(name = 'V_552',
               particles = [ P.u__tilde__, P.b, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_323})

V_553 = Vertex(name = 'V_553',
               particles = [ P.u__tilde__, P.b, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_324})

V_554 = Vertex(name = 'V_554',
               particles = [ P.u__tilde__, P.b, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_325})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.b, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_326})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.b, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_327})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.b, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_328})

V_558 = Vertex(name = 'V_558',
               particles = [ P.c__tilde__, P.b, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_329})

V_559 = Vertex(name = 'V_559',
               particles = [ P.t__tilde__, P.b, P.sl1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_330})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t__tilde__, P.b, P.sl4__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_331})

V_561 = Vertex(name = 'V_561',
               particles = [ P.t__tilde__, P.b, P.sl5__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_332})

V_562 = Vertex(name = 'V_562',
               particles = [ P.t__tilde__, P.b, P.sl6__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_333})

V_563 = Vertex(name = 'V_563',
               particles = [ P.vm, P.e__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_334})

V_564 = Vertex(name = 'V_564',
               particles = [ P.vm, P.e__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_335})

V_565 = Vertex(name = 'V_565',
               particles = [ P.vm, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_336})

V_566 = Vertex(name = 'V_566',
               particles = [ P.vm, P.e__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_337})

V_567 = Vertex(name = 'V_567',
               particles = [ P.vt, P.e__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_338})

V_568 = Vertex(name = 'V_568',
               particles = [ P.vt, P.e__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_339})

V_569 = Vertex(name = 'V_569',
               particles = [ P.vt, P.e__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_340})

V_570 = Vertex(name = 'V_570',
               particles = [ P.vt, P.e__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_341})

V_571 = Vertex(name = 'V_571',
               particles = [ P.ve, P.mu__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_342})

V_572 = Vertex(name = 'V_572',
               particles = [ P.ve, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_343})

V_573 = Vertex(name = 'V_573',
               particles = [ P.ve, P.mu__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_344})

V_574 = Vertex(name = 'V_574',
               particles = [ P.ve, P.mu__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_345})

V_575 = Vertex(name = 'V_575',
               particles = [ P.vt, P.mu__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_346})

V_576 = Vertex(name = 'V_576',
               particles = [ P.vt, P.mu__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_347})

V_577 = Vertex(name = 'V_577',
               particles = [ P.vt, P.mu__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_348})

V_578 = Vertex(name = 'V_578',
               particles = [ P.vt, P.mu__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_349})

V_579 = Vertex(name = 'V_579',
               particles = [ P.ve, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_350})

V_580 = Vertex(name = 'V_580',
               particles = [ P.ve, P.tau__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_351})

V_581 = Vertex(name = 'V_581',
               particles = [ P.ve, P.tau__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_352})

V_582 = Vertex(name = 'V_582',
               particles = [ P.ve, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_353})

V_583 = Vertex(name = 'V_583',
               particles = [ P.vm, P.tau__minus__, P.sl1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_354})

V_584 = Vertex(name = 'V_584',
               particles = [ P.vm, P.tau__minus__, P.sl2__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_355})

V_585 = Vertex(name = 'V_585',
               particles = [ P.vm, P.tau__minus__, P.sl3__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_356})

V_586 = Vertex(name = 'V_586',
               particles = [ P.vm, P.tau__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_357})

V_587 = Vertex(name = 'V_587',
               particles = [ P.a, P.sl1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_360})

V_588 = Vertex(name = 'V_588',
               particles = [ P.a, P.sl1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_361})

V_589 = Vertex(name = 'V_589',
               particles = [ P.a, P.sl2__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_362})

V_590 = Vertex(name = 'V_590',
               particles = [ P.a, P.sl3__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_363})

V_591 = Vertex(name = 'V_591',
               particles = [ P.a, P.sl4__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_358})

V_592 = Vertex(name = 'V_592',
               particles = [ P.a, P.sl5__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_359})

V_593 = Vertex(name = 'V_593',
               particles = [ P.a, P.sl1__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_364})

V_594 = Vertex(name = 'V_594',
               particles = [ P.a, P.sl6__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_365})

V_595 = Vertex(name = 'V_595',
               particles = [ P.e__plus__, P.n1, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1853,(0,1):C.GC_908})

V_596 = Vertex(name = 'V_596',
               particles = [ P.e__plus__, P.n1, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1022,(0,0):C.GC_1840})

V_597 = Vertex(name = 'V_597',
               particles = [ P.mu__plus__, P.n1, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1854,(0,1):C.GC_904})

V_598 = Vertex(name = 'V_598',
               particles = [ P.mu__plus__, P.n1, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1023,(0,0):C.GC_1841})

V_599 = Vertex(name = 'V_599',
               particles = [ P.tau__plus__, P.n1, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1855,(0,1):C.GC_1024})

V_600 = Vertex(name = 'V_600',
               particles = [ P.tau__plus__, P.n1, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1856,(0,1):C.GC_1025})

V_601 = Vertex(name = 'V_601',
               particles = [ P.e__plus__, P.n2, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1888,(0,1):C.GC_909})

V_602 = Vertex(name = 'V_602',
               particles = [ P.e__plus__, P.n2, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1040,(0,0):C.GC_1875})

V_603 = Vertex(name = 'V_603',
               particles = [ P.mu__plus__, P.n2, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1889,(0,1):C.GC_905})

V_604 = Vertex(name = 'V_604',
               particles = [ P.mu__plus__, P.n2, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1041,(0,0):C.GC_1876})

V_605 = Vertex(name = 'V_605',
               particles = [ P.tau__plus__, P.n2, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1890,(0,1):C.GC_1042})

V_606 = Vertex(name = 'V_606',
               particles = [ P.tau__plus__, P.n2, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1891,(0,1):C.GC_1043})

V_607 = Vertex(name = 'V_607',
               particles = [ P.e__plus__, P.n3, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1923,(0,1):C.GC_910})

V_608 = Vertex(name = 'V_608',
               particles = [ P.e__plus__, P.n3, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1058,(0,0):C.GC_1910})

V_609 = Vertex(name = 'V_609',
               particles = [ P.mu__plus__, P.n3, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1924,(0,1):C.GC_906})

V_610 = Vertex(name = 'V_610',
               particles = [ P.mu__plus__, P.n3, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1059,(0,0):C.GC_1911})

V_611 = Vertex(name = 'V_611',
               particles = [ P.tau__plus__, P.n3, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1925,(0,1):C.GC_1060})

V_612 = Vertex(name = 'V_612',
               particles = [ P.tau__plus__, P.n3, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1926,(0,1):C.GC_1061})

V_613 = Vertex(name = 'V_613',
               particles = [ P.e__plus__, P.n4, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1958,(0,1):C.GC_911})

V_614 = Vertex(name = 'V_614',
               particles = [ P.e__plus__, P.n4, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1076,(0,0):C.GC_1945})

V_615 = Vertex(name = 'V_615',
               particles = [ P.mu__plus__, P.n4, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1959,(0,1):C.GC_907})

V_616 = Vertex(name = 'V_616',
               particles = [ P.mu__plus__, P.n4, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,1):C.GC_1077,(0,0):C.GC_1946})

V_617 = Vertex(name = 'V_617',
               particles = [ P.tau__plus__, P.n4, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1960,(0,1):C.GC_1078})

V_618 = Vertex(name = 'V_618',
               particles = [ P.tau__plus__, P.n4, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1961,(0,1):C.GC_1079})

V_619 = Vertex(name = 'V_619',
               particles = [ P.ve__tilde__, P.x1__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2115})

V_620 = Vertex(name = 'V_620',
               particles = [ P.ve__tilde__, P.x1__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2104})

V_621 = Vertex(name = 'V_621',
               particles = [ P.vm__tilde__, P.x1__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2116})

V_622 = Vertex(name = 'V_622',
               particles = [ P.vm__tilde__, P.x1__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2105})

V_623 = Vertex(name = 'V_623',
               particles = [ P.vt__tilde__, P.x1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2119})

V_624 = Vertex(name = 'V_624',
               particles = [ P.vt__tilde__, P.x1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2120})

V_625 = Vertex(name = 'V_625',
               particles = [ P.ve__tilde__, P.x2__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2142})

V_626 = Vertex(name = 'V_626',
               particles = [ P.ve__tilde__, P.x2__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2131})

V_627 = Vertex(name = 'V_627',
               particles = [ P.vm__tilde__, P.x2__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2143})

V_628 = Vertex(name = 'V_628',
               particles = [ P.vm__tilde__, P.x2__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2132})

V_629 = Vertex(name = 'V_629',
               particles = [ P.vt__tilde__, P.x2__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2146})

V_630 = Vertex(name = 'V_630',
               particles = [ P.vt__tilde__, P.x2__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2147})

V_631 = Vertex(name = 'V_631',
               particles = [ P.e__plus__, P.ve, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_366})

V_632 = Vertex(name = 'V_632',
               particles = [ P.e__plus__, P.ve, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_367})

V_633 = Vertex(name = 'V_633',
               particles = [ P.e__plus__, P.ve, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_368})

V_634 = Vertex(name = 'V_634',
               particles = [ P.mu__plus__, P.ve, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_369})

V_635 = Vertex(name = 'V_635',
               particles = [ P.mu__plus__, P.ve, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_370})

V_636 = Vertex(name = 'V_636',
               particles = [ P.mu__plus__, P.ve, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_371})

V_637 = Vertex(name = 'V_637',
               particles = [ P.tau__plus__, P.ve, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_372})

V_638 = Vertex(name = 'V_638',
               particles = [ P.tau__plus__, P.ve, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_373})

V_639 = Vertex(name = 'V_639',
               particles = [ P.tau__plus__, P.ve, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_374})

V_640 = Vertex(name = 'V_640',
               particles = [ P.e__plus__, P.vm, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_375})

V_641 = Vertex(name = 'V_641',
               particles = [ P.e__plus__, P.vm, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_376})

V_642 = Vertex(name = 'V_642',
               particles = [ P.e__plus__, P.vm, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_377})

V_643 = Vertex(name = 'V_643',
               particles = [ P.mu__plus__, P.vm, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_378})

V_644 = Vertex(name = 'V_644',
               particles = [ P.mu__plus__, P.vm, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_379})

V_645 = Vertex(name = 'V_645',
               particles = [ P.mu__plus__, P.vm, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_380})

V_646 = Vertex(name = 'V_646',
               particles = [ P.tau__plus__, P.vm, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_381})

V_647 = Vertex(name = 'V_647',
               particles = [ P.tau__plus__, P.vm, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_382})

V_648 = Vertex(name = 'V_648',
               particles = [ P.tau__plus__, P.vm, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_383})

V_649 = Vertex(name = 'V_649',
               particles = [ P.e__plus__, P.vt, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_384})

V_650 = Vertex(name = 'V_650',
               particles = [ P.e__plus__, P.vt, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_385})

V_651 = Vertex(name = 'V_651',
               particles = [ P.mu__plus__, P.vt, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_386})

V_652 = Vertex(name = 'V_652',
               particles = [ P.mu__plus__, P.vt, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_387})

V_653 = Vertex(name = 'V_653',
               particles = [ P.tau__plus__, P.vt, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_388})

V_654 = Vertex(name = 'V_654',
               particles = [ P.tau__plus__, P.vt, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_389})

V_655 = Vertex(name = 'V_655',
               particles = [ P.d__tilde__, P.u, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_390})

V_656 = Vertex(name = 'V_656',
               particles = [ P.d__tilde__, P.u, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_391})

V_657 = Vertex(name = 'V_657',
               particles = [ P.d__tilde__, P.u, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_392})

V_658 = Vertex(name = 'V_658',
               particles = [ P.d__tilde__, P.u, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_393})

V_659 = Vertex(name = 'V_659',
               particles = [ P.s__tilde__, P.u, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_394})

V_660 = Vertex(name = 'V_660',
               particles = [ P.s__tilde__, P.u, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_395})

V_661 = Vertex(name = 'V_661',
               particles = [ P.s__tilde__, P.u, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_396})

V_662 = Vertex(name = 'V_662',
               particles = [ P.s__tilde__, P.u, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_397})

V_663 = Vertex(name = 'V_663',
               particles = [ P.b__tilde__, P.u, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_398})

V_664 = Vertex(name = 'V_664',
               particles = [ P.b__tilde__, P.u, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_399})

V_665 = Vertex(name = 'V_665',
               particles = [ P.b__tilde__, P.u, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_400})

V_666 = Vertex(name = 'V_666',
               particles = [ P.b__tilde__, P.u, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_401})

V_667 = Vertex(name = 'V_667',
               particles = [ P.d__tilde__, P.c, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_402})

V_668 = Vertex(name = 'V_668',
               particles = [ P.d__tilde__, P.c, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_403})

V_669 = Vertex(name = 'V_669',
               particles = [ P.d__tilde__, P.c, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_404})

V_670 = Vertex(name = 'V_670',
               particles = [ P.d__tilde__, P.c, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_405})

V_671 = Vertex(name = 'V_671',
               particles = [ P.s__tilde__, P.c, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_406})

V_672 = Vertex(name = 'V_672',
               particles = [ P.s__tilde__, P.c, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_407})

V_673 = Vertex(name = 'V_673',
               particles = [ P.s__tilde__, P.c, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_408})

V_674 = Vertex(name = 'V_674',
               particles = [ P.s__tilde__, P.c, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_409})

V_675 = Vertex(name = 'V_675',
               particles = [ P.b__tilde__, P.c, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_410})

V_676 = Vertex(name = 'V_676',
               particles = [ P.b__tilde__, P.c, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_411})

V_677 = Vertex(name = 'V_677',
               particles = [ P.b__tilde__, P.c, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_412})

V_678 = Vertex(name = 'V_678',
               particles = [ P.b__tilde__, P.c, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_413})

V_679 = Vertex(name = 'V_679',
               particles = [ P.d__tilde__, P.t, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_414})

V_680 = Vertex(name = 'V_680',
               particles = [ P.d__tilde__, P.t, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_415})

V_681 = Vertex(name = 'V_681',
               particles = [ P.d__tilde__, P.t, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_416})

V_682 = Vertex(name = 'V_682',
               particles = [ P.d__tilde__, P.t, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_417})

V_683 = Vertex(name = 'V_683',
               particles = [ P.s__tilde__, P.t, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_418})

V_684 = Vertex(name = 'V_684',
               particles = [ P.s__tilde__, P.t, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_419})

V_685 = Vertex(name = 'V_685',
               particles = [ P.s__tilde__, P.t, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_420})

V_686 = Vertex(name = 'V_686',
               particles = [ P.s__tilde__, P.t, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_421})

V_687 = Vertex(name = 'V_687',
               particles = [ P.b__tilde__, P.t, P.sl1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_422})

V_688 = Vertex(name = 'V_688',
               particles = [ P.b__tilde__, P.t, P.sl4__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_423})

V_689 = Vertex(name = 'V_689',
               particles = [ P.b__tilde__, P.t, P.sl5__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_424})

V_690 = Vertex(name = 'V_690',
               particles = [ P.b__tilde__, P.t, P.sl6__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_425})

V_691 = Vertex(name = 'V_691',
               particles = [ P.vm__tilde__, P.e__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_426})

V_692 = Vertex(name = 'V_692',
               particles = [ P.vm__tilde__, P.e__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_427})

V_693 = Vertex(name = 'V_693',
               particles = [ P.vm__tilde__, P.e__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_428})

V_694 = Vertex(name = 'V_694',
               particles = [ P.vm__tilde__, P.e__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_429})

V_695 = Vertex(name = 'V_695',
               particles = [ P.vt__tilde__, P.e__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_430})

V_696 = Vertex(name = 'V_696',
               particles = [ P.vt__tilde__, P.e__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_431})

V_697 = Vertex(name = 'V_697',
               particles = [ P.vt__tilde__, P.e__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_432})

V_698 = Vertex(name = 'V_698',
               particles = [ P.vt__tilde__, P.e__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_433})

V_699 = Vertex(name = 'V_699',
               particles = [ P.ve__tilde__, P.mu__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_434})

V_700 = Vertex(name = 'V_700',
               particles = [ P.ve__tilde__, P.mu__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_435})

V_701 = Vertex(name = 'V_701',
               particles = [ P.ve__tilde__, P.mu__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_436})

V_702 = Vertex(name = 'V_702',
               particles = [ P.ve__tilde__, P.mu__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_437})

V_703 = Vertex(name = 'V_703',
               particles = [ P.vt__tilde__, P.mu__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_438})

V_704 = Vertex(name = 'V_704',
               particles = [ P.vt__tilde__, P.mu__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_439})

V_705 = Vertex(name = 'V_705',
               particles = [ P.vt__tilde__, P.mu__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_440})

V_706 = Vertex(name = 'V_706',
               particles = [ P.vt__tilde__, P.mu__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_441})

V_707 = Vertex(name = 'V_707',
               particles = [ P.ve__tilde__, P.tau__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_442})

V_708 = Vertex(name = 'V_708',
               particles = [ P.ve__tilde__, P.tau__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_443})

V_709 = Vertex(name = 'V_709',
               particles = [ P.ve__tilde__, P.tau__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_444})

V_710 = Vertex(name = 'V_710',
               particles = [ P.ve__tilde__, P.tau__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_445})

V_711 = Vertex(name = 'V_711',
               particles = [ P.vm__tilde__, P.tau__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_446})

V_712 = Vertex(name = 'V_712',
               particles = [ P.vm__tilde__, P.tau__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_447})

V_713 = Vertex(name = 'V_713',
               particles = [ P.vm__tilde__, P.tau__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_448})

V_714 = Vertex(name = 'V_714',
               particles = [ P.vm__tilde__, P.tau__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_449})

V_715 = Vertex(name = 'V_715',
               particles = [ P.a, P.a, P.sl1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_452})

V_716 = Vertex(name = 'V_716',
               particles = [ P.a, P.a, P.sl1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_453})

V_717 = Vertex(name = 'V_717',
               particles = [ P.a, P.a, P.sl2__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_454})

V_718 = Vertex(name = 'V_718',
               particles = [ P.a, P.a, P.sl3__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_455})

V_719 = Vertex(name = 'V_719',
               particles = [ P.a, P.a, P.sl4__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_450})

V_720 = Vertex(name = 'V_720',
               particles = [ P.a, P.a, P.sl5__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_451})

V_721 = Vertex(name = 'V_721',
               particles = [ P.a, P.a, P.sl1__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_456})

V_722 = Vertex(name = 'V_722',
               particles = [ P.a, P.a, P.sl6__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_457})

V_723 = Vertex(name = 'V_723',
               particles = [ P.h02, P.sl1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2362})

V_724 = Vertex(name = 'V_724',
               particles = [ P.h02, P.sl1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2363})

V_725 = Vertex(name = 'V_725',
               particles = [ P.h02, P.sl2__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2324})

V_726 = Vertex(name = 'V_726',
               particles = [ P.h02, P.sl2__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2298})

V_727 = Vertex(name = 'V_727',
               particles = [ P.h02, P.sl3__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2325})

V_728 = Vertex(name = 'V_728',
               particles = [ P.h02, P.sl3__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2299})

V_729 = Vertex(name = 'V_729',
               particles = [ P.h02, P.sl3__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2364})

V_730 = Vertex(name = 'V_730',
               particles = [ P.h02, P.sl4__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2330})

V_731 = Vertex(name = 'V_731',
               particles = [ P.h02, P.sl2__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2365})

V_732 = Vertex(name = 'V_732',
               particles = [ P.h02, P.sl5__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2331})

V_733 = Vertex(name = 'V_733',
               particles = [ P.h02, P.sl1__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2366})

V_734 = Vertex(name = 'V_734',
               particles = [ P.h02, P.sl6__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2367})

V_735 = Vertex(name = 'V_735',
               particles = [ P.h01, P.sl1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2317})

V_736 = Vertex(name = 'V_736',
               particles = [ P.h01, P.sl1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2318})

V_737 = Vertex(name = 'V_737',
               particles = [ P.h01, P.sl2__plus__, P.sl2__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2319})

V_738 = Vertex(name = 'V_738',
               particles = [ P.h01, P.sl2__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2290})

V_739 = Vertex(name = 'V_739',
               particles = [ P.h01, P.sl3__plus__, P.sl3__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2320})

V_740 = Vertex(name = 'V_740',
               particles = [ P.h01, P.sl3__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2291})

V_741 = Vertex(name = 'V_741',
               particles = [ P.h01, P.sl3__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2292})

V_742 = Vertex(name = 'V_742',
               particles = [ P.h01, P.sl4__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2315})

V_743 = Vertex(name = 'V_743',
               particles = [ P.h01, P.sl2__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2293})

V_744 = Vertex(name = 'V_744',
               particles = [ P.h01, P.sl5__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2316})

V_745 = Vertex(name = 'V_745',
               particles = [ P.h01, P.sl1__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2321})

V_746 = Vertex(name = 'V_746',
               particles = [ P.h01, P.sl6__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2322})

V_747 = Vertex(name = 'V_747',
               particles = [ P.A0, P.sl1__plus__, P.sl1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2438})

V_748 = Vertex(name = 'V_748',
               particles = [ P.A0, P.sl1__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2439})

V_749 = Vertex(name = 'V_749',
               particles = [ P.A0, P.sl2__plus__, P.sl5__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2436})

V_750 = Vertex(name = 'V_750',
               particles = [ P.A0, P.sl3__plus__, P.sl4__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2437})

V_751 = Vertex(name = 'V_751',
               particles = [ P.A0, P.sl3__minus__, P.sl4__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2440})

V_752 = Vertex(name = 'V_752',
               particles = [ P.A0, P.sl2__minus__, P.sl5__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2441})

V_753 = Vertex(name = 'V_753',
               particles = [ P.A0, P.sl1__minus__, P.sl6__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2442})

V_754 = Vertex(name = 'V_754',
               particles = [ P.A0, P.sl6__plus__, P.sl6__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2443})

V_755 = Vertex(name = 'V_755',
               particles = [ P.e__plus__, P.e__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_458})

V_756 = Vertex(name = 'V_756',
               particles = [ P.e__plus__, P.e__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_459})

V_757 = Vertex(name = 'V_757',
               particles = [ P.mu__plus__, P.e__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_460})

V_758 = Vertex(name = 'V_758',
               particles = [ P.mu__plus__, P.e__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_461})

V_759 = Vertex(name = 'V_759',
               particles = [ P.tau__plus__, P.e__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_462})

V_760 = Vertex(name = 'V_760',
               particles = [ P.tau__plus__, P.e__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_463})

V_761 = Vertex(name = 'V_761',
               particles = [ P.e__plus__, P.mu__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_464})

V_762 = Vertex(name = 'V_762',
               particles = [ P.e__plus__, P.mu__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_465})

V_763 = Vertex(name = 'V_763',
               particles = [ P.mu__plus__, P.mu__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_466})

V_764 = Vertex(name = 'V_764',
               particles = [ P.mu__plus__, P.mu__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_467})

V_765 = Vertex(name = 'V_765',
               particles = [ P.tau__plus__, P.mu__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_468})

V_766 = Vertex(name = 'V_766',
               particles = [ P.tau__plus__, P.mu__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_469})

V_767 = Vertex(name = 'V_767',
               particles = [ P.e__plus__, P.tau__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_470})

V_768 = Vertex(name = 'V_768',
               particles = [ P.e__plus__, P.tau__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_471})

V_769 = Vertex(name = 'V_769',
               particles = [ P.mu__plus__, P.tau__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_472})

V_770 = Vertex(name = 'V_770',
               particles = [ P.mu__plus__, P.tau__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_473})

V_771 = Vertex(name = 'V_771',
               particles = [ P.tau__plus__, P.tau__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_474})

V_772 = Vertex(name = 'V_772',
               particles = [ P.tau__plus__, P.tau__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_475})

V_773 = Vertex(name = 'V_773',
               particles = [ P.d__tilde__, P.d, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_476})

V_774 = Vertex(name = 'V_774',
               particles = [ P.d__tilde__, P.d, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_477})

V_775 = Vertex(name = 'V_775',
               particles = [ P.d__tilde__, P.d, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_478})

V_776 = Vertex(name = 'V_776',
               particles = [ P.s__tilde__, P.d, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_479})

V_777 = Vertex(name = 'V_777',
               particles = [ P.s__tilde__, P.d, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_480})

V_778 = Vertex(name = 'V_778',
               particles = [ P.s__tilde__, P.d, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_481})

V_779 = Vertex(name = 'V_779',
               particles = [ P.b__tilde__, P.d, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_482})

V_780 = Vertex(name = 'V_780',
               particles = [ P.b__tilde__, P.d, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_483})

V_781 = Vertex(name = 'V_781',
               particles = [ P.b__tilde__, P.d, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_484})

V_782 = Vertex(name = 'V_782',
               particles = [ P.d__tilde__, P.s, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_485})

V_783 = Vertex(name = 'V_783',
               particles = [ P.d__tilde__, P.s, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_486})

V_784 = Vertex(name = 'V_784',
               particles = [ P.d__tilde__, P.s, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_487})

V_785 = Vertex(name = 'V_785',
               particles = [ P.s__tilde__, P.s, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_488})

V_786 = Vertex(name = 'V_786',
               particles = [ P.s__tilde__, P.s, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_489})

V_787 = Vertex(name = 'V_787',
               particles = [ P.s__tilde__, P.s, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_490})

V_788 = Vertex(name = 'V_788',
               particles = [ P.b__tilde__, P.s, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_491})

V_789 = Vertex(name = 'V_789',
               particles = [ P.b__tilde__, P.s, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_492})

V_790 = Vertex(name = 'V_790',
               particles = [ P.b__tilde__, P.s, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_493})

V_791 = Vertex(name = 'V_791',
               particles = [ P.d__tilde__, P.b, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_494})

V_792 = Vertex(name = 'V_792',
               particles = [ P.d__tilde__, P.b, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_495})

V_793 = Vertex(name = 'V_793',
               particles = [ P.d__tilde__, P.b, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_496})

V_794 = Vertex(name = 'V_794',
               particles = [ P.s__tilde__, P.b, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_497})

V_795 = Vertex(name = 'V_795',
               particles = [ P.s__tilde__, P.b, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_498})

V_796 = Vertex(name = 'V_796',
               particles = [ P.s__tilde__, P.b, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_499})

V_797 = Vertex(name = 'V_797',
               particles = [ P.b__tilde__, P.b, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_500})

V_798 = Vertex(name = 'V_798',
               particles = [ P.b__tilde__, P.b, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_501})

V_799 = Vertex(name = 'V_799',
               particles = [ P.b__tilde__, P.b, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_502})

V_800 = Vertex(name = 'V_800',
               particles = [ P.n1, P.ve, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2058})

V_801 = Vertex(name = 'V_801',
               particles = [ P.n2, P.ve, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2059})

V_802 = Vertex(name = 'V_802',
               particles = [ P.n3, P.ve, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2060})

V_803 = Vertex(name = 'V_803',
               particles = [ P.n4, P.ve, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2061})

V_804 = Vertex(name = 'V_804',
               particles = [ P.n1, P.vm, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2054})

V_805 = Vertex(name = 'V_805',
               particles = [ P.n2, P.vm, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2055})

V_806 = Vertex(name = 'V_806',
               particles = [ P.n3, P.vm, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2056})

V_807 = Vertex(name = 'V_807',
               particles = [ P.n4, P.vm, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2057})

V_808 = Vertex(name = 'V_808',
               particles = [ P.n1, P.vt, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2050})

V_809 = Vertex(name = 'V_809',
               particles = [ P.n2, P.vt, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2051})

V_810 = Vertex(name = 'V_810',
               particles = [ P.n3, P.vt, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2052})

V_811 = Vertex(name = 'V_811',
               particles = [ P.n4, P.vt, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_2053})

V_812 = Vertex(name = 'V_812',
               particles = [ P.H__plus__, P.sl1__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2474})

V_813 = Vertex(name = 'V_813',
               particles = [ P.H__plus__, P.sl2__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2444})

V_814 = Vertex(name = 'V_814',
               particles = [ P.H__plus__, P.sl3__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2445})

V_815 = Vertex(name = 'V_815',
               particles = [ P.H__plus__, P.sl4__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2477})

V_816 = Vertex(name = 'V_816',
               particles = [ P.H__plus__, P.sl5__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2476})

V_817 = Vertex(name = 'V_817',
               particles = [ P.H__plus__, P.sl6__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2475})

V_818 = Vertex(name = 'V_818',
               particles = [ P.sd1__tilde__, P.sd1, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1512})

V_819 = Vertex(name = 'V_819',
               particles = [ P.sd1__tilde__, P.sd1, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1520})

V_820 = Vertex(name = 'V_820',
               particles = [ P.sd1__tilde__, P.sd1, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1528})

V_821 = Vertex(name = 'V_821',
               particles = [ P.sd1__tilde__, P.sd2, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1513})

V_822 = Vertex(name = 'V_822',
               particles = [ P.sd1__tilde__, P.sd2, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1521})

V_823 = Vertex(name = 'V_823',
               particles = [ P.sd1__tilde__, P.sd2, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1529})

V_824 = Vertex(name = 'V_824',
               particles = [ P.sd1__tilde__, P.sd3, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1514})

V_825 = Vertex(name = 'V_825',
               particles = [ P.sd1__tilde__, P.sd3, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1522})

V_826 = Vertex(name = 'V_826',
               particles = [ P.sd1__tilde__, P.sd3, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1530})

V_827 = Vertex(name = 'V_827',
               particles = [ P.sd1__tilde__, P.sd4, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1515})

V_828 = Vertex(name = 'V_828',
               particles = [ P.sd1__tilde__, P.sd4, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1523})

V_829 = Vertex(name = 'V_829',
               particles = [ P.sd1__tilde__, P.sd4, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1531})

V_830 = Vertex(name = 'V_830',
               particles = [ P.sd1__tilde__, P.sd5, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1188})

V_831 = Vertex(name = 'V_831',
               particles = [ P.sd1__tilde__, P.sd5, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1196})

V_832 = Vertex(name = 'V_832',
               particles = [ P.sd1__tilde__, P.sd5, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1204})

V_833 = Vertex(name = 'V_833',
               particles = [ P.sd1__tilde__, P.sd6, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1189})

V_834 = Vertex(name = 'V_834',
               particles = [ P.sd1__tilde__, P.sd6, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1197})

V_835 = Vertex(name = 'V_835',
               particles = [ P.sd1__tilde__, P.sd6, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1205})

V_836 = Vertex(name = 'V_836',
               particles = [ P.sd1, P.sd2__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1516})

V_837 = Vertex(name = 'V_837',
               particles = [ P.sd1, P.sd2__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1524})

V_838 = Vertex(name = 'V_838',
               particles = [ P.sd1, P.sd2__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1532})

V_839 = Vertex(name = 'V_839',
               particles = [ P.sd2__tilde__, P.sd2, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1517})

V_840 = Vertex(name = 'V_840',
               particles = [ P.sd2__tilde__, P.sd2, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1525})

V_841 = Vertex(name = 'V_841',
               particles = [ P.sd2__tilde__, P.sd2, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1533})

V_842 = Vertex(name = 'V_842',
               particles = [ P.sd2__tilde__, P.sd3, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1518})

V_843 = Vertex(name = 'V_843',
               particles = [ P.sd2__tilde__, P.sd3, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1526})

V_844 = Vertex(name = 'V_844',
               particles = [ P.sd2__tilde__, P.sd3, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1534})

V_845 = Vertex(name = 'V_845',
               particles = [ P.sd2__tilde__, P.sd4, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1519})

V_846 = Vertex(name = 'V_846',
               particles = [ P.sd2__tilde__, P.sd4, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1527})

V_847 = Vertex(name = 'V_847',
               particles = [ P.sd2__tilde__, P.sd4, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1535})

V_848 = Vertex(name = 'V_848',
               particles = [ P.sd2__tilde__, P.sd5, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1190})

V_849 = Vertex(name = 'V_849',
               particles = [ P.sd2__tilde__, P.sd5, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1198})

V_850 = Vertex(name = 'V_850',
               particles = [ P.sd2__tilde__, P.sd5, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1206})

V_851 = Vertex(name = 'V_851',
               particles = [ P.sd2__tilde__, P.sd6, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1191})

V_852 = Vertex(name = 'V_852',
               particles = [ P.sd2__tilde__, P.sd6, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1199})

V_853 = Vertex(name = 'V_853',
               particles = [ P.sd2__tilde__, P.sd6, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1207})

V_854 = Vertex(name = 'V_854',
               particles = [ P.sd1, P.sd3__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1212})

V_855 = Vertex(name = 'V_855',
               particles = [ P.sd1, P.sd3__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1220})

V_856 = Vertex(name = 'V_856',
               particles = [ P.sd1, P.sd3__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1228})

V_857 = Vertex(name = 'V_857',
               particles = [ P.sd2, P.sd3__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1213})

V_858 = Vertex(name = 'V_858',
               particles = [ P.sd2, P.sd3__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1221})

V_859 = Vertex(name = 'V_859',
               particles = [ P.sd2, P.sd3__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1229})

V_860 = Vertex(name = 'V_860',
               particles = [ P.sd3__tilde__, P.sd3, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1214})

V_861 = Vertex(name = 'V_861',
               particles = [ P.sd3__tilde__, P.sd3, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1222})

V_862 = Vertex(name = 'V_862',
               particles = [ P.sd3__tilde__, P.sd3, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1230})

V_863 = Vertex(name = 'V_863',
               particles = [ P.sd3__tilde__, P.sd4, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1215})

V_864 = Vertex(name = 'V_864',
               particles = [ P.sd3__tilde__, P.sd4, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1223})

V_865 = Vertex(name = 'V_865',
               particles = [ P.sd3__tilde__, P.sd4, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1231})

V_866 = Vertex(name = 'V_866',
               particles = [ P.sd1, P.sd4__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1216})

V_867 = Vertex(name = 'V_867',
               particles = [ P.sd1, P.sd4__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1224})

V_868 = Vertex(name = 'V_868',
               particles = [ P.sd1, P.sd4__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1232})

V_869 = Vertex(name = 'V_869',
               particles = [ P.sd2, P.sd4__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1217})

V_870 = Vertex(name = 'V_870',
               particles = [ P.sd2, P.sd4__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1225})

V_871 = Vertex(name = 'V_871',
               particles = [ P.sd2, P.sd4__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1233})

V_872 = Vertex(name = 'V_872',
               particles = [ P.sd3, P.sd4__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1218})

V_873 = Vertex(name = 'V_873',
               particles = [ P.sd3, P.sd4__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1226})

V_874 = Vertex(name = 'V_874',
               particles = [ P.sd3, P.sd4__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1234})

V_875 = Vertex(name = 'V_875',
               particles = [ P.sd4__tilde__, P.sd4, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1219})

V_876 = Vertex(name = 'V_876',
               particles = [ P.sd4__tilde__, P.sd4, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1227})

V_877 = Vertex(name = 'V_877',
               particles = [ P.sd4__tilde__, P.sd4, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1235})

V_878 = Vertex(name = 'V_878',
               particles = [ P.sd1, P.sd5__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1500})

V_879 = Vertex(name = 'V_879',
               particles = [ P.sd1, P.sd5__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1504})

V_880 = Vertex(name = 'V_880',
               particles = [ P.sd1, P.sd5__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1508})

V_881 = Vertex(name = 'V_881',
               particles = [ P.sd2, P.sd5__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1501})

V_882 = Vertex(name = 'V_882',
               particles = [ P.sd2, P.sd5__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1505})

V_883 = Vertex(name = 'V_883',
               particles = [ P.sd2, P.sd5__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1509})

V_884 = Vertex(name = 'V_884',
               particles = [ P.sd3, P.sd5__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_539})

V_885 = Vertex(name = 'V_885',
               particles = [ P.sd3, P.sd5__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_543})

V_886 = Vertex(name = 'V_886',
               particles = [ P.sd3, P.sd5__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_547})

V_887 = Vertex(name = 'V_887',
               particles = [ P.sd4, P.sd5__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_540})

V_888 = Vertex(name = 'V_888',
               particles = [ P.sd4, P.sd5__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_544})

V_889 = Vertex(name = 'V_889',
               particles = [ P.sd4, P.sd5__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_548})

V_890 = Vertex(name = 'V_890',
               particles = [ P.sd5__tilde__, P.sd5, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1192})

V_891 = Vertex(name = 'V_891',
               particles = [ P.sd5__tilde__, P.sd5, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1200})

V_892 = Vertex(name = 'V_892',
               particles = [ P.sd5__tilde__, P.sd5, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1208})

V_893 = Vertex(name = 'V_893',
               particles = [ P.sd5__tilde__, P.sd6, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1193})

V_894 = Vertex(name = 'V_894',
               particles = [ P.sd5__tilde__, P.sd6, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1201})

V_895 = Vertex(name = 'V_895',
               particles = [ P.sd5__tilde__, P.sd6, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1209})

V_896 = Vertex(name = 'V_896',
               particles = [ P.sd1, P.sd6__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1502})

V_897 = Vertex(name = 'V_897',
               particles = [ P.sd1, P.sd6__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1506})

V_898 = Vertex(name = 'V_898',
               particles = [ P.sd1, P.sd6__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1510})

V_899 = Vertex(name = 'V_899',
               particles = [ P.sd2, P.sd6__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1503})

V_900 = Vertex(name = 'V_900',
               particles = [ P.sd2, P.sd6__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1507})

V_901 = Vertex(name = 'V_901',
               particles = [ P.sd2, P.sd6__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1511})

V_902 = Vertex(name = 'V_902',
               particles = [ P.sd3, P.sd6__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_541})

V_903 = Vertex(name = 'V_903',
               particles = [ P.sd3, P.sd6__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_545})

V_904 = Vertex(name = 'V_904',
               particles = [ P.sd3, P.sd6__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_549})

V_905 = Vertex(name = 'V_905',
               particles = [ P.sd4, P.sd6__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_542})

V_906 = Vertex(name = 'V_906',
               particles = [ P.sd4, P.sd6__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_546})

V_907 = Vertex(name = 'V_907',
               particles = [ P.sd4, P.sd6__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_550})

V_908 = Vertex(name = 'V_908',
               particles = [ P.sd5, P.sd6__tilde__, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1194})

V_909 = Vertex(name = 'V_909',
               particles = [ P.sd5, P.sd6__tilde__, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1202})

V_910 = Vertex(name = 'V_910',
               particles = [ P.sd5, P.sd6__tilde__, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1210})

V_911 = Vertex(name = 'V_911',
               particles = [ P.sd6__tilde__, P.sd6, P.sv1__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1195})

V_912 = Vertex(name = 'V_912',
               particles = [ P.sd6__tilde__, P.sd6, P.sv2__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1203})

V_913 = Vertex(name = 'V_913',
               particles = [ P.sd6__tilde__, P.sd6, P.sv3__tilde__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1211})

V_914 = Vertex(name = 'V_914',
               particles = [ P.sl1__plus__, P.sl1__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1544})

V_915 = Vertex(name = 'V_915',
               particles = [ P.sl1__plus__, P.sl1__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1552})

V_916 = Vertex(name = 'V_916',
               particles = [ P.sl1__plus__, P.sl2__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1545})

V_917 = Vertex(name = 'V_917',
               particles = [ P.sl1__plus__, P.sl2__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1553})

V_918 = Vertex(name = 'V_918',
               particles = [ P.sl1__plus__, P.sl3__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1546})

V_919 = Vertex(name = 'V_919',
               particles = [ P.sl1__plus__, P.sl3__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1554})

V_920 = Vertex(name = 'V_920',
               particles = [ P.sl1__plus__, P.sl4__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1240})

V_921 = Vertex(name = 'V_921',
               particles = [ P.sl1__plus__, P.sl4__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1246})

V_922 = Vertex(name = 'V_922',
               particles = [ P.sl1__plus__, P.sl5__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1241})

V_923 = Vertex(name = 'V_923',
               particles = [ P.sl1__plus__, P.sl5__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1247})

V_924 = Vertex(name = 'V_924',
               particles = [ P.sl1__plus__, P.sl6__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1547})

V_925 = Vertex(name = 'V_925',
               particles = [ P.sl1__plus__, P.sl6__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1555})

V_926 = Vertex(name = 'V_926',
               particles = [ P.sl1__minus__, P.sl2__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1252})

V_927 = Vertex(name = 'V_927',
               particles = [ P.sl1__minus__, P.sl2__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1264})

V_928 = Vertex(name = 'V_928',
               particles = [ P.sl2__plus__, P.sl2__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1253})

V_929 = Vertex(name = 'V_929',
               particles = [ P.sl2__plus__, P.sl2__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1265})

V_930 = Vertex(name = 'V_930',
               particles = [ P.sl2__plus__, P.sl3__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1254})

V_931 = Vertex(name = 'V_931',
               particles = [ P.sl2__plus__, P.sl3__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1266})

V_932 = Vertex(name = 'V_932',
               particles = [ P.sl2__plus__, P.sl6__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1255})

V_933 = Vertex(name = 'V_933',
               particles = [ P.sl2__plus__, P.sl6__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1267})

V_934 = Vertex(name = 'V_934',
               particles = [ P.sl1__minus__, P.sl3__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1256})

V_935 = Vertex(name = 'V_935',
               particles = [ P.sl1__minus__, P.sl3__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1260})

V_936 = Vertex(name = 'V_936',
               particles = [ P.sl2__minus__, P.sl3__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1257})

V_937 = Vertex(name = 'V_937',
               particles = [ P.sl2__minus__, P.sl3__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1261})

V_938 = Vertex(name = 'V_938',
               particles = [ P.sl3__plus__, P.sl3__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1258})

V_939 = Vertex(name = 'V_939',
               particles = [ P.sl3__plus__, P.sl3__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1262})

V_940 = Vertex(name = 'V_940',
               particles = [ P.sl3__plus__, P.sl6__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1259})

V_941 = Vertex(name = 'V_941',
               particles = [ P.sl3__plus__, P.sl6__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1263})

V_942 = Vertex(name = 'V_942',
               particles = [ P.sl1__minus__, P.sl4__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1536})

V_943 = Vertex(name = 'V_943',
               particles = [ P.sl1__minus__, P.sl4__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1540})

V_944 = Vertex(name = 'V_944',
               particles = [ P.sl2__minus__, P.sl4__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_551})

V_945 = Vertex(name = 'V_945',
               particles = [ P.sl2__minus__, P.sl4__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_555})

V_946 = Vertex(name = 'V_946',
               particles = [ P.sl3__minus__, P.sl4__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_552})

V_947 = Vertex(name = 'V_947',
               particles = [ P.sl3__minus__, P.sl4__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_556})

V_948 = Vertex(name = 'V_948',
               particles = [ P.sl4__plus__, P.sl4__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1236})

V_949 = Vertex(name = 'V_949',
               particles = [ P.sl4__plus__, P.sl4__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1242})

V_950 = Vertex(name = 'V_950',
               particles = [ P.sl4__plus__, P.sl5__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1237})

V_951 = Vertex(name = 'V_951',
               particles = [ P.sl4__plus__, P.sl5__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1243})

V_952 = Vertex(name = 'V_952',
               particles = [ P.sl4__plus__, P.sl6__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1537})

V_953 = Vertex(name = 'V_953',
               particles = [ P.sl4__plus__, P.sl6__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1541})

V_954 = Vertex(name = 'V_954',
               particles = [ P.sl1__minus__, P.sl5__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1538})

V_955 = Vertex(name = 'V_955',
               particles = [ P.sl1__minus__, P.sl5__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1542})

V_956 = Vertex(name = 'V_956',
               particles = [ P.sl2__minus__, P.sl5__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_553})

V_957 = Vertex(name = 'V_957',
               particles = [ P.sl2__minus__, P.sl5__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_557})

V_958 = Vertex(name = 'V_958',
               particles = [ P.sl3__minus__, P.sl5__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_554})

V_959 = Vertex(name = 'V_959',
               particles = [ P.sl3__minus__, P.sl5__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_558})

V_960 = Vertex(name = 'V_960',
               particles = [ P.sl4__minus__, P.sl5__plus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1238})

V_961 = Vertex(name = 'V_961',
               particles = [ P.sl4__minus__, P.sl5__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1248})

V_962 = Vertex(name = 'V_962',
               particles = [ P.sl5__plus__, P.sl5__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1239})

V_963 = Vertex(name = 'V_963',
               particles = [ P.sl5__plus__, P.sl5__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1249})

V_964 = Vertex(name = 'V_964',
               particles = [ P.sl5__plus__, P.sl6__minus__, P.sv1__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1539})

V_965 = Vertex(name = 'V_965',
               particles = [ P.sl5__plus__, P.sl6__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1543})

V_966 = Vertex(name = 'V_966',
               particles = [ P.sl1__minus__, P.sl6__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1548})

V_967 = Vertex(name = 'V_967',
               particles = [ P.sl1__minus__, P.sl6__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1556})

V_968 = Vertex(name = 'V_968',
               particles = [ P.sl2__minus__, P.sl6__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1549})

V_969 = Vertex(name = 'V_969',
               particles = [ P.sl2__minus__, P.sl6__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1557})

V_970 = Vertex(name = 'V_970',
               particles = [ P.sl3__minus__, P.sl6__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1550})

V_971 = Vertex(name = 'V_971',
               particles = [ P.sl3__minus__, P.sl6__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1558})

V_972 = Vertex(name = 'V_972',
               particles = [ P.sl4__minus__, P.sl6__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1244})

V_973 = Vertex(name = 'V_973',
               particles = [ P.sl4__minus__, P.sl6__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1250})

V_974 = Vertex(name = 'V_974',
               particles = [ P.sl5__minus__, P.sl6__plus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1245})

V_975 = Vertex(name = 'V_975',
               particles = [ P.sl5__minus__, P.sl6__plus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1251})

V_976 = Vertex(name = 'V_976',
               particles = [ P.sl6__plus__, P.sl6__minus__, P.sv2__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1551})

V_977 = Vertex(name = 'V_977',
               particles = [ P.sl6__plus__, P.sl6__minus__, P.sv3__tilde__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_1559})

V_978 = Vertex(name = 'V_978',
               particles = [ P.h02, P.sv1__tilde__, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2328})

V_979 = Vertex(name = 'V_979',
               particles = [ P.h02, P.sv2__tilde__, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2328})

V_980 = Vertex(name = 'V_980',
               particles = [ P.h02, P.sv3__tilde__, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2328})

V_981 = Vertex(name = 'V_981',
               particles = [ P.h01, P.sv1__tilde__, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2303})

V_982 = Vertex(name = 'V_982',
               particles = [ P.h01, P.sv2__tilde__, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2303})

V_983 = Vertex(name = 'V_983',
               particles = [ P.h01, P.sv3__tilde__, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_2303})

V_984 = Vertex(name = 'V_984',
               particles = [ P.ve__tilde__, P.n1, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1844})

V_985 = Vertex(name = 'V_985',
               particles = [ P.vm__tilde__, P.n1, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1843})

V_986 = Vertex(name = 'V_986',
               particles = [ P.vt__tilde__, P.n1, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1842})

V_987 = Vertex(name = 'V_987',
               particles = [ P.ve__tilde__, P.n2, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1879})

V_988 = Vertex(name = 'V_988',
               particles = [ P.vm__tilde__, P.n2, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1878})

V_989 = Vertex(name = 'V_989',
               particles = [ P.vt__tilde__, P.n2, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1877})

V_990 = Vertex(name = 'V_990',
               particles = [ P.ve__tilde__, P.n3, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1914})

V_991 = Vertex(name = 'V_991',
               particles = [ P.vm__tilde__, P.n3, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1913})

V_992 = Vertex(name = 'V_992',
               particles = [ P.vt__tilde__, P.n3, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1912})

V_993 = Vertex(name = 'V_993',
               particles = [ P.ve__tilde__, P.n4, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1949})

V_994 = Vertex(name = 'V_994',
               particles = [ P.vm__tilde__, P.n4, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1948})

V_995 = Vertex(name = 'V_995',
               particles = [ P.vt__tilde__, P.n4, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1947})

V_996 = Vertex(name = 'V_996',
               particles = [ P.e__plus__, P.x1__minus__, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2158,(0,1):C.GC_1098})

V_997 = Vertex(name = 'V_997',
               particles = [ P.mu__plus__, P.x1__minus__, P.sv2 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2159,(0,1):C.GC_1099})

V_998 = Vertex(name = 'V_998',
               particles = [ P.tau__plus__, P.x1__minus__, P.sv1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2160,(0,1):C.GC_1100})

V_999 = Vertex(name = 'V_999',
               particles = [ P.e__plus__, P.x2__minus__, P.sv3 ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_2179,(0,1):C.GC_1117})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.mu__plus__, P.x2__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2180,(0,1):C.GC_1118})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.tau__plus__, P.x2__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2181,(0,1):C.GC_1119})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.H__minus__, P.sl1__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2478})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.H__minus__, P.sl2__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2446})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.H__minus__, P.sl3__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2447})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.H__minus__, P.sl4__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2481})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.H__minus__, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2480})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.H__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2479})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.d__tilde__, P.d, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_595})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.d__tilde__, P.d, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_596})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.d__tilde__, P.d, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_597})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.s__tilde__, P.d, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_598})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.s__tilde__, P.d, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_599})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.s__tilde__, P.d, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_600})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.b__tilde__, P.d, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_601})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.b__tilde__, P.d, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_602})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.b__tilde__, P.d, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_603})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.d__tilde__, P.s, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_604})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.d__tilde__, P.s, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_605})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.d__tilde__, P.s, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_606})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.s__tilde__, P.s, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_607})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.s__tilde__, P.s, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_608})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.s__tilde__, P.s, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_609})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.b__tilde__, P.s, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_610})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.b__tilde__, P.s, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_611})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.b__tilde__, P.s, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_612})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.d__tilde__, P.b, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_613})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.d__tilde__, P.b, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_614})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.d__tilde__, P.b, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_615})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.s__tilde__, P.b, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_616})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.s__tilde__, P.b, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_617})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.s__tilde__, P.b, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_618})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.b__tilde__, P.b, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_619})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.b__tilde__, P.b, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_620})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.b__tilde__, P.b, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_621})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.e__plus__, P.e__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_622})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.e__plus__, P.e__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_623})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.mu__plus__, P.e__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_624})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.mu__plus__, P.e__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_625})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.tau__plus__, P.e__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_626})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.tau__plus__, P.e__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_627})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.e__plus__, P.mu__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_628})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.e__plus__, P.mu__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_629})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.mu__plus__, P.mu__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_630})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.mu__plus__, P.mu__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_631})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.tau__plus__, P.mu__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_632})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.tau__plus__, P.mu__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_633})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.e__plus__, P.tau__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_634})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.e__plus__, P.tau__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_635})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.mu__plus__, P.tau__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_636})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.mu__plus__, P.tau__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_637})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.tau__plus__, P.tau__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_638})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.tau__plus__, P.tau__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_639})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.sd1__tilde__, P.sd1, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1572})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.sd1__tilde__, P.sd1, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1580})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.sd1__tilde__, P.sd1, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1588})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.sd1__tilde__, P.sd2, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1573})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.sd1__tilde__, P.sd2, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1581})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.sd1__tilde__, P.sd2, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1589})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.sd1__tilde__, P.sd3, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1292})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.sd1__tilde__, P.sd3, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1300})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.sd1__tilde__, P.sd3, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1308})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.sd1__tilde__, P.sd4, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1293})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.sd1__tilde__, P.sd4, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1301})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.sd1__tilde__, P.sd4, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1309})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.sd1__tilde__, P.sd5, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1560})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.sd1__tilde__, P.sd5, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1564})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.sd1__tilde__, P.sd5, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1568})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.sd1__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1561})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.sd1__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1565})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.sd1__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1569})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.sd1, P.sd2__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1574})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.sd1, P.sd2__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1582})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.sd1, P.sd2__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1590})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.sd2__tilde__, P.sd2, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1575})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.sd2__tilde__, P.sd2, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1583})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.sd2__tilde__, P.sd2, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1591})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.sd2__tilde__, P.sd3, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1294})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.sd2__tilde__, P.sd3, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1302})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.sd2__tilde__, P.sd3, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1310})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.sd2__tilde__, P.sd4, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1295})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.sd2__tilde__, P.sd4, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1303})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.sd2__tilde__, P.sd4, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1311})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.sd2__tilde__, P.sd5, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1562})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.sd2__tilde__, P.sd5, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1566})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.sd2__tilde__, P.sd5, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1570})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.sd2__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1563})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.sd2__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1567})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.sd2__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1571})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.sd1, P.sd3__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1576})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.sd1, P.sd3__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1584})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.sd1, P.sd3__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1592})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.sd2, P.sd3__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1577})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.sd2, P.sd3__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1585})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.sd2, P.sd3__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1593})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.sd3__tilde__, P.sd3, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1296})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.sd3__tilde__, P.sd3, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1304})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.sd3__tilde__, P.sd3, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1312})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.sd3__tilde__, P.sd4, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1297})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.sd3__tilde__, P.sd4, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1305})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.sd3__tilde__, P.sd4, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1313})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.sd3__tilde__, P.sd5, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_640})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.sd3__tilde__, P.sd5, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_644})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.sd3__tilde__, P.sd5, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_648})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.sd3__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_641})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.sd3__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_645})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.sd3__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_649})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.sd1, P.sd4__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1578})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.sd1, P.sd4__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1586})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.sd1, P.sd4__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1594})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.sd2, P.sd4__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1579})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.sd2, P.sd4__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1587})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.sd2, P.sd4__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1595})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.sd3, P.sd4__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1298})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.sd3, P.sd4__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1306})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.sd3, P.sd4__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1314})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.sd4__tilde__, P.sd4, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1299})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.sd4__tilde__, P.sd4, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1307})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.sd4__tilde__, P.sd4, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1315})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.sd4__tilde__, P.sd5, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_642})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.sd4__tilde__, P.sd5, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_646})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.sd4__tilde__, P.sd5, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_650})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.sd4__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_643})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.sd4__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_647})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.sd4__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_651})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.sd1, P.sd5__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1268})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.sd1, P.sd5__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1276})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.sd1, P.sd5__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1284})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.sd2, P.sd5__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1269})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.sd2, P.sd5__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1277})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.sd2, P.sd5__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1285})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.sd5__tilde__, P.sd5, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1270})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.sd5__tilde__, P.sd5, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1278})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.sd5__tilde__, P.sd5, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1286})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.sd5__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1271})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.sd5__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1279})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.sd5__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1287})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.sd1, P.sd6__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1272})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.sd1, P.sd6__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1280})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.sd1, P.sd6__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1288})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.sd2, P.sd6__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1273})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.sd2, P.sd6__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1281})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.sd2, P.sd6__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1289})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.sd5, P.sd6__tilde__, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1274})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.sd5, P.sd6__tilde__, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1282})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.sd5, P.sd6__tilde__, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1290})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.sd6__tilde__, P.sd6, P.sv1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1275})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.sd6__tilde__, P.sd6, P.sv2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1283})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.sd6__tilde__, P.sd6, P.sv3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1291})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.sl1__plus__, P.sl1__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1604})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.sl1__plus__, P.sl1__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1612})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.sl1__plus__, P.sl2__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1332})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.sl1__plus__, P.sl2__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1344})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.sl1__plus__, P.sl3__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1333})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.sl1__plus__, P.sl3__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1340})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.sl1__plus__, P.sl4__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1596})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.sl1__plus__, P.sl4__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1600})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.sl1__plus__, P.sl5__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1597})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.sl1__plus__, P.sl5__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1602})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.sl1__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1605})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.sl1__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1613})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.sl1__minus__, P.sl2__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1606})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.sl1__minus__, P.sl2__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1614})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.sl2__plus__, P.sl2__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1334})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.sl2__plus__, P.sl2__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1345})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.sl2__plus__, P.sl3__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1335})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.sl2__plus__, P.sl3__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1341})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.sl2__plus__, P.sl4__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_652})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.sl2__plus__, P.sl4__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_656})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.sl2__plus__, P.sl5__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_653})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.sl2__plus__, P.sl5__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_658})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.sl2__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1607})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.sl2__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1615})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.sl1__minus__, P.sl3__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1608})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.sl1__minus__, P.sl3__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1616})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.sl2__minus__, P.sl3__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1336})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.sl2__minus__, P.sl3__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1346})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.sl3__plus__, P.sl3__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1337})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.sl3__plus__, P.sl3__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1342})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.sl3__plus__, P.sl4__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_654})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.sl3__plus__, P.sl4__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_657})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.sl3__plus__, P.sl5__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_655})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.sl3__plus__, P.sl5__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_659})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.sl3__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1609})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.sl3__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1617})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.sl1__minus__, P.sl4__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1320})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.sl1__minus__, P.sl4__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1326})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.sl4__plus__, P.sl4__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1316})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.sl4__plus__, P.sl4__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1321})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.sl4__plus__, P.sl5__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1317})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.sl4__plus__, P.sl5__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1327})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.sl4__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1322})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.sl4__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1328})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.sl1__minus__, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1323})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.sl1__minus__, P.sl5__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1329})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.sl4__minus__, P.sl5__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1318})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.sl4__minus__, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1324})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.sl5__plus__, P.sl5__minus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1319})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.sl5__plus__, P.sl5__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1330})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.sl5__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1325})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.sl5__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1331})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.sl1__minus__, P.sl6__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1610})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.sl1__minus__, P.sl6__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1618})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.sl2__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1338})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.sl2__minus__, P.sl6__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1347})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.sl3__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1339})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.sl3__minus__, P.sl6__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1343})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.sl4__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1598})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.sl4__minus__, P.sl6__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1601})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.sl5__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1599})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.sl5__minus__, P.sl6__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1603})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.sl6__plus__, P.sl6__minus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1611})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.sl6__plus__, P.sl6__minus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1619})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.n1, P.u, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1030,(0,0):C.GC_2088})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.n1, P.u, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1869,(0,1):C.GC_2093})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.n2, P.u, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1048,(0,0):C.GC_2089})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.n2, P.u, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1904,(0,1):C.GC_2094})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.n3, P.u, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1066,(0,0):C.GC_2090})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.n3, P.u, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1939,(0,1):C.GC_2095})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.n4, P.u, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1084,(0,0):C.GC_2091})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.n4, P.u, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1974,(0,1):C.GC_2096})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.n1, P.c, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1031,(0,0):C.GC_2083})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.n1, P.c, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1870,(0,1):C.GC_2098})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.n2, P.c, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1049,(0,0):C.GC_2084})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.n2, P.c, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1905,(0,1):C.GC_2099})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.n3, P.c, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1067,(0,0):C.GC_2085})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.n3, P.c, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1940,(0,1):C.GC_2100})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.n4, P.c, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1085,(0,0):C.GC_2086})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.n4, P.c, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1975,(0,1):C.GC_2101})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.n1, P.t, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2068,(0,1):C.GC_2063})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.n1, P.t, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2078,(0,1):C.GC_2073})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.n2, P.t, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2069,(0,1):C.GC_2064})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.n2, P.t, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2079,(0,1):C.GC_2074})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.n3, P.t, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2070,(0,1):C.GC_2065})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.n3, P.t, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2080,(0,1):C.GC_2075})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.n4, P.t, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2071,(0,1):C.GC_2066})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.n4, P.t, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2081,(0,1):C.GC_2076})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.e__plus__, P.d, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_696})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.e__plus__, P.d, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_697})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.e__plus__, P.d, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_698})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.e__plus__, P.d, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_699})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.mu__plus__, P.d, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_700})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.mu__plus__, P.d, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_701})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.mu__plus__, P.d, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_702})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.mu__plus__, P.d, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_703})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.tau__plus__, P.d, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_704})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.tau__plus__, P.d, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_705})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.tau__plus__, P.d, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_706})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.tau__plus__, P.d, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_707})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.e__plus__, P.s, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_708})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.e__plus__, P.s, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_709})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.e__plus__, P.s, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_710})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.e__plus__, P.s, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_711})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.mu__plus__, P.s, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_712})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.mu__plus__, P.s, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_713})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.mu__plus__, P.s, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_714})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.mu__plus__, P.s, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_715})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.tau__plus__, P.s, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_716})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.tau__plus__, P.s, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_717})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.tau__plus__, P.s, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_718})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.tau__plus__, P.s, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_719})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.e__plus__, P.b, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_720})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.e__plus__, P.b, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_721})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.e__plus__, P.b, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_722})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.e__plus__, P.b, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_723})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.mu__plus__, P.b, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_724})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.mu__plus__, P.b, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_725})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.mu__plus__, P.b, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_726})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.mu__plus__, P.b, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_727})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.tau__plus__, P.b, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_728})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.tau__plus__, P.b, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_729})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.tau__plus__, P.b, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_730})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.tau__plus__, P.b, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_731})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.a, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_736})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.a, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_738})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.a, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_740})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.a, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_742})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.a, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_744})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.a, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_746})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.a, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_732})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.a, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_734})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.H__plus__, P.sd1, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2488})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.H__plus__, P.sd1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2489})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.H__plus__, P.sd2, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2490})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.H__plus__, P.sd2, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2491})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.H__plus__, P.sd3, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2492})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.H__plus__, P.sd3, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2448})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.H__plus__, P.sd4, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2493})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.H__plus__, P.sd4, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2449})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.H__plus__, P.sd5, P.su3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2452})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.H__plus__, P.sd5, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2482})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.H__plus__, P.sd6, P.su4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2453})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.H__plus__, P.sd6, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2483})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.s__tilde__, P.d__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_752})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.s__tilde__, P.d__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_753})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.s__tilde__, P.d__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_754})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.s__tilde__, P.d__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_755})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.b__tilde__, P.d__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_756})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.b__tilde__, P.d__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_757})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.b__tilde__, P.d__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_758})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.b__tilde__, P.d__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_759})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.b__tilde__, P.s__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_760})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.b__tilde__, P.s__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_761})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.b__tilde__, P.s__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_762})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.b__tilde__, P.s__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_763})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.sd1, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1780})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.sd1, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1781})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.sd1, P.sl1__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1676})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.sd1, P.sl1__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1677})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.sd1, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1628})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.sd1, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1629})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.sd1, P.sl2__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1380})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.sd1, P.sl2__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1381})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.sd1, P.sl2__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1382})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.sd1, P.sl2__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1383})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.sd1, P.sl3__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1384})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.sd1, P.sl3__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1385})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.sd1, P.sl3__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1386})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.sd1, P.sl3__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1387})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.sd1, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1782})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.sd1, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1783})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.sd1, P.sl4__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1678})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.sd1, P.sl4__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1679})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.sd1, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1620})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.sd1, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1621})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.sd1, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1784})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.sd1, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1785})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.sd1, P.sl5__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1680})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.sd1, P.sl5__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1681})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.sd1, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1622})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.sd1, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1623})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.sd1, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1786})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.sd1, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1787})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.sd1, P.sl6__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1682})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.sd1, P.sl6__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1683})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.sd1, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1630})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.sd1, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1631})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.sd2, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1788})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.sd2, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1789})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.sd2, P.sl1__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1684})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.sd2, P.sl1__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1685})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.sd2, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1632})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.sd2, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1633})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.sd2, P.sl2__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1388})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.sd2, P.sl2__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1389})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.sd2, P.sl2__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1390})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.sd2, P.sl2__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1391})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.sd2, P.sl3__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1392})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.sd2, P.sl3__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1393})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.sd2, P.sl3__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1394})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.sd2, P.sl3__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1395})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.sd2, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1790})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.sd2, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1791})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.sd2, P.sl4__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1686})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.sd2, P.sl4__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1687})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.sd2, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1624})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.sd2, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1625})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.sd2, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1792})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.sd2, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1793})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.sd2, P.sl5__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1688})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.sd2, P.sl5__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1689})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.sd2, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1626})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.sd2, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1627})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.sd2, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1794})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.sd2, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1795})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.sd2, P.sl6__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1690})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.sd2, P.sl6__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1691})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.sd2, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1634})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.sd2, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1635})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.sd3, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1796})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.sd3, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1797})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.sd3, P.sl1__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1692})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.sd3, P.sl1__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1693})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.sd3, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1636})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.sd3, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1637})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.sd3, P.sl2__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1396})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.sd3, P.sl2__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1397})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.sd3, P.sl2__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1398})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.sd3, P.sl2__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1399})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.sd3, P.sl3__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1400})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.sd3, P.sl3__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1401})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.sd3, P.sl3__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1402})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.sd3, P.sl3__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1403})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.sd3, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1798})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.sd3, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1799})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.sd3, P.sl4__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1694})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.sd3, P.sl4__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1695})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.sd3, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_764})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.sd3, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_765})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.sd3, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1800})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.sd3, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1801})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.sd3, P.sl5__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1696})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.sd3, P.sl5__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1697})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.sd3, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_766})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.sd3, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_767})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.sd3, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1802})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.sd3, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1803})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.sd3, P.sl6__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1698})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.sd3, P.sl6__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1699})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.sd3, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1638})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.sd3, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1639})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.sd4, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1804})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.sd4, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1805})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.sd4, P.sl1__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1700})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.sd4, P.sl1__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1701})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.sd4, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1640})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.sd4, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1641})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.sd4, P.sl2__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1404})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.sd4, P.sl2__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1405})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.sd4, P.sl2__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1406})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.sd4, P.sl2__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1407})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.sd4, P.sl3__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1408})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.sd4, P.sl3__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1409})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.sd4, P.sl3__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1410})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.sd4, P.sl3__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1411})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.sd4, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1806})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.sd4, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1807})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.sd4, P.sl4__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1702})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.sd4, P.sl4__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1703})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.sd4, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_768})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.sd4, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_769})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.sd4, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1808})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.sd4, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1809})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.sd4, P.sl5__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1704})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.sd4, P.sl5__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1705})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.sd4, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_770})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.sd4, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_771})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.sd4, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1810})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.sd4, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1811})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.sd4, P.sl6__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1706})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.sd4, P.sl6__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1707})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.sd4, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1642})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.sd4, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1643})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.sd5, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1348})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.sd5, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1349})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.sd5, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1350})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.sd5, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1351})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.sd5, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1352})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.sd5, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1353})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.sd5, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1354})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.sd5, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1355})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.sd5, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1356})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.sd5, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1357})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.sd5, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1358})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.sd5, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1359})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.sd5, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1360})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.sd5, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1361})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.sd5, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1362})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.sd5, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1363})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.sd6, P.sl1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1364})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.sd6, P.sl1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1365})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.sd6, P.sl1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1366})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.sd6, P.sl1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1367})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.sd6, P.sl4__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1368})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.sd6, P.sl4__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1369})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.sd6, P.sl4__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1370})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.sd6, P.sl4__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1371})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.sd6, P.sl5__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1372})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.sd6, P.sl5__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1373})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.sd6, P.sl5__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1374})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.sd6, P.sl5__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1375})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.sd6, P.sl6__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1376})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.sd6, P.sl6__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1377})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.sd6, P.sl6__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1378})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.sd6, P.sl6__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1379})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1708})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1709})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1412})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1413})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su5__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1710})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.sd1__tilde__, P.sd3__tilde__, P.su6__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1711})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1716})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1717})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1414})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1415})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su5__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1718})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.sd1__tilde__, P.sd4__tilde__, P.su6__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1719})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.sd1__tilde__, P.sd5__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1420})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.sd1__tilde__, P.sd5__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1421})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.sd1__tilde__, P.sd5__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1422})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.sd1__tilde__, P.sd5__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1423})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.sd1__tilde__, P.sd6__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1432})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.sd1__tilde__, P.sd6__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1433})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.sd1__tilde__, P.sd6__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1434})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.sd1__tilde__, P.sd6__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1435})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1712})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1713})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1416})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1417})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su5__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1714})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.sd2__tilde__, P.sd3__tilde__, P.su6__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1715})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1720})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1721})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1418})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1419})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su5__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1722})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.sd2__tilde__, P.sd4__tilde__, P.su6__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1723})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.sd2__tilde__, P.sd5__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1424})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.sd2__tilde__, P.sd5__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1425})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.sd2__tilde__, P.sd5__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1426})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.sd2__tilde__, P.sd5__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1427})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.sd2__tilde__, P.sd6__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1436})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.sd2__tilde__, P.sd6__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1437})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.sd2__tilde__, P.sd6__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1438})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.sd2__tilde__, P.sd6__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1439})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1724})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1725})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_10})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_11})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su5__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1726})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.sd3__tilde__, P.sd4__tilde__, P.su6__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1727})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.sd3__tilde__, P.sd6__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1440})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.sd3__tilde__, P.sd6__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1441})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.sd3__tilde__, P.sd6__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1442})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.sd3__tilde__, P.sd6__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1443})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.sd4__tilde__, P.sd5__tilde__, P.su1__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1428})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.sd4__tilde__, P.sd5__tilde__, P.su2__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1429})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.sd4__tilde__, P.sd5__tilde__, P.su3__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1430})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.sd4__tilde__, P.sd5__tilde__, P.su4__tilde__ ],
                color = [ 'EpsilonBar(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1431})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.u__tilde__, P.n1, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1865,(0,1):C.GC_916})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.u__tilde__, P.n1, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1026,(0,0):C.GC_1845})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.c__tilde__, P.n1, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1866,(0,1):C.GC_912})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.c__tilde__, P.n1, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1027,(0,0):C.GC_1846})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.t__tilde__, P.n1, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1867,(0,1):C.GC_1028})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.t__tilde__, P.n1, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1868,(0,1):C.GC_1029})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.u__tilde__, P.n2, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1900,(0,1):C.GC_917})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.u__tilde__, P.n2, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1044,(0,0):C.GC_1880})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.c__tilde__, P.n2, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1901,(0,1):C.GC_913})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.c__tilde__, P.n2, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1045,(0,0):C.GC_1881})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.t__tilde__, P.n2, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1902,(0,1):C.GC_1046})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.t__tilde__, P.n2, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1903,(0,1):C.GC_1047})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.u__tilde__, P.n3, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1935,(0,1):C.GC_918})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.u__tilde__, P.n3, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1062,(0,0):C.GC_1915})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.c__tilde__, P.n3, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1936,(0,1):C.GC_914})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.c__tilde__, P.n3, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1063,(0,0):C.GC_1916})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.t__tilde__, P.n3, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1937,(0,1):C.GC_1064})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.t__tilde__, P.n3, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1938,(0,1):C.GC_1065})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.u__tilde__, P.n4, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1970,(0,1):C.GC_919})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.u__tilde__, P.n4, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1080,(0,0):C.GC_1950})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.c__tilde__, P.n4, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1971,(0,1):C.GC_915})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.c__tilde__, P.n4, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,1):C.GC_1081,(0,0):C.GC_1951})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.t__tilde__, P.n4, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1972,(0,1):C.GC_1082})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.t__tilde__, P.n4, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1973,(0,1):C.GC_1083})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.d__tilde__, P.x1__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2161})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.d__tilde__, P.x1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2156,(0,1):C.GC_1090})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.s__tilde__, P.x1__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2162})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.s__tilde__, P.x1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2157,(0,1):C.GC_1091})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.b__tilde__, P.x1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2167,(0,1):C.GC_1092})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.b__tilde__, P.x1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2168,(0,1):C.GC_1093})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.d__tilde__, P.x2__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2182})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.d__tilde__, P.x2__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2177,(0,1):C.GC_1109})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.s__tilde__, P.x2__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2183})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.s__tilde__, P.x2__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2178,(0,1):C.GC_1110})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.b__tilde__, P.x2__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2188,(0,1):C.GC_1111})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.b__tilde__, P.x2__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2189,(0,1):C.GC_1112})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.d__tilde__, P.e__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_12})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.d__tilde__, P.e__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_13})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.d__tilde__, P.e__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_14})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.d__tilde__, P.e__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_15})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.s__tilde__, P.e__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_16})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.s__tilde__, P.e__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_17})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.s__tilde__, P.e__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_18})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.s__tilde__, P.e__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_19})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.b__tilde__, P.e__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_20})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.b__tilde__, P.e__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_21})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.b__tilde__, P.e__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_22})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.b__tilde__, P.e__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_23})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.d__tilde__, P.mu__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_24})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.d__tilde__, P.mu__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_25})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.d__tilde__, P.mu__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_26})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.d__tilde__, P.mu__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_27})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.s__tilde__, P.mu__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_28})

V_1572 = Vertex(name = 'V_1572',
                particles = [ P.s__tilde__, P.mu__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_29})

V_1573 = Vertex(name = 'V_1573',
                particles = [ P.s__tilde__, P.mu__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_30})

V_1574 = Vertex(name = 'V_1574',
                particles = [ P.s__tilde__, P.mu__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_31})

V_1575 = Vertex(name = 'V_1575',
                particles = [ P.b__tilde__, P.mu__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_32})

V_1576 = Vertex(name = 'V_1576',
                particles = [ P.b__tilde__, P.mu__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_33})

V_1577 = Vertex(name = 'V_1577',
                particles = [ P.b__tilde__, P.mu__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_34})

V_1578 = Vertex(name = 'V_1578',
                particles = [ P.b__tilde__, P.mu__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_35})

V_1579 = Vertex(name = 'V_1579',
                particles = [ P.d__tilde__, P.tau__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_36})

V_1580 = Vertex(name = 'V_1580',
                particles = [ P.d__tilde__, P.tau__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_37})

V_1581 = Vertex(name = 'V_1581',
                particles = [ P.d__tilde__, P.tau__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_38})

V_1582 = Vertex(name = 'V_1582',
                particles = [ P.d__tilde__, P.tau__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_39})

V_1583 = Vertex(name = 'V_1583',
                particles = [ P.s__tilde__, P.tau__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_40})

V_1584 = Vertex(name = 'V_1584',
                particles = [ P.s__tilde__, P.tau__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_41})

V_1585 = Vertex(name = 'V_1585',
                particles = [ P.s__tilde__, P.tau__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_42})

V_1586 = Vertex(name = 'V_1586',
                particles = [ P.s__tilde__, P.tau__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_43})

V_1587 = Vertex(name = 'V_1587',
                particles = [ P.b__tilde__, P.tau__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_44})

V_1588 = Vertex(name = 'V_1588',
                particles = [ P.b__tilde__, P.tau__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_45})

V_1589 = Vertex(name = 'V_1589',
                particles = [ P.b__tilde__, P.tau__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_46})

V_1590 = Vertex(name = 'V_1590',
                particles = [ P.b__tilde__, P.tau__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_47})

V_1591 = Vertex(name = 'V_1591',
                particles = [ P.s, P.d, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_48})

V_1592 = Vertex(name = 'V_1592',
                particles = [ P.s, P.d, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_49})

V_1593 = Vertex(name = 'V_1593',
                particles = [ P.s, P.d, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_50})

V_1594 = Vertex(name = 'V_1594',
                particles = [ P.s, P.d, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_51})

V_1595 = Vertex(name = 'V_1595',
                particles = [ P.b, P.d, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_52})

V_1596 = Vertex(name = 'V_1596',
                particles = [ P.b, P.d, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_53})

V_1597 = Vertex(name = 'V_1597',
                particles = [ P.b, P.d, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_54})

V_1598 = Vertex(name = 'V_1598',
                particles = [ P.b, P.d, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_55})

V_1599 = Vertex(name = 'V_1599',
                particles = [ P.b, P.s, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_56})

V_1600 = Vertex(name = 'V_1600',
                particles = [ P.b, P.s, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_57})

V_1601 = Vertex(name = 'V_1601',
                particles = [ P.b, P.s, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_58})

V_1602 = Vertex(name = 'V_1602',
                particles = [ P.b, P.s, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_59})

V_1603 = Vertex(name = 'V_1603',
                particles = [ P.H__minus__, P.sd1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2498})

V_1604 = Vertex(name = 'V_1604',
                particles = [ P.H__minus__, P.sd1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2499})

V_1605 = Vertex(name = 'V_1605',
                particles = [ P.H__minus__, P.sd2__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2500})

V_1606 = Vertex(name = 'V_1606',
                particles = [ P.H__minus__, P.sd2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2501})

V_1607 = Vertex(name = 'V_1607',
                particles = [ P.H__minus__, P.sd3__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2486})

V_1608 = Vertex(name = 'V_1608',
                particles = [ P.H__minus__, P.sd3__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2426})

V_1609 = Vertex(name = 'V_1609',
                particles = [ P.H__minus__, P.sd4__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2487})

V_1610 = Vertex(name = 'V_1610',
                particles = [ P.H__minus__, P.sd4__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2427})

V_1611 = Vertex(name = 'V_1611',
                particles = [ P.H__minus__, P.sd5__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2502})

V_1612 = Vertex(name = 'V_1612',
                particles = [ P.H__minus__, P.sd5__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2472})

V_1613 = Vertex(name = 'V_1613',
                particles = [ P.H__minus__, P.sd6__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2503})

V_1614 = Vertex(name = 'V_1614',
                particles = [ P.H__minus__, P.sd6__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2473})

V_1615 = Vertex(name = 'V_1615',
                particles = [ P.a, P.a, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_90})

V_1616 = Vertex(name = 'V_1616',
                particles = [ P.a, P.a, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_93})

V_1617 = Vertex(name = 'V_1617',
                particles = [ P.a, P.a, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_96})

V_1618 = Vertex(name = 'V_1618',
                particles = [ P.a, P.a, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_99})

V_1619 = Vertex(name = 'V_1619',
                particles = [ P.a, P.a, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_102})

V_1620 = Vertex(name = 'V_1620',
                particles = [ P.a, P.a, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_105})

V_1621 = Vertex(name = 'V_1621',
                particles = [ P.a, P.a, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_84})

V_1622 = Vertex(name = 'V_1622',
                particles = [ P.a, P.a, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_87})

V_1623 = Vertex(name = 'V_1623',
                particles = [ P.h02, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2336})

V_1624 = Vertex(name = 'V_1624',
                particles = [ P.h02, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2337})

V_1625 = Vertex(name = 'V_1625',
                particles = [ P.h02, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2338})

V_1626 = Vertex(name = 'V_1626',
                particles = [ P.h02, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2339})

V_1627 = Vertex(name = 'V_1627',
                particles = [ P.h02, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2340})

V_1628 = Vertex(name = 'V_1628',
                particles = [ P.h02, P.su3__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2282})

V_1629 = Vertex(name = 'V_1629',
                particles = [ P.h02, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2341})

V_1630 = Vertex(name = 'V_1630',
                particles = [ P.h02, P.su4__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2283})

V_1631 = Vertex(name = 'V_1631',
                particles = [ P.h02, P.su4, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2284})

V_1632 = Vertex(name = 'V_1632',
                particles = [ P.h02, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2334})

V_1633 = Vertex(name = 'V_1633',
                particles = [ P.h02, P.su3, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2285})

V_1634 = Vertex(name = 'V_1634',
                particles = [ P.h02, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2335})

V_1635 = Vertex(name = 'V_1635',
                particles = [ P.h01, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2350})

V_1636 = Vertex(name = 'V_1636',
                particles = [ P.h01, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2351})

V_1637 = Vertex(name = 'V_1637',
                particles = [ P.h01, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2352})

V_1638 = Vertex(name = 'V_1638',
                particles = [ P.h01, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2353})

V_1639 = Vertex(name = 'V_1639',
                particles = [ P.h01, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2301})

V_1640 = Vertex(name = 'V_1640',
                particles = [ P.h01, P.su3__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2294})

V_1641 = Vertex(name = 'V_1641',
                particles = [ P.h01, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2302})

V_1642 = Vertex(name = 'V_1642',
                particles = [ P.h01, P.su4__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2295})

V_1643 = Vertex(name = 'V_1643',
                particles = [ P.h01, P.su4, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2354})

V_1644 = Vertex(name = 'V_1644',
                particles = [ P.h01, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2305})

V_1645 = Vertex(name = 'V_1645',
                particles = [ P.h01, P.su3, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2355})

V_1646 = Vertex(name = 'V_1646',
                particles = [ P.h01, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2306})

V_1647 = Vertex(name = 'V_1647',
                particles = [ P.A0, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2504})

V_1648 = Vertex(name = 'V_1648',
                particles = [ P.A0, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2505})

V_1649 = Vertex(name = 'V_1649',
                particles = [ P.A0, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2506})

V_1650 = Vertex(name = 'V_1650',
                particles = [ P.A0, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2507})

V_1651 = Vertex(name = 'V_1651',
                particles = [ P.A0, P.su3__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2450})

V_1652 = Vertex(name = 'V_1652',
                particles = [ P.A0, P.su4__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2451})

V_1653 = Vertex(name = 'V_1653',
                particles = [ P.A0, P.su4, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2508})

V_1654 = Vertex(name = 'V_1654',
                particles = [ P.A0, P.su3, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_2509})

V_1655 = Vertex(name = 'V_1655',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1728})

V_1656 = Vertex(name = 'V_1656',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1729})

V_1657 = Vertex(name = 'V_1657',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1644})

V_1658 = Vertex(name = 'V_1658',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1645})

V_1659 = Vertex(name = 'V_1659',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1452})

V_1660 = Vertex(name = 'V_1660',
                particles = [ P.sd1__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1453})

V_1661 = Vertex(name = 'V_1661',
                particles = [ P.sd1__tilde__, P.sl2__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1156})

V_1662 = Vertex(name = 'V_1662',
                particles = [ P.sd1__tilde__, P.sl2__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1157})

V_1663 = Vertex(name = 'V_1663',
                particles = [ P.sd1__tilde__, P.sl2__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1158})

V_1664 = Vertex(name = 'V_1664',
                particles = [ P.sd1__tilde__, P.sl2__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1159})

V_1665 = Vertex(name = 'V_1665',
                particles = [ P.sd1__tilde__, P.sl3__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1160})

V_1666 = Vertex(name = 'V_1666',
                particles = [ P.sd1__tilde__, P.sl3__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1161})

V_1667 = Vertex(name = 'V_1667',
                particles = [ P.sd1__tilde__, P.sl3__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1162})

V_1668 = Vertex(name = 'V_1668',
                particles = [ P.sd1__tilde__, P.sl3__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1163})

V_1669 = Vertex(name = 'V_1669',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1730})

V_1670 = Vertex(name = 'V_1670',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1731})

V_1671 = Vertex(name = 'V_1671',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1646})

V_1672 = Vertex(name = 'V_1672',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1647})

V_1673 = Vertex(name = 'V_1673',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1444})

V_1674 = Vertex(name = 'V_1674',
                particles = [ P.sd1__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1445})

V_1675 = Vertex(name = 'V_1675',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1732})

V_1676 = Vertex(name = 'V_1676',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1733})

V_1677 = Vertex(name = 'V_1677',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1648})

V_1678 = Vertex(name = 'V_1678',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1649})

V_1679 = Vertex(name = 'V_1679',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1446})

V_1680 = Vertex(name = 'V_1680',
                particles = [ P.sd1__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1447})

V_1681 = Vertex(name = 'V_1681',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1734})

V_1682 = Vertex(name = 'V_1682',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1735})

V_1683 = Vertex(name = 'V_1683',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1650})

V_1684 = Vertex(name = 'V_1684',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1651})

V_1685 = Vertex(name = 'V_1685',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1454})

V_1686 = Vertex(name = 'V_1686',
                particles = [ P.sd1__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1455})

V_1687 = Vertex(name = 'V_1687',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1736})

V_1688 = Vertex(name = 'V_1688',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1737})

V_1689 = Vertex(name = 'V_1689',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1652})

V_1690 = Vertex(name = 'V_1690',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1653})

V_1691 = Vertex(name = 'V_1691',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1456})

V_1692 = Vertex(name = 'V_1692',
                particles = [ P.sd2__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1457})

V_1693 = Vertex(name = 'V_1693',
                particles = [ P.sd2__tilde__, P.sl2__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1164})

V_1694 = Vertex(name = 'V_1694',
                particles = [ P.sd2__tilde__, P.sl2__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1165})

V_1695 = Vertex(name = 'V_1695',
                particles = [ P.sd2__tilde__, P.sl2__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1166})

V_1696 = Vertex(name = 'V_1696',
                particles = [ P.sd2__tilde__, P.sl2__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1167})

V_1697 = Vertex(name = 'V_1697',
                particles = [ P.sd2__tilde__, P.sl3__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1168})

V_1698 = Vertex(name = 'V_1698',
                particles = [ P.sd2__tilde__, P.sl3__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1169})

V_1699 = Vertex(name = 'V_1699',
                particles = [ P.sd2__tilde__, P.sl3__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1170})

V_1700 = Vertex(name = 'V_1700',
                particles = [ P.sd2__tilde__, P.sl3__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1171})

V_1701 = Vertex(name = 'V_1701',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1738})

V_1702 = Vertex(name = 'V_1702',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1739})

V_1703 = Vertex(name = 'V_1703',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1654})

V_1704 = Vertex(name = 'V_1704',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1655})

V_1705 = Vertex(name = 'V_1705',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1448})

V_1706 = Vertex(name = 'V_1706',
                particles = [ P.sd2__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1449})

V_1707 = Vertex(name = 'V_1707',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1740})

V_1708 = Vertex(name = 'V_1708',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1741})

V_1709 = Vertex(name = 'V_1709',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1656})

V_1710 = Vertex(name = 'V_1710',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1657})

V_1711 = Vertex(name = 'V_1711',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1450})

V_1712 = Vertex(name = 'V_1712',
                particles = [ P.sd2__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1451})

V_1713 = Vertex(name = 'V_1713',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1742})

V_1714 = Vertex(name = 'V_1714',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1743})

V_1715 = Vertex(name = 'V_1715',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1658})

V_1716 = Vertex(name = 'V_1716',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1659})

V_1717 = Vertex(name = 'V_1717',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1458})

V_1718 = Vertex(name = 'V_1718',
                particles = [ P.sd2__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1459})

V_1719 = Vertex(name = 'V_1719',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1744})

V_1720 = Vertex(name = 'V_1720',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1745})

V_1721 = Vertex(name = 'V_1721',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1660})

V_1722 = Vertex(name = 'V_1722',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1661})

V_1723 = Vertex(name = 'V_1723',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1460})

V_1724 = Vertex(name = 'V_1724',
                particles = [ P.sd3__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1461})

V_1725 = Vertex(name = 'V_1725',
                particles = [ P.sd3__tilde__, P.sl2__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1172})

V_1726 = Vertex(name = 'V_1726',
                particles = [ P.sd3__tilde__, P.sl2__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1173})

V_1727 = Vertex(name = 'V_1727',
                particles = [ P.sd3__tilde__, P.sl2__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1174})

V_1728 = Vertex(name = 'V_1728',
                particles = [ P.sd3__tilde__, P.sl2__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1175})

V_1729 = Vertex(name = 'V_1729',
                particles = [ P.sd3__tilde__, P.sl3__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1176})

V_1730 = Vertex(name = 'V_1730',
                particles = [ P.sd3__tilde__, P.sl3__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1177})

V_1731 = Vertex(name = 'V_1731',
                particles = [ P.sd3__tilde__, P.sl3__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1178})

V_1732 = Vertex(name = 'V_1732',
                particles = [ P.sd3__tilde__, P.sl3__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1179})

V_1733 = Vertex(name = 'V_1733',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1746})

V_1734 = Vertex(name = 'V_1734',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1747})

V_1735 = Vertex(name = 'V_1735',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1662})

V_1736 = Vertex(name = 'V_1736',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1663})

V_1737 = Vertex(name = 'V_1737',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_108})

V_1738 = Vertex(name = 'V_1738',
                particles = [ P.sd3__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_109})

V_1739 = Vertex(name = 'V_1739',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1748})

V_1740 = Vertex(name = 'V_1740',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1749})

V_1741 = Vertex(name = 'V_1741',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1664})

V_1742 = Vertex(name = 'V_1742',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1665})

V_1743 = Vertex(name = 'V_1743',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_110})

V_1744 = Vertex(name = 'V_1744',
                particles = [ P.sd3__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_111})

V_1745 = Vertex(name = 'V_1745',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1750})

V_1746 = Vertex(name = 'V_1746',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1751})

V_1747 = Vertex(name = 'V_1747',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1666})

V_1748 = Vertex(name = 'V_1748',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1667})

V_1749 = Vertex(name = 'V_1749',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1462})

V_1750 = Vertex(name = 'V_1750',
                particles = [ P.sd3__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1463})

V_1751 = Vertex(name = 'V_1751',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1752})

V_1752 = Vertex(name = 'V_1752',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1753})

V_1753 = Vertex(name = 'V_1753',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1668})

V_1754 = Vertex(name = 'V_1754',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1669})

V_1755 = Vertex(name = 'V_1755',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1464})

V_1756 = Vertex(name = 'V_1756',
                particles = [ P.sd4__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1465})

V_1757 = Vertex(name = 'V_1757',
                particles = [ P.sd4__tilde__, P.sl2__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1180})

V_1758 = Vertex(name = 'V_1758',
                particles = [ P.sd4__tilde__, P.sl2__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1181})

V_1759 = Vertex(name = 'V_1759',
                particles = [ P.sd4__tilde__, P.sl2__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1182})

V_1760 = Vertex(name = 'V_1760',
                particles = [ P.sd4__tilde__, P.sl2__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1183})

V_1761 = Vertex(name = 'V_1761',
                particles = [ P.sd4__tilde__, P.sl3__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1184})

V_1762 = Vertex(name = 'V_1762',
                particles = [ P.sd4__tilde__, P.sl3__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1185})

V_1763 = Vertex(name = 'V_1763',
                particles = [ P.sd4__tilde__, P.sl3__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1186})

V_1764 = Vertex(name = 'V_1764',
                particles = [ P.sd4__tilde__, P.sl3__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1187})

V_1765 = Vertex(name = 'V_1765',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1754})

V_1766 = Vertex(name = 'V_1766',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1755})

V_1767 = Vertex(name = 'V_1767',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1670})

V_1768 = Vertex(name = 'V_1768',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1671})

V_1769 = Vertex(name = 'V_1769',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_112})

V_1770 = Vertex(name = 'V_1770',
                particles = [ P.sd4__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_113})

V_1771 = Vertex(name = 'V_1771',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1756})

V_1772 = Vertex(name = 'V_1772',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1757})

V_1773 = Vertex(name = 'V_1773',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1672})

V_1774 = Vertex(name = 'V_1774',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1673})

V_1775 = Vertex(name = 'V_1775',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_114})

V_1776 = Vertex(name = 'V_1776',
                particles = [ P.sd4__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_115})

V_1777 = Vertex(name = 'V_1777',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1758})

V_1778 = Vertex(name = 'V_1778',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1759})

V_1779 = Vertex(name = 'V_1779',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1674})

V_1780 = Vertex(name = 'V_1780',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su4 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1675})

V_1781 = Vertex(name = 'V_1781',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1466})

V_1782 = Vertex(name = 'V_1782',
                particles = [ P.sd4__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1467})

V_1783 = Vertex(name = 'V_1783',
                particles = [ P.sd5__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1124})

V_1784 = Vertex(name = 'V_1784',
                particles = [ P.sd5__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1125})

V_1785 = Vertex(name = 'V_1785',
                particles = [ P.sd5__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1126})

V_1786 = Vertex(name = 'V_1786',
                particles = [ P.sd5__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1127})

V_1787 = Vertex(name = 'V_1787',
                particles = [ P.sd5__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1128})

V_1788 = Vertex(name = 'V_1788',
                particles = [ P.sd5__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1129})

V_1789 = Vertex(name = 'V_1789',
                particles = [ P.sd5__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1130})

V_1790 = Vertex(name = 'V_1790',
                particles = [ P.sd5__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1131})

V_1791 = Vertex(name = 'V_1791',
                particles = [ P.sd5__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1132})

V_1792 = Vertex(name = 'V_1792',
                particles = [ P.sd5__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1133})

V_1793 = Vertex(name = 'V_1793',
                particles = [ P.sd5__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1134})

V_1794 = Vertex(name = 'V_1794',
                particles = [ P.sd5__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1135})

V_1795 = Vertex(name = 'V_1795',
                particles = [ P.sd5__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1136})

V_1796 = Vertex(name = 'V_1796',
                particles = [ P.sd5__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1137})

V_1797 = Vertex(name = 'V_1797',
                particles = [ P.sd5__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1138})

V_1798 = Vertex(name = 'V_1798',
                particles = [ P.sd5__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1139})

V_1799 = Vertex(name = 'V_1799',
                particles = [ P.sd6__tilde__, P.sl1__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1140})

V_1800 = Vertex(name = 'V_1800',
                particles = [ P.sd6__tilde__, P.sl1__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1141})

V_1801 = Vertex(name = 'V_1801',
                particles = [ P.sd6__tilde__, P.sl1__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1142})

V_1802 = Vertex(name = 'V_1802',
                particles = [ P.sd6__tilde__, P.sl1__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1143})

V_1803 = Vertex(name = 'V_1803',
                particles = [ P.sd6__tilde__, P.sl4__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1144})

V_1804 = Vertex(name = 'V_1804',
                particles = [ P.sd6__tilde__, P.sl4__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1145})

V_1805 = Vertex(name = 'V_1805',
                particles = [ P.sd6__tilde__, P.sl4__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1146})

V_1806 = Vertex(name = 'V_1806',
                particles = [ P.sd6__tilde__, P.sl4__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1147})

V_1807 = Vertex(name = 'V_1807',
                particles = [ P.sd6__tilde__, P.sl5__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1148})

V_1808 = Vertex(name = 'V_1808',
                particles = [ P.sd6__tilde__, P.sl5__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1149})

V_1809 = Vertex(name = 'V_1809',
                particles = [ P.sd6__tilde__, P.sl5__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1150})

V_1810 = Vertex(name = 'V_1810',
                particles = [ P.sd6__tilde__, P.sl5__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1151})

V_1811 = Vertex(name = 'V_1811',
                particles = [ P.sd6__tilde__, P.sl6__minus__, P.su1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1152})

V_1812 = Vertex(name = 'V_1812',
                particles = [ P.sd6__tilde__, P.sl6__minus__, P.su2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1153})

V_1813 = Vertex(name = 'V_1813',
                particles = [ P.sd6__tilde__, P.sl6__minus__, P.su5 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1154})

V_1814 = Vertex(name = 'V_1814',
                particles = [ P.sd6__tilde__, P.sl6__minus__, P.su6 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1155})

V_1815 = Vertex(name = 'V_1815',
                particles = [ P.sd1, P.sd3, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1760})

V_1816 = Vertex(name = 'V_1816',
                particles = [ P.sd1, P.sd3, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1761})

V_1817 = Vertex(name = 'V_1817',
                particles = [ P.sd1, P.sd3, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1468})

V_1818 = Vertex(name = 'V_1818',
                particles = [ P.sd1, P.sd3, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1469})

V_1819 = Vertex(name = 'V_1819',
                particles = [ P.sd1, P.sd3, P.su5 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1762})

V_1820 = Vertex(name = 'V_1820',
                particles = [ P.sd1, P.sd3, P.su6 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1763})

V_1821 = Vertex(name = 'V_1821',
                particles = [ P.sd1, P.sd4, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1768})

V_1822 = Vertex(name = 'V_1822',
                particles = [ P.sd1, P.sd4, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1769})

V_1823 = Vertex(name = 'V_1823',
                particles = [ P.sd1, P.sd4, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1470})

V_1824 = Vertex(name = 'V_1824',
                particles = [ P.sd1, P.sd4, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1471})

V_1825 = Vertex(name = 'V_1825',
                particles = [ P.sd1, P.sd4, P.su5 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1770})

V_1826 = Vertex(name = 'V_1826',
                particles = [ P.sd1, P.sd4, P.su6 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1771})

V_1827 = Vertex(name = 'V_1827',
                particles = [ P.sd1, P.sd5, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1476})

V_1828 = Vertex(name = 'V_1828',
                particles = [ P.sd1, P.sd5, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1477})

V_1829 = Vertex(name = 'V_1829',
                particles = [ P.sd1, P.sd5, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1478})

V_1830 = Vertex(name = 'V_1830',
                particles = [ P.sd1, P.sd5, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1479})

V_1831 = Vertex(name = 'V_1831',
                particles = [ P.sd1, P.sd6, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1488})

V_1832 = Vertex(name = 'V_1832',
                particles = [ P.sd1, P.sd6, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1489})

V_1833 = Vertex(name = 'V_1833',
                particles = [ P.sd1, P.sd6, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1490})

V_1834 = Vertex(name = 'V_1834',
                particles = [ P.sd1, P.sd6, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1491})

V_1835 = Vertex(name = 'V_1835',
                particles = [ P.sd2, P.sd3, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1764})

V_1836 = Vertex(name = 'V_1836',
                particles = [ P.sd2, P.sd3, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1765})

V_1837 = Vertex(name = 'V_1837',
                particles = [ P.sd2, P.sd3, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1472})

V_1838 = Vertex(name = 'V_1838',
                particles = [ P.sd2, P.sd3, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1473})

V_1839 = Vertex(name = 'V_1839',
                particles = [ P.sd2, P.sd3, P.su5 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1766})

V_1840 = Vertex(name = 'V_1840',
                particles = [ P.sd2, P.sd3, P.su6 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1767})

V_1841 = Vertex(name = 'V_1841',
                particles = [ P.sd2, P.sd4, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1772})

V_1842 = Vertex(name = 'V_1842',
                particles = [ P.sd2, P.sd4, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1773})

V_1843 = Vertex(name = 'V_1843',
                particles = [ P.sd2, P.sd4, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1474})

V_1844 = Vertex(name = 'V_1844',
                particles = [ P.sd2, P.sd4, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1475})

V_1845 = Vertex(name = 'V_1845',
                particles = [ P.sd2, P.sd4, P.su5 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1774})

V_1846 = Vertex(name = 'V_1846',
                particles = [ P.sd2, P.sd4, P.su6 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1775})

V_1847 = Vertex(name = 'V_1847',
                particles = [ P.sd2, P.sd5, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1480})

V_1848 = Vertex(name = 'V_1848',
                particles = [ P.sd2, P.sd5, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1481})

V_1849 = Vertex(name = 'V_1849',
                particles = [ P.sd2, P.sd5, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1482})

V_1850 = Vertex(name = 'V_1850',
                particles = [ P.sd2, P.sd5, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1483})

V_1851 = Vertex(name = 'V_1851',
                particles = [ P.sd2, P.sd6, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1492})

V_1852 = Vertex(name = 'V_1852',
                particles = [ P.sd2, P.sd6, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1493})

V_1853 = Vertex(name = 'V_1853',
                particles = [ P.sd2, P.sd6, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1494})

V_1854 = Vertex(name = 'V_1854',
                particles = [ P.sd2, P.sd6, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1495})

V_1855 = Vertex(name = 'V_1855',
                particles = [ P.sd3, P.sd4, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1776})

V_1856 = Vertex(name = 'V_1856',
                particles = [ P.sd3, P.sd4, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1777})

V_1857 = Vertex(name = 'V_1857',
                particles = [ P.sd3, P.sd4, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_116})

V_1858 = Vertex(name = 'V_1858',
                particles = [ P.sd3, P.sd4, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_117})

V_1859 = Vertex(name = 'V_1859',
                particles = [ P.sd3, P.sd4, P.su5 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1778})

V_1860 = Vertex(name = 'V_1860',
                particles = [ P.sd3, P.sd4, P.su6 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1779})

V_1861 = Vertex(name = 'V_1861',
                particles = [ P.sd3, P.sd6, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1496})

V_1862 = Vertex(name = 'V_1862',
                particles = [ P.sd3, P.sd6, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1497})

V_1863 = Vertex(name = 'V_1863',
                particles = [ P.sd3, P.sd6, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1498})

V_1864 = Vertex(name = 'V_1864',
                particles = [ P.sd3, P.sd6, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1499})

V_1865 = Vertex(name = 'V_1865',
                particles = [ P.sd4, P.sd5, P.su1 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1484})

V_1866 = Vertex(name = 'V_1866',
                particles = [ P.sd4, P.sd5, P.su2 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1485})

V_1867 = Vertex(name = 'V_1867',
                particles = [ P.sd4, P.sd5, P.su3 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1486})

V_1868 = Vertex(name = 'V_1868',
                particles = [ P.sd4, P.sd5, P.su4 ],
                color = [ 'Epsilon(1,2,3)' ],
                lorentz = [ L.SSS1 ],
                couplings = {(0,0):C.GC_1487})

V_1869 = Vertex(name = 'V_1869',
                particles = [ P.go, P.d, P.sd4__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2003})

V_1870 = Vertex(name = 'V_1870',
                particles = [ P.go, P.d, P.sd6__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_2013})

V_1871 = Vertex(name = 'V_1871',
                particles = [ P.go, P.s, P.sd3__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_1998})

V_1872 = Vertex(name = 'V_1872',
                particles = [ P.go, P.s, P.sd5__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_2008})

V_1873 = Vertex(name = 'V_1873',
                particles = [ P.go, P.b, P.sd1__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1983,(0,1):C.GC_1978})

V_1874 = Vertex(name = 'V_1874',
                particles = [ P.go, P.b, P.sd2__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_1993,(0,1):C.GC_1988})

V_1875 = Vertex(name = 'V_1875',
                particles = [ P.g, P.sd1__tilde__, P.sd1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_773})

V_1876 = Vertex(name = 'V_1876',
                particles = [ P.g, P.sd1__tilde__, P.sd2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_775})

V_1877 = Vertex(name = 'V_1877',
                particles = [ P.g, P.sd1, P.sd2__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_777})

V_1878 = Vertex(name = 'V_1878',
                particles = [ P.g, P.sd2__tilde__, P.sd2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_779})

V_1879 = Vertex(name = 'V_1879',
                particles = [ P.g, P.sd3__tilde__, P.sd3 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_781})

V_1880 = Vertex(name = 'V_1880',
                particles = [ P.g, P.sd4__tilde__, P.sd4 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_783})

V_1881 = Vertex(name = 'V_1881',
                particles = [ P.g, P.sd5__tilde__, P.sd5 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_749})

V_1882 = Vertex(name = 'V_1882',
                particles = [ P.g, P.sd6__tilde__, P.sd6 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_751})

V_1883 = Vertex(name = 'V_1883',
                particles = [ P.go, P.u, P.su4__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2087})

V_1884 = Vertex(name = 'V_1884',
                particles = [ P.go, P.u, P.su5__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_2092})

V_1885 = Vertex(name = 'V_1885',
                particles = [ P.go, P.c, P.su3__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2082})

V_1886 = Vertex(name = 'V_1886',
                particles = [ P.go, P.c, P.su6__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_2097})

V_1887 = Vertex(name = 'V_1887',
                particles = [ P.go, P.t, P.su1__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2067,(0,1):C.GC_2062})

V_1888 = Vertex(name = 'V_1888',
                particles = [ P.go, P.t, P.su2__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2077,(0,1):C.GC_2072})

V_1889 = Vertex(name = 'V_1889',
                particles = [ P.g, P.su1__tilde__, P.su1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_737})

V_1890 = Vertex(name = 'V_1890',
                particles = [ P.g, P.su1__tilde__, P.su2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_739})

V_1891 = Vertex(name = 'V_1891',
                particles = [ P.g, P.su1, P.su2__tilde__ ],
                color = [ 'T(1,2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_741})

V_1892 = Vertex(name = 'V_1892',
                particles = [ P.g, P.su2__tilde__, P.su2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_743})

V_1893 = Vertex(name = 'V_1893',
                particles = [ P.g, P.su3__tilde__, P.su3 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_745})

V_1894 = Vertex(name = 'V_1894',
                particles = [ P.g, P.su4__tilde__, P.su4 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_747})

V_1895 = Vertex(name = 'V_1895',
                particles = [ P.g, P.su5__tilde__, P.su5 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_733})

V_1896 = Vertex(name = 'V_1896',
                particles = [ P.g, P.su6__tilde__, P.su6 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_735})

V_1897 = Vertex(name = 'V_1897',
                particles = [ P.d__tilde__, P.go, P.sd4 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_789})

V_1898 = Vertex(name = 'V_1898',
                particles = [ P.d__tilde__, P.go, P.sd6 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_791})

V_1899 = Vertex(name = 'V_1899',
                particles = [ P.s__tilde__, P.go, P.sd3 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_788})

V_1900 = Vertex(name = 'V_1900',
                particles = [ P.s__tilde__, P.go, P.sd5 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_790})

V_1901 = Vertex(name = 'V_1901',
                particles = [ P.b__tilde__, P.go, P.sd1 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_784,(0,1):C.GC_785})

V_1902 = Vertex(name = 'V_1902',
                particles = [ P.b__tilde__, P.go, P.sd2 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_786,(0,1):C.GC_787})

V_1903 = Vertex(name = 'V_1903',
                particles = [ P.a, P.g, P.sd1__tilde__, P.sd1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_257})

V_1904 = Vertex(name = 'V_1904',
                particles = [ P.a, P.g, P.sd1__tilde__, P.sd2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_260})

V_1905 = Vertex(name = 'V_1905',
                particles = [ P.a, P.g, P.sd1, P.sd2__tilde__ ],
                color = [ 'T(2,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_263})

V_1906 = Vertex(name = 'V_1906',
                particles = [ P.a, P.g, P.sd2__tilde__, P.sd2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_266})

V_1907 = Vertex(name = 'V_1907',
                particles = [ P.a, P.g, P.sd3__tilde__, P.sd3 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_269})

V_1908 = Vertex(name = 'V_1908',
                particles = [ P.a, P.g, P.sd4__tilde__, P.sd4 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_272})

V_1909 = Vertex(name = 'V_1909',
                particles = [ P.a, P.g, P.sd5__tilde__, P.sd5 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_251})

V_1910 = Vertex(name = 'V_1910',
                particles = [ P.a, P.g, P.sd6__tilde__, P.sd6 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_254})

V_1911 = Vertex(name = 'V_1911',
                particles = [ P.u__tilde__, P.go, P.su4 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_797})

V_1912 = Vertex(name = 'V_1912',
                particles = [ P.u__tilde__, P.go, P.su5 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_798})

V_1913 = Vertex(name = 'V_1913',
                particles = [ P.c__tilde__, P.go, P.su3 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_796})

V_1914 = Vertex(name = 'V_1914',
                particles = [ P.c__tilde__, P.go, P.su6 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_799})

V_1915 = Vertex(name = 'V_1915',
                particles = [ P.t__tilde__, P.go, P.su1 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_792,(0,1):C.GC_793})

V_1916 = Vertex(name = 'V_1916',
                particles = [ P.t__tilde__, P.go, P.su2 ],
                color = [ 'T(2,3,1)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_794,(0,1):C.GC_795})

V_1917 = Vertex(name = 'V_1917',
                particles = [ P.a, P.g, P.su1__tilde__, P.su1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_91})

V_1918 = Vertex(name = 'V_1918',
                particles = [ P.a, P.g, P.su1__tilde__, P.su2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_94})

V_1919 = Vertex(name = 'V_1919',
                particles = [ P.a, P.g, P.su1, P.su2__tilde__ ],
                color = [ 'T(2,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_97})

V_1920 = Vertex(name = 'V_1920',
                particles = [ P.a, P.g, P.su2__tilde__, P.su2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_100})

V_1921 = Vertex(name = 'V_1921',
                particles = [ P.a, P.g, P.su3__tilde__, P.su3 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_103})

V_1922 = Vertex(name = 'V_1922',
                particles = [ P.a, P.g, P.su4__tilde__, P.su4 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_106})

V_1923 = Vertex(name = 'V_1923',
                particles = [ P.a, P.g, P.su5__tilde__, P.su5 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_85})

V_1924 = Vertex(name = 'V_1924',
                particles = [ P.a, P.g, P.su6__tilde__, P.su6 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_88})

V_1925 = Vertex(name = 'V_1925',
                particles = [ P.g, P.g, P.sd1__tilde__, P.sd1 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_258,(0,0):C.GC_258})

V_1926 = Vertex(name = 'V_1926',
                particles = [ P.g, P.g, P.sd1__tilde__, P.sd2 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_261,(0,0):C.GC_261})

V_1927 = Vertex(name = 'V_1927',
                particles = [ P.g, P.g, P.sd1, P.sd2__tilde__ ],
                color = [ 'T(1,-1,4)*T(2,3,-1)', 'T(1,3,-1)*T(2,-1,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_264,(0,0):C.GC_264})

V_1928 = Vertex(name = 'V_1928',
                particles = [ P.g, P.g, P.sd2__tilde__, P.sd2 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_267,(0,0):C.GC_267})

V_1929 = Vertex(name = 'V_1929',
                particles = [ P.g, P.g, P.sd3__tilde__, P.sd3 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_270,(0,0):C.GC_270})

V_1930 = Vertex(name = 'V_1930',
                particles = [ P.g, P.g, P.sd4__tilde__, P.sd4 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_273,(0,0):C.GC_273})

V_1931 = Vertex(name = 'V_1931',
                particles = [ P.g, P.g, P.sd5__tilde__, P.sd5 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_252,(0,0):C.GC_252})

V_1932 = Vertex(name = 'V_1932',
                particles = [ P.g, P.g, P.sd6__tilde__, P.sd6 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_255,(0,0):C.GC_255})

V_1933 = Vertex(name = 'V_1933',
                particles = [ P.g, P.g, P.su1__tilde__, P.su1 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_92,(0,0):C.GC_92})

V_1934 = Vertex(name = 'V_1934',
                particles = [ P.g, P.g, P.su1__tilde__, P.su2 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_95,(0,0):C.GC_95})

V_1935 = Vertex(name = 'V_1935',
                particles = [ P.g, P.g, P.su1, P.su2__tilde__ ],
                color = [ 'T(1,-1,4)*T(2,3,-1)', 'T(1,3,-1)*T(2,-1,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_98,(0,0):C.GC_98})

V_1936 = Vertex(name = 'V_1936',
                particles = [ P.g, P.g, P.su2__tilde__, P.su2 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_101,(0,0):C.GC_101})

V_1937 = Vertex(name = 'V_1937',
                particles = [ P.g, P.g, P.su3__tilde__, P.su3 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_104,(0,0):C.GC_104})

V_1938 = Vertex(name = 'V_1938',
                particles = [ P.g, P.g, P.su4__tilde__, P.su4 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_107,(0,0):C.GC_107})

V_1939 = Vertex(name = 'V_1939',
                particles = [ P.g, P.g, P.su5__tilde__, P.su5 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_86,(0,0):C.GC_86})

V_1940 = Vertex(name = 'V_1940',
                particles = [ P.g, P.g, P.su6__tilde__, P.su6 ],
                color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(1,0):C.GC_89,(0,0):C.GC_89})

V_1941 = Vertex(name = 'V_1941',
                particles = [ P.x1__minus__, P.u, P.sd4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1094})

V_1942 = Vertex(name = 'V_1942',
                particles = [ P.x1__minus__, P.u, P.sd6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2163,(0,1):C.GC_1086})

V_1943 = Vertex(name = 'V_1943',
                particles = [ P.x2__minus__, P.u, P.sd4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1113})

V_1944 = Vertex(name = 'V_1944',
                particles = [ P.x2__minus__, P.u, P.sd6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2184,(0,1):C.GC_1105})

V_1945 = Vertex(name = 'V_1945',
                particles = [ P.x1__minus__, P.c, P.sd3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1095})

V_1946 = Vertex(name = 'V_1946',
                particles = [ P.x1__minus__, P.c, P.sd5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2164,(0,1):C.GC_1087})

V_1947 = Vertex(name = 'V_1947',
                particles = [ P.x2__minus__, P.c, P.sd3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1114})

V_1948 = Vertex(name = 'V_1948',
                particles = [ P.x2__minus__, P.c, P.sd5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2185,(0,1):C.GC_1106})

V_1949 = Vertex(name = 'V_1949',
                particles = [ P.x1__minus__, P.t, P.sd1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2165,(0,1):C.GC_1101})

V_1950 = Vertex(name = 'V_1950',
                particles = [ P.x1__minus__, P.t, P.sd2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2166,(0,1):C.GC_1102})

V_1951 = Vertex(name = 'V_1951',
                particles = [ P.x2__minus__, P.t, P.sd1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2186,(0,1):C.GC_1120})

V_1952 = Vertex(name = 'V_1952',
                particles = [ P.x2__minus__, P.t, P.sd2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2187,(0,1):C.GC_1121})

V_1953 = Vertex(name = 'V_1953',
                particles = [ P.x1__minus__, P.ve, P.sl3__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1096})

V_1954 = Vertex(name = 'V_1954',
                particles = [ P.x1__minus__, P.ve, P.sl4__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1088})

V_1955 = Vertex(name = 'V_1955',
                particles = [ P.x2__minus__, P.ve, P.sl3__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1115})

V_1956 = Vertex(name = 'V_1956',
                particles = [ P.x2__minus__, P.ve, P.sl4__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1107})

V_1957 = Vertex(name = 'V_1957',
                particles = [ P.x1__minus__, P.vm, P.sl2__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1097})

V_1958 = Vertex(name = 'V_1958',
                particles = [ P.x1__minus__, P.vm, P.sl5__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1089})

V_1959 = Vertex(name = 'V_1959',
                particles = [ P.x2__minus__, P.vm, P.sl2__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1116})

V_1960 = Vertex(name = 'V_1960',
                particles = [ P.x2__minus__, P.vm, P.sl5__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1108})

V_1961 = Vertex(name = 'V_1961',
                particles = [ P.x1__minus__, P.vt, P.sl1__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1103})

V_1962 = Vertex(name = 'V_1962',
                particles = [ P.x1__minus__, P.vt, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1104})

V_1963 = Vertex(name = 'V_1963',
                particles = [ P.x2__minus__, P.vt, P.sl1__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1122})

V_1964 = Vertex(name = 'V_1964',
                particles = [ P.x2__minus__, P.vt, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1123})

V_1965 = Vertex(name = 'V_1965',
                particles = [ P.e__minus__, P.x1__plus__, P.sv3__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2106,(0,1):C.GC_1812})

V_1966 = Vertex(name = 'V_1966',
                particles = [ P.mu__minus__, P.x1__plus__, P.sv2__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2107,(0,1):C.GC_1813})

V_1967 = Vertex(name = 'V_1967',
                particles = [ P.tau__minus__, P.x1__plus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2108,(0,1):C.GC_1814})

V_1968 = Vertex(name = 'V_1968',
                particles = [ P.e__minus__, P.x2__plus__, P.sv3__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2133,(0,1):C.GC_1825})

V_1969 = Vertex(name = 'V_1969',
                particles = [ P.mu__minus__, P.x2__plus__, P.sv2__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2134,(0,1):C.GC_1826})

V_1970 = Vertex(name = 'V_1970',
                particles = [ P.tau__minus__, P.x2__plus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2135,(0,1):C.GC_1827})

V_1971 = Vertex(name = 'V_1971',
                particles = [ P.d, P.x1__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1817})

V_1972 = Vertex(name = 'V_1972',
                particles = [ P.d, P.x1__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2109,(0,1):C.GC_1815})

V_1973 = Vertex(name = 'V_1973',
                particles = [ P.s, P.x1__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1818})

V_1974 = Vertex(name = 'V_1974',
                particles = [ P.s, P.x1__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2110,(0,1):C.GC_1816})

V_1975 = Vertex(name = 'V_1975',
                particles = [ P.b, P.x1__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2111,(0,1):C.GC_1823})

V_1976 = Vertex(name = 'V_1976',
                particles = [ P.b, P.x1__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2112,(0,1):C.GC_1824})

V_1977 = Vertex(name = 'V_1977',
                particles = [ P.d, P.x2__plus__, P.su4__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1830})

V_1978 = Vertex(name = 'V_1978',
                particles = [ P.d, P.x2__plus__, P.su5__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2136,(0,1):C.GC_1828})

V_1979 = Vertex(name = 'V_1979',
                particles = [ P.s, P.x2__plus__, P.su3__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS2 ],
                couplings = {(0,0):C.GC_1831})

V_1980 = Vertex(name = 'V_1980',
                particles = [ P.s, P.x2__plus__, P.su6__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2137,(0,1):C.GC_1829})

V_1981 = Vertex(name = 'V_1981',
                particles = [ P.b, P.x2__plus__, P.su1__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2138,(0,1):C.GC_1836})

V_1982 = Vertex(name = 'V_1982',
                particles = [ P.b, P.x2__plus__, P.su2__tilde__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS1, L.FFS2 ],
                couplings = {(0,0):C.GC_2139,(0,1):C.GC_1837})

V_1983 = Vertex(name = 'V_1983',
                particles = [ P.a, P.W__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2484})

V_1984 = Vertex(name = 'V_1984',
                particles = [ P.a, P.W__minus__, P.h01, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2537})

V_1985 = Vertex(name = 'V_1985',
                particles = [ P.a, P.W__minus__, P.A0, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2544})

V_1986 = Vertex(name = 'V_1986',
                particles = [ P.W__minus__, P.A0, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2543})

V_1987 = Vertex(name = 'V_1987',
                particles = [ P.W__minus__, P.h01, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2536})

V_1988 = Vertex(name = 'V_1988',
                particles = [ P.W__minus__, P.sd1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_836})

V_1989 = Vertex(name = 'V_1989',
                particles = [ P.W__minus__, P.sd1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_837})

V_1990 = Vertex(name = 'V_1990',
                particles = [ P.W__minus__, P.sd2__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_838})

V_1991 = Vertex(name = 'V_1991',
                particles = [ P.W__minus__, P.sd2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_839})

V_1992 = Vertex(name = 'V_1992',
                particles = [ P.W__minus__, P.sd5__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_840})

V_1993 = Vertex(name = 'V_1993',
                particles = [ P.W__minus__, P.sd6__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_841})

V_1994 = Vertex(name = 'V_1994',
                particles = [ P.a, P.W__minus__, P.h02, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2533})

V_1995 = Vertex(name = 'V_1995',
                particles = [ P.W__minus__, P.h02, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2532})

V_1996 = Vertex(name = 'V_1996',
                particles = [ P.W__minus__, P.sl1__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_842})

V_1997 = Vertex(name = 'V_1997',
                particles = [ P.W__minus__, P.sl4__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_845})

V_1998 = Vertex(name = 'V_1998',
                particles = [ P.W__minus__, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_844})

V_1999 = Vertex(name = 'V_1999',
                particles = [ P.W__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_843})

V_2000 = Vertex(name = 'V_2000',
                particles = [ P.a, P.W__minus__, P.sl1__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_860})

V_2001 = Vertex(name = 'V_2001',
                particles = [ P.a, P.W__minus__, P.sl4__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_863})

V_2002 = Vertex(name = 'V_2002',
                particles = [ P.a, P.W__minus__, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_862})

V_2003 = Vertex(name = 'V_2003',
                particles = [ P.a, P.W__minus__, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_861})

V_2004 = Vertex(name = 'V_2004',
                particles = [ P.a, P.W__minus__, P.sd1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_824})

V_2005 = Vertex(name = 'V_2005',
                particles = [ P.a, P.W__minus__, P.sd1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_826})

V_2006 = Vertex(name = 'V_2006',
                particles = [ P.a, P.W__minus__, P.sd2__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_828})

V_2007 = Vertex(name = 'V_2007',
                particles = [ P.a, P.W__minus__, P.sd2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_830})

V_2008 = Vertex(name = 'V_2008',
                particles = [ P.a, P.W__minus__, P.sd5__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_832})

V_2009 = Vertex(name = 'V_2009',
                particles = [ P.a, P.W__minus__, P.sd6__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_834})

V_2010 = Vertex(name = 'V_2010',
                particles = [ P.g, P.W__minus__, P.sd1__tilde__, P.su1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_825})

V_2011 = Vertex(name = 'V_2011',
                particles = [ P.g, P.W__minus__, P.sd1__tilde__, P.su2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_827})

V_2012 = Vertex(name = 'V_2012',
                particles = [ P.g, P.W__minus__, P.sd2__tilde__, P.su1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_829})

V_2013 = Vertex(name = 'V_2013',
                particles = [ P.g, P.W__minus__, P.sd2__tilde__, P.su2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_831})

V_2014 = Vertex(name = 'V_2014',
                particles = [ P.g, P.W__minus__, P.sd5__tilde__, P.su6 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_833})

V_2015 = Vertex(name = 'V_2015',
                particles = [ P.g, P.W__minus__, P.sd6__tilde__, P.su5 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_835})

V_2016 = Vertex(name = 'V_2016',
                particles = [ P.a, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVV1 ],
                couplings = {(0,0):C.GC_4})

V_2017 = Vertex(name = 'V_2017',
                particles = [ P.a, P.W__plus__, P.H__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2484})

V_2018 = Vertex(name = 'V_2018',
                particles = [ P.a, P.W__plus__, P.H__minus__, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2537})

V_2019 = Vertex(name = 'V_2019',
                particles = [ P.a, P.W__plus__, P.A0, P.H__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2545})

V_2020 = Vertex(name = 'V_2020',
                particles = [ P.W__plus__, P.A0, P.H__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2543})

V_2021 = Vertex(name = 'V_2021',
                particles = [ P.W__plus__, P.H__minus__, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2536})

V_2022 = Vertex(name = 'V_2022',
                particles = [ P.W__plus__, P.sd1, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_846})

V_2023 = Vertex(name = 'V_2023',
                particles = [ P.W__plus__, P.sd1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_847})

V_2024 = Vertex(name = 'V_2024',
                particles = [ P.W__plus__, P.sd2, P.su1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_848})

V_2025 = Vertex(name = 'V_2025',
                particles = [ P.W__plus__, P.sd2, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_849})

V_2026 = Vertex(name = 'V_2026',
                particles = [ P.W__plus__, P.sd5, P.su6__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_850})

V_2027 = Vertex(name = 'V_2027',
                particles = [ P.W__plus__, P.sd6, P.su5__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_851})

V_2028 = Vertex(name = 'V_2028',
                particles = [ P.a, P.W__plus__, P.H__minus__, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2533})

V_2029 = Vertex(name = 'V_2029',
                particles = [ P.W__plus__, P.H__minus__, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2532})

V_2030 = Vertex(name = 'V_2030',
                particles = [ P.W__plus__, P.sl1__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_852})

V_2031 = Vertex(name = 'V_2031',
                particles = [ P.W__plus__, P.sl4__minus__, P.sv3__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_855})

V_2032 = Vertex(name = 'V_2032',
                particles = [ P.W__plus__, P.sl5__minus__, P.sv2__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_854})

V_2033 = Vertex(name = 'V_2033',
                particles = [ P.W__plus__, P.sl6__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_853})

V_2034 = Vertex(name = 'V_2034',
                particles = [ P.a, P.W__plus__, P.sl1__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_856})

V_2035 = Vertex(name = 'V_2035',
                particles = [ P.a, P.W__plus__, P.sl4__minus__, P.sv3__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_859})

V_2036 = Vertex(name = 'V_2036',
                particles = [ P.a, P.W__plus__, P.sl5__minus__, P.sv2__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_858})

V_2037 = Vertex(name = 'V_2037',
                particles = [ P.a, P.W__plus__, P.sl6__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_857})

V_2038 = Vertex(name = 'V_2038',
                particles = [ P.a, P.W__plus__, P.sd1, P.su1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_864})

V_2039 = Vertex(name = 'V_2039',
                particles = [ P.a, P.W__plus__, P.sd1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_866})

V_2040 = Vertex(name = 'V_2040',
                particles = [ P.a, P.W__plus__, P.sd2, P.su1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_868})

V_2041 = Vertex(name = 'V_2041',
                particles = [ P.a, P.W__plus__, P.sd2, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_870})

V_2042 = Vertex(name = 'V_2042',
                particles = [ P.a, P.W__plus__, P.sd5, P.su6__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_872})

V_2043 = Vertex(name = 'V_2043',
                particles = [ P.a, P.W__plus__, P.sd6, P.su5__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_874})

V_2044 = Vertex(name = 'V_2044',
                particles = [ P.g, P.W__plus__, P.sd1, P.su1__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_865})

V_2045 = Vertex(name = 'V_2045',
                particles = [ P.g, P.W__plus__, P.sd1, P.su2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_867})

V_2046 = Vertex(name = 'V_2046',
                particles = [ P.g, P.W__plus__, P.sd2, P.su1__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_869})

V_2047 = Vertex(name = 'V_2047',
                particles = [ P.g, P.W__plus__, P.sd2, P.su2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_871})

V_2048 = Vertex(name = 'V_2048',
                particles = [ P.g, P.W__plus__, P.sd5, P.su6__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_873})

V_2049 = Vertex(name = 'V_2049',
                particles = [ P.g, P.W__plus__, P.sd6, P.su5__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_875})

V_2050 = Vertex(name = 'V_2050',
                particles = [ P.W__minus__, P.W__plus__, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2323})

V_2051 = Vertex(name = 'V_2051',
                particles = [ P.W__minus__, P.W__plus__, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2300})

V_2052 = Vertex(name = 'V_2052',
                particles = [ P.W__minus__, P.W__plus__, P.h01, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2396})

V_2053 = Vertex(name = 'V_2053',
                particles = [ P.W__minus__, P.W__plus__, P.h02, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2396})

V_2054 = Vertex(name = 'V_2054',
                particles = [ P.W__minus__, P.W__plus__, P.A0, P.A0 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2542})

V_2055 = Vertex(name = 'V_2055',
                particles = [ P.W__minus__, P.W__plus__, P.H__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2542})

V_2056 = Vertex(name = 'V_2056',
                particles = [ P.W__minus__, P.W__plus__, P.sd1__tilde__, P.sd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_803})

V_2057 = Vertex(name = 'V_2057',
                particles = [ P.W__minus__, P.W__plus__, P.sd1__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_804})

V_2058 = Vertex(name = 'V_2058',
                particles = [ P.W__minus__, P.W__plus__, P.sd1, P.sd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_805})

V_2059 = Vertex(name = 'V_2059',
                particles = [ P.W__minus__, P.W__plus__, P.sd2__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_806})

V_2060 = Vertex(name = 'V_2060',
                particles = [ P.W__minus__, P.W__plus__, P.sd5__tilde__, P.sd5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_807})

V_2061 = Vertex(name = 'V_2061',
                particles = [ P.W__minus__, P.W__plus__, P.sd6__tilde__, P.sd6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_808})

V_2062 = Vertex(name = 'V_2062',
                particles = [ P.W__minus__, P.W__plus__, P.sl1__plus__, P.sl1__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_809})

V_2063 = Vertex(name = 'V_2063',
                particles = [ P.W__minus__, P.W__plus__, P.sl1__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_810})

V_2064 = Vertex(name = 'V_2064',
                particles = [ P.W__minus__, P.W__plus__, P.sl4__plus__, P.sl4__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_811})

V_2065 = Vertex(name = 'V_2065',
                particles = [ P.W__minus__, P.W__plus__, P.sl5__plus__, P.sl5__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_812})

V_2066 = Vertex(name = 'V_2066',
                particles = [ P.W__minus__, P.W__plus__, P.sl1__minus__, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_813})

V_2067 = Vertex(name = 'V_2067',
                particles = [ P.W__minus__, P.W__plus__, P.sl6__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_814})

V_2068 = Vertex(name = 'V_2068',
                particles = [ P.W__minus__, P.W__plus__, P.sv1__tilde__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_801})

V_2069 = Vertex(name = 'V_2069',
                particles = [ P.W__minus__, P.W__plus__, P.sv2__tilde__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_801})

V_2070 = Vertex(name = 'V_2070',
                particles = [ P.W__minus__, P.W__plus__, P.sv3__tilde__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_801})

V_2071 = Vertex(name = 'V_2071',
                particles = [ P.W__minus__, P.W__plus__, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_815})

V_2072 = Vertex(name = 'V_2072',
                particles = [ P.W__minus__, P.W__plus__, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_816})

V_2073 = Vertex(name = 'V_2073',
                particles = [ P.W__minus__, P.W__plus__, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_817})

V_2074 = Vertex(name = 'V_2074',
                particles = [ P.W__minus__, P.W__plus__, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_818})

V_2075 = Vertex(name = 'V_2075',
                particles = [ P.W__minus__, P.W__plus__, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_819})

V_2076 = Vertex(name = 'V_2076',
                particles = [ P.W__minus__, P.W__plus__, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_820})

V_2077 = Vertex(name = 'V_2077',
                particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVV2 ],
                couplings = {(0,0):C.GC_5})

V_2078 = Vertex(name = 'V_2078',
                particles = [ P.W__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVV1 ],
                couplings = {(0,0):C.GC_822})

V_2079 = Vertex(name = 'V_2079',
                particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVVV2 ],
                couplings = {(0,0):C.GC_802})

V_2080 = Vertex(name = 'V_2080',
                particles = [ P.ve__tilde__, P.e__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2402})

V_2081 = Vertex(name = 'V_2081',
                particles = [ P.vm__tilde__, P.mu__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2403})

V_2082 = Vertex(name = 'V_2082',
                particles = [ P.vt__tilde__, P.tau__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFS1 ],
                couplings = {(0,0):C.GC_2404})

V_2083 = Vertex(name = 'V_2083',
                particles = [ P.a, P.Z, P.H__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2550})

V_2084 = Vertex(name = 'V_2084',
                particles = [ P.Z, P.A0, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2539})

V_2085 = Vertex(name = 'V_2085',
                particles = [ P.Z, P.H__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2549})

V_2086 = Vertex(name = 'V_2086',
                particles = [ P.Z, P.sd1__tilde__, P.sd1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_954})

V_2087 = Vertex(name = 'V_2087',
                particles = [ P.Z, P.sd1__tilde__, P.sd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_955})

V_2088 = Vertex(name = 'V_2088',
                particles = [ P.Z, P.sd1, P.sd2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_956})

V_2089 = Vertex(name = 'V_2089',
                particles = [ P.Z, P.sd2__tilde__, P.sd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_957})

V_2090 = Vertex(name = 'V_2090',
                particles = [ P.Z, P.sd3__tilde__, P.sd3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_926})

V_2091 = Vertex(name = 'V_2091',
                particles = [ P.Z, P.sd4__tilde__, P.sd4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_927})

V_2092 = Vertex(name = 'V_2092',
                particles = [ P.Z, P.sd5__tilde__, P.sd5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_948})

V_2093 = Vertex(name = 'V_2093',
                particles = [ P.Z, P.sd6__tilde__, P.sd6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_949})

V_2094 = Vertex(name = 'V_2094',
                particles = [ P.a, P.Z, P.sd1__tilde__, P.sd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_988})

V_2095 = Vertex(name = 'V_2095',
                particles = [ P.a, P.Z, P.sd1__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_990})

V_2096 = Vertex(name = 'V_2096',
                particles = [ P.a, P.Z, P.sd1, P.sd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_992})

V_2097 = Vertex(name = 'V_2097',
                particles = [ P.a, P.Z, P.sd2__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_994})

V_2098 = Vertex(name = 'V_2098',
                particles = [ P.a, P.Z, P.sd3__tilde__, P.sd3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_938})

V_2099 = Vertex(name = 'V_2099',
                particles = [ P.a, P.Z, P.sd4__tilde__, P.sd4 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_940})

V_2100 = Vertex(name = 'V_2100',
                particles = [ P.a, P.Z, P.sd5__tilde__, P.sd5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_984})

V_2101 = Vertex(name = 'V_2101',
                particles = [ P.a, P.Z, P.sd6__tilde__, P.sd6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_986})

V_2102 = Vertex(name = 'V_2102',
                particles = [ P.Z, P.A0, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_2535})

V_2103 = Vertex(name = 'V_2103',
                particles = [ P.Z, P.sl1__plus__, P.sl1__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_958})

V_2104 = Vertex(name = 'V_2104',
                particles = [ P.Z, P.sl1__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_959})

V_2105 = Vertex(name = 'V_2105',
                particles = [ P.Z, P.sl2__plus__, P.sl2__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_928})

V_2106 = Vertex(name = 'V_2106',
                particles = [ P.Z, P.sl3__plus__, P.sl3__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_929})

V_2107 = Vertex(name = 'V_2107',
                particles = [ P.Z, P.sl4__plus__, P.sl4__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_950})

V_2108 = Vertex(name = 'V_2108',
                particles = [ P.Z, P.sl5__plus__, P.sl5__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_951})

V_2109 = Vertex(name = 'V_2109',
                particles = [ P.Z, P.sl1__minus__, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_960})

V_2110 = Vertex(name = 'V_2110',
                particles = [ P.Z, P.sl6__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_961})

V_2111 = Vertex(name = 'V_2111',
                particles = [ P.a, P.Z, P.sl1__plus__, P.sl1__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_968})

V_2112 = Vertex(name = 'V_2112',
                particles = [ P.a, P.Z, P.sl1__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_969})

V_2113 = Vertex(name = 'V_2113',
                particles = [ P.a, P.Z, P.sl2__plus__, P.sl2__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_932})

V_2114 = Vertex(name = 'V_2114',
                particles = [ P.a, P.Z, P.sl3__plus__, P.sl3__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_933})

V_2115 = Vertex(name = 'V_2115',
                particles = [ P.a, P.Z, P.sl4__plus__, P.sl4__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_966})

V_2116 = Vertex(name = 'V_2116',
                particles = [ P.a, P.Z, P.sl5__plus__, P.sl5__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_967})

V_2117 = Vertex(name = 'V_2117',
                particles = [ P.a, P.Z, P.sl1__minus__, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_970})

V_2118 = Vertex(name = 'V_2118',
                particles = [ P.a, P.Z, P.sl6__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_971})

V_2119 = Vertex(name = 'V_2119',
                particles = [ P.Z, P.sv1__tilde__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_922})

V_2120 = Vertex(name = 'V_2120',
                particles = [ P.Z, P.sv2__tilde__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_922})

V_2121 = Vertex(name = 'V_2121',
                particles = [ P.Z, P.sv3__tilde__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_922})

V_2122 = Vertex(name = 'V_2122',
                particles = [ P.Z, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_962})

V_2123 = Vertex(name = 'V_2123',
                particles = [ P.Z, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_963})

V_2124 = Vertex(name = 'V_2124',
                particles = [ P.Z, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_964})

V_2125 = Vertex(name = 'V_2125',
                particles = [ P.Z, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_965})

V_2126 = Vertex(name = 'V_2126',
                particles = [ P.Z, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_930})

V_2127 = Vertex(name = 'V_2127',
                particles = [ P.Z, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_931})

V_2128 = Vertex(name = 'V_2128',
                particles = [ P.Z, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_952})

V_2129 = Vertex(name = 'V_2129',
                particles = [ P.Z, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1 ],
                couplings = {(0,0):C.GC_953})

V_2130 = Vertex(name = 'V_2130',
                particles = [ P.a, P.Z, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_976})

V_2131 = Vertex(name = 'V_2131',
                particles = [ P.a, P.Z, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_978})

V_2132 = Vertex(name = 'V_2132',
                particles = [ P.a, P.Z, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_980})

V_2133 = Vertex(name = 'V_2133',
                particles = [ P.a, P.Z, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_982})

V_2134 = Vertex(name = 'V_2134',
                particles = [ P.a, P.Z, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_934})

V_2135 = Vertex(name = 'V_2135',
                particles = [ P.a, P.Z, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_936})

V_2136 = Vertex(name = 'V_2136',
                particles = [ P.a, P.Z, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_972})

V_2137 = Vertex(name = 'V_2137',
                particles = [ P.a, P.Z, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_974})

V_2138 = Vertex(name = 'V_2138',
                particles = [ P.g, P.Z, P.sd1__tilde__, P.sd1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_989})

V_2139 = Vertex(name = 'V_2139',
                particles = [ P.g, P.Z, P.sd1__tilde__, P.sd2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_991})

V_2140 = Vertex(name = 'V_2140',
                particles = [ P.g, P.Z, P.sd1, P.sd2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_993})

V_2141 = Vertex(name = 'V_2141',
                particles = [ P.g, P.Z, P.sd2__tilde__, P.sd2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_995})

V_2142 = Vertex(name = 'V_2142',
                particles = [ P.g, P.Z, P.sd3__tilde__, P.sd3 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_939})

V_2143 = Vertex(name = 'V_2143',
                particles = [ P.g, P.Z, P.sd4__tilde__, P.sd4 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_941})

V_2144 = Vertex(name = 'V_2144',
                particles = [ P.g, P.Z, P.sd5__tilde__, P.sd5 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_985})

V_2145 = Vertex(name = 'V_2145',
                particles = [ P.g, P.Z, P.sd6__tilde__, P.sd6 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_987})

V_2146 = Vertex(name = 'V_2146',
                particles = [ P.g, P.Z, P.su1__tilde__, P.su1 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_977})

V_2147 = Vertex(name = 'V_2147',
                particles = [ P.g, P.Z, P.su1__tilde__, P.su2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_979})

V_2148 = Vertex(name = 'V_2148',
                particles = [ P.g, P.Z, P.su1, P.su2__tilde__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_981})

V_2149 = Vertex(name = 'V_2149',
                particles = [ P.g, P.Z, P.su2__tilde__, P.su2 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_983})

V_2150 = Vertex(name = 'V_2150',
                particles = [ P.g, P.Z, P.su3__tilde__, P.su3 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_935})

V_2151 = Vertex(name = 'V_2151',
                particles = [ P.g, P.Z, P.su4__tilde__, P.su4 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_937})

V_2152 = Vertex(name = 'V_2152',
                particles = [ P.g, P.Z, P.su5__tilde__, P.su5 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_973})

V_2153 = Vertex(name = 'V_2153',
                particles = [ P.g, P.Z, P.su6__tilde__, P.su6 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_975})

V_2154 = Vertex(name = 'V_2154',
                particles = [ P.W__minus__, P.Z, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2485})

V_2155 = Vertex(name = 'V_2155',
                particles = [ P.W__minus__, P.Z, P.h01, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2538})

V_2156 = Vertex(name = 'V_2156',
                particles = [ P.W__minus__, P.Z, P.A0, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2546})

V_2157 = Vertex(name = 'V_2157',
                particles = [ P.W__minus__, P.Z, P.h02, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2534})

V_2158 = Vertex(name = 'V_2158',
                particles = [ P.W__minus__, P.Z, P.sl1__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_882})

V_2159 = Vertex(name = 'V_2159',
                particles = [ P.W__minus__, P.Z, P.sl4__plus__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_885})

V_2160 = Vertex(name = 'V_2160',
                particles = [ P.W__minus__, P.Z, P.sl5__plus__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_884})

V_2161 = Vertex(name = 'V_2161',
                particles = [ P.W__minus__, P.Z, P.sl6__plus__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_883})

V_2162 = Vertex(name = 'V_2162',
                particles = [ P.W__minus__, P.Z, P.sd1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_876})

V_2163 = Vertex(name = 'V_2163',
                particles = [ P.W__minus__, P.Z, P.sd1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_877})

V_2164 = Vertex(name = 'V_2164',
                particles = [ P.W__minus__, P.Z, P.sd2__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_878})

V_2165 = Vertex(name = 'V_2165',
                particles = [ P.W__minus__, P.Z, P.sd2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_879})

V_2166 = Vertex(name = 'V_2166',
                particles = [ P.W__minus__, P.Z, P.sd5__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_880})

V_2167 = Vertex(name = 'V_2167',
                particles = [ P.W__minus__, P.Z, P.sd6__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_881})

V_2168 = Vertex(name = 'V_2168',
                particles = [ P.W__plus__, P.Z, P.H__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2485})

V_2169 = Vertex(name = 'V_2169',
                particles = [ P.W__plus__, P.Z, P.H__minus__, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2538})

V_2170 = Vertex(name = 'V_2170',
                particles = [ P.W__plus__, P.Z, P.A0, P.H__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2547})

V_2171 = Vertex(name = 'V_2171',
                particles = [ P.W__plus__, P.Z, P.H__minus__, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2534})

V_2172 = Vertex(name = 'V_2172',
                particles = [ P.W__plus__, P.Z, P.sl1__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_892})

V_2173 = Vertex(name = 'V_2173',
                particles = [ P.W__plus__, P.Z, P.sl4__minus__, P.sv3__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_895})

V_2174 = Vertex(name = 'V_2174',
                particles = [ P.W__plus__, P.Z, P.sl5__minus__, P.sv2__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_894})

V_2175 = Vertex(name = 'V_2175',
                particles = [ P.W__plus__, P.Z, P.sl6__minus__, P.sv1__tilde__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_893})

V_2176 = Vertex(name = 'V_2176',
                particles = [ P.W__plus__, P.Z, P.sd1, P.su1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_886})

V_2177 = Vertex(name = 'V_2177',
                particles = [ P.W__plus__, P.Z, P.sd1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_887})

V_2178 = Vertex(name = 'V_2178',
                particles = [ P.W__plus__, P.Z, P.sd2, P.su1__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_888})

V_2179 = Vertex(name = 'V_2179',
                particles = [ P.W__plus__, P.Z, P.sd2, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_889})

V_2180 = Vertex(name = 'V_2180',
                particles = [ P.W__plus__, P.Z, P.sd5, P.su6__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_890})

V_2181 = Vertex(name = 'V_2181',
                particles = [ P.W__plus__, P.Z, P.sd6, P.su5__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_891})

V_2182 = Vertex(name = 'V_2182',
                particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVV5 ],
                couplings = {(0,0):C.GC_823})

V_2183 = Vertex(name = 'V_2183',
                particles = [ P.Z, P.Z, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2329})

V_2184 = Vertex(name = 'V_2184',
                particles = [ P.Z, P.Z, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVS1 ],
                couplings = {(0,0):C.GC_2304})

V_2185 = Vertex(name = 'V_2185',
                particles = [ P.Z, P.Z, P.h01, P.h01 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2397})

V_2186 = Vertex(name = 'V_2186',
                particles = [ P.Z, P.Z, P.h02, P.h02 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2397})

V_2187 = Vertex(name = 'V_2187',
                particles = [ P.Z, P.Z, P.A0, P.A0 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2548})

V_2188 = Vertex(name = 'V_2188',
                particles = [ P.Z, P.Z, P.H__minus__, P.H__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_2551})

V_2189 = Vertex(name = 'V_2189',
                particles = [ P.Z, P.Z, P.sd1__tilde__, P.sd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1002})

V_2190 = Vertex(name = 'V_2190',
                particles = [ P.Z, P.Z, P.sd1__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1003})

V_2191 = Vertex(name = 'V_2191',
                particles = [ P.Z, P.Z, P.sd1, P.sd2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1004})

V_2192 = Vertex(name = 'V_2192',
                particles = [ P.Z, P.Z, P.sd2__tilde__, P.sd2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1005})

V_2193 = Vertex(name = 'V_2193',
                particles = [ P.Z, P.Z, P.sd3__tilde__, P.sd3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_942})

V_2194 = Vertex(name = 'V_2194',
                particles = [ P.Z, P.Z, P.sd4__tilde__, P.sd4 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_943})

V_2195 = Vertex(name = 'V_2195',
                particles = [ P.Z, P.Z, P.sd5__tilde__, P.sd5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_996})

V_2196 = Vertex(name = 'V_2196',
                particles = [ P.Z, P.Z, P.sd6__tilde__, P.sd6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_997})

V_2197 = Vertex(name = 'V_2197',
                particles = [ P.Z, P.Z, P.sl1__plus__, P.sl1__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1006})

V_2198 = Vertex(name = 'V_2198',
                particles = [ P.Z, P.Z, P.sl1__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1007})

V_2199 = Vertex(name = 'V_2199',
                particles = [ P.Z, P.Z, P.sl2__plus__, P.sl2__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_944})

V_2200 = Vertex(name = 'V_2200',
                particles = [ P.Z, P.Z, P.sl3__plus__, P.sl3__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_945})

V_2201 = Vertex(name = 'V_2201',
                particles = [ P.Z, P.Z, P.sl4__plus__, P.sl4__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_998})

V_2202 = Vertex(name = 'V_2202',
                particles = [ P.Z, P.Z, P.sl5__plus__, P.sl5__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_999})

V_2203 = Vertex(name = 'V_2203',
                particles = [ P.Z, P.Z, P.sl1__minus__, P.sl6__plus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1008})

V_2204 = Vertex(name = 'V_2204',
                particles = [ P.Z, P.Z, P.sl6__plus__, P.sl6__minus__ ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1009})

V_2205 = Vertex(name = 'V_2205',
                particles = [ P.Z, P.Z, P.sv1__tilde__, P.sv1 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_920})

V_2206 = Vertex(name = 'V_2206',
                particles = [ P.Z, P.Z, P.sv2__tilde__, P.sv2 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_920})

V_2207 = Vertex(name = 'V_2207',
                particles = [ P.Z, P.Z, P.sv3__tilde__, P.sv3 ],
                color = [ '1' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_920})

V_2208 = Vertex(name = 'V_2208',
                particles = [ P.Z, P.Z, P.su1__tilde__, P.su1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1010})

V_2209 = Vertex(name = 'V_2209',
                particles = [ P.Z, P.Z, P.su1__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1011})

V_2210 = Vertex(name = 'V_2210',
                particles = [ P.Z, P.Z, P.su1, P.su2__tilde__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1012})

V_2211 = Vertex(name = 'V_2211',
                particles = [ P.Z, P.Z, P.su2__tilde__, P.su2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1013})

V_2212 = Vertex(name = 'V_2212',
                particles = [ P.Z, P.Z, P.su3__tilde__, P.su3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_946})

V_2213 = Vertex(name = 'V_2213',
                particles = [ P.Z, P.Z, P.su4__tilde__, P.su4 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_947})

V_2214 = Vertex(name = 'V_2214',
                particles = [ P.Z, P.Z, P.su5__tilde__, P.su5 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1000})

V_2215 = Vertex(name = 'V_2215',
                particles = [ P.Z, P.Z, P.su6__tilde__, P.su6 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                couplings = {(0,0):C.GC_1001})

V_2216 = Vertex(name = 'V_2216',
                particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
                color = [ '1' ],
                lorentz = [ L.VVVV2 ],
                couplings = {(0,0):C.GC_800})

V_2217 = Vertex(name = 'V_2217',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_1})

V_2218 = Vertex(name = 'V_2218',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_1})

V_2219 = Vertex(name = 'V_2219',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_1})

V_2220 = Vertex(name = 'V_2220',
                particles = [ P.e__plus__, P.e__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_3})

V_2221 = Vertex(name = 'V_2221',
                particles = [ P.mu__plus__, P.mu__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_3})

V_2222 = Vertex(name = 'V_2222',
                particles = [ P.tau__plus__, P.tau__minus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_3})

V_2223 = Vertex(name = 'V_2223',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_2})

V_2224 = Vertex(name = 'V_2224',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_2})

V_2225 = Vertex(name = 'V_2225',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_2})

V_2226 = Vertex(name = 'V_2226',
                particles = [ P.go, P.go, P.g ],
                color = [ 'f(3,2,1)' ],
                lorentz = [ L.FFV6 ],
                couplings = {(0,0):C.GC_8})

V_2227 = Vertex(name = 'V_2227',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2228 = Vertex(name = 'V_2228',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2229 = Vertex(name = 'V_2229',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2230 = Vertex(name = 'V_2230',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2231 = Vertex(name = 'V_2231',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2232 = Vertex(name = 'V_2232',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_7})

V_2233 = Vertex(name = 'V_2233',
                particles = [ P.x1__minus__, P.x1__plus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2173,(0,1):C.GC_2125})

V_2234 = Vertex(name = 'V_2234',
                particles = [ P.x2__minus__, P.x1__plus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2194,(0,1):C.GC_2127})

V_2235 = Vertex(name = 'V_2235',
                particles = [ P.x1__minus__, P.x2__plus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2175,(0,1):C.GC_2152})

V_2236 = Vertex(name = 'V_2236',
                particles = [ P.x2__minus__, P.x2__plus__, P.a ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2196,(0,1):C.GC_2154})

V_2237 = Vertex(name = 'V_2237',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2238 = Vertex(name = 'V_2238',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2239 = Vertex(name = 'V_2239',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2240 = Vertex(name = 'V_2240',
                particles = [ P.e__plus__, P.ve, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2241 = Vertex(name = 'V_2241',
                particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2242 = Vertex(name = 'V_2242',
                particles = [ P.tau__plus__, P.vt, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2243 = Vertex(name = 'V_2243',
                particles = [ P.n1, P.x1__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1871,(0,1):C.GC_2121})

V_2244 = Vertex(name = 'V_2244',
                particles = [ P.n2, P.x1__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1906,(0,1):C.GC_2122})

V_2245 = Vertex(name = 'V_2245',
                particles = [ P.n3, P.x1__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1941,(0,1):C.GC_2123})

V_2246 = Vertex(name = 'V_2246',
                particles = [ P.n4, P.x1__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1976,(0,1):C.GC_2124})

V_2247 = Vertex(name = 'V_2247',
                particles = [ P.n1, P.x2__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1872,(0,1):C.GC_2148})

V_2248 = Vertex(name = 'V_2248',
                particles = [ P.n2, P.x2__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1907,(0,1):C.GC_2149})

V_2249 = Vertex(name = 'V_2249',
                particles = [ P.n3, P.x2__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1942,(0,1):C.GC_2150})

V_2250 = Vertex(name = 'V_2250',
                particles = [ P.n4, P.x2__plus__, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1977,(0,1):C.GC_2151})

V_2251 = Vertex(name = 'V_2251',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2252 = Vertex(name = 'V_2252',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2253 = Vertex(name = 'V_2253',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2254 = Vertex(name = 'V_2254',
                particles = [ P.x1__minus__, P.n1, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2169,(0,1):C.GC_1859})

V_2255 = Vertex(name = 'V_2255',
                particles = [ P.x2__minus__, P.n1, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2190,(0,1):C.GC_1860})

V_2256 = Vertex(name = 'V_2256',
                particles = [ P.x1__minus__, P.n2, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2170,(0,1):C.GC_1894})

V_2257 = Vertex(name = 'V_2257',
                particles = [ P.x2__minus__, P.n2, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2191,(0,1):C.GC_1895})

V_2258 = Vertex(name = 'V_2258',
                particles = [ P.x1__minus__, P.n3, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2171,(0,1):C.GC_1929})

V_2259 = Vertex(name = 'V_2259',
                particles = [ P.x2__minus__, P.n3, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2192,(0,1):C.GC_1930})

V_2260 = Vertex(name = 'V_2260',
                particles = [ P.x1__minus__, P.n4, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2172,(0,1):C.GC_1964})

V_2261 = Vertex(name = 'V_2261',
                particles = [ P.x2__minus__, P.n4, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2193,(0,1):C.GC_1965})

V_2262 = Vertex(name = 'V_2262',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2263 = Vertex(name = 'V_2263',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2264 = Vertex(name = 'V_2264',
                particles = [ P.vt__tilde__, P.tau__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_821})

V_2265 = Vertex(name = 'V_2265',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_923})

V_2266 = Vertex(name = 'V_2266',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_923})

V_2267 = Vertex(name = 'V_2267',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_923})

V_2268 = Vertex(name = 'V_2268',
                particles = [ P.e__plus__, P.e__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_925})

V_2269 = Vertex(name = 'V_2269',
                particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_925})

V_2270 = Vertex(name = 'V_2270',
                particles = [ P.tau__plus__, P.tau__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_922,(0,1):C.GC_925})

V_2271 = Vertex(name = 'V_2271',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_921,(0,1):C.GC_924})

V_2272 = Vertex(name = 'V_2272',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_921,(0,1):C.GC_924})

V_2273 = Vertex(name = 'V_2273',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV5 ],
                couplings = {(0,0):C.GC_921,(0,1):C.GC_924})

V_2274 = Vertex(name = 'V_2274',
                particles = [ P.ve__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_921})

V_2275 = Vertex(name = 'V_2275',
                particles = [ P.vm__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_921})

V_2276 = Vertex(name = 'V_2276',
                particles = [ P.vt__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2 ],
                couplings = {(0,0):C.GC_921})

V_2277 = Vertex(name = 'V_2277',
                particles = [ P.n1, P.n1, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV4 ],
                couplings = {(0,0):C.GC_1861})

V_2278 = Vertex(name = 'V_2278',
                particles = [ P.n2, P.n1, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1896,(0,1):C.GC_1862})

V_2279 = Vertex(name = 'V_2279',
                particles = [ P.n3, P.n1, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1931,(0,1):C.GC_1863})

V_2280 = Vertex(name = 'V_2280',
                particles = [ P.n4, P.n1, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1966,(0,1):C.GC_1864})

V_2281 = Vertex(name = 'V_2281',
                particles = [ P.n2, P.n2, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV4 ],
                couplings = {(0,0):C.GC_1897})

V_2282 = Vertex(name = 'V_2282',
                particles = [ P.n3, P.n2, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1932,(0,1):C.GC_1898})

V_2283 = Vertex(name = 'V_2283',
                particles = [ P.n4, P.n2, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1967,(0,1):C.GC_1899})

V_2284 = Vertex(name = 'V_2284',
                particles = [ P.n3, P.n3, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV4 ],
                couplings = {(0,0):C.GC_1933})

V_2285 = Vertex(name = 'V_2285',
                particles = [ P.n4, P.n3, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_1968,(0,1):C.GC_1934})

V_2286 = Vertex(name = 'V_2286',
                particles = [ P.n4, P.n4, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV4 ],
                couplings = {(0,0):C.GC_1969})

V_2287 = Vertex(name = 'V_2287',
                particles = [ P.x1__minus__, P.x1__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2174,(0,1):C.GC_2126})

V_2288 = Vertex(name = 'V_2288',
                particles = [ P.x2__minus__, P.x1__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2195,(0,1):C.GC_2128})

V_2289 = Vertex(name = 'V_2289',
                particles = [ P.x1__minus__, P.x2__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2176,(0,1):C.GC_2153})

V_2290 = Vertex(name = 'V_2290',
                particles = [ P.x2__minus__, P.x2__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                couplings = {(0,0):C.GC_2197,(0,1):C.GC_2155})

