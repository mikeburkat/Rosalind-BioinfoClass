'''
Created on Feb 17, 2014

@author: mike
'''

class GreedySorting:
    
    def __init__(self):
        self.permutation = "(-3 +4 +1 +5 -2)" # testing
        
        self.permutation = "(-367 -317 +207 -136 -389 +333 +179 +184 -174 -349 -214 -22 +25 -406 +409 -407 +212 -5 +85 -418 -4 -228 +210 +348 -66 -316 -373 -58 -170 -103 +161 +416 +50 +29 -380 -158 +151 +233 +71 -277 +243 -244 -284 +24 +90 +387 -175 +37 +46 +330 +426 -45 -117 +247 -265 +369 +441 +54 -414 +104 -134 -385 -374 +216 +305 -335 +368 -74 -351 +126 +283 +353 -249 +377 +213 -263 -344 +256 +89 +303 +61 -171 +167 -97 -108 +429 +307 -394 -400 -415 -205 -33 +150 +397 +242 -124 +370 -30 -110 -275 -62 +300 +318 -218 -201 +149 -183 -378 +51 -257 -437 -153 +241 -118 +320 -434 -341 +91 +282 +440 -188 -285 -423 +32 +253 -401 +323 +166 -239 -23 +334 +142 +286 +196 +193 -56 +425 -73 +382 +337 -390 -116 +392 -2 +221 -219 +430 -72 +114 -105 +298 +130 +82 +278 -388 +325 -168 -145 +139 -138 +395 +345 +252 +435 +404 -301 -413 +302 +258 -8 -129 -202 -185 -147 +315 -76 +365 -304 -15 +280 +234 -79 +292 +191 -339 +338 -93 +186 -306 -119 +272 -403 -204 -120 +287 +398 +262 +101 +112 +260 -68 -10 -405 -295 +296 -356 +235 +371 -192 +250 -358 -92 -131 -384 -43 +230 -211 +376 -3 +327 -107 -261 +402 +189 -294 -290 +336 -111 -53 +14 +65 -268 +63 +180 -35 +9 +433 +141 +248 -140 -163 -310 +165 -355 +215 -379 -86 +113 +410 -181 -27 -427 -264 -223 -77 +436 -236 -340 -47 +328 -64 +309 +146 -67 +276 +232 -100 -48 +312 +408 +366 +391 +143 -178 +20 +155 +314 +421 -281 +19 +251 +372 +420 -360 +98 -88 -229 -227 +381 -271 +199 +144 -422 -200 +209 -245 -417 -319 -57 -176 +411 +419 +197 -270 -156 +342 +208 +194 +121 -428 -52 -187 -267 -21 -78 -16 +154 -133 -383 +203 +13 +87 +266 +99 +393 +438 +169 -259 +152 -173 +354 +361 -198 -39 +240 +308 -17 +84 -347 -164 -238 +231 -289 -255 +34 -431 -350 -363 -299 +297 +352 +49 +195 -83 -293 +182 -59 -439 -396 -375 -122 -273 +125 -159 +246 -412 -102 -224 -217 +357 -127 +222 +226 -313 -279 +6 -96 -288 -137 +157 -254 -206 +94 -123 +70 +364 +321 -225 -346 -343 -38 +106 +28 -162 +41 -95 -160 -322 +7 +42 +26 +128 -291 +109 -332 +237 +386 +11 -81 -329 -18 +311 +115 -60 -31 -177 +399 -75 +269 +55 +40 +12 +362 -36 +220 -324 +80 -331 +44 -424 -172 +135 -274 +148 -1 +359 +132 -326 -432 -190 -69)"
        
        self.permList = []
        
    
    def toList(self, permutation):
        permList = []
        permutation = permutation[1:-1]
        permList = permutation.split(" ")
        return permList
    
    def printFormatted(self, permList):
        s = '('
        for x in permList:
            s = s + x + " "
        s = s[:-1] + ")"
        print s
        
        
    def reverse(self, i, j, permList):
        #print i, j, permList
        
        front = permList[:i]
        middle = permList[i:j+1]
        back = permList[j+1:]
        
        negRev = []
        for x in middle:
            if ( int(x) < 0 ):
                negRev.insert(0, "+" + x[1:])
            else:
                negRev.insert(0, "-" + x[1:])
        
        rev = front + negRev + back
        
        #print front,"x", middle, "x", back
        #print rev
        return rev
        
    def gSort(self, permList):
        import math
        i = 0
        while (i < len(permList) ):
            j = i
            while (j < len(permList)):
                
                
                if (i == len(permList) - 1):
                    if ( int(permList[i]) < 0 ):
                        permList[i] = "+" + permList[i][1:]
                        self.printFormatted(permList)
                        break
                    else:
                        break
                    
                
                
                val = int(permList[j])
                
                if (i == j and val == i+1):
                    break
                
                val = math.fabs(val)
                if (val == i+1):
                    permList = self.reverse(i, j, permList)
                    if ( int(permList[i]) < 0 ):
                        self.printFormatted(permList)
                        permList[i] = "+" + permList[i][1:]
                        self.printFormatted(permList)
                    else:
                        self.printFormatted(permList)
                    break
                j += 1
            i += 1
        
        
    
    def run(self):
        self.permList = self.toList(self.permutation)
        self.gSort(self.permList)
        
        


if __name__ == '__main__':
    gs = GreedySorting()
    gs.run()
    