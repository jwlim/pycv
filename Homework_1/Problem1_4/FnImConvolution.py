def FnImConvol( OriginImage, Kernel, Padding ) :
    "This function is to perform 2D convoluttion"
    
    ## Function Name: FnImConvol ******************************************
    #
    # Description: Function of 2D convolution
    # Author: Wonatek Lim ( lwt1849@gmail.com )
    # Copyright 2015 Wontaek Lim, All Right Reserved
    #
    # Input
    #  - OriginImage:  Image array
    #  - Kernel:       Kernel array
    #  - Padding:      Type of padding( 'zero', 'wrap', 'clamp', 'mirror' )
    #
    #***********************************************************************
    
    import math
    #from numpy import*
    import numpy as np
    
    # 1. Get ImageSize, KernelSize
    [ ImWidth, ImHeight] = OriginImage.shape;
    [ KerWidth, KerHeight] = Kernel.shape;
    
    HalfWidthKernel = math.ceil( KerWidth/2 )
    HalfHeightKernel = math.ceil( KerHeight/2 )
    
    # 2. Create result array
    FilteredImage = np.zeros( (ImWidth, ImHeight) )
    
    # 3. 2D Convolution
    for ImageIndexX in range(ImWidth):
        for ImageIndexY in range(ImHeight):
            
            AccumedValue = 0.0
            
            for KernelIndexX in range(KerWidth):
                ConvImIndexX = int( ImageIndexX - HalfWidthKernel + KernelIndexX )

                for KernelIndexY in range(KerHeight):
                    ConvImIndexY = int( ImageIndexY - HalfHeightKernel + KernelIndexY )
                    
                    # 03-1. Padding: zero
                    if Padding == 'zero':
                        if (ConvImIndexX >= 0 ) and (ConvImIndexY >= 0) and (ConvImIndexX < ImWidth) and (ConvImIndexY < ImHeight):
                            SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                            AccumedValue = AccumedValue + SumVal
        
                    # 03-2. Padding: wrap
                    elif Padding == 'wrap':
                        if ConvImIndexX < 0:
                            ConvImIndexX = ConvImIndexX + ImWidth
                        elif ConvImIndexX >= ImWidth:
                            ConvImIndexX = ConvImIndexX - ImWidth
        
                        if ConvImIndexY < 0:
                            ConvImIndexY = ConvImIndexY + ImHeight
                        elif ConvImIndexY >= ImHeight:
                            ConvImIndexY = ConvImIndexY - ImHeight
        
                        SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                        AccumedValue = AccumedValue + SumVal
        
        
                    # 03-3. Padding: clamp
                    elif Padding == 'clamp':
                        if ConvImIndexX < 0:
                            ConvImIndexX = 0
                        elif ConvImIndexX >= ImWidth:
                            ConvImIndexX = ImWidth - 1
                                
                        if ConvImIndexY < 0:
                            ConvImIndexY = 0
                        elif ConvImIndexY >= ImHeight:
                            ConvImIndexY = ImHeight - 1
                                
                        SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                        AccumedValue = AccumedValue + SumVal


                    # 03-4. Padding: mirror
                    elif Padding == 'mirror':
                        if ConvImIndexX < 0:
                            ConvImIndexX = abs(ConvImIndexX) - 1
                        elif ConvImIndexX >= ImWidth:
                            ConvImIndexX = ImWidth - ConvImIndexX
                                
                        if ConvImIndexY < 0:
                            ConvImIndexY = abs(ConvImIndexY) - 1
                        elif ConvImIndexY >= ImHeight:
                            ConvImIndexY = ImHeight - ConvImIndexY

                        SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                        AccumedValue = AccumedValue + SumVal
        
        
                    # --. Default Padding: zero
                    else:
                        if (ConvImIndexX >= 0 ) and (ConvImIndexY >= 0) and (ConvImIndexX < ImWidth) and (ConvImIndexY < ImHeight):
                            SumVal = OriginImage[ConvImIndexX, ConvImIndexY] * Kernel[KernelIndexX, KernelIndexY]
                            AccumedValue = AccumedValue + SumVal
        
            # Update value
            FilteredImage[ImageIndexX, ImageIndexY] = AccumedValue


    return FilteredImage